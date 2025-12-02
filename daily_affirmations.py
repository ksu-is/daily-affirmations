# daily_affirmations.py
# Author: Abigail Henderson
# Simple app to show a random daily affirmation and log habits
# Sprint 3 update: cleaned formatting and preparing for random affirmation feature

import csv
import random
from datetime import date, datetime
from pathlib import Path

affirmations = [
    "I am doing my best and improving every day.",
    "Progress is progress, no matter how small.",
    "I am capable of achieving my goals.",
    "Today I’ll focus on what I can control.",
    "Consistency matters more than perfection."
]

habits = [
    "Drank enough water",
    "Studied or read today",
    "Took a walk or stretched"
]

data_folder = Path("data")
log_file = data_folder / "log.csv"

def get_affirmation():
    """Return a random daily affirmation."""
    return random.choice(affirmations)

def log_habits():
    """Prompt user for habit completion and log results."""
    results = []
    print("\nCheck off today's habits (y/n):")
    for h in habits:
        while True:
            ans = input(f"- {h}: ").strip().lower()
            if ans in ["y", "n"]:
                break
            print("Please enter y or n.")
        results.append(ans)

    note = input("Any quick note for today? ").strip()

    data_folder.mkdir(exist_ok=True)
    new_file = not log_file.exists()
    with open(log_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["date"] + habits + ["note"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S")] + results + [note])

    print("Entry saved!\n")

def show_summary():
    """Display last few entries from the log file."""
    if not log_file.exists():
        print("No log found yet.")
        return
    print("\nRecent entries:\n")
    with open(log_file, encoding="utf-8") as f:
        lines = f.readlines()[-5:]
        for line in lines:
            print(line.strip())

def main():
    """Main app flow."""
    print("\n--- Daily Affirmations ---")
    print(get_affirmation())
    print("---------------------------")
    log_habits()
    see_summary = input("View summary? (y/n): ").strip().lower()
    if see_summary == "y":
        show_summary()

if __name__ == "__main__":
    main()
