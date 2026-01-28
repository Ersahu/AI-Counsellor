# Dummy University Data
UNIVERSITIES_DATA = [
    {
        "name": "Stanford University",
        "country": "USA",
        "city": "Stanford",
        "avg_cost": 55000,
        "ranking_band": "Top 10",
        "acceptance_difficulty": "High",
        "description": "World-renowned research university with exceptional engineering programs."
    },
    {
        "name": "MIT",
        "country": "USA",
        "city": "Cambridge",
        "avg_cost": 53000,
        "ranking_band": "Top 10",
        "acceptance_difficulty": "High",
        "description": "Leading institution for technology and innovation."
    },
    {
        "name": "University of Toronto",
        "country": "Canada",
        "city": "Toronto",
        "avg_cost": 28000,
        "ranking_band": "Top 50",
        "acceptance_difficulty": "Medium",
        "description": "Canada's top university with excellent computer science programs."
    },
    {
        "name": "University of British Columbia",
        "country": "Canada",
        "city": "Vancouver",
        "avg_cost": 25000,
        "ranking_band": "Top 50",
        "acceptance_difficulty": "Medium",
        "description": "Beautiful campus with strong research focus."
    },
    {
        "name": "Imperial College London",
        "country": "UK",
        "city": "London",
        "avg_cost": 35000,
        "ranking_band": "Top 20",
        "acceptance_difficulty": "High",
        "description": "Specialized in science, engineering, medicine and business."
    },
    {
        "name": "University of Melbourne",
        "country": "Australia",
        "city": "Melbourne",
        "avg_cost": 38000,
        "ranking_band": "Top 50",
        "acceptance_difficulty": "Medium",
        "description": "Australia's leading research university."
    },
    {
        "name": "Technical University of Munich",
        "country": "Germany",
        "city": "Munich",
        "avg_cost": 15000,
        "ranking_band": "Top 100",
        "acceptance_difficulty": "Low",
        "description": "Excellent engineering programs with low tuition fees."
    },
    {
        "name": "National University of Singapore",
        "country": "Singapore",
        "city": "Singapore",
        "avg_cost": 22000,
        "ranking_band": "Top 50",
        "acceptance_difficulty": "Medium",
        "description": "Asia's top university with global recognition."
    },
    {
        "name": "Carnegie Mellon University",
        "country": "USA",
        "city": "Pittsburgh",
        "avg_cost": 50000,
        "ranking_band": "Top 50",
        "acceptance_difficulty": "High",
        "description": "World leader in computer science and technology."
    },
    {
        "name": "University of Waterloo",
        "country": "Canada",
        "city": "Waterloo",
        "avg_cost": 26000,
        "ranking_band": "Top 100",
        "acceptance_difficulty": "Medium",
        "description": "Known for co-op programs and strong tech industry connections."
    }
]

# Sample AI Responses
SAMPLE_AI_RESPONSES = {
    "profile_assessment": {
        "explanation": "Based on your profile, you have a strong academic foundation with a 3.7 GPA in Computer Science. Your GRE is completed and IELTS is in progress. However, your SOP is still not started, which is critical for applications.",
        "profile_assessment": {
            "academics": "Strong",
            "exams": "In Progress",
            "sop": "Not Started"
        },
        "recommendations": [
            {
                "university": "Carnegie Mellon University",
                "category": "Dream",
                "fit_reason": "Perfect match for your CS background and career goals in AI",
                "risk": "High competition, need excellent SOP and recommendations",
                "acceptance_chance": "Low"
            },
            {
                "university": "University of Toronto",
                "category": "Target",
                "fit_reason": "Strong CS program, reasonable costs, good fit for your profile",
                "risk": "Moderate competition",
                "acceptance_chance": "Medium"
            },
            {
                "university": "University of Waterloo",
                "category": "Safe",
                "fit_reason": "Excellent co-op opportunities, lower competition than top-tier schools",
                "risk": "Less prestigious but strong industry connections",
                "acceptance_chance": "High"
            }
        ],
        "actions": [
            {
                "type": "ADD_TASK",
                "payload": {
                    "title": "Complete IELTS exam",
                    "description": "Register and prepare for IELTS exam within next 2 months",
                    "priority": "high"
                }
            },
            {
                "type": "ADD_TASK",
                "payload": {
                    "title": "Start SOP draft",
                    "description": "Begin working on Statement of Purpose highlighting your research interests",
                    "priority": "high"
                }
            }
        ],
        "next_stage_suggestion": "Let's shortlist 3-5 universities that match your profile. Which countries interest you most?"
    }
}