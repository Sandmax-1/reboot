from dataclasses import dataclass
from typing import List
from google.cloud import datastore
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances

with open("skills.txt") as f:
    SKILLS = list([i.strip() for i in f.readlines()])



def get_mentors():
    client = datastore.Client(project="de-idiomisers")
    query = client.query(kind="Mentor")
    
    mentors = []
    for result in query.fetch():
        mentors.append({
            "name": result.key.name, 
            "skills": result.get("skills"), 
            "bio": result.get("bio"), 
            "age": result.get("age")})

    return pd.DataFrame(mentors)


def generate_skills_matrix():

    people = get_mentors()

    num_people = len(people)
    num_skills = len(SKILLS)
    
    skills_matrix = np.zeros((num_people, num_skills))

    for index, person in people.iterrows():
        skills = person["skills"]
        skills_indices = [SKILLS.index(skill) for skill in skills]
        skills_matrix[index, skills_indices] = 1
    return skills_matrix




# def generate_mentor(mentee_skills: List[str], mentors_matrix: np.ndarray, mentors):
#     mentee_matrix = np.array([[1 if skill in mentee_skills else 0 for skill in SKILLS]])
#     new_m = np.concatenate([mentee_matrix, mentors_matrix], axis=0)
#     distance_matrix = pairwise_distances(new_m, metric="cosine")
#     distances = distance_matrix[-1,:-1]
#     sorted_mentor_idx = np.argsort(distances)

#     return [mentors.iloc[idx] for idx in sorted_mentor_idx[:5]]

matrix = generate_skills_matrix()
mentors = get_mentors()
# mentor = generate_mentor(["API Development", "User Research"], matrix, mentors)
