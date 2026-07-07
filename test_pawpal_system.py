"""Test cases for the PawPal system.

Run with:  python3 -m unittest test_pawpal_system -v
"""

import unittest
from datetime import date, timedelta

from pawpal_system import Task, Pet, Owner, Scheduler


class TestTask(unittest.TestCase):
    def test_mark_complete_sets_is_complete_true(self):
        task = Task("Morning walk", "07:30", 30, "high", "daily")
        self.assertFalse(task.is_complete)  # starts incomplete
        task.mark_complete()
        self.assertTrue(task.is_complete)  # now complete


class TestPet(unittest.TestCase):
    def test_add_task_increases_task_count(self):
        pet = Pet("Rex", "Labrador", 4, "none")
        self.assertEqual(len(pet.tasks), 0)
        pet.add_task(Task("Morning walk", "07:30", 30, "high", "daily"))
        self.assertEqual(len(pet.tasks), 1)
        pet.add_task(Task("Feed dinner", "18:00", 15, "medium", "daily"))
        self.assertEqual(len(pet.tasks), 2)

    def test_new_pet_has_independent_task_list(self):
        # Guards against a shared default list between pets.
        a = Pet("Rex", "Labrador", 4, "none")
        b = Pet("Milo", "Beagle", 2, "none")
        a.add_task(Task("Walk", "07:30", 30, "high", "daily"))
        self.assertEqual(len(b.tasks), 0)


class TestScheduler(unittest.TestCase):
    def _owner(self):
        rex = Pet("Rex", "Labrador", 4, "none", tasks=[
            Task("Morning walk", "07:30", 30, "high", "daily"),
            Task("Vet checkup", "14:00", 60, "high", "weekly"),
        ])
        whiskers = Pet("Whiskers", "Tabby", 2, "none", tasks=[
            Task("Feed breakfast", "08:00", 15, "medium", "daily"),
        ])
        return Owner("Alex", pets=[rex, whiskers])

    def test_sort_by_time_orders_across_pets(self):
        times = [t.time for t in Scheduler(self._owner()).sort_by_time()]
        self.assertEqual(times, ["07:30", "08:00", "14:00"])

    def test_filter_tasks_excludes_completed(self):
        owner = self._owner()
        owner.pets[0].tasks[0].mark_complete()  # complete the 07:30 walk
        remaining = [t.name for t in Scheduler(owner).filter_tasks()]
        self.assertNotIn("Morning walk", remaining)
        self.assertEqual(len(remaining), 2)

    def test_detect_conflicts_flags_overlap(self):
        pet = Pet("Rex", "Labrador", 4, "none", tasks=[
            Task("Walk", "07:00", 60, "high", "daily"),    # ends 08:00
            Task("Grooming", "07:30", 30, "medium", "daily"),  # overlaps
        ])
        conflicts = Scheduler(Owner("Alex", pets=[pet])).detect_conflicts()
        self.assertEqual(len(conflicts), 1)

    def test_no_false_conflict_when_back_to_back(self):
        pet = Pet("Rex", "Labrador", 4, "none", tasks=[
            Task("Walk", "07:00", 30, "high", "daily"),   # ends 07:30
            Task("Feed", "07:30", 15, "medium", "daily"),  # starts 07:30
        ])
        conflicts = Scheduler(Owner("Alex", pets=[pet])).detect_conflicts()
        self.assertEqual(len(conflicts), 0)

    def test_complete_daily_task_rolls_over_to_tomorrow(self):
        rex = Pet("Rex", "Labrador", 4, "none", tasks=[
            Task("Morning walk", "07:30", 30, "high", "daily"),
        ])
        whiskers = Pet("Whiskers", "Tabby", 2, "none", tasks=[
            Task("Feed breakfast", "08:00", 15, "medium", "daily"),
        ])
        owner = Owner("Alex", pets=[rex, whiskers])
        original = rex.tasks[0]

        new_task = Scheduler(owner).complete_task(original)

        # A new task was created and returned.
        self.assertIsNotNone(new_task)
        # It is scheduled for tomorrow.
        self.assertEqual(new_task.date, date.today() + timedelta(days=1))
        # It landed on the correct pet (Rex), not Whiskers.
        self.assertIn(new_task, rex.tasks)
        self.assertNotIn(new_task, whiskers.tasks)
        self.assertEqual(len(rex.tasks), 2)
        self.assertEqual(len(whiskers.tasks), 1)
        # It mirrors the original task's details but is not complete.
        self.assertEqual(new_task.name, "Morning walk")
        self.assertEqual(new_task.time, "07:30")
        self.assertFalse(new_task.is_complete)
        # The original task is now marked complete.
        self.assertTrue(original.is_complete)


if __name__ == "__main__":
    unittest.main(verbosity=2)
