import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("<h1 style='text-align:center;'>🌬️ Breathing Exercise</h1>", unsafe_allow_html=True)

TOTAL_ROUNDS = 5

# SESSION STATE
if "round" not in st.session_state:
    st.session_state.round = 1

if "running" not in st.session_state:
    st.session_state.running = False


# START
if not st.session_state.running:
    st.markdown(f"<h3 style='text-align:center;'>Round {st.session_state.round}</h3>", unsafe_allow_html=True)

    if st.button("Start", use_container_width=True):
        st.session_state.running = True
        st.rerun()


# RUN TIMER
else:
    placeholder = st.empty()

    phases = [
        ("Inhale", 4),
        ("Hold", 4),
        ("Exhale", 6)
    ]

    for phase, duration in phases:
        for i in range(duration, 0, -1):
            placeholder.markdown(f"""
            <div style="text-align:center">
                <h2>{phase}</h2>
                <h1>{i}</h1>
            </div>
            """, unsafe_allow_html=True)

            time.sleep(1)

    # ROUND COMPLETE
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
