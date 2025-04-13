import time
import random
import os

def slow_print(text, delay=0.05):
    """Prints text with a slight delay for animation effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    """Clears the screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

def save_score(player_name, score, total_questions):
    """Saves the player's score to a text file."""
    with open("quiz_scores.txt", "a") as file:
        file.write(f"{player_name}: {score}/{total_questions}\n")

def ask_question(question, options, correct_answer, hard_mode, score):
    """Handles asking questions and checking answers."""
    slow_print(f"\n{question}", 0.03)
    random.shuffle(options)
    
    for option in options:
        slow_print(option, 0.02)
    print("\n")

    start_time = time.time()
    answer = input("Your answer: ").strip().lower()
    
    if hard_mode and time.time() - start_time > 5:
        slow_print("⏳ Time's up! ❌", 0.03)
        slow_print(f"The correct answer was {correct_answer.upper()}.", 0.03)
        return score

    if answer == correct_answer:
        responses = ["✅ Correct! Great job! 🎉", "👏 Nice work!", "🎯 Spot on!", "🔥 You're on fire!", "💪 Keep going!"]
        slow_print(random.choice(responses) + "\n", 0.03)
        score += 1
    else:
        slow_print("❌ Oops! That’s incorrect.", 0.03)
        slow_print(f"The correct answer was {correct_answer.upper()}.", 0.03)
    
    time.sleep(2)
    return score
