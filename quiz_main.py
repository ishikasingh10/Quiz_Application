from quiz_functions import slow_print, clear_screen, save_score, ask_question
from quiz_questions import questions
from colorama import init, Fore
import time
import random

init(autoreset=True)

def run_quiz():
    clear_screen()
    slow_print(Fore.MAGENTA + "✨ Welcome to the ULTIMATE QUIZ GAME ✨\n")
    time.sleep(1)

    player_name = input(Fore.YELLOW + "👤 Enter your name: ").strip().title()
    slow_print(Fore.GREEN + f"Hello {player_name}! Let's dive into the challenge! 🧠\n")
    time.sleep(2)

    slow_print(Fore.BLUE + "🎯 Rules:")
    slow_print(Fore.WHITE + "✅ One chance per question")
    slow_print("✅ Answer with a/b/c/d")
    slow_print("✅ Try to score high!\n")
    time.sleep(2)

    slow_print(Fore.CYAN + "🎮 Choose difficulty:")
    slow_print(Fore.WHITE + "1️⃣ Easy (no time limit)")
    slow_print("2️⃣ Hard (5-second limit per question)")

    difficulty = input(Fore.YELLOW + "Enter 1 or 2: ").strip()
    hard_mode = difficulty == "2"

    score = 0
    total = len(questions)
    random.shuffle(questions)

    for i, q in enumerate(questions):
        slow_print(Fore.LIGHTYELLOW_EX + f"\n📘 Question {i + 1} of {total}")
        score = ask_question(q[0], q[1], q[2], hard_mode, score)
        slow_print(Fore.YELLOW + f"📊 Score: {score}/{i + 1}\n")

    slow_print(Fore.CYAN + "\n⏳ Calculating final score...", 0.1)
    time.sleep(2)

    save_score(player_name, score, total)
    slow_print(Fore.GREEN + f"\n🏁 FINAL SCORE: {score}/{total}", 0.07)

    if score == total:
        slow_print(Fore.LIGHTMAGENTA_EX + "🌟 Perfect score! You're a genius! 🎉")
    elif score >= total // 2:
        slow_print(Fore.CYAN + "👍 Good job! Keep learning!")
    else:
        slow_print(Fore.RED + "😅 Better luck next time!")

    slow_print(Fore.GREEN + "\n🎉 Thanks for playing! Come back soon! 🎮")

if __name__ == "__main__":
    run_quiz()
