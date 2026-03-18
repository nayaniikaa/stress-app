import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Stress Support Assistant",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- GLOBAL OCEAN UI ----------------
st.markdown("""
<style>

/* 🌊 Ocean gradient background */
body {
    background: linear-gradient(135deg, #dbeafe, #e0f2fe, #f0f9ff);
}

/* 🧊 Card container */
.block-container {
    background: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}

/* 🧠 Titles */
h1, h2, h3 {
    text-align: center;
    color: #0f172a;
}

/* ✨ Text */
p, div {
    color: #334155;
    font-size: 16px;
}

/* 🎯 Buttons */
.stButton>button {
    width: 100%;
    border-radius: 14px;
    padding: 12px;
    font-size: 15px;
    background: #e0f2fe;
    color: #0f172a;
    border: none;
    transition: all 0.2s ease;
}

/* Hover */
.stButton>button:hover {
    background: #bae6fd;
    transform: scale(1.03);
}

/* Progress bar */
.stProgress > div > div {
    background-color: #0284c7;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<h1>🧠 Stress Support Assistant</h1>
<p>Take a moment. Understand what you're feeling.</p>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------------- PROGRESS (FIXED) ----------------
total_steps = 5
progress = (st.session_state.step - 1) / total_steps
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
    st.write("### How are you feeling right now?")

    emotions = [
        "Stressed", "Anxious", "Overwhelmed", "Sad", "Angry",
        "Tired", "Confused", "Panicking", "Low", "Frustrated"
    ]

    cols = st.columns(2)

    for i, emotion in enumerate(emotions):
        if cols[i % 2].button(emotion, use_container_width=True):
            st.session_state.feeling = emotion
            st.session_state.step = 2
            st.rerun()

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    st.write("### Where do you feel it in your body?")

    options = ["Chest", "Head", "Shoulders", "Stomach"]
    cols = st.columns(2)

    for i, opt in enumerate(options):
        if cols[i % 2].button(opt, use_container_width=True):
            st.session_state.body = opt.lower()
            st.session_state.step = 3
            st.rerun()

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    st.write("### How intense is it?")

    options = ["Mild", "Moderate", "Severe"]

    for opt in options:
        if st.button(opt, use_container_width=True):
            st.session_state.intensity = opt.lower()
            st.session_state.step = 4
            st.rerun()

# ---------------- STEP 4 ----------------
elif st.session_state.step == 4:
    st.write("### What best describes your state?")

    states = ["Overthinking", "Tired", "Panicking", "Low mood", "Restless"]

    for s in states:
        if st.button(s, use_container_width=True):
            st.session_state.state = s
            st.session_state.step = 5
            st.rerun()

# ---------------- STEP 5 ----------------
elif st.session_state.step == 5:
    method = choose_method(
        st.session_state.body,
        st.session_state.state,
        st.session_state.intensity
    )

    st.write("### 🧾 Your Analysis")

    st.info(
        f"You are feeling **{st.session_state.feeling}**, "
        f"with **{st.session_state.intensity} intensity**, "
        f"showing as **{st.session_state.state}**, "
        f"and tension in your **{st.session_state.body}**."
    )

    st.divider()

    if method == "breathing":
        if st.button("🌬️ Start Breathing Exercise", use_container_width=True):
            st.switch_page("pages/breathing.py")

    elif method == "grounding":
        if st.button("🧘 Start Grounding Exercise", use_container_width=True):
            st.switch_page("pages/grounding.py")

    elif method == "reframing":
        if st.button("🧠 Start Thought Reframing", use_container_width=True):
            st.switch_page("pages/reframing.py")

    else:
        if st.button("⚡ Start Action Reset", use_container_width=True):
            st.switch_page("pages/action_reset.py")

    # RESET BUTTON
    if st.button("🔄 Start New Session", use_container_width=True):
        st.session_state.clear()
        st.rerun()
