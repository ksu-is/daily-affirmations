# daily-affirmations
Python app for daily affirmations and habit tracking

## Why this project
- Simple daily check-in to stay positive and consistent  
- CSV storage keeps it beginner-friendly and transparent  
- Easy to expand later with summaries or charts  

---

## Project Progress Overview
### Sprint 1
- Set up GitHub repository and basic project structure  
- Created README and roadmap files  
- Added starter code for habit logging and CSV setup  
- Reviewed related Python repositories  

### Sprint 2
- Added input validation (y/n answers only)  
- Added timestamps to CSV log entries  
- Updated roadmap and README  
- Made multiple commits documenting progress  

### Sprint 3
- Cleaned code formatting and comments  
- Prepared for random affirmation feature  
- Created project marketing PowerPoint slide  
- Uploaded slide to GitHub for documentation  

---

## Current Features
- Prints a random daily affirmation from a local list  
- Prompts user to mark 2–3 daily habits as done  
- Saves progress with date, habits, and notes in `data/log.csv`  
- Input validation for y/n answers  
- Records timestamp for each entry  

---

## Planned Features
- View progress by week or month  
- Add random daily affirmation from external file  
- Show simple charts using `matplotlib`  
- Optional lock-screen export with daily quote  

---

## Tech Stack
- Python 3.11+  
- Standard library only (`csv`, `datetime`, `random`, `pathlib`)  
- Optional later: `pandas`, `matplotlib`, `Pillow`  

---

## Example Usage
```bash
python daily_affirmations.py
# => "I am doing my best and improving every day."
# Prompts: "Did you complete Habit 1 today? (y/n)"
