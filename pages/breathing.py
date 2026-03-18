import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("<h1 style='text-align:center;'>🌬️ Breathe</h1>", unsafe_allow_html=True)

TOTAL_ROUNDS = 5

# SESSION STATE
if "round" not in st.session_state:
    st.session_state.round = 1

if "phase" not in st.session_state:
    st.session_state.phase = "start"


# START SCREEN
if st.session_state.phase == "start":
    st.markdown(f"<h3 style='text-align:center;'>Round {st.session_state.round}</h3>", unsafe_allow_html=True)

    if st.button("Start", use_container_width=True):
        st.session_state.phase = "running"
        st.rerun()


# BREATHING LOOP
elif st.session_state.phase == "running":
    placeholder = st.empty()

    # (phase, duration, start_scale, end_scale)
    phases = [
        ("Inhale", 4, 1.0, 1.4),
        ("Hold", 4, 1.4, 1.4),
        ("Exhale", 6, 1.4, 1.0)
    ]

    for phase, duration, start_scale, end_scale in phases:
        for i in range(duration):
            progress = i / duration
            scale = start_scale + (end_scale - start_scale) * progress

            placeholder.markdown(f"""
            <div style="text-align:center">
                <h2>{phase}</h2>
                <div style="
                    width:180px;
                    height:180px;
                    margin:auto;
                    border-radius:50%;
                    background: radial-gradient(circle, #38bdf8, #0ea5e9);
                    transform: scale({scale});
                    transition: all 0.5s ease;
                "></div>
            </div>
            """, unsafe_allow_html=True)

            time.sleep(1)

    st.session_state.phase = "done"
    st.rerun()


# AFTER ROUND
elif st.session_state.phase == "done":
    current = st.session_state.round
    remaining = TOTAL_ROUNDS - current

    st.success(f"✅ Round {current} complete")

    if remaining > 0:
        st.info(f"{remaining} more to go")

        if st.button(f"Next Round ({current + 1})", use_container_width=True):
            st.session_state.round += 1
            st.session_state.phase = "start"
            st.rerun()

    else:
        st.balloons()
        st.success("🎉 You completed all 5 rounds!")

        if st.button("🏠 Return Home", use_container_width=True):
            st.session_state.clear()
            st.switch_page("app.py")
