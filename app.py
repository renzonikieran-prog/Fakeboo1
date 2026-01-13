import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Fakebook")

# 1. Memory Management (Session State)
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

# 2. CONTENT MAPPING (Poster + Activities)
activity_content = [
    ("image(1).png", "TARGET DAY 2026: The ultimate multi-activity experience. 🎯 £54.99 All-Inclusive."),
    ("Gemini_Generated_Image_wdo2rzwdo2rzwdo2.png", "Professional archery range setup at the Stouthall grounds. 🏹"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.png", "Mastering survival skills in the deep Stouthall woods. 🔥"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.png", "Elite tactical gear ready for the field. 🔫"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.png", "The historic Stouthall Mansion: Home of the Hive. 🏰"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.png", "Indoor neon arena for all-weather action. 🌈"),
    ("Gemini_Generated_Image_of95w8of95w8of95.png", "Focus and precision training today. 🎯"),
    ("Gemini_Generated_Image_hunw61hunw61hunw.png", "Victory celebration after the ultimate challenge! 🙌"),
    ("Gemini_Generated_Image_xz9er1xz9er1xz9e.png", "Team logic and strategy crates. 🧠"),
    ("Gemini_Generated_Image_vv49c1vv49c1vv49.png", "Cooperative indoor sports and team building. 🏗️")
]

# 3. UI STYLING
st.markdown("""
    <style>
    .fb-logo { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; font-size: 28px; letter-spacing: -1px; }
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
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
    st.markdown('<div class="content-box"><b>Hub:</b> Swansea.<br><b>Site:</b> Stouthall Mansion.<br><b>Target Day Rate:</b> £54.99.</div>', unsafe_allow_html=True)
    
    # NEWSLETTER
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Newsletter Signup", placeholder="email@example.com", key="side_nl")
    if st.button("Subscribe"): st.toast("Welcome to the Hive! 🐝")

    # MESSAGING SYSTEM
    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Message Us"):
        m_name = st.text_input("Name", key="m_n")
        m_text = st.text_area("Message", key="m_t")
        if st.button("Send"):
            if m_name and m_text:
                st.session_state.sent_messages.insert(0, f"<b>{m_name}:</b> {m_text}")
                st.rerun()
    for m in st.session_state.sent_messages:
        st.markdown(f'<div class="content-box" style="font-size:10px;">{m}</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1: # ABOUT & REVIEWS
        st.markdown('<div class="section-header">Company Overview: Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">Blast Hive is South Wales\' premier adventure provider, specializing in high-intensity, logic-driven activity days. Operating from the historic 30-acre <b>Stouthall Country Mansion</b>, we offer professional instruction in elite survival skills, tactical sports, and team-building challenges. Our mission is to deliver world-class outdoor experiences that foster resilience and leadership—all at a transparent, all-inclusive flat rate. <br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">Community Feedback</div>', unsafe_allow_html=True)
        with st.expander("⭐ Leave a Review"):
            r_n = st.text_input("Reviewer Name")
            r_s = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_t = st.text_area("Your Experience")
            if st.button("Post Review"):
                if r_n and r_t:
                    st.session_state.user_reviews.insert(0, {"name": r_n, "stars": r_s, "text": r_t})
                    st.rerun()
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="content-box">{r["stars"]} "{r["text"]}" - {r["name"]}</div>', unsafe_allow_html=True)

    with tab_posts: # 55 UNIQUE POSTS
        for i in range(55):
            st.markdown('<div class="post-card">', unsafe_allow_html=True)
            img, cap = activity_content[i % len(activity_content)]
            st.write(cap)
            if os.path.exists(img):
                st.image(img, width=450)
            c1, c2 = st.columns([1, 4])
            if c1.button(f"👍 {st.session_state.post_likes[i]} Likes", key=f"feed_pl_{i}"):
                st.session_state.post_likes[i] += 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    with tab2: # PHOTO GALLERY
        if st.session_state.photo_index is None:
            cols = st.columns(3)
            for i, (img, title) in enumerate(activity_content):
                with cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                        if st.button(f"View {i+1}", key=f"gal_v_{i}"):
                            st.session_state.photo_index = i
                            st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(activity_content[idx][0], use_container_width=True, caption=activity_content[idx][1])
            if st.button("❌ Close Gallery"):
                st.session_state.photo_index = None
                st.rerun()

    with tab3: # RESTRICTED BOOKING
        st.markdown('<div class="section-header">Target Day Booking - £54.99</div>', unsafe_allow_html=True)
        dt = st.selectbox("Select Date (August 4th-11th):", ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th"])
        if st.button("Reserve Ticket"):
            st.session_state.my_bookings.append({"event": "Target Day", "date": f"{dt} August", "id": f"BH-{random.randint(1000, 9999)}"})
            st.success(f"Reserved for August {dt}!")

    with tab4: # MY BOOKINGS
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]} | Rate: £54.99</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"del_b_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()

    with tab5: # FAQs
        st.markdown('<div class="section-header">Frequently Asked Questions</div>', unsafe_allow_html=True)
        faqs = [
            ("What is Target Day?", "A premier multi-activity event featuring archery, airsoft, and tactical laser tag."),
            ("What is the cost?", "The flat rate is £54.99 per person, covering all gear and instruction."),
            ("Where is the site?", "All events take place at Stouthall Country Mansion."),
            ("Is it safe?", "Sessions are led by qualified instructors who are first-aid trained.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
