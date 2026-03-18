import streamlit as st

st.set_page_config(page_title="AI Stress Assistant")

st.title("🧠 AI Stress Coping Assistant")

# Initialize session
if "step" not in st.session_state:
    st.session_state.step = 1


# DECISION LOGIC
def choose_method(body, state, intensity):
    if body == "chest" or intensity == "severe":
        return "breathing"
    elif state == "Overthinking" or body == "head":
        return "grounding"
    elif state == "Low mood":
        return "reframing"
    else:
        return "action"


# STEP 1: Emotion selection
if st.session_state.step == 1:
    st.write("How are you feeling right now?")

    emotions = [
        "Stressed", "Anxious", "Overwhelmed", "Sad", "Angry",
        "Tired", "Confused", "Panicking", "Low", "Frustrated"
    ]

    cols = st.columns(2)

    for i, emotion in enumerate(emotions):
        if cols[i % 2].button(emotion):
            st.session_state.feeling = emotion
            st.session_state.step = 2
            st.rerun()


# STEP 2: Body
elif st.session_state.step == 2:
    st.write("Where do you feel it in your body?")

    if st.button("Chest"):
        st.session_state.body = "chest"
        st.session_state.step = 3
        st.rerun()

    if st.button("Head"):
        st.session_state.body = "head"
        st.session_state.step = 3
        st.rerun()

    if st.button("Shoulders"):
        st.session_state.body = "shoulders"
        st.session_state.step = 3
        st.rerun()

    if st.button("Stomach"):
        st.session_state.body = "stomach"
        st.session_state.step = 3
        st.rerun()


# STEP 3: Intensity
elif st.session_state.step == 3:
    st.write("How intense is it?")

    if st.button("Mild"):
        st.session_state.intensity = "mild"
        st.session_state.step = 4
        st.rerun()

    if st.button("Moderate"):
        st.session_state.intensity = "moderate"
        st.session_state.step = 4
        st.rerun()

    if st.button("Severe"):
        st.session_state.intensity = "severe"
        st.session_state.step = 4
        st.rerun()


# STEP 4: Mental state
elif st.session_state.step == 4:
    st.write("What best describes your state?")

    states = ["Overthinking", "Tired", "Panicking", "Low mood", "Restless"]

    for s in states:
        if st.button(s):
            st.session_state.state = s
            st.session_state.step = 5
            st.rerun()


# STEP 5: Result
elif st.session_state.step == 5:
    method = choose_method(
        st.session_state.body,
        st.session_state.state,
        st.session_state.intensity
    )

    st.subheader("🧾 Analysis")

    st.write(
        f"You are feeling **{st.session_state.feeling}**, "
        f"with **{st.session_state.intensity} intensity**, "
        f"showing as **{st.session_state.state}**, "
        f"and tension in your **{st.session_state.body}**."
    )

    st.divider()

    # ROUTING
    if method == "breathing":
        st.success("Best approach: Calm your body with breathing.")
        if st.button("Start Breathing Exercise"):
            st.switch_page("pages/breathing.py")

    elif method == "grounding":
        st.success("Best approach: Ground your senses.")
        if st.button("Start Grounding Exercise"):
            st.switch_page("pages/grounding.py")

    elif method == "reframing":
        st.success("Best approach: Reframe your thoughts.")
        if st.button("Start Thought Reframing"):
            st.switch_page("pages/reframing.py")

    else:
        st.success("Best approach: Reset your state with action.")
        if st.button("Start Action Reset"):
            st.switch_page("pages/action_reset.py")