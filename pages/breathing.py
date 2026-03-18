import streamlit as st
import time

st.title(" Guided Breathing")

TOTAL_ROUNDS = 5

# Initialize session state
if "round" not in st.session_state:
    st.session_state.round = 1

if "phase" not in st.session_state:
    st.session_state.phase = "start"  # start / running / done


# START SCREEN
if st.session_state.phase == "start":
    st.write(f"Ready for Round {st.session_state.round}?")

    if st.button(f"Start Round {st.session_state.round}"):
        st.session_state.phase = "running"
        st.rerun()


# BREATHING RUN
elif st.session_state.phase == "running":
    placeholder = st.empty()

    phases = [("Inhale", 4), ("Hold", 4), ("Exhale", 6)]

    for phase, seconds in phases:
        for i in range(seconds, 0, -1):
            progress = int(((seconds - i) / seconds) * 360)

            placeholder.markdown(f"""
            <div style="text-align:center">
                <h2>{phase}</h2>
                <div style="
                    width:160px;
                    height:160px;
                    border-radius:50%;
                    border:10px solid #4CAF50;
                    border-top:{progress}deg solid transparent;
                    margin:auto;
                "></div>
                <h1>{i}</h1>
            </div>
            """, unsafe_allow_html=True)

            time.sleep(1)

    # Round complete
    st.session_state.phase = "done"
    st.rerun()


# AFTER ROUND (THIS WAS MISSING PROPERLY)
elif st.session_state.phase == "done":
    current = st.session_state.round
    remaining = TOTAL_ROUNDS - current

    st.success(f"✅ Round {current} complete!")

    if remaining > 0:
        st.info(f"✔ {current} done, {remaining} more to go")

        if st.button(f"Start Round {current + 1}"):
            st.session_state.round += 1
            st.session_state.phase = "start"
            st.rerun()

    else:
        st.success("🎉 Good job completing all 5 rounds!")
