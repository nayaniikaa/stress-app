import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"] {display:none;}
body {
    background: linear-gradient(135deg, #e0f2fe, #f0f9ff, #ecfeff);
}
.block-container {padding:2rem;}
</style>
""", unsafe_allow_html=True)

st.title("🌬️ Breathe")

INHALE, HOLD, EXHALE = 4, 4, 6
TOTAL_CYCLES = 5
TOTAL_TIME = (INHALE + HOLD + EXHALE) * TOTAL_CYCLES

if "running" not in st.session_state:
    st.session_state.running = False
if "stop" not in st.session_state:
    st.session_state.stop = False

col1, col2 = st.columns(2)

if col1.button("Start", use_container_width=True):
    st.session_state.running = True
    st.session_state.stop = False
    st.rerun()

if col2.button("Stop", use_container_width=True):
    st.session_state.stop = True
    st.session_state.running = False

circle = st.empty()
text = st.empty()
progress = st.progress(0)

def animate(size, color):
    circle.markdown(f"""
    <div style='display:flex;justify-content:center;'>
        <div style='width:{size}px;height:{size}px;border-radius:50%;background:{color};transition:1s;'></div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.running:
    elapsed = 0

    for _ in range(TOTAL_CYCLES):

        for _ in range(INHALE):
            if st.session_state.stop: break
            animate(220, "#38bdf8")
            text.markdown("### Inhale")
            time.sleep(1)
            elapsed += 1
            progress.progress(elapsed / TOTAL_TIME)

        for _ in range(HOLD):
            if st.session_state.stop: break
            animate(220, "#0ea5e9")
            text.markdown("### Hold")
            time.sleep(1)
            elapsed += 1
            progress.progress(elapsed / TOTAL_TIME)

        for _ in range(EXHALE):
            if st.session_state.stop: break
            animate(120, "#7dd3fc")
            text.markdown("### Exhale")
            time.sleep(1)
            elapsed += 1
            progress.progress(elapsed / TOTAL_TIME)

    st.session_state.running = False

    if not st.session_state.stop:
        progress.progress(1.0)
        st.success("🌿 Done.")

# 🔻 NAV
st.markdown("---")
c1,c2,c3,c4 = st.columns(4)

if c1.button("⚡", use_container_width=True):
    st.switch_page("pages/action reset.py")
if c2.button("🌬️", use_container_width=True):
    pass
if c3.button("🌍", use_container_width=True):
    st.switch_page("pages/grounding.py")
if c4.button("🧠", use_container_width=True):
    st.switch_page("pages/reframing.py")
