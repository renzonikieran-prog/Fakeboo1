import streamlit as st
import os

st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# --- INITIALIZE SESSION STATE ---
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"

# --- CSS FOR UI ---
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; }
    .search-box { background-color: white; padding: 5px; border-radius: 2px; color: #333; width: 200px; font-size: 14px; font-weight: bold; border: 1px solid #ccc; }
    .section-header { background-color: #adb9d3; color: white; padding: 5px 10px; font-weight: bold; font-size: 14px; margin-top: 15px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.5; color: #1c1e21; }
    .photo-container { border: 1px solid #dddfe2; background-color: white; padding: 10px; margin-bottom: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:15px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div class="search-box">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.2])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business name:</b> Blast Hive.<br><b>Location:</b> Swansea, Sketty.</div>', unsafe_allow_html=True)

with col_right:
    # --- MAIN TABS ---
    tab1, tab2, tab3 = st.tabs(["📄 Info", "🖼️ Photos", "🎟️ Book Now!"])

    # --- TAB 1: INFO ---
    with tab1:
        st.markdown('<div class="section-header">About your business</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company... [Your Full Text Here]</div>', unsafe_allow_html=True)

    # --- TAB 2: PHOTOS (The Revamped Gallery) ---
    with tab2:
        posters = [
            ("target_day.jpg", "Target Day"),
            ("adrenaline_weekend.jpg", "Adrenaline Weekend"),
            ("ultimate_challenge.jpg", "Ultimate Challenge"),
            ("social_play_fest.jpg", "Social Play Fest"),
            ("extreme_impact.jpg", "Extreme Impact"),
            ("skill_switch.jpg", "Skill Switch Experience")
        ]

        if st.session_state.photo_index is None:
            st.markdown('<div class="section-header">Event Gallery (Click to enlarge)</div>', unsafe_allow_html=True)
            g_cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with g_cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                        if st.button(f"Enlarge", key=f"zoom_{i}"):
                            st.session_state.photo_index = i
                            st.rerun()
        else:
            idx = st.session_state.photo_index
            curr_img, curr_title = posters[idx]
            st.image(curr_img, use_container_width=True)
            if st.button("❌ Close Gallery"):
                st.session_state.photo_index = None
                st.rerun()

    # --- TAB 3: BOOK NOW! (The Booking System) ---
    with tab3:
        st.markdown('<div class="section-header">Book Your Experience</div>', unsafe_allow_html=True)
        
        if st.session_state.booking_step == "select":
            event_choice = st.selectbox("Choose an event:", [p[1] for p in posters])
            st.write(f"### Total: £54.99")
            
            if st.button("Confirm Booking"):
                st.session_state.booking_step = "ask_receipt"
                st.rerun()

        elif st.session_state.booking_step == "ask_receipt":
            st.success("✅ Successfully booked!")
            st.write("Would you like a receipt?")
            r_col1, r_col2 = st.columns(2)
            with r_col1:
                if st.button("Yes"):
                    st.session_state.booking_step = "receipt_sent"
                    st.rerun()
            with r_col2:
                if st.button("No"):
                    st.session_state.booking_step = "select"
                    st.rerun()

        elif st.session_state.booking_step == "receipt_sent":
            st.info("📩 Email sent to *********@gmail.com")
            if st.button("Thank you!"):
                st.session_state.booking_step = "select"
                st.rerun()
