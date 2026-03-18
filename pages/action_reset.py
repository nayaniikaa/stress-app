import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"] {display:none;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ Quick Reset")

tasks = [
    ("Stretch Arms",10),
    ("Neck Roll",8),
    ("Shoulder Roll",10),
    ("Breathe",10),
    ("Hydrate",0)
]

if "step" not in st.session_state:
    st.session_state.step = 0

st.progress(st.session_state.step / len(tasks))

if st.session_state.step < len(tasks):
    title, duration = tasks[st.session_state.step]

    st.subheader(title)

    if duration > 0:
        if st.button("Start"):
            for i in range(duration,0,-1):
                st.write(i)
                time.sleep(1)
            st.success("Done")
    else:
        if st.button("Done"):
            st.success("Hydrated")

    if st.button("Next"):
        st.session_state.step += 1
        st.rerun()

else:
    st.success("🔥 Reset done")

# NAV
st.markdown("---")
c1,c2,c3,c4 = st.columns(4)

if c1.button("⚡", use_container_width=True):
    pass
if c2.button("🌬️", use_container_width=True):
    st.switch_page("pages/breathing.py")
if c3.button("🌍", use_container_width=True):
    st.switch_page("pages/grounding.py")
if c4.button("🧠", use_container_width=True):
    st.switch_page("pages/reframing.py")
