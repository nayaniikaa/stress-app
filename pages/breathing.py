import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# 🌊 OCEAN STYLE
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #e0f2fe, #f0f9ff, #ecfeff);
}
.block-container {
    background: white;
    padding: 2rem;
    border-radius: 18px;
}
h1, h2 {
    text-align: center;
    color: #0f172a;
}
</style>
""", unsafe_allow_html=True)

st.title("🌬️ Breathing Exercise")

# SETTINGS
CYCLES = 6
INHALE = 10
HOLD = 5
EXHALE = 10

# SESSION STATE
if "running" not in st.session_state:
    st.session_state.running = False


# START BUTTON
if not st.session_state.running:
    st.write("### Take a deep breath. Follow the rhythm.")

    if st.button("Start", use_container_width=True):
        st.session_state.running = True
        st.rerun()


# TIMER FUNCTION
def run_phase(text, seconds):
    placeholder = st.empty()

    for i in range(seconds, 0, -1):
        placeholder.markdown(f"""
        <div style='text-align:center'>
            <h2>{text}</h2>
            <h1>{i}</h1>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)


# MAIN FLOW (CONTINUOUS)
if st.session_state.running:

    for cycle in range(CYCLES):
        run_phase("Inhale", INHALE)
        run_phase("Hold", HOLD)
        run_phase("Exhale", EXHALE)

    st.session_state.running = False

    st.balloons()
    st.success("🌿 You completed the breathing session.")

    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state.clear()
        st.switch_page("app.py")
