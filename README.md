# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Today's Schedule for Alex
========================================
07:30 - Morning walk (30 min, high priority)
08:00 - Feed breakfast (15 min, medium priority)
14:00 - Vet checkup (60 min, high priority)


```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:

pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
test_add_task_increases_task_count (test_pawpal_system.TestPet.test_add_task_increases_task_count) ... ok
test_new_pet_has_independent_task_list (test_pawpal_system.TestPet.test_new_pet_has_independent_task_list) ... ok
test_complete_daily_task_rolls_over_to_tomorrow (test_pawpal_system.TestScheduler.test_complete_daily_task_rolls_over_to_tomorrow) ... ok
test_detect_conflicts_flags_overlap (test_pawpal_system.TestScheduler.test_detect_conflicts_flags_overlap) ... ok
test_filter_tasks_excludes_completed (test_pawpal_system.TestScheduler.test_filter_tasks_excludes_completed) ... ok
test_no_false_conflict_when_back_to_back (test_pawpal_system.TestScheduler.test_no_false_conflict_when_back_to_back) ... ok
test_sort_by_time_orders_across_pets (test_pawpal_system.TestScheduler.test_sort_by_time_orders_across_pets) ... ok
test_mark_complete_sets_is_complete_true (test_pawpal_system.TestTask.test_mark_complete_sets_is_complete_true) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.000s
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting |Scheduler.sort_by_time() | Sorts tasks earliest to latest |
| Filtering | Scheduler.filter_tasks()| Skips completed tasks |
| Conflict handling | Scheduler.detect_conflicts() | Flags overlapping time windows|
| Recurring tasks |Scheduler.complete_task() | Rolls daily tasks over to tomorrow|

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1.Open PawPal+.
2.Enter owner information.
3.Add pet Mochi.
4.Add Morning Walk at 07:30.
5.Add Vet Medication at 07:30 to demonstrate conflict detection.
6.Show the overlap warning.
7.Change the medication time to 08:00.
8.Rebuild the schedule.
9.Mark the walk as completed.
10.Finish by highlighting the organized daily schedule and progress tracking.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
