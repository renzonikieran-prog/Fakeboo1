import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# 1. Memory Management (Session State)
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = []
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(45, 950) for _ in range(100)]

# 2. EVENT DATA
event_data = {
    "Target Day": ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th August"],
    "Adrenaline Weekend": ["12th", "13th", "14th", "18th", "19th August"],
    "Ultimate Challenge Day": ["6th", "7th", "11th", "20th August"],
    "Social Play Fest": ["9th", "10th", "15th", "16th August"],
    "Extreme Impact Day": ["4th", "5th", "17th", "22nd August"],
    "Skill Switch Experience": ["8th", "14th", "21st", "23rd August"]
}

# 3. VERIFIED GALLERY DATA (Using your uploaded cinematic images)
posters = [
    ("target_day.jpg", "Target Day Poster"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend Poster"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Poster"),
    ("social_play_fest.jpg", "Social Play Fest Poster"),
    ("extreme_impact.jpg", "Extreme Impact Poster"),
    ("skill_switch.jpg", "Skill Switch Poster"),
    ("Gemini_Generated_Image_wdo2rzwdo2rzwdo2.jpg", "Archery Field Setup"),
    ("Gemini_Generated_Image_of95w8of95w8of95.jpg", "Outdoor Archery Action"),
    ("Gemini_Generated_Image_4nwpmx4nwpmx4nwp.jpg", "Indoor Archery Arena"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.jpg", "Bushcraft Fire Starting"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.jpg", "Laser Tag Equipment Delivery"),
    ("Gemini_Generated_Image_q74buoq74buoq74b.jpg", "Outdoor Laser Tag Action"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.jpg", "Indoor Neon Arena"),
    ("Gemini_Generated_Image_hunw61hunw61hunw.jpg", "Victory Celebration"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.jpg", "Stouthall Mansion Site"),
    ("Gemini_Generated_Image_xz9er1xz9er1xz9e.jpg", "Indoor Team Logic Challenge"),
    ("Gemini_Generated_Image_vv49c1vv49c1vv49.jpg", "Indoor Cooperative Games"),
    ("Gemini_Generated_Image_olevawolevawolev.jpg", "Outdoor Physical Puzzles"),
    ("Gemini_Generated_Image_cueiazcueiazcuei.jpg", "Outdoor Team Competition")
]

# 4. UI STYLING
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .stat-bar { background-color: #f0f2f5; padding: 10px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 4px; margin-bottom: 15px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 15px; border-radius: 8px; margin-bottom: 5px; font-weight: bold; }
    .motto { color: #adb9d3; font-weight: bold; font-size: 22px; text-align: center; display: block; margin-top: 20px; letter-spacing: 3px; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# 5. HEADER
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    # Business Site Image
    if os.path.exists("Gemini_Generated_Image_lpugatlpugatlpug.jpg"):
        st.image("Gemini_Generated_Image_lpugatlpugatlpug.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business Hub:</b> Swansea.<br><b>Activity Site:</b> Stouthall Country Mansion.<br><b>Wet Weather:</b> Indoor arena at Stouthall.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Newsletter Signup", placeholder="email@example.com", key="side_nl")
    if st.button("Subscribe"): st.toast("Welcome to the Hive! 🐝")

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    # --- TAB 1: INFO ---
    with tab1:
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company offering exciting days out for young people. While we are based in Swansea, <b>all activities take place at the Stouthall Country Mansion</b>. We provide unforgettable experiences including bushcraft, team sports, and murder mystery days full of brain-boggling puzzles.<br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)

    # --- TAB 2: POSTS (Using Your Images) ---
    with tab_posts:
        st.markdown('<div class="section-header">Stouthall Activity Feed</div>', unsafe_allow_html=True)
        
        posts_content = [
            ("The range is ready! Final setups for Target Day at Stouthall. 🏹", "Gemini_Generated_Image_wdo2rzwdo2rzwdo2.jpg"),
            ("Intense concentration at our forest archery session. 🎯", "Gemini_Generated_Image_of95w8of95w8of95.jpg"),
            ("The indoor archery hall is looking spectacular for today's sessions! 🏹", "Gemini_Generated_Image_4nwpmx4nwpmx4nwp.jpg"),
            ("Mastering the primitive skills: Fire lighting in the woods. 🔥", "Gemini_Generated_Image_fqzz3rfqzz3rfqzz.jpg"),
            ("New hardware arrival! Fresh laser gear delivered to HQ today. 🔫", "Gemini_Generated_Image_sbz4c8sbz4c8sbz4.jpg"),
            ("High-intensity combat in our woodland laser tag zone. 🌲", "Gemini_Generated_Image_q74buoq74buoq74b.jpg"),
            ("The neon arena is the place to be for fast-paced action. 🌈", "Gemini_Generated_Image_g2yanmg2yanmg2ya.jpg"),
            ("That victory feeling! Celebrating a great team effort today. 🙌", "Gemini_Generated_Image_hunw61hunw61hunw.jpg")
        ]
        
        # Fill to 35 unique posts
        for i in range(len(posts_content), 35):
            posts_content.append((f"Update #{i+1}: Another fantastic session at Stouthall Mansion! See the booking tab for open dates.", None))

        for i, (txt, img) in enumerate(posts_content):
            st.markdown(f'<div class="post-card">{txt}</div>', unsafe_allow_html=True)
            if img and os.path.exists(img): 
                st.image(img, width=420)
            c1, c2 = st.columns([1, 4])
            if c1.button(f"👍 {st.session_state.post_likes[i]}", key=f"feed_pl_{i}"):
                st.session_state.post_likes[i] += 1; st.rerun()

    # --- TAB 3: PHOTOS (Full High-Quality Gallery) ---
    with tab2:
        if st.session_state.photo_index is None:
            cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                    if st.button(f"View {title}", key=f"gal_v_{i}"):
                        st.session_state.photo_index = i; st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(posters[idx][0], width=550, caption=posters[idx][1])
            c1, c2, c3 = st.columns(3)
            if c1.button("⬅ Previous"): st.session_state.photo_index = (idx-1)%len(posters); st.rerun()
            if c2.button("Next ➡"): st.session_state.photo_index = (idx+1)%len(posters); st.rerun()
            if c3.button("❌ Close Gallery"): st.session_state.photo_index = None; st.rerun()

    # --- TAB 4: BOOKING ---
    with tab3:
        st.markdown('<div class="section-header">Book Your Adventure - £54.99</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Choose Event:", list(event_data.keys()))
            dt = st.selectbox("Choose Date:", event_data[evt])
            if st.button("Confirm Details"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "receipt_confirm"; st.rerun()
        
        elif st.session_state.booking_step == "receipt_confirm":
            st.warning("Booking Saved! Do you require a receipt?")
            if st.button("Yes, Send Receipt"): st.session_state.booking_step = "receipt_sent"; st.rerun()
            if st.button("No Receipt, Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

        elif st.session_state.booking_step == "receipt_sent":
            st.success("📩 Receipt sent to your email!")
            if st.button("Return to Booking"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    # --- TAB 5: MY BOOKINGS ---
    with tab4:
        st.markdown('<div class="section-header">Confirmed Slots</div>', unsafe_allow_html=True)
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]}</div>', unsafe_allow_html=True)
            if st.button(f"Cancel Booking {b['id']}", key=f"del_b_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()

    # --- TAB 6: FAQ ---
    with tab5:
        faqs = [
            ("Where is the site?", "Head office Swansea, but ALL events are held at Stouthall Mansion."),
            ("What if it rains?", "We move to the indoor arena at Stouthall."),
            ("What is the cost?", "£54.99 per person for all activities.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
