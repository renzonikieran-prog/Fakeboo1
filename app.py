import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Fakebook")

# 1. Memory Management (Session State)
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = [
        {"name": "Liam W.", "stars": "⭐⭐⭐⭐⭐", "text": "Best laser tag experience in Wales! Professional staff."},
        {"name": "Chloe M.", "stars": "⭐⭐⭐⭐", "text": "Really enjoyed the bushcraft session."},
        {"name": "Dan R.", "stars": "⭐⭐⭐⭐⭐", "text": "The puzzles at Stouthall were brain-melters. Loved it!"}
    ]
if "sent_messages" not in st.session_state:
    st.session_state.sent_messages = []
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(45, 950) for _ in range(100)]

# 2. MATCHED CAMPAIGN CONTENT (Text matches Image)
# Posters = .jpg | Activities = .png
content_map = [
    ("target_day.jpg", "The official Target Day 2026 poster is here! Get ready for our biggest archery event of the summer. 🏹 #TargetDay"),
    ("adrenaline_weekend.jpg", "Are you bold enough for the Adrenaline Weekend? High-stakes tactical fun at Stouthall. 🔫 #Adrenaline"),
    ("ultimate_challenge.jpg", "6 Activities. 1 Champion. The Ultimate Challenge poster reveals what you're up against this August. 🏆"),
    ("Gemini_Generated_Image_wdo2rzwdo2rzwdo2.png", "The range is set! Our outdoor archery field at Stouthall is looking perfect for the morning session. 🏹"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.png", "Mastering the elements. Today's survivalists learned the art of fire-lighting in the deep woods. 🔥 #Bushcraft"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.png", "Fresh delivery at HQ! Our new tactical laser gear has arrived and is ready for the Adrenaline Weekend. 🔫"),
    ("Gemini_Generated_Image_of95w8of95w8of95.png", "Intense focus during our expert archery clinic. Precision and discipline are the keys to the hive. 🎯"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.png", "A cinematic look at Stouthall Mansion—the 30-acre home of Blast Hive adventure. 🏰 #Stouthall"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.png", "The neon arena is glowing. Our indoor facility ensures the action never stops, rain or shine. 🌈 #IndoorGaming"),
    ("Gemini_Generated_Image_xz9er1xz9er1xz9e.png", "Logic puzzles are the ultimate team test. Can your group crack the Stouthall Mystery crates? 🧠 #EscapeRoom"),
    ("Gemini_Generated_Image_hunw61hunw61hunw.png", "That victory feeling! Celebrating a hard-fought win at the end of a Physical Challenge session. 🙌 #Winners"),
    ("Gemini_Generated_Image_olevawolevawolev.png", "Outdoor logic challenges in the sun. It takes more than just speed to win at Blast Hive. 🧩 #Strategy"),
    ("Gemini_Generated_Image_vv49c1vv49c1vv49.png", "Indoor cooperative games are in full swing today. Building trust through high-energy sports. 🏗️ #Teamwork"),
    ("Gemini_Generated_Image_cueiazcueiazcuei.png", "The final sprint! A race across the mansion grounds to finish the Ultimate Challenge Day. 🏃 #Fitness")
]

# 3. UI STYLING
st.markdown("""
    <style>
    .fb-logo { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; font-size: 28px; letter-spacing: -1px; }
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .stat-bar { background-color: #f0f2f5; padding: 10px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 4px; margin-bottom: 15px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); font-weight: bold; }
    .motto { color: #adb9d3; font-weight: bold; font-size: 22px; text-align: center; display: block; margin-top: 20px; letter-spacing: 3px; }
    </style>
    """, unsafe_allow_html=True)

# 4. HEADER
st.markdown('<div class="nav-bar"><span class="fb-logo">fakebook</span><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Hub:</b> Swansea.<br><b>Site:</b> Stouthall Country Mansion.<br><b>Rate:</b> £54.99 per person.</div>', unsafe_allow_html=True)
    
    # Message Logic
    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Message Us"):
        m_name = st.text_input("Name", key="m_n")
        m_text = st.text_area("Message", key="m_t")
        if st.button("Send"):
            if m_name and m_text:
                st.session_state.sent_messages.insert(0, f"<b>{m_name}:</b> {m_text}")
                st.success("Sent!")
    for m in st.session_state.sent_messages:
        st.markdown(f'<div class="content-box" style="font-size:10px;">{m}</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1: # IMPROVED ABOUT SECTION
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">Company Overview: Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">Blast Hive is South Wales\' premier adventure provider for young people. Operating exclusively on the historic 30-acre <b>Stouthall Country Mansion</b> estate, we deliver high-intensity, logic-driven activity days designed to foster teamwork, resilience, and skill. Our all-inclusive day sessions feature professional instruction in bushcraft, tactical sports, and elite problem-solving. We pride ourselves on offering fair, transparent pricing to ensure every young person can experience an unforgettable day of adventure. <br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">Community Reviews</div>', unsafe_allow_html=True)
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="content-box">{r["stars"]} "{r["text"]}" - {r["name"]}</div>', unsafe_allow_html=True)

    with tab_posts: # 55 UNIQUE POSTS
        st.markdown('<div class="section-header">Recent Activity</div>', unsafe_allow_html=True)
        for i in range(55):
            st.markdown('<div class="post-card">', unsafe_allow_html=True)
            # Cycle through the matched content map
            img, cap = content_map[i % len(content_map)]
            st.write(cap)
            if os.path.exists(img):
                st.image(img, width=450)
            c1, c2 = st.columns([1, 4])
            if c1.button(f"👍 {st.session_state.post_likes[i]}", key=f"feed_pl_{i}"):
                st.session_state.post_likes[i] += 1
                st.rerun()
            if c2.button("🔗 Share", key=f"feed_ps_{i}"): st.success("📢 Shared!")
            st.markdown('</div>', unsafe_allow_html=True)

    with tab3: # BOOKING
        st.markdown('<div class="section-header">Book Your Adventure - £54.99</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Choose Event:", ["Target Day", "Adrenaline Weekend", "Ultimate Challenge Day"])
            dt = st.selectbox("Choose Date:", ["4th August", "8th August", "12th August"])
            if st.button("Confirm Details"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "receipt_confirm"; st.rerun()
        elif st.session_state.booking_step == "receipt_confirm":
            st.warning("Do you require a digital receipt?")
            col1, col2 = st.columns(2)
            if col1.button("Yes, Send Receipt"): st.session_state.booking_step = "receipt_sent"; st.rerun()
            if col2.button("No, Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()
