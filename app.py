import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Fakebook")

# 1. Memory Management (Session State)
# Ensuring all features stay active and don't "disappear" on reload
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    # Hardcoded random reviews to ensure section is never empty
    st.session_state.user_reviews = [
        {"name": "Liam W.", "stars": "⭐⭐⭐⭐⭐", "text": "Best laser tag experience in Wales! Professional staff."},
        {"name": "Chloe M.", "stars": "⭐⭐⭐⭐", "text": "Really enjoyed the bushcraft session."},
        {"name": "Dan R.", "stars": "⭐⭐⭐⭐⭐", "text": "The puzzles at Stouthall were brain-melters. Loved it!"}
    ]
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(45, 950) for _ in range(100)]
if "sent_messages" not in st.session_state:
    st.session_state.sent_messages = []

# 2. CONTENT MAPPING (Matches Text to Image)
# Activities = .png | Posters = .jpg
content_map = [
    ("target_day.jpg", "The official Target Day 2026 poster is here! 🏹 #TargetDay"),
    ("adrenaline_weekend.jpg", "High-stakes tactical fun at Stouthall. 🔫 #Adrenaline"),
    ("ultimate_challenge.jpg", "6 Activities. 1 Champion. Are you ready? 🏆"),
    ("Gemini_Generated_Image_wdo2rzwdo2rzwdo2.png", "The archery range is looking perfect this morning. 🏹"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.png", "Mastering the art of fire-lighting in the deep woods. 🔥 #Bushcraft"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.png", "Fresh delivery! Our new tactical laser gear has arrived. 🔫"),
    ("Gemini_Generated_Image_of95w8of95w8of95.png", "Intense focus during our expert archery clinic. 🎯"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.png", "A cinematic look at Stouthall Mansion—the home of adventure. 🏰"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.png", "The neon arena ensures the action never stops. 🌈 #IndoorGaming"),
    ("Gemini_Generated_Image_xz9er1xz9er1xz9e.png", "Logic puzzles are the ultimate team test. 🧠 #EscapeRoom")
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
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# 4. HEADER
st.markdown('<div class="nav-bar"><span class="fb-logo">fakebook</span><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    # LOGO
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Hub:</b> Swansea.<br><b>Site:</b> Stouthall Mansion.<br><b>Rate:</b> £54.99 per person.</div>', unsafe_allow_html=True)
    
    # RESTORED NEWSLETTER
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Newsletter Signup", placeholder="email@example.com", key="side_nl")
    if st.button("Subscribe"): st.toast("Welcome to the Hive! 🐝")

    # RESTORED MESSAGE TEAM
    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Message Us"):
        m_name = st.text_input("Name", key="m_n")
        m_text = st.text_area("Message", key="m_t")
        if st.button("Send Message"):
            if m_name and m_text:
                st.session_state.sent_messages.insert(0, f"<b>{m_name}:</b> {m_text}")
                st.success("Message Sent!")
    for m in st.session_state.sent_messages:
        st.markdown(f'<div class="content-box" style="font-size:10px;">{m}</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1: # ABOUT & RESTORED REVIEWS
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">Company Overview</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">Blast Hive is South Wales\' premier adventure provider. Operating exclusively on the historic 30-acre Stouthall Mansion estate, we deliver high-intensity activity days designed to foster teamwork and resilience. <br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        with st.expander("⭐ Leave a Review"):
            r_n = st.text_input("Reviewer Name")
            r_s = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_t = st.text_area("Experience?")
            if st.button("Post Review"):
                if r_n and r_t:
                    st.session_state.user_reviews.insert(0, {"name": r_n, "stars": r_s, "text": r_t})
                    st.rerun()
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="content-box">{r["stars"]} "{r["text"]}" - {r["name"]}</div>', unsafe_allow_html=True)

    with tab_posts: # 55 UNIQUE POSTS WITH LIKES
        for i in range(55):
            st.markdown('<div class="post-card">', unsafe_allow_html=True)
            img, cap = content_map[i % len(content_map)]
            st.write(cap)
            if os.path.exists(img):
                st.image(img, width=450)
            c1, c2 = st.columns([1, 4])
            if c1.button(f"👍 {st.session_state.post_likes[i]} Likes", key=f"feed_pl_{i}"):
                st.session_state.post_likes[i] += 1
                st.rerun()
            if c2.button("🔗 Share", key=f"feed_ps_{i}"): st.success("📢 Shared!")
            st.markdown('</div>', unsafe_allow_html=True)

    with tab2: # RESTORED PHOTO GALLERY
        if st.session_state.photo_index is None:
            cols = st.columns(3)
            for i, (img, title) in enumerate(content_map):
                with cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                        if st.button(f"View {title}", key=f"gal_v_{i}"):
                            st.session_state.photo_index = i
                            st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(content_map[idx][0], use_container_width=True, caption=content_map[idx][1])
            if st.button("❌ Close Gallery"):
                st.session_state.photo_index = None
                st.rerun()

    with tab3: # BOOKING
        st.markdown('<div class="section-header">Book Your Adventure - £54.99</div>', unsafe_allow_html=True)
        evt = st.selectbox("Choose Event:", ["Target Day", "Adrenaline Weekend", "Ultimate Challenge Day"])
        dt = st.selectbox("Choose Date:", ["4th August", "8th August", "12th August"])
        if st.button("Confirm Details"):
            st.session_state.my_bookings.append({"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"})
            st.success("Reserved! Receipt sent to connected email.")

    with tab4: # MY BOOKINGS
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]}</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"del_b_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()

    with tab5: # RESTORED FAQs
        faqs = [
            ("Where is the site?", "All events are held at Stouthall Mansion."),
            ("What if it rains?", "We use our indoor arena at Stouthall."),
            ("What is the cost?", "£54.99 per person for all activities."),
            ("Are staff qualified?", "Yes, Enhanced DBS checked and First Aid trained.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
