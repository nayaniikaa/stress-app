import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>[data-testid="stSidebar"]{display:none;}</style>
""", unsafe_allow_html=True)

st.title("🌍 Grounding (5-4-3-2-1)")

steps = [
    "5 things you see",
    "4 things you feel",
    "3 things you hear",
    "2 things you smell",
    "1 thing you taste"
]

if "g_step" not in st.session_state:
    st.session_state.g_step = 0

st.progress(st.session_state.g_step / len(steps))

if st.session_state.g_step < len(steps):
    st.subheader(steps[st.session_state.g_step])
    st.text_area("Your response")

    if st.button("Next"):
        st.session_state.g_step += 1
        st.rerun()
else:
    st.success("🌿 You are grounded.")

# NAV
st.markdown("---")
c1,c2,c3,c4 = st.columns(4)

if c1.button("Action", use_container_width=True):
    st.switch_page("pages/action_reset.py")
if c2.button("Breathe", use_container_width=True):
    st.switch_page("pages/breathing.py")
if c3.button("Grounding", use_container_width=True):
    pass
if c4.button("Reframing", use_container_width=True):
    st.switch_page("pages/reframing.py")
