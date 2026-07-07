from datetime import date, timedelta
from typing import List, Optional, Tuple


def _to_minutes(time_str: str) -> int:
    """Convert a 'HH:MM' time string into minutes since midnight."""
    hours, minutes = time_str.split(":")
    return int(hours) * 60 + int(minutes)


class Task:
    def __init__(
        self,
        name: str,
        time: str,
        duration: int,
        priority: str,
        frequency: str,
        is_complete: bool = False,
        date: Optional[date] = None,
    ):
        self.name = name
        self.time = time
        self.duration = duration
        self.priority = priority
        self.frequency = frequency
        self.is_complete = is_complete
        self.date = date
    def mark_complete(self):
        self.is_complete =  True
        

class Pet:
    def __init__(
        self,
        name: str,
        breed: str,
        age: int,
        health_issues: str,
        tasks: List[Task] = None,
    ):
        self.name = name
        self.breed = breed
        self.age = age
        self.health_issues = health_issues
        self.tasks = tasks if tasks is not None else []

    def add_task(self, task: Task) -> None:
        """Attach a task to this pet."""
        self.tasks.append(task)


class Owner:
    def __init__(
        self,
        name: str,
        pets: List[Pet] = None,
        available_time: str = "",
    ):
        self.name = name
        self.pets = pets if pets is not None else []
        self.available_time = available_time


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def _all_tasks(self) -> List[Task]:
        """Collect every task belonging to each of the owner's pets."""
        tasks = []
        for pet in self.owner.pets:
            tasks.extend(pet.tasks)
        return tasks

    def sort_by_time(self) -> List[Task]:
        """Return all of the owner's tasks ordered from earliest to latest."""
        return sorted(self._all_tasks(), key=lambda task: _to_minutes(task.time))

    def detect_conflicts(self) -> List[Tuple[Task, Task]]:
        """Return pairs of tasks whose time windows overlap."""
        ordered = self.sort_by_time()
        conflicts = []
        for i in range(len(ordered)):
            for j in range(i + 1, len(ordered)):
                first, second = ordered[i], ordered[j]
                first_end = _to_minutes(first.time) + first.duration
                second_start = _to_minutes(second.time)
                if second_start < first_end:
                    conflicts.append((first, second))
        return conflicts

    def generate_plan(self) -> List[str]:
        """Build a readable, time-ordered plan explaining each scheduled task."""
        plan = []
        for task in self.filter_tasks():
            line = (
                f"{task.time} - {task.name} "
                f"({task.duration} min, {task.priority} priority)"
            )
            plan.append(line)

        conflicts = self.detect_conflicts()
        for first, second in conflicts:
            plan.append(
                f"⚠️ Conflict: '{first.name}' overlaps with '{second.name}'"
            )
        return plan

    def filter_tasks(self) -> List[Task]:
        """Return the time-ordered tasks that still need to be done."""
        return [task for task in self.sort_by_time() if not task.is_complete]

    def _find_pet(self, task: Task) -> Optional[Pet]:
        """Return the pet whose task list contains this task, if any."""
        for pet in self.owner.pets:
            if task in pet.tasks:
                return pet
        return None

    def complete_task(self, task: Task) -> Optional[Task]:
        """Mark a task complete and, for daily tasks, roll it over to tomorrow.

        Returns the newly created task scheduled for tomorrow, or None if the
        task was not a daily task (or its owning pet could not be found).
        """
        task.mark_complete()

        if task.frequency != "daily":
            return None

        pet = self._find_pet(task)
        if pet is None:
            return None

        tomorrow = date.today() + timedelta(days=1)
        next_task = Task(
            name=task.name,
            time=task.time,
            duration=task.duration,
            priority=task.priority,
            frequency=task.frequency,
            date=tomorrow,
        )
        pet.add_task(next_task)
        return next_task
