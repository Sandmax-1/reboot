from typing import List
import openai
import random
from google.cloud import datastore

CITIES = ["London", "Bristol", "Leicester", "Birmingham", "Newport", "Cardiff", "Edinburgh", "Bath", "Slough"]

with open("skills.txt") as f:
    SKILLS = list([i.strip() for i in f.readlines()])


def chat_gpt_client(prompt, temp=0):
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", max_tokens=100, temperature=temp,messages=[{"role":"user", "content": prompt}])
    return completion.choices[0].message["content"]


def create_mentor(count):
    gender = random.choice(["Male", "Female"])
    age = random.randint(18, 70)
    city = random.choice(CITIES)
    skills = random.sample(SKILLS, 10)
    name = chat_gpt_client(f"Give me a single {gender} full name with 2 words", temp=1.5)
    if len(name.strip().split(" ")) > 2:
        print("skipping name ", name, len(name.strip().split(" ")))
        return
    bio_prompt = f"""You are {name}, a {age} year old {gender} living in {city}, you have the following skill: {", ".join(skills)}, give a short first person sentence about a {gender} person who is {age} years old who works in data, specify a few of their interests. Only the bio"""
    
    person_key = datastore_client.key("Mentor", name)
    person = datastore.Entity(key=person_key)
    
    person['bio'] = chat_gpt_client(bio_prompt, temp=1)  
    person['gender'] = gender
    person['city'] = city
    person['age'] = age
    person['skills'] = skills

    print(f"loading {name} into datastore")
    datastore_client.put(person)



def generate_mentors(count):

    from multiprocessing.pool import ThreadPool
    pool = ThreadPool(processes=1)

    mentors = []

    with ThreadPool(50) as pool:
        for result in pool.map(create_mentor, range(count)):
            mentors.append(result)

    return mentors


# if __name__ == "__main__":
#     datastore_client = datastore.Client(project="de-idiomisers")
#     mentors = generate_mentors(50)
