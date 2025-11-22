# Daily Affirmations — Project Roadmap

## Sprint 1 Goals
- [x] Choose project idea and mark "Go" in Teams
- [x] Create repo under `ksu-is`, add `README.md`
- [x] Add `projectroadmap.md` with task list
- [x] Explore one similar Python repo and note takeaways
- [x] Create minimal `daily_affirmations.py` with stub functions
- [x] Commit at least once after editing README and roadmap

## Sprint 1 Tasks
- [x] Create folders `data/` and `docs/`
- [x] Add `data/log.csv` with header: `date,habit_1,habit_2,habit_3,notes`
- [x] In `daily_affirmations.py` add:
  - [x] `get_affirmation()` from a local list
  - [x] `log_habits()` to ask y/n for 2–3 habits
  - [x] Write a CSV row for today
- [x] Test by running once and confirming `data/log.csv` updated
- [x] Commit and push with message: `feat: initial stub + csv logging`

## Habits for now
- Habit 1: 10 minutes focused study  
- Habit 2: Hydration check  
- Habit 3: Evening reflection or stretch  

## Related Repository — Quick Evaluation
Reviewed **30 Days of Python**: https://github.com/Asabeneh/30-Days-Of-Python  

**Takeaways**
- Organized by topic and easy to navigate  
- Clear comments and short, focused functions  
- Demonstrates lists, loops, and file handling effectively  

**How I applied it**
- Used small, clear functions in my own script  
- Added brief comments and logical file organization  
- Adopted simple Markdown documentation style  

## Definition of Done — Sprint 1
- [x] Repo exists under `ksu-is` with README and roadmap  
- [x] `daily_affirmations.py` runs and appends to `data/log.csv`  
- [x] One related repo reviewed and notes recorded here  

---

## Sprint 2 Summary
**Goal:** Begin coding and manage updates with Git.  

**Completed**
- [x] Added input validation (accepts only y/n for each habit)  
- [x] Added timestamp to each CSV log entry  
- [x] Tested entries multiple times and verified `data/log.csv` updates correctly  
- [x] Made 6+ commits with meaningful comments  
- [x] Updated README with run instructions and purpose  
- [x] Confirmed repository is active under `ksu-is` organization  

**Next Steps (Sprint 3)**
- [ ] Add a random daily affirmation message  
- [ ] Create a weekly summary command  
- [ ] Explore visualization (matplotlib or pandas)  

### Run Notes
Tested locally on Python 3.x. The script successfully created and appended multiple daily log entries with timestamps. Everything ran without errors.
