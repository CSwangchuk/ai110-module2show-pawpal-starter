import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to **PawPal+**, a pet care planning assistant. Set up your owner profile,
add pets and their care tasks, then generate a time-ordered daily plan.
"""
)

with st.expander("Scenario", expanded=False):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

st.divider()

# --- Persist the Owner object across reruns ---
if "owner" not in st.session_state:
    st.session_state.owner = None

st.subheader("1. Owner")
owner_name = st.text_input("Owner name", value="Jordan")
available_time = st.text_input("Available time window", value="07:00-18:00")

if st.button("Create / update owner"):
    if st.session_state.owner is None:
        st.session_state.owner = Owner(owner_name, available_time=available_time)
    else:
        # Keep existing pets, just refresh the owner's details.
        st.session_state.owner.name = owner_name
        st.session_state.owner.available_time = available_time
    st.success(f"Owner '{owner_name}' ready.")

owner = st.session_state.owner

if owner is None:
    st.info("Create an owner above to get started.")
    st.stop()

st.divider()

# --- Add pets to the owner ---
st.subheader("2. Pets")
col1, col2 = st.columns(2)
with col1:
    pet_name = st.text_input("Pet name", value="Mochi")
    breed = st.text_input("Breed", value="Shiba Inu")
with col2:
    age = st.number_input("Age (years)", min_value=0, max_value=40, value=3)
    health_issues = st.text_input("Health issues", value="none")

if st.button("Add pet"):
    owner.pets.append(Pet(pet_name, breed, int(age), health_issues))
    st.success(f"Added pet '{pet_name}'.")

if not owner.pets:
    st.info("Add at least one pet to start scheduling tasks.")
    st.stop()

st.write("Current pets:")
st.table(
    [
        {
            "name": pet.name,
            "breed": pet.breed,
            "age": pet.age,
            "health_issues": pet.health_issues,
            "tasks": len(pet.tasks),
        }
        for pet in owner.pets
    ]
)

st.divider()

# --- Add tasks to a chosen pet ---
st.subheader("3. Tasks")
pet_names = [pet.name for pet in owner.pets]
selected_pet_name = st.selectbox("Assign task to pet", pet_names)

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
    task_time = st.text_input("Time (HH:MM)", value="07:30")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    frequency = st.selectbox("Frequency", ["daily", "weekly", "monthly"])
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    selected_pet = next(pet for pet in owner.pets if pet.name == selected_pet_name)
    selected_pet.add_task(
        Task(task_title, task_time, int(duration), priority, frequency)
    )
    st.success(f"Added '{task_title}' to {selected_pet_name}.")

st.divider()

# --- Generate the schedule via the Scheduler ---
st.subheader("4. Build Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner)
    plan = scheduler.generate_plan()
    if not plan:
        st.info("No tasks to schedule yet. Add some tasks above.")
    else:
        st.markdown(f"### Today's Schedule for {owner.name}")
        for line in plan:
            st.write(line)
