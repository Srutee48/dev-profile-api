from fastapi import FastAPI
import random

app = FastAPI()

facts = [
    "Python was named after Monty Python, not the snake.",
    "The first computer bug was an actual real bug — a moth.",
    "Git was created by Linus Torvalds in just 10 days.",
    "There are over 700 programming languages in existence.",
    "The first programmer in history was Ada Lovelace in the 1840s."
]

@app.get("/")
def home():
    return {
        "developer": "Swesu",
        "status": "building in public",
        "level": "rising"
    }

@app.get("/fact")
def get_fact():
    return {
        "fact": random.choice(facts)
    }