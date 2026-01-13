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
        {"name": "Liam W.", "stars": "⭐⭐⭐⭐⭐", "text": "Best laser tag experience in Wales! Professional staff."},
        {"name": "Chloe M.", "stars": "⭐⭐⭐⭐", "text": "Really enjoyed the bushcraft session."},
        {"name": "Dan R.", "stars": "⭐⭐⭐⭐⭐", "text": "The puzzles at Stouthall were brain-melters. Loved it!"}
    ]
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(45, 950) for _ in range(100)]
if "sent_messages" not in st.session_state:
    st.session_state.sent_messages = []

# 2. CONTENT MAPPING (Poster + Activities)
activity_content = [
    ("image(1).png", "Target Day 2026: Axe Throwing, Airsoft, Paintball, and Laser Tag. 🎯 £54.99 per person."),
    ("Gemini_Generated_Image_wdo2rzwdo2rzwdo2.png", "Morning sessions on the archery range. 🏹"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.png", "Survival skills: Master of the campfire. 🔥"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.png", "Tactical gear delivery: Ready for combat. 🔫"),
    ("Gemini_Generated_Image_of95w8of95w8of95.png", "Precision and focus: Archery clinic at Stouthall. 🎯"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.png", "The historic Stouthall Mansion grounds. 🏰"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.png", "Neon arena: Action rain or shine. 🌈"),
    ("Gemini_Generated_Image_xz9er1xz9er1xz9e.png", "Teamwork: Crack the mystery logic crates. 🧠"),
    ("Gemini_Generated_Image_hunw61hunw61hunw.png", "The feeling of a hard-fought victory. 🙌"),
    ("Gemini_Generated_Image_olevawolevawolev.png", "Outdoor strategy puzzles in the sun. 🧩"),
    ("Gemini_Generated_Image_vv49c1vv49c1vv49.png", "Building trust through cooperative play. 🏗️"),
    ("Gemini_Generated_Image_cueiazcueiazcuei.png", "The final sprint across the estate. 🏃")
]

# 3. UI STYLING
st.markdown("""
    <style>
    .fb-logo { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; font-size: 28px; letter-spacing: -1px; }
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); font-weight: bold; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# 4. HEADER
st.markdown('<div class="nav-bar"><span class="fb-logo">fakebook</span><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Hub:</b> Swansea.<br><b>Site:</b> Stouthall Mansion.<br><b>Price:</b> £54.99.</div>', unsafe_allow_html=True)
    
    with st.expander("Message Team"):
        m_name = st.text_input("Name", key="m_n")
        m_text = st.text_area("Message", key="m_t")
        if st.button("Send"):
            if m_name and m_text:
                st.session_state.sent_messages.insert(0, f"<b>{m_name}:</b> {m_text}")
                st.rerun()

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1: # ABOUT
        st.markdown('<div class="section-header">About Target Day 2026</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">Blast Hive presents the 2026 Target Day season at Stouthall Mansion. Experience elite axe throwing, airsoft, and tactical laser tag for a flat rate of £54.99.</div>', unsafe_allow_html=True)

    with tab3: # RESTRICTED BOOKING
        st.markdown('<div class="section-header">Target Day Booking - £54.99</div>', unsafe_allow_html=True)
        dt = st.selectbox("Select Date (August 4th-11th):", ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th"])
        if st.button("Reserve Ticket"):
            st.session_state.my_bookings.append({"event": "Target Day", "date": f"{dt} August", "id": f"BH-{random.randint(1000, 9999)}"})
            st.success(f"Reserved for {dt} August!")

    with tab5: # UPDATED FAQs
        st.markdown('<div class="section-header">Target Day FAQ</div>', unsafe_allow_html=True)
        faqs = [
            ("What is Target Day?", "A multi-activity event featuring archery, airsoft, paintball, and axe throwing."),
            ("What dates are available?", "Booking is open exclusively from August 4th to August 11th, 2026."),
            ("How much does it cost?", "The all-inclusive price is £54.99 per person."),
            ("Are the activities safe?", "Yes, all sessions are led by first-aid trained instructors with professional gear."),
            ("Where do I go?", "All Target Day events take place at Stouthall Country Mansion.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
