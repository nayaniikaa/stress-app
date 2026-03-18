import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# ❌ REMOVE SIDEBAR + UI
st.markdown("""
<style>
[data-testid="stSidebar"] {display:none;}
body {
    background: linear-gradient(135deg, #dbeafe, #e0f2fe, #f0f9ff);
}
.block-container {
    padding: 2rem;
}
h1, h2 {
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title(" Quick Reset")

# 🔄 FORCE CLEAN START (fixes progress issue)
if "initialized" not in st.session_state:
    st.session_state.step = 0
    st.session_state.task_done = False
    st.session_state.initialized = True

# OPTIONAL RESET BUTTON
if st.button("🔄 Reset Session"):
    st.session_state.clear()
    st.rerun()

tasks = [
    ("Stretch Arms", 10),
    ("Neck Roll", 8),
    ("Shoulder Roll", 10),
    ("Breathe", 10),
    ("Hydrate", 0)
]

# ✅ PROGRESS (correct logic)
st.progress(st.session_state.step / len(tasks))

# ---------------- TASK FLOW ----------------
if st.session_state.step < len(tasks):
    title, duration = tasks[st.session_state.step]

    st.subheader(title)

    # TIMER TASK
    if duration > 0:
        if st.button("Start", use_container_width=True):

            placeholder = st.empty()

            for i in range(duration, 0, -1):
                placeholder.markdown(f"""
                <div style='text-align:center'>
                    <h1>⏳ {i}</h1>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(1)

            placeholder.markdown("""
            <div style='text-align:center'>
                <h2>✅ Done</h2>
            </div>
            """, unsafe_allow_html=True)

            # ✅ Mark task complete
            st.session_state.task_done = True

    # NON-TIMER TASK
    else:
        if st.button("Done", use_container_width=True):
            st.success("💧 Hydrated")
            st.session_state.task_done = True

    # ✅ NEXT BUTTON (locked until done)
    if st.button(
        "Next →",
        use_container_width=True,
        disabled=not st.session_state.task_done
    ):
        st.session_state.step += 1
        st.session_state.task_done = False
        st.rerun()

# ---------------- COMPLETION ----------------
else:
    st.success("🔥 Reset done")

# ---------------- BOTTOM NAV ----------------
st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

if c1.button("Action", use_container_width=True):
    pass

if c2.button("Breathe", use_container_width=True):
    st.switch_page("pages/breathing.py")

if c3.button("Grounding", use_container_width=True):
    st.switch_page("pages/grounding.py")

if c4.button("Reframing", use_container_width=True):
    st.switch_page("pages/reframing.py")
