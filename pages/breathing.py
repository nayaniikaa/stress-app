import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.title(" Breathing Exercise")

TOTAL_ROUNDS = 5

# SESSION STATE
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


# SAFE CIRCLE TIMER FUNCTION
def show_circle_timer(phase, duration):
    placeholder = st.empty()

    for i in range(duration, 0, -1):
        progress = int(((duration - i) / duration) * 360)

        html = f"""
        <div style='text-align:center'>
            <h2>{phase}</h2>
            <div style='
                width:180px;
                height:180px;
                border-radius:50%;
                margin:auto;
                background: conic-gradient(#38bdf8 {progress}deg, #1e293b {progress}deg);
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:28px;
                color:white;
            '>
                {i}
            </div>
        </div>
        """

        placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(1)


# RUN
else:
    show_circle_timer("Inhale", 4)
    show_circle_timer("Hold", 4)
    show_circle_timer("Exhale", 6)

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

        if st.button("🏠 Return Home", use_container_width=True):
            st.session_state.clear()
            st.switch_page("app.py")
