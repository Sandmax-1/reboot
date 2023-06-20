from google.cloud import datastore
import tqdm
from generate_mentors import generate_mentors

# Instantiates a client
datastore_client = datastore.Client(project="de-idiomisers")

mentors = generate_mentors(100)

for mentor in tqdm.tqdm(mentors):
    
    person_key = datastore_client.key("Mentor", mentor.name)
    person = datastore.Entity(key=person_key)
    
    person['bio'] = mentor.bio
    person['gender'] = mentor.gender
    person['city'] = mentor.city
    person['skills'] = mentor.skills

    print(f"loading {mentor.name} into datastore")

    datastore_client.put(person)

