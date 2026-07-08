# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
    These are the classes I inlcuded and will be the initial UML design
    Task: This is the task such as walking, grooming etc and will have these attributes
        name
        time
        duration
        priority
        frequency
        is_complete
        
    Pet: This class holds the information about the pet such as name breed age etc and also includes a task attribute which hold information about the tasks the pet will be doing 
        name
        breed
        age
        health_issues
        tasks
    Owner: This is the owner class and holds name pet the owner has and the owners available time
        name
        pets
        available_time
    Scheduler: This is the brain of the of app as it schedules everything taking in the information and displaying it as the user needs
        sort_by_time()
        detect_conflicts()
        generate_plan()
        filter_tasks()

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
yes i changed and added owner as an attribute to Scheduler as schedule needs the owners details to make the schedule 
Task — added date attribute and mark_complete() method
Pet — added add_task() method
Scheduler — added complete_task() and _find_pet() methods
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
the scheduler looks and the task and it makes sure the schedule is sorted in time like task are in order and completed tasks are not shown again and tasks shouldn't overlap

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
My scheduler warns about conflicts but does not prevent the user from scheduling them. This is reasonable because the owner might have free time or have someone else helping them.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
Design brainstorming — i used claude chat to think through what attributes and methods each class needed before writing any code
Code generation - I used Claude Code to generate class skeletons, implement methods, and write tests
Verification — I used claude chat to review and understand what Claude Code gave you before accepting it
Debugging — Claude Code helped fix the file naming issue and wire the UI to my backend




**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
Claude Code initially encoded the date into the task name (e.g. 'Morning walk (2026-07-07)') but I rejected this and asked it to add a proper date attribute to the Task class instead, as it was cleaner and more maintainable.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
I tested behaviors such as test_mark_complete_sets_is_complete_true
test_add_task_increases_task_count
test_detect_conflicts_flags_overlap
test_complete_daily_task_rolls_over_to_tomorrow. These tests were important because if these weren't there we wouldn't be able to alter the app and it could also crash the system."

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I am  4 out of 5 confident the scheduler works because i did some test cases . If I had more time I would test everything again to make sure everything is correct .

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
begin able to run it without any errors

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
i would desgin the mark_complete method 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
it is important to run test cases to make sure the system works and does not have any bugs moreover you need to make sure to verify the codes properly

