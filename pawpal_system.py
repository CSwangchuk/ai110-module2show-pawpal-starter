from typing import List


class Task:
    def __init__(
        self,
        name: str,
        time: str,
        duration: int,
        priority: str,
        frequency: str,
        is_complete: bool = False,
    ):
        self.name = name
        self.time = time
        self.duration = duration
        self.priority = priority
        self.frequency = frequency
        self.is_complete = is_complete


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

    def sort_by_time(self) -> List[Task]:
        pass

    def detect_conflicts(self) -> List:
        pass

    def generate_plan(self) -> List:
        pass

    def filter_tasks(self) -> List[Task]:
        pass
