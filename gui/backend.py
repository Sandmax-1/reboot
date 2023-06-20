skills = """
Teamwork skills
Interpersonal skills
Empathy/compassion
Active listening
Patience
Understanding body language
Ability to quickly build relationships
Team building
Diplomacy
Persuasion
Conflict resolution
Reconciliation
Personable
Customer service skills
Positive attitude
Respectful
Proper business etiquette
Capable of networking
Capable of mentoring/teaching
Ability to collaborate
Capable of exchanging ideas
Encourages other team members
A sense of humour
Client-oriented
Time management
Decision-making skills
Planning
Task delegation skills
Flexibility
Ability to multitask
Punctuality
Capable of meeting deadlines
Scheduling
Capable of prioritising tasks
Problem-solving skills
Creative thinking
Critical thinking
Quick learner
Attention to detail
Focus
Attentive
Rational
Ability to brainstorm
Inspiration
Desire to experiment with new ideas
Meticulous
Deductive reasoning (top-down thinking)
Inductive reasoning (bottom-down thinking)
Modesty
Observant
Introspection
Self-aware
High energy
Dedication
Knows how to follow instructions
A good work ethic
Loyalty
Integrity
Reliable
Disciplined
Committed
Honesty
Thoughtful
Enthusiasm
Adaptability
Stress management
Ability to negotiate
Public speaking
Trustworthiness
Ability to handle criticism
Efficiency
Innovation
Control over emotions
Resilience
Ambition
Presentation skills
Capable of giving feedback
Inspiring
Assertive
Resourceful
Determination
Self-confident
Responsible
Self-management
Open-minded
Diligent
Insightful
Capable of questioning ideas
Self-control
Know when to take responsibility
Independent
Physical endurance/stamina
Motivation
Computer skills
Tolerant of change
Aware of social issues
Love to learn/curious
Culturally sensitive
A solid understanding of social media
"""
import os
import openai

def get_skills_from_bio(bio, num_of_skills):
    key = os.environ['openai_key']

    openai.api_key = key
    # Create prompt to ask.
    prompt = f" I have a bio of a person, can you extract the skills of this person please: {bio}. I would like the {num_of_skills} most demonstrated skills from this list: {skills} please. Remember, the skills you give me should be from the list I gave you please. Can the list be comma-separated please"
    #print(prompt)
    # Set up the message chain with just a single message where we (the user) ask the prompt.
    messages = [{"role": "user", "content": prompt}]
    
    # Get the response via API call.
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, temperature=0.0)

    # Pull out the returned content.
    returned_skills = response.choices[0].message["content"]
    
    # Construct the output, a list of the skills.
    if "1." in returned_skills:
        list_of_skills = [item.split('. ')[1] for item in returned_skills.split('\n') if item]
    else:
        # Remove the full stop.
        returned_skills = returned_skills[:-1]
        list_of_skills = returned_skills.split(", ")
    
    return list_of_skills