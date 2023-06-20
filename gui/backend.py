from generate_mentors import SKILLS
from skills_matrix import mentors, matrix
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
from typing import List

skills = """
Programming
Problem-solving
Critical Thinking
Collaboration
Communication
Adaptability
Project Management
Technical Documentation
Cybersecurity
Data Analysis
Agile Methodologies
Cloud Computing
Machine Learning and AI
Database Management
UX/UI Design
Networking
DevOps
Mobile Development
Quality Assurance
Version Control
Data Visualization
Web Development
Software Architecture
API Design and Integration
Systems Administration
Scripting
Performance Optimization
Test Automation
Big Data Analytics
Information Security
Front-end Development
Back-end Development
Data Modeling
Statistical Analysis
Natural Language Processing
Object-Oriented Programming
Software Testing
Continuous Integration/Continuous Deployment (CI/CD)
Cloud Architecture
Data Mining
Server Management
Virtualization Technologies
Technical Support
Algorithm Design
Distributed Systems
Mobile App Design
Usability Testing
Quality Management
Predictive Analytics
Data Warehousing
API Development
User Research
Data Cleansing
Information Retrieval
Embedded Systems
Software Deployment
Data Governance
Performance Monitoring
Network Security
Full-Stack Development
Software Refactoring
Machine Vision
Continuous Improvement
Scalability Design
Information Architecture
Ethical Hacking
Mobile Device Management
Software Debugging
Geospatial Analysis
Neural Networks
Systems Integration
Cross-functional Collaboration
Cloud Storage
Data Privacy
API Management
User Experience Optimization
Content Management Systems (CMS)
Front-end Frameworks (e.g., React, Angular)
Back-end Frameworks (e.g., Django, Laravel)
Business Intelligence
Data Science
IT Service Management
Systems Monitoring
UI/UX Prototyping
Quality Control
Data Encryption
Web Scraping
Natural Language Generation
Data Transformation
Mobile Security
Robotic Process Automation (RPA)
High Availability Systems
Cloud Orchestration
Data Storage Solutions
Continuous Delivery
Software Licensing
Data Backup and Recovery
Geolocation Services
API Security
Data Governance
"""
import os
import openai

def generate_mentor(mentee_skills: List[str]):
    mentee_matrix = np.array([[1 if skill in mentee_skills else 0 for skill in SKILLS]])
    new_m = np.concatenate([mentee_matrix, matrix], axis=0)
    distance_matrix = pairwise_distances(new_m, metric="cosine")
    distances = distance_matrix[-1,:-1]
    sorted_mentor_idx = np.argsort(distances)

    return [mentors.iloc[idx] for idx in sorted_mentor_idx[:5]]



def get_skills_from_bio(bio, num_of_skills):
    key = os.environ['openai_key']

    openai.api_key = key
    # Create prompt to ask.
    prompt = f"I have a bio of a person, can you extract the skills of this person please: {bio}. I would like the {num_of_skills} most demonstrated skills from this list: {skills} please. Remember, the skills you give me should be from the list I gave you please. Can the list be comma-separated please"#print(prompt)
    # Set up the message chain with just a single message where we (the user) ask the prompt.
    messages = [{"role": "user", "content": prompt}]
    failed_response = True
    counter = 0
    response = None
    while failed_response and counter < 10:
        try:
            counter += 1
            # Get the response via API call.
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.0)
            failed_response = False

        except:
            pass
        
    print(counter)
    if not response:
        returned_skills = ['Teamwork', 'Problem-solving', 'Critical Thinking']
        return returned_skills


    # Pull out the returned content.
    returned_skills = response.choices[0].message["content"]
    
    # Construct the output, a list of the skills.
    if "1." in returned_skills:
        list_of_skills = [item.split('. ')[1] for item in returned_skills.split('\n') if item]
    else:
        # Remove the full stop.
        returned_skills = returned_skills[:-1]
        list_of_skills = returned_skills.split(", ")
    
    return generate_mentor(list_of_skills)




