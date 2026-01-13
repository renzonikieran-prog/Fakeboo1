import streamlit as st
import os
import random
from datetime import datetime

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Fakebook")

# 1. LIVE DATA LOGIC
target_date = datetime(2026, 8, 4)
now = datetime.now()
delta = target_date - now
days_left = delta.days

# 2. Memory Management (Session State)
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = [
        {"name": "Liam W.", "stars": "⭐⭐⭐⭐⭐", "text": "Target Day was incredible. The axe throwing was a highlight!"},
        {"name": "Chloe M.", "stars": "⭐⭐⭐⭐", "text": "Professional staff and a stunning location at Stouthall."},
        {"name": "Dan R.", "stars": "⭐⭐⭐⭐⭐", "text": "Best £54.99 I've spent. Tactical laser tag was so intense!"}
    ]
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(45, 950) for _ in range(100)]
if "sent_messages" not in st.session_state:
    st.session_state.sent_messages = []

# 3. CONTENT MAPPING
activity_content = [
    ("image(1).png", "TARGET DAY 2026: The ultimate multi-activity experience. 🎯 £54.99 All-Inclusive."),
    ("Gemini_Generated_Image_wdo2rzwdo2rzwdo2.png", "Professional archery range setup at Stouthall. 🏹"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.png", "Mastering survival skills in the deep woods. 🔥"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.png", "Elite tactical gear ready for the field. 🔫"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.png", "The historic Stouthall Mansion: Home of the Hive. 🏰"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.png", "Indoor neon arena for all-weather action. 🌈")
]

# 4. UI STYLING
st.markdown("""
    <style>
    .fb-logo { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; font-size: 28px; letter-spacing: -1px; }
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .countdown-timer { background-color: #f02849; color: white; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 14px; }
    .stat-bar { background-color: #f0f2f5; padding: 15px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 8px; margin-bottom: 20px; text-align: center; }
    .stat-item { color: #1c1e21; font-size: 14px; }
    .stat-value { font-weight: bold; font-size: 18px; display: block; color: #adb9d3; }
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 5. HEADER (Includes Countdown)
st.markdown(f'''
    <div class="nav-bar">
        <span class="fb-logo">fakebook</span>
        <div style="display:flex; gap:15px; align-items:center;">
            <div class="countdown-timer">⏳ {days_left} Days Until Target Day!</div>
            <span>Profile</span><span>Inbox</span><span>Friends</span>
            <div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div>
        </div>
    </div>
''', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Hub:</b> Swansea.<br><b>Site:</b> Stouthall Mansion.<br><b>Rate:</b> £54.99.</div>', unsafe_allow_html=True)
    
    # Newsletter & Messaging
    st.text_input("Newsletter Signup", placeholder="email@example.com", key="side_nl")
    if st.button("Subscribe"): st.toast("Welcome to the Hive! 🐝")
    
    with st.expander("Message Team"):
        m_name = st.text_input("Name", key="m_n")
        m_text = st.text_area("Message", key="m_t")
        if st.button("Send"):
            if m_name and m_text:
                st.session_state.sent_messages.insert(0, f"<b>{m_name}:</b> {m_text}")
                st.rerun()

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1: # FOLLOWERS, STAR RATING & ABOUT
        # STAT BAR FOR FOLLOWERS AND STARS
        st.markdown(f'''
            <div class="stat-bar">
                <div class="stat-item"><span class="stat-value">1,428</span>Followers</div>
                <div class="stat-item"><span class="stat-value">914</span>Check-ins</div>
                <div class="stat-item"><span class="stat-value">4.9 ⭐</span>Overall Rating</div>
            </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">Company Overview: Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">South Wales\' premier adventure provider. 30 acres of elite challenges at Stouthall Mansion. All-inclusive rate of £54.99.</div>', unsafe_allow_html=True)
        
        # REVIEWS
        st.markdown('<div class="section-header">User Reviews</div>', unsafe_allow_html=True)
        with st.expander("⭐ Post a Star Rating"):
            r_n = st.text_input("Reviewer Name")
            r_s = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_t = st.text_area("Experience Details")
            if st.button("Post Review"):
                if r_n and r_t:
                    st.session_state.user_reviews.insert(0, {"name": r_n, "stars": r_s, "text": r_t})
                    st.rerun()
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="content-box">{r["stars"]} "{r["text"]}" - {r["name"]}</div>', unsafe_allow_html=True)

    with tab_posts: # POST LIKES (55 Posts)
        for i in range(55):
            st.markdown('<div class="post-card">', unsafe_allow_html=True)
            img, cap = activity_content[i % len(activity_content)]
            st.write(cap)
            if os.path.exists(img):
                st.image(img, width=450)
            # LIKE BUTTON
            if st.button(f"👍 {st.session_state.post_likes[i]} Likes", key=f"feed_pl_{i}"):
                st.session_state.post_likes[i] += 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    with tab3: # Booking Restricted
        st.markdown('<div class="section-header">Target Day Booking - £54.99</div>', unsafe_allow_html=True)
        dt = st.selectbox("Select Date (August 4th-11th):", ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th"])
        if st.button("Confirm Ticket"):
            st.session_state.my_bookings.append({"event": "Target Day", "date": f"{dt} August", "id": f"BH-{random.randint(1000, 9999)}"})
            st.success(f"Reserved! See you on August {dt}!")
