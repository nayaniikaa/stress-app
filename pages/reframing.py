import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>[data-testid="stSidebar"]{display:none;}</style>
""", unsafe_allow_html=True)

st.title("🧠 Thought Reframing")

questions = [
    "Is this actually true?",
    "What evidence supports this thought?",
    "What evidence contradicts it?",
    "What would you tell a friend?",
    "What's a more balanced thought?"
]

if "r_step" not in st.session_state:
    st.session_state.r_step = 0

st.write(f"Step {st.session_state.r_step+1} of {len(questions)}")
st.subheader(questions[st.session_state.r_step])

st.text_area("Your response")

if st.button("Next"):
    st.session_state.r_step += 1
    st.rerun()

if st.session_state.r_step >= len(questions):
    st.success("💡 New perspective unlocked.")

# NAV
st.markdown("---")
c1,c2,c3,c4 = st.columns(4)

if c1.button("⚡", use_container_width=True):
    st.switch_page("pages/action_reset.py")
if c2.button("🌬️", use_container_width=True):
    st.switch_page("pages/breathing.py")
if c3.button("🌍", use_container_width=True):
    st.switch_page("pages/grounding.py")
if c4.button("🧠", use_container_width=True):
    pass
