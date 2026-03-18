import streamlit as st

st.title("🧠 Grounding Exercise")

steps = [
    ("5 things you can see", 5),
    ("4 things you can feel", 4),
    ("3 things you can hear", 3),
    ("2 things you can smell", 2),
    ("1 thing you can taste", 1),
]

if "g_step" not in st.session_state:
    st.session_state.g_step = 0

# Current step
if st.session_state.g_step < len(steps):
    question, count = steps[st.session_state.g_step]

    st.subheader(question)

    inputs = []
    valid = True

    for i in range(count):
        value = st.text_input(f"Item {i+1}", key=f"{st.session_state.g_step}_{i}")
        inputs.append(value)
        if value.strip() == "":
            valid = False

    if valid:
        if st.button("Next"):
            st.session_state.g_step += 1
            st.rerun()
    else:
        st.warning("Please fill all fields before continuing.")

else:
    st.success("✨ You're grounded. Well done.")