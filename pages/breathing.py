import streamlit as st
import time

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# ❌ REMOVE SIDEBAR + UI
st.markdown("""
<style>
[data-testid="stSidebar"] {display:none;}
body {
    background: linear-gradient(135deg, #e0f2fe, #f0f9ff, #ecfeff);
}
.block-container {padding:2rem;}
h1, h2 {text-align:center;}
</style>
""", unsafe_allow_html=True)

st.title("🌬️ Breathe")

INHALE, HOLD, EXHALE = 4, 4, 6
TOTAL_CYCLES = 5
TOTAL_TIME = (INHALE + HOLD + EXHALE) * TOTAL_CYCLES

# SESSION
if "running" not in st.session_state:
    st.session_state.running = False
if "stop" not in st.session_state:
    st.session_state.stop = False

# BUTTONS
col1, col2 = st.columns(2)

if col1.button("Start", use_container_width=True):
    st.session_state.running = True
    st.session_state.stop = False
    st.rerun()

if col2.button("Stop", use_container_width=True):
    st.session_state.stop = True
    st.session_state.running = False

# UI
circle = st.empty()
text = st.empty()
progress = st.progress(0)

# 🔥 BALL WITH COUNTDOWN INSIDE
def draw_circle(size, color, number):
    circle.markdown(f"""
    <div style='display:flex;justify-content:center;align-items:center;'>
        <div style='
            width:{size}px;
            height:{size}px;
            border-radius:50%;
            background:{color};
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:40px;
            color:white;
            font-weight:bold;
        '>
            {number}
        </div>
    </div>
    """, unsafe_allow_html=True)

# 🔥 SMOOTH SIZE CHANGE (FAKE ANIMATION)
def animate_phase(start_size, end_size, seconds, label, color, elapsed):
    step = (end_size - start_size) / seconds

    for i in range(seconds, 0, -1):
        if st.session_state.stop:
            return False, elapsed

        size = start_size + step * (seconds - i)

        draw_circle(int(size), color, i)
        text.markdown(f"### {label}")

        time.sleep(1)

        elapsed += 1
        progress.progress(elapsed / TOTAL_TIME)

    return True, elapsed


# MAIN FLOW
if st.session_state.running:
    elapsed = 0

    for _ in range(TOTAL_CYCLES):

        # INHALE (grow)
        ok, elapsed = animate_phase(120, 220, INHALE, "Inhale", "#38bdf8", elapsed)
        if not ok: break

        # HOLD (stay big)
        ok, elapsed = animate_phase(220, 220, HOLD, "Hold", "#0ea5e9", elapsed)
        if not ok: break

        # EXHALE (shrink)
        ok, elapsed = animate_phase(220, 120, EXHALE, "Exhale", "#7dd3fc", elapsed)
        if not ok: break

    st.session_state.running = False

    if not st.session_state.stop:
        progress.progress(1.0)
        draw_circle(150, "#22c55e", "✓")
        st.success("🌿 Done.")

# 🔻 NAV
st.markdown("---")
c1, c2, c3, c4 = st.columns(4)

if c1.button("⚡", use_container_width=True):
    st.switch_page("action_reset.py")

if c2.button("🌬️", use_container_width=True):
    pass

if c3.button("🌍", use_container_width=True):
    st.switch_page("grounding.py")

if c4.button("🧠", use_container_width=True):
    st.switch_page("reframing.py")
