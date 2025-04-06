import random
import time
import json
import os

def load_scores():
    if os.path.exists("scores.json"):
        with open("scores.json", "r") as f:
            return json.load(f)
    return []

def save_score(name, attempts, duration):
    scores = load_scores()
    scores.append({
        "name": name,
        "attempts": attempts,
        "time": round(duration, 2)
    })
    with open("scores.json", "w") as f:
        json.dump(scores, f, indent=4)

def display_leaderboard():
    scores = sorted(load_scores(), key=lambda x: (x['attempts'], x['time']))
    print("\n🏆 Leaderboard:")
    for index, entry in enumerate(scores[:5]):
        print(f"{index+1}. {entry['name']} - {entry['attempts']} tries in {entry['time']}s")

def game():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    name = input("Enter your name: ")
    print("Guess a number between 1 and 100...")

    start_time = time.time()

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                duration = time.time() - start_time
                print(f"🎉 Congrats {name}, you got it in {attempts} tries and {round(duration, 2)} seconds!")
                save_score(name, attempts, duration)
                break
        except ValueError:
            print("Please enter a valid number.")

    display_leaderboard()

if __name__ == "__main__":
    game()
