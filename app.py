import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Stress Assistant",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Animated background */
body {
    background: linear-gradient(-45deg, #0f172a, #1e293b, #020617, #1e293b);
    background-size: 400% 400%;
    animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Glass card */
.block-container {
    background: rgba(15, 23, 42, 0.6);
    padding: 2rem;
    border-radius: 18px;
    backdrop-filter: blur(12px);
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 14px;
    padding: 12px;
    font-size: 16px;
    background: rgba(30, 41, 59, 0.8);
    color: white;
    border: 1px solid #334155;
    transition: all 0.25s ease;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: #334155;
    border: 1px solid #64748b;
}

/* Headings */
h1, h2, h3 {
    text-align: center;
    color: white;
}

p {
    text-align: center;
    color: #94a3b8;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<h1> AI Stress Coping Assistant</h1>
<p>Understand your stress. Reset your mind. Take control.</p>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------------- PROGRESS BAR ----------------
total_steps = 5
progress = st.session_state.step / total_steps
st.progress(progress)

# ---------------- LOGIC ----------------
def choose_method(body, state, intensity):
    if body == "chest" or intensity == "severe":
        return "breathing"
    elif state == "Overthinking" or body == "head":
        return "grounding"
    elif state == "Low mood":
        return "reframing"
    else:
        return "action"

# ---------------- STEP 1 ----------------
if st.session_state.step == 1:
    st.markdown("### How are you feeling right now?")

    emotions = [
        "Stressed", "Anxious", "Overwhelmed", "Sad", "Angry",
        "Tired", "Confused", "Panicking", "Low", "Frustrated"
    ]

    cols = st.columns(2)

    for i, emotion in enumerate(emotions):
        if cols[i % 2].button(emotion, use_container_width=True):
            st.session_state.feeling = emotion
            st.session_state.step = 2
            st.toast("Got it 👍")
            st.rerun()

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    st.markdown("### Where do you feel it in your body?")

    options = ["Chest", "Head", "Shoulders", "Stomach"]
    cols = st.columns(2)

    for i, opt in enumerate(options):
        if cols[i % 2].button(opt, use_container_width=True):
            st.session_state.body = opt.lower()
            st.session_state.step = 3
            st.toast("Noted ✔")
            st.rerun()

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    st.markdown("### How intense is it?")

    options = ["Mild", "Moderate", "Severe"]

    for opt in options:
        if st.button(opt, use_container_width=True):
            st.session_state.intensity = opt.lower()
            st.session_state.step = 4
            st.toast("Okay 👍")
            st.rerun()

# ---------------- STEP 4 ----------------
elif st.session_state.step == 4:
    st.markdown("### What best describes your state?")

    states = ["Overthinking", "Tired", "Panicking", "Low mood", "Restless"]

    for s in states:
        if st.button(s, use_container_width=True):
            st.session_state.state = s
            st.session_state.step = 5
            st.toast("Almost there 🔥")
            st.rerun()

# ---------------- STEP 5 ----------------
elif st.session_state.step == 5:
    method = choose_method(
        st.session_state.body,
        st.session_state.state,
        st.session_state.intensity
    )

    st.markdown("### 🧾 Your Analysis")

    st.info(
        f"You are feeling **{st.session_state.feeling}**, "
        f"with **{st.session_state.intensity} intensity**, "
        f"showing as **{st.session_state.state}**, "
        f"and tension in your **{st.session_state.body}**."
    )

    st.divider()

    if method == "breathing":
        st.success("Best approach: Calm your body with breathing.")
        if st.button("Start Breathing Exercise", use_container_width=True):
            st.switch_page("pages/breathing.py")

    elif method == "grounding":
        st.success("Best approach: Ground your senses.")
        if st.button("Start Grounding Exercise", use_container_width=True):
            st.switch_page("pages/grounding.py")

    elif method == "reframing":
        st.success("Best approach: Reframe your thoughts.")
        if st.button("Start Thought Reframing", use_container_width=True):
            st.switch_page("pages/reframing.py")

    else:
        st.success("Best approach: Reset your state with action.")
        if st.button("Start Action Reset", use_container_width=True):
            st.switch_page("pages/action_reset.py")
