import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# 🌊 SAME DESIGN
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
p {
    text-align: center;
    color: #334155;
}
</style>
""", unsafe_allow_html=True)

st.title(" Grounding Exercise")

# STEPS
steps = [
    "Look around and notice **5 things you can see** 👀",
    "Now notice **4 things you can feel** 🤲",
    "Listen for **3 things you can hear** 👂",
    "Notice **2 things you can smell** 👃",
    "Focus on **1 thing you can taste or feel inside** 🌿"
]

# SESSION
if "g_step" not in st.session_state:
    st.session_state.g_step = 0


# FLOW
if st.session_state.g_step < len(steps):
    st.markdown(f"### Step {st.session_state.g_step + 1}")

    st.write(steps[st.session_state.g_step])

    if st.button("Done", use_container_width=True):
        st.session_state.g_step += 1
        st.rerun()

# COMPLETION
else:
    st.success("🌿 You are now more grounded and present.")

    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state.clear()
        st.switch_page("app.py")
