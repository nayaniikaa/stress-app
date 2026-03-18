import streamlit as st
import time
st.progress((st.session_state.task_step + 1) / len(tasks))
st.title(" Reset Your State")

tasks = [
    ("Stretch 1: Arms Up", "Raise both arms above your head and stretch upward.", 10),
    ("Stretch 2: Neck Roll", "Slowly roll your neck clockwise.", 8),
    ("Stretch 3: Shoulder Roll", "Roll your shoulders backward slowly.", 10),
    ("Stretch 4: Forward Bend", "Bend forward and let your arms hang loose.", 10),

    ("Breathing Reset", "Take slow deep breaths.", 30),
    
    ("Hydrate", "Take a sip of water slowly.", 0),

    ("Vision Break", "Look at something far away and relax your eyes.", 10),

    ("Posture Reset", "Sit straight and relax your shoulders.", 10)
]

if "task_step" not in st.session_state:
    st.session_state.task_step = 0

if st.session_state.task_step < len(tasks):
    title, instruction, duration = tasks[st.session_state.task_step]

    st.subheader(title)
    st.write(instruction)

    # WITH TIMER
    if duration > 0:
        if st.button("Start"):
            placeholder = st.empty()

            for i in range(duration, 0, -1):
                placeholder.markdown(f"### ⏳ {i} seconds")
                time.sleep(1)

            st.success("✅ Done!")

    # WITHOUT TIMER (like water)
    else:
        if st.button("Done"):
            st.success("💧 Good. Stay hydrated.")

    # NEXT BUTTON
    if st.button("Next"):
        st.session_state.task_step += 1
        st.rerun()

else:
    st.success("🔥 You reset your state. Great job!")
    st.balloons()
