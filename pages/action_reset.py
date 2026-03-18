import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("<h1 style='text-align:center;'> Reset Your State</h1>", unsafe_allow_html=True)

# TASKS (title, instruction, duration)
tasks = [
    ("Stretch: Arms Up", "Raise both arms above your head and stretch upward.", 10),
    ("Stretch: Neck Roll", "Slowly roll your neck clockwise.", 8),
    ("Stretch: Shoulder Roll", "Roll your shoulders backward slowly.", 10),
    ("Stretch: Forward Bend", "Bend forward and let your arms hang loose.", 10),

    ("Breathing Reset", "Take slow deep breaths.", 15),

    ("Hydrate", "Take a sip of water slowly.", 0),

    ("Vision Break", "Look at something far away and relax your eyes.", 10),

    ("Posture Reset", "Sit straight and relax your shoulders.", 10)
]

# SESSION STATE
if "task_step" not in st.session_state:
    st.session_state.task_step = 0

# PROGRESS BAR
st.progress((st.session_state.task_step ) / len(tasks))

# TASK FLOW
if st.session_state.task_step < len(tasks):
    title, instruction, duration = tasks[st.session_state.task_step]

    st.subheader(title)
    st.write(instruction)

    # TIMER TASKS
    if duration > 0:
        if st.button("Start", use_container_width=True):
            placeholder = st.empty()

            for i in range(duration, 0, -1):
                placeholder.markdown(f"### ⏳ {i} seconds")
                time.sleep(1)

            st.success("✅ Done!")

    # NON-TIMER TASK (water)
    else:
        if st.button("Done", use_container_width=True):
            st.success("💧 Good. Stay hydrated.")

    # NEXT BUTTON
    if st.button("Next →", use_container_width=True):
        st.session_state.task_step += 1
        st.rerun()

# COMPLETION
else:
    st.balloons()
    st.success("🔥 You reset your state. Great job!")

    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state.clear()
        st.switch_page("app.py")
