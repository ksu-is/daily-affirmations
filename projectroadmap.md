# Project Roadmap — Daily Affirmations

## Sprint 1 Goals
- [x] Choose project idea and mark "Go" in Teams
- [x] Create repo under `ksu-is`, add README.md
- [x] Add `projectroadmap.md` with task list
- [ ] Explore one similar Python repo and note takeaways
- [ ] Create minimal `daily_affirmations.py` with stub functions
- [ ] Commit at least once after editing README and roadmap

## Sprint 1 Tasks (assign to self)
- [ ] Create folders `data/` and `docs/`
- [ ] Add empty `data/log.csv` with header: `date,habit_1,habit_2,habit_3,notes`
- [ ] In `daily_affirmations.py` add:
  - [ ] `get_random_affirmation()` from a local list
  - [ ] `prompt_habits()` to ask y/n for 2–3 habits
  - [ ] `append_log_row()` to write a CSV row for today
- [ ] Test by running once and confirming `data/log.csv` updated
- [ ] Commit and push with message: `feat: initial stub + csv logging`

## Habits for now
- Habit 1: 10 minutes focused study
- Habit 2: Hydration check
- Habit 3: Evening reflection or stretch

## Related repository — quick evaluation
I reviewed a simple CLI habit tracker repository that logs daily completions to a CSV and prints summaries. It reinforces that a CSV approach is enough for Sprint 1 and keeps dependencies low. Their structure suggests separating prompt logic from file I/O which I will mirror for clean functions and easier testing.

**Repository reviewed:** I reviewed the open-source project [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python). It includes examples of user input, file handling, and daily logging, concepts that directly support my Daily Affirmations project. The repo helped me understand how to structure a simple CLI-based project and organize functions logically.

**Findings I will adopt**
- Use a fixed CSV header with ISO dates
- Keep a short list of 2–3 habits at first
- Keep functions small: one for prompting, one for saving

**What I will do differently**
- Include a daily affirmation before prompts to improve motivation
- Keep everything stdlib in Sprint 1 to avoid setup friction

## Future Sprint Ideas
- Streak calculation and basic charts with `matplotlib`
- Export the day’s affirmation to a small PNG for phone lock screen
- Optional GUI later (Tkinter) after core logic is solid

## Definition of Done for Sprint 1
- Repo exists under `ksu-is` with README and roadmap committed
- A stub `daily_affirmations.py` runs and creates or appends to `data/log.csv`
