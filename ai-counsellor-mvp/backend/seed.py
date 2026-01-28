# Create initial universities data
import psycopg2
import json
from data.dummy_universities import UNIVERSITIES_DATA

def seed_database():
    conn = psycopg2.connect(
        host="localhost",
        database="ai_counsellor",
        user="postgres",
        password="password"
    )
    
    cur = conn.cursor()
    
    # Insert universities
    for uni in UNIVERSITIES_DATA:
        cur.execute("""
            INSERT INTO universities (name, country, city, avg_cost, ranking_band, acceptance_difficulty, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            uni['name'],
            uni['country'],
            uni['city'],
            uni['avg_cost'],
            uni['ranking_band'],
            uni['acceptance_difficulty'],
            uni['description']
        ))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()