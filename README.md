# daily-affirmations
Python app for daily affirmations and habit tracking

## Why this project
- Quick daily check-in that supports mood and consistency
- CSV storage keeps it beginner-friendly and transparent
- Easy to extend in later sprints with graphs or a tiny GUI

## Core features (Sprint 1 scope)
- Print a random affirmation from a local list
- Prompt the user to mark habits as done for today
- Save results to `data/log.csv` with date, habits, and notes

## Planned features
- View progress by week or month
- Show current streaks per habit
- Simple charts using `matplotlib`
- Optional lock-screen PNG export with the day’s affirmation

## Tech stack
- Python 3.11+
- Standard library only for Sprint 1 (csv, datetime, random)
- Optional later: pandas, matplotlib, Pillow

## Example usage (future)
```bash
python daily_affirmations.py
# => "I am consistent. Small steps add up."
# Prompts: "Did you complete Habit A today? (y/n)"
