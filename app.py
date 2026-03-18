import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# ❌ REMOVE SIDEBAR
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# ---------------- GLOBAL OCEAN UI ----------------
st.markdown("""
<style>

/* 🌊 Background */
body {
    background: linear-gradient(135deg, #dbeafe, #e0f2fe, #f0f9ff);
}

/* 🧊 Card */
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
}

/* 🎯 Buttons */
.stButton>button {
    width: 100%;
    border-radius: 14px;
    padding: 12px;
    background: #e0f2fe;
    color: #0f172a;
    border: none;
    transition: 0.2s;
}

.stButton>button:hover {
    background: #bae6fd;
    transform: scale(1.03);
}

/* 📊 Progress */
.stProgress > div > div {
    background-color: #0284c7;
}

/* 🔻 Bottom Nav Styling */
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: white;
    padding: 10px;
    box-shadow: 0 -5px 15px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<h1>🧠 Stress Support Assistant</h1>
<p style='text-align:center;'>Take a moment. Understand what you're feeling.</p>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------------- PROGRESS ----------------
total_steps = 5
progress = (st.session_state.step - 1) / total_steps
st.progress(progress)

# ---------------- LOGIC ----------------
def choose_method(body, state, intensity):
    if "Chest (tight/heavy)" in body or intensity == "severe":
        return "breathing"
    elif "Racing thoughts" in state or "Head (pressure)" in body:
        return "grounding"
    elif "Low energy / drained" in state:
        return "reframing"
    else:
        return "action"

# ---------------- STEP 1 ----------------
if st.session_state.step == 1:
    st.write("### How are you feeling right now?")

    emotions = [
        "Stressed", "Anxious", "Overwhelmed", "Sad",
        "Angry", "Frustrated", "Confused", "Not sure"
    ]

    selected = st.multiselect("Select all that apply:", emotions)

    if st.button("Continue"):
        if selected:
            st.session_state.feeling = selected
            st.session_state.step = 2
            st.rerun()
        else:
            st.warning("Pick at least one option")

# ---------------- STEP 2 ----------------
elif st.session_state.step == 2:
    st.write("### Where do you feel it in your body?")

    options = [
        "Chest (tight/heavy)", "Head (pressure)",
        "Shoulders & Neck (tension)", "Stomach (uneasy)",
        "Jaw (clenched)", "Whole body"
    ]

    selected = st.multiselect("Select all that apply:", options)

    if st.button("Continue"):
        if selected:
            st.session_state.body = selected
            st.session_state.step = 3
            st.rerun()
        else:
            st.warning("Pick at least one option")

# ---------------- STEP 3 ----------------
elif st.session_state.step == 3:
    st.write("### How intense is it?")

    for opt in ["Mild", "Moderate", "Severe"]:
        if st.button(opt):
            st.session_state.intensity = opt.lower()
            st.session_state.step = 4
            st.rerun()

# ---------------- STEP 4 ----------------
elif st.session_state.step == 4:
    st.write("### What’s happening right now?")

    states = [
        "Racing thoughts", "Constant worry",
        "Feeling on edge", "Low energy / drained",
        "Can’t focus", "Panic / losing control"
    ]

    selected = st.multiselect("Select all that apply:", states)

    if st.button("Continue"):
        if selected:
            st.session_state.state = selected
            st.session_state.step = 5
            st.rerun()
        else:
            st.warning("Pick at least one option")

# ---------------- STEP 5 ----------------
elif st.session_state.step == 5:

    method = choose_method(
        st.session_state.body,
        st.session_state.state,
        st.session_state.intensity
    )

    st.write("### 🧾 Your Analysis")

    st.info(
        f"You are feeling **{', '.join(st.session_state.feeling)}**, "
        f"with **{st.session_state.intensity} intensity**, "
        f"experiencing **{', '.join(st.session_state.state)}**, "
        f"and tension in your **{', '.join(st.session_state.body)}**."
    )

    st.divider()

    if method == "breathing":
        if st.button("🌬️ Start Breathing Exercise"):
            st.switch_page("pages/breathing.py")

    elif method == "grounding":
        if st.button("🌍 Start Grounding Exercise"):
            st.switch_page("pages/grounding.py")

    elif method == "reframing":
        if st.button("🧠 Start Thought Reframing"):
            st.switch_page("pages/reframing.py")

    else:
        if st.button("⚡ Start Action Reset"):
            st.switch_page("pages/action reset.py")

    if st.button("🔄 Start New Session"):
        st.session_state.clear()
        st.rerun()

# ---------------- BOTTOM NAV ----------------
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

if col1.button("⚡", use_container_width=True):
    st.switch_page("pages/action reset.py")

if col2.button("🌬️", use_container_width=True):
    st.switch_page("pages/breathing.py")

if col3.button("🌍", use_container_width=True):
    st.switch_page("pages/grounding.py")

if col4.button("🧠", use_container_width=True):
    st.switch_page("pages/reframing.py")
