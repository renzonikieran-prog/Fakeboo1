import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# Core memory for interactive features
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []

# --- DATA MAPPING ---
event_data = {
    "Target Day": ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th August"],
    "Adrenaline Weekend": ["12th", "13th", "14th", "18th", "19th"],
    "Ultimate Challenge Day": ["6th", "7th", "11th", "20th"],
    "Social Play Fest": ["9th", "10th", "15th", "16th"],
    "Extreme Impact Day": ["4th", "5th", "17th", "22th"],
    "Skill Switch Experience": ["8th", "14th", "21st", "23rd"]
}

posters = [
    ("target_day.jpg", "Target Day"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Day"),
    ("social_play_fest.jpg", "Social Play Fest"),
    ("extreme_impact.jpg", "Extreme Impact Day"),
    ("skill_switch.jpg", "Skill Switch Experience")
]

# --- UI STYLING ---
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; }
    .search-box { background-color: white; padding: 5px; border-radius: 2px; color: #333; width: 220px; font-size: 14px; font-weight: bold; border: 1px solid #ccc; }
    .section-header { background-color: #adb9d3; color: white; padding: 6px 12px; font-weight: bold; font-size: 14px; margin-top: 18px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; font-size: 14px; }
    .quote-box { font-style: italic; color: #4b4f56; border-left: 4px solid #adb9d3; padding-left: 12px; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div class="search-box">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    # Business Logo
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business:</b> Blast Hive.<br><b>Location:</b> Swansea, Sketty.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Message the Team</div>', unsafe_allow_html=True)
    with st.expander("Open Contact Form"):
        u_name = st.text_input("Name")
        if st.button("Send Message"):
            st.success(f"Message sent! Thanks {u_name}.")

    st.markdown('<div class="section-header">Likes</div>', unsafe_allow_html=True)
    st.markdown("""<div class="content-box">
        👍 Adventure Sports Wales<br>
        👍 Gower Activity Centres<br>
        👍 Swansea Youth Hub
    </div>""", unsafe_allow_html=True)

with col_right:
    tab1, tab2, tab3, tab4 = st.tabs(["📄 Info", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings"])

    # --- TAB 1: INFO ---
    with tab1:
        st.markdown('<div class="section-header">About Your Business</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company that offers exciting days out for the young people in our area. We are based in Swansea and have offered days put that include a wild bushcraft day, competitive team sports day and even a thrilling murder mystery day full of brain boggling puzzles. We offer the fairest prices we possibly can in order for your children and you young people to have the most unforgettable days. We cannot wait to see you guys have fun at our next exciting events. We hope to see you there, when you’re ready, READY, AIM, BLAST!</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">Frequently Asked Questions (FAQ)</div>', unsafe_allow_html=True)
        st.markdown("""<div class="content-box">
            <p class="faq-q">Is all equipment provided?</p><p>Yes! We provide all safety gear and specialized equipment.</p>
            <p class="faq-q">What happens if it rains?</p><p>We have indoor facilities in Sketty for backup!</p>
            <p class="faq-q">Do you offer group discounts?</p><p>Yes! Use the contact form for groups of 10+.</p>
        </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-header">Quotes & Reviews</div>', unsafe_allow_html=True)
        st.markdown("""<div class="content-box">
            <div class="quote-box">"Best summer activity company in Swansea!" - Parent Review</div>
            <div class="quote-box">"Ready, Aim, BLAST!" - Official Motto</div>
        </div>""", unsafe_allow_html=True)

    # --- TAB 2: PHOTOS (The Photo Gallery) ---
    with tab2:
        if st.session_state.photo_index is None:
            st.markdown('<div class="section-header">Event Gallery (Click View to Enlarge)</div>', unsafe_allow_html=True)
            g_cols = st.columns(4)
            for i, (img, title) in enumerate(posters):
                with g_cols[i % 4]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                        if st.button("View", key=f"gal_{i}"):
                            st.session_state.photo_index = i
                            st.rerun()
        else:
            # Enlarge view with scrolling
            idx = st.session_state.photo_index
            st.image(posters[idx][0], caption=posters[idx][1], use_container_width=True)
            c1, c2, c3 = st.columns(3)
            if c1.button("⬅ Prev"): st.session_state.photo_index = (idx-1)%len(posters); st.rerun()
            if c2.button("Next ➡"): st.session_state.photo_index = (idx+1)%len(posters); st.rerun()
            if c3.button("❌ Close Gallery", type="primary"): st.session_state.photo_index = None; st.rerun()

    # --- TAB 3: BOOK NOW (The Booking Section) ---
    with tab3:
        st.markdown('<div class="section-header">Make a Booking</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Select Activity:", list(event_data.keys()))
            dt = st.selectbox("Choose Date (Refer to posters for dates):", event_data[evt])
            if st.button("Confirm Booking Details"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "confirm"
                st.rerun()
        
        elif st.session_state.booking_step == "confirm":
            st.success(f"Booking Registered: {st.session_state.temp_booking['event']}")
            if st.button("Yes, Send Receipt"): st.session_state.booking_step = "receipt"; st.rerun()
            if st.button("No, Just Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

        elif st.session_state.booking_step == "receipt":
            st.info("📩 Receipt sent to your email!")
            if st.button("Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    # --- TAB 4: MY BOOKINGS (The My Bookings Section) ---
    with tab4:
        st.markdown('<div class="section-header">Your Active Bookings</div>', unsafe_allow_html=True)
        if not st.session_state.my_bookings:
            st.info("No active bookings found. Use the 'Book Now' tab to start!")
        else:
            for i, b in enumerate(st.session_state.my_bookings):
                st.markdown(f'<div class="content-box">🎯 <b>{b["event"]}</b><br>📅 Date: {b["date"]}<br>🆔 ID: {b["id"]}</div>', unsafe_allow_html=True)
                if st.button(f"Cancel {b['id']}", key=f"del_{i}"):
                    st.session_state.my_bookings.pop(i); st.rerun()
