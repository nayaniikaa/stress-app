import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# 🌊 CLEAN OCEAN STYLE
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
INHALE = 10
HOLD = 5
EXHALE = 10
TOTAL_CYCLES = 6

TOTAL_TIME = (INHALE + HOLD + EXHALE) * TOTAL_CYCLES

# SESSION STATE
if "running" not in st.session_state:
    st.session_state.running = False

if "stop" not in st.session_state:
    st.session_state.stop = False

# START / STOP BUTTONS
col1, col2 = st.columns(2)

if col1.button("Start", use_container_width=True):
    st.session_state.running = True
    st.session_state.stop = False
    st.rerun()

if col2.button("Stop", use_container_width=True):
    st.session_state.stop = True
    st.session_state.running = False

# PHASE FUNCTION
def run_phase(label, seconds, placeholder, progress_bar, elapsed_time):
    for i in range(seconds, 0, -1):
        if st.session_state.stop:
            return False, elapsed_time

        placeholder.markdown(f"""
        <div style='text-align:center'>
            <h2>{label}</h2>
            <h1>{i}</h1>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(1)

        elapsed_time += 1
        progress_bar.progress(elapsed_time / TOTAL_TIME)

    return True, elapsed_time

# MAIN FLOW
if st.session_state.running:
    placeholder = st.empty()
    progress_bar = st.progress(0)
    elapsed_time = 0

    for _ in range(TOTAL_CYCLES):

        ok, elapsed_time = run_phase("Inhale", INHALE, placeholder, progress_bar, elapsed_time)
        if not ok:
            break

        ok, elapsed_time = run_phase("Hold", HOLD, placeholder, progress_bar, elapsed_time)
        if not ok:
            break

        ok, elapsed_time = run_phase("Exhale", EXHALE, placeholder, progress_bar, elapsed_time)
        if not ok:
            break

    st.session_state.running = False

    if not st.session_state.stop:
        progress_bar.progress(1.0)  # ensure full at end
        st.balloons()
        st.success("🌿 You completed the breathing session.")

    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state.clear()
        st.switch_page("app.py")
