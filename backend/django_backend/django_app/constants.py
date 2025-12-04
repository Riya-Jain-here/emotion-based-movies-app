import random

MOVIES = {
    "happy": [
        "Zindagi Na Milegi Dobara", "3 Idiots", "Yeh Jawaani Hai Deewani",
        "The Intern", "Paddington"
    ],
    "sad": [
        "Taare Zameen Par", "The Pursuit of Happyness", "Dear Zindagi",
        "Lion", "Marley & Me"
    ],
    "angry": [
        "Joker", "John Wick", "KGF", "Mad Max: Fury Road", "Gladiator"
    ],
    "fear": [
        "The Conjuring", "IT", "The Nun", "A Quiet Place", "Hereditary"
    ],
    "calm": [
        "Life of Pi", "Soul", "The Hundred-Foot Journey", "Into the Wild", "The Lunchbox"
    ],
    "stressed": [
        "The Social Dilemma", "Up in the Air", "The Devil Wears Prada",
        "Inside Out", "Good Will Hunting"
    ],
    "surprised": [
        "Inception", "Interstellar", "Arrival", "Now You See Me", "The Sixth Sense"
    ],
}

def recommend(emotion:str, k:int=3):
    candidates=MOVIES.get(emotion, [])
    if not candidates:
        return []
    if k>=len(candidates):
        return random.sample(candidates, len(candidates))
    return random.sample(candidates, k)
    
