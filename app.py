import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# Memory Management (Session State)
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = []
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(50, 950) for _ in range(100)]

# Event Dates
event_data = {
    "Target Day": ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th August"],
    "Adrenaline Weekend": ["12th", "13th", "14th", "18th", "19th August"],
    "Ultimate Challenge Day": ["6th", "7th", "11th", "20th August"],
    "Social Play Fest": ["9th", "10th", "15th", "16th August"],
    "Extreme Impact Day": ["4th", "5th", "17th", "22nd August"],
    "Skill Switch Experience": ["8th", "14th", "21st", "23rd August"]
}

# 3. MAPPED GALLERY DATA (Using your custom high-quality files)
posters = [
    ("target_day.jpg", "Target Day Poster"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend Poster"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Poster"),
    ("social_play_fest.jpg", "Social Play Fest Poster"),
    ("extreme_impact.jpg", "Extreme Impact Poster"),
    ("skill_switch.jpg", "Skill Switch Experience Poster"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.jpg", "Stouthall Mansion Site"),
    ("Gemini_Generated_Image_wdo2rzwdo2rzwdo2.jpg", "Outdoor Archery Setup"),
    ("Gemini_Generated_Image_of95w8of95w8of95.jpg", "Outdoor Archery Action"),
    ("Gemini_Generated_Image_4nwpmx4nwpmx4nwp.jpg", "Indoor Archery Arena"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.jpg", "Bushcraft Fire Starting"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.jpg", "Laser Tag Equipment Delivery"),
    ("Gemini_Generated_Image_q74buoq74buoq74b.jpg", "Outdoor Laser Tag Action"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.jpg", "Indoor Neon Laser Arena"),
    ("Gemini_Generated_Image_hunw61hunw61hunw.jpg", "Outdoor Victory Celebration"),
    ("Gemini_Generated_Image_xz9er1xz9er1xz9e.jpg", "Logic Puzzle Teamwork"),
    ("Gemini_Generated_Image_vv49c1vv49c1vv49.jpg", "Indoor Team Games"),
    ("Gemini_Generated_Image_olevawolevawolev.jpg", "Outdoor Physical Puzzles"),
    ("Gemini_Generated_Image_cueiazcueiazcuei.jpg", "Team Sports Competition")
]

# --- UI STYLING ---
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .stat-bar { background-color: #f0f2f5; padding: 10px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 4px; margin-bottom: 15px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 15px; border-radius: 8px; margin-bottom: 5px; font-weight: bold; }
    .motto { color: #adb9d3; font-weight: bold; font-size: 22px; text-align: center; display: block; margin-top: 20px; letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("Gemini_Generated_Image_lpugatlpugatlpug.jpg"):
        st.image("Gemini_Generated_Image_lpugatlpugatlpug.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business HQ:</b> Swansea.<br><b>Activity Grounds:</b> Stouthall Mansion.<br><b>Indoor Arena:</b> On-site at Stouthall.</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1:
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company offering exciting days out for young people. While based in Swansea, <b>all activities take place at Stouthall Mansion</b>. We provide unforgettable experiences including bushcraft, team sports, and murder mystery puzzles.<br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)

    # --- TAB 2: POSTS (35 UNIQUE POSTS WITH NEW IMAGES) ---
    with tab_posts:
        posts_data = [
            ("The outdoor range is officially set up for Target Day! 🏹", "Gemini_Generated_Image_wdo2rzwdo2rzwdo2.jpg"),
            ("Focused minds at the archery targets this morning. 🎯", "Gemini_Generated_Image_of95w8of95w8of95.jpg"),
            ("Rainy day? No problem. Our indoor archery hall is open. 🌧️", "Gemini_Generated_Image_4nwpmx4nwpmx4nwp.jpg"),
            ("Mastering the spark in our teamwork-focused bushcraft session. 🔥", "Gemini_Generated_Image_fqzz3rfqzz3rfqzz.jpg"),
            ("Unpacking the future: New laser tag vests arrived at HQ! 🔫", "Gemini_Generated_Image_sbz4c8sbz4c8sbz4.jpg"),
            ("Incredible energy in the outdoor laser tag arena today. 🌲", "Gemini_Generated_Image_q74buoq74buoq74b.jpg"),
            ("Lighting up the dark in the neon laser arena. 🌈", "Gemini_Generated_Image_g2yanmg2yanmg2ya.jpg"),
            ("A huge win for the team! Victory celebration at sunset. 🙌", "Gemini_Generated_Image_hunw61hunw61hunw.jpg"),
            ("Concentration levels are high for these logic puzzles. 🧠", "Gemini_Generated_Image_xz9er1xz9er1xz9e.jpg"),
            ("Physics and teamwork in our indoor challenge games. 🏗️", "Gemini_Generated_Image_vv49c1vv49c1vv49.jpg"),
            ("Physical puzzles set up across the Stouthall lawns. 🧩", "Gemini_Generated_Image_olevawolevawolev.jpg"),
            ("Competitive spirits on the field today! 🏃", "Gemini_Generated_Image_cueiazcueiazcuei.jpg")
        ]
        
        # Fill to 35 unique text-only posts
        for i in range(len(posts_data), 35):
            posts_data.append((f"Update: Stouthall Mansion activity slot {i} is now active. Check booking for availability.", None))

        for i, (txt, img) in enumerate(posts_data):
            st.markdown(f'<div class="post-card">{txt}</div>', unsafe_allow_html=True)
            if img and os.path.exists(img):
                st.image(img, width=450)
            c1, c2 = st.columns([1, 4])
            if c1.button(f"👍 {st.session_state.post_likes[i]}", key=f"lk_{i}"):
                st.session_state.post_likes[i] += 1; st.rerun()

    # --- TAB 3: PHOTOS (Full High-Quality Gallery) ---
    with tab2:
        if st.session_state.photo_index is None:
            cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                    if st.button(f"View {title}", key=f"gv_{i}"):
                        st.session_state.photo_index = i; st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(posters[idx][0], width=550, caption=posters[idx][1])
            if st.button("❌ Close Full View"):
                st.session_state.photo_index = None; st.rerun()

    # --- TAB 4: BOOKING ---
    with tab3:
        st.markdown('<div class="section-header">Book Your Adventure - £54.99</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Event:", list(event_data.keys()))
            dt = st.selectbox("Date:", event_data[evt])
            if st.button("Confirm Booking Details"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "receipt_confirm"; st.rerun()
        
        elif st.session_state.booking_step == "receipt_confirm":
            st.warning("Booking Saved! Do you require a receipt?")
            if st.button("Yes, Send to *******@gmail.com"): st.session_state.booking_step = "receipt_sent"; st.rerun()
            if st.button("No Receipt, Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

        elif st.session_state.booking_step == "receipt_sent":
            st.success("📩 Receipt sent to *******@gmail.com!")
            if st.button("Return to Booking Hub"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    # --- TAB 5: MY BOOKINGS ---
    with tab4:
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]}</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"can_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()
