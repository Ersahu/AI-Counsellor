import google.genai as genai
from sqlalchemy.orm import Session
from app.models import User, UserProfile, Shortlist
from app.core.config import settings
import json

# Configure Gemini
client = genai.Client(api_key=settings.GEMINI_API_KEY)

class AICounsellor:
    def __init__(self):
        self.model_name = 'gemini-1.5-flash'
    
    def get_system_prompt(self, user: User, profile: UserProfile, stage: str) -> str:
        base_prompt = f"""
        You are an AI Study Abroad Counsellor. You help students make informed decisions about studying abroad.
        
        USER PROFILE:
        Name: {user.name}
        Education Level: {profile.education_level}
        Degree: {profile.degree}
        GPA: {profile.gpa}
        Target Degree: {profile.target_degree}
        Field: {profile.field}
        Countries Interested: {', '.join(json.loads(profile.countries)) if profile.countries else 'Not specified'}
        Budget Range: {profile.budget_range}
        Funding Type: {profile.funding_type}
        IELTS Status: {profile.ielts_status}
        GRE Status: {profile.gre_status}
        SOP Status: {profile.sop_status}
        
        CURRENT STAGE: {stage}
        
        INSTRUCTIONS:
        1. Provide clear, actionable advice
        2. Assess profile strengths and gaps
        3. Recommend universities with fit reasons and risks
        4. Suggest specific actions
        5. Guide user to next logical step
        
        RESPONSE FORMAT (STRICT JSON):
        {{
          "explanation": "clear reasoning text",
          "profile_assessment": {{
            "academics": "Strong / Average / Weak",
            "exams": "Not Started / In Progress / Completed",
            "sop": "Not Started / Draft / Ready"
          }},
          "recommendations": [
            {{
              "university": "University Name",
              "category": "Dream / Target / Safe",
              "fit_reason": "why it fits",
              "risk": "main risk",
              "acceptance_chance": "Low / Medium / High"
            }}
          ],
          "actions": [
            {{
              "type": "SHORTLIST",
              "payload": {{
                "university_id": 1,
                "category": "Target"
              }}
            }}
          ],
          "next_stage_suggestion": "what the user should do next"
        }}
        """
        
        stage_specific_prompts = {
            "onboarding": "User has just completed onboarding. Assess their profile comprehensively and suggest immediate next steps.",
            "discovery": "User is in university discovery phase. Help them understand their options and shortlist suitable universities.",
            "locking": "User needs to lock universities. Push them to make decisions and commit to specific choices.",
            "application": "User is preparing applications. Focus on timeline adherence."
        }
        
        return base_prompt + "\n\n" + stage_specific_prompts.get(stage, "")
    
    def get_response(self, user_message: str, user: User, db: Session) -> dict:
        # Get user profile
        profile = db.query(UserProfile).filter(UserProfile.user_id == user.id).first()
        if not profile:
            return {
                "error": "Complete your profile first",
                "next_stage_suggestion": "Please complete the mandatory onboarding"
            }
        
        # Get system prompt
        prompt = self.get_system_prompt(user, profile, user.current_stage)
        
        # Add user message
        full_prompt = f"{prompt}\n\nUSER MESSAGE: {user_message}\n\nRESPONSE:"
        
        try:
            # Get AI response
            response = client.models.generate_content(model=self.model_name, contents=full_prompt)
            
            # Parse JSON response
            response_text = response.text.strip()
            if response_text.startswith("```json"):
                response_text = response_text[7:-3].strip()
            elif response_text.startswith("```"):
                response_text = response_text[3:-3].strip()
            
            parsed_response = json.loads(response_text)
            
            # Execute actions
            self.execute_actions(parsed_response.get("actions", []), user, db)
            
            return parsed_response
            
        except Exception as e:
            return {
                "error": "AI processing failed",
                "explanation": f"Sorry, I encountered an error: {str(e)}",
                "next_stage_suggestion": "Please try again"
            }
    
    def execute_actions(self, actions: list, user: User, db: Session):
        for action in actions:
            action_type = action.get("type")
            payload = action.get("payload", {})
            
            if action_type == "SHORTLIST":
                shortlist = Shortlist(
                    user_id=user.id,
                    university_id=payload.get("university_id"),
                    category=payload.get("category", "Target")
                )
                db.add(shortlist)
            
            db.commit()

# Global instance
ai_counsellor = AICounsellor()
client = genai.Client(api_key=settings.GEMINI_API_KEY)