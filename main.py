from pawpal_system import Task, Pet, Owner, Scheduler


def main():
    # Create tasks with different times for each pet
    rex_tasks = [
        Task("Morning walk", "07:30", 30, "high", "daily"),
        Task("Vet checkup", "14:00", 60, "high", "weekly"),
    ]
    whiskers_tasks = [
        Task("Feed breakfast", "08:00", 15, "medium", "daily"),
    ]

    # Create at least two pets
    rex = Pet("Rex", "Labrador", 4, "none", tasks=rex_tasks)
    whiskers = Pet("Whiskers", "Tabby Cat", 2, "sensitive stomach", tasks=whiskers_tasks)

    # Create an owner with the pets
    owner = Owner("Alex", pets=[rex, whiskers], available_time="07:00-18:00")

    # Build the schedule

    scheduler = Scheduler(owner)

    print(f"Today's Schedule for {owner.name}")
    print("=" * 40)
    for line in scheduler.generate_plan():
        print(line)


if __name__ == "__main__":
    main()
