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

# SETTINGS (60 sec total approx)
INHALE = 10
HOLD = 5
EXHALE = 10
TOTAL_CYCLES = 6   # 6 cycles = ~60 seconds

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


# PHASE FUNCTION (REPLACES TEXT EACH TIME)
def run_phase(label, seconds, placeholder):
    for i in range(seconds, 0, -1):
        if st.session_state.stop:
            return False

        placeholder.markdown(f"""
        <div style='text-align:center'>
            <h2>{label}</h2>
            <h1>{i}</h1>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(1)

    return True


# MAIN FLOW
if st.session_state.running:
    placeholder = st.empty()

    for _ in range(TOTAL_CYCLES):

        if not run_phase("Inhale", INHALE, placeholder):
            break

        if not run_phase("Hold", HOLD, placeholder):
            break

        if not run_phase("Exhale", EXHALE, placeholder):
            break

    st.session_state.running = False

    if not st.session_state.stop:
        st.balloons()
        st.success("🌿 You completed the breathing session.")

    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state.clear()
        st.switch_page("app.py")
