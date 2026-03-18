import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# SAME UI STYLE
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #dbeafe, #e0f2fe, #f0f9ff);
}
.block-container {
    background: white;
    padding: 2rem;
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌬️ Breathing Exercise")

TOTAL_ROUNDS = 5

if "round" not in st.session_state:
    st.session_state.round = 1

if "running" not in st.session_state:
    st.session_state.running = False


if not st.session_state.running:
    st.write(f"### Round {st.session_state.round}")

    if st.button("Start", use_container_width=True):
        st.session_state.running = True
        st.rerun()


def circle_timer(phase, duration):
    placeholder = st.empty()

    for i in range(duration, 0, -1):
        progress = int(((duration - i) / duration) * 360)

        placeholder.markdown(f"""
        <div style='text-align:center'>
            <h2>{phase}</h2>
            <div style='
                width:160px;
                height:160px;
                border-radius:50%;
                margin:auto;
                background: conic-gradient(#0284c7 {progress}deg, #e2e8f0 {progress}deg);
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:26px;
                color:#0f172a;
            '>
                {i}
            </div>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(1)


if st.session_state.running:
    circle_timer("Inhale", 4)
    circle_timer("Hold", 4)
    circle_timer("Exhale", 6)

    st.session_state.running = False

    if st.session_state.round < TOTAL_ROUNDS:
        if st.button("Next Round", use_container_width=True):
            st.session_state.round += 1
            st.rerun()
    else:
        st.balloons()
        st.success("You completed all rounds!")

        if st.button("Back Home"):
            st.session_state.clear()
            st.switch_page("app.py")
