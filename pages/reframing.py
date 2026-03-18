import streamlit as st
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

st.title("Thought Reframing")

# User-friendly categories
types = {
    "Is this actually true?": [
        "What evidence supports this thought?",
        "What evidence goes against it?",
        "Am I basing this on facts or feelings?",
        "Am I misinterpreting the situation?",
        "Am I 100% sure this will happen?"
    ],

    "Is there another way to see this?": [
        "Is there another way to look at this?",
        "What is another possible explanation?",
        "Would someone else see this differently?",
        "Am I assuming my view is the only one?",
        "How would a neutral person see this?"
    ],

    "Am I overthinking this?": [
        "Am I catastrophizing?",
        "Am I thinking in extremes?",
        "Am I predicting the future without proof?",
        "Am I putting pressure on myself with 'should' statements?",
        "Is this really as bad as it seems?"
    ],

    "Is this thought helping me?": [
        "Is this thought helping me or hurting me?",
        "What effect is this thinking having on me?",
        "Is this moving me toward my goals?",
        "What happens if I let this thought go?",
        "Is this useful right now?"
    ],

    "Can I handle this?": [
        "What is the worst that could happen?",
        "Could I handle it if it did?",
        "Will this matter in a year?",
        "What can I learn from this situation?",
        "What is one small action I can take right now?"
    ]
}

# Session state init
if "rf_mode" not in st.session_state:
    st.session_state.rf_mode = None
    st.session_state.rf_step = 0
    st.session_state.rf_answers = []

# STEP 1: Choose type
if st.session_state.rf_mode is None:
    st.write("Choose what fits your thoughts right now:")

    for key in types.keys():
        if st.button(key):
            st.session_state.rf_mode = key
            st.session_state.rf_step = 0
            st.session_state.rf_answers = []
            st.rerun()


# STEP 2: Ask questions
else:
    questions = types[st.session_state.rf_mode]

    if st.session_state.rf_step < len(questions):
        st.subheader(st.session_state.rf_mode)
        st.write(f"Step {st.session_state.rf_step + 1} of {len(questions)}")

        st.write(questions[st.session_state.rf_step])

        answer = st.text_area("Your response", key=f"rf_{st.session_state.rf_step}")

        if st.button("Next"):
            if answer.strip():
                st.session_state.rf_answers.append(answer)
                st.session_state.rf_step += 1
                st.rerun()
            else:
                st.warning("Please answer before continuing.")

    # FINAL OUTPUT
    else:
        st.success("✨ You've completed reframing")

        st.write("### 🧠 What you just did:")
        st.info(
            "You questioned your thoughts, explored different perspectives, "
            "and created a more balanced way of thinking."
        )
col1, col2, col3, col4 = st.columns(4)

if col1.button("⚡ Reset", use_container_width=True):
    st.switch_page("action reset.py")

if col2.button("🌬️ Breathe", use_container_width=True):
    st.switch_page("breathing.py")

if col3.button("🌍 Ground", use_container_width=True):
    st.switch_page("grounding.py")

if col4.button("🧠 Reframe", use_container_width=True):
    st.switch_page("reframing.py")
        st.write("### 💡 Key takeaway:")
        st.write(
            "Your thoughts are not always facts. You have the ability to challenge and reshape them."
        )
