import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# 🌊 SAME OCEAN STYLE
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
h1, h2, h3 {
    text-align: center;
    color: #0f172a;
}
</style>
""", unsafe_allow_html=True)

st.title("🌬️ Breathing Exercise")

TOTAL_ROUNDS = 5

# SESSION
if "round" not in st.session_state:
    st.session_state.round = 1

if "running" not in st.session_state:
    st.session_state.running = False


# START SCREEN
if not st.session_state.running:
    st.write(f"### Round {st.session_state.round}")

    if st.button("Start", use_container_width=True):
        st.session_state.running = True
        st.rerun()


# TIMER FUNCTION (TEXT ONLY)
def run_phase(phase, seconds):
    placeholder = st.empty()

    for i in range(seconds, 0, -1):
        placeholder.markdown(f"""
        <div style='text-align:center'>
            <h2>{phase}</h2>
            <h1>{i}</h1>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1)


# RUN FLOW
if st.session_state.running:
    run_phase("Inhale", 4)
    run_phase("Hold", 4)
    run_phase("Exhale", 6)

    st.session_state.running = False

    current = st.session_state.round
    remaining = TOTAL_ROUNDS - current

    st.success(f"✅ Round {current} complete")

    if remaining > 0:
        st.info(f"{remaining} more to go")

        if st.button(f"Next Round ({current + 1})", use_container_width=True):
            st.session_state.round += 1
            st.rerun()
    else:
        st.balloons()
        st.success("🎉 You completed all rounds!")

        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.clear()
            st.switch_page("app.py")
