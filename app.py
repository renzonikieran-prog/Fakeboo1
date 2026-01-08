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
        {"name": "Liam W.", "stars": "⭐⭐⭐⭐⭐", "text": "Best laser tag experience in Wales!"},
        {"name": "Chloe M.", "stars": "⭐⭐⭐⭐", "text": "Really enjoyed the bushcraft, just wish it lasted longer!"},
        {"name": "Dan R.", "stars": "⭐⭐⭐⭐⭐", "text": "The puzzles at Stouthall were actual brain-melters. Loved it."},
        {"name": "Eira G.", "stars": "⭐⭐⭐⭐⭐", "text": "Super professional staff and the mansion grounds are stunning."}
    ]
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(45, 1200) for _ in range(110)]

# 2. DATA MAPPING
event_data = {
    "Target Day": ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th August"],
    "Adrenaline Weekend": ["12th", "13th", "14th", "18th", "19th August"],
    "Ultimate Challenge Day": ["6th", "7th", "11th", "20th August"],
    "Social Play Fest": ["9th", "10th", "15th", "16th August"],
    "Extreme Impact Day": ["4th", "5th", "17th", "22nd August"],
    "Skill Switch Experience": ["8th", "14th", "21st", "23rd August"]
}

# Combined Image List for Feed (Posters + Activities)
# Posters are .jpg, Activities are .png per your instructions
all_media = [
    ("target_day.jpg", "Target Day is approaching! Book your slot now."),
    ("adrenaline_weekend.jpg", "Are you ready for the Adrenaline Weekend?"),
    ("ultimate_challenge.jpg", "The Ultimate Challenge awaits at Stouthall."),
    ("social_play_fest.jpg", "Join the community at our Social Play Fest!"),
    ("extreme_impact.jpg", "Extreme Impact: Not for the faint of heart."),
    ("skill_switch.jpg", "Learn something new with the Skill Switch Experience."),
    ("Gemini_Generated_Image_wdo2rzwdo2rzwdo2.png", "The range is looking perfect this morning. 🏹"),
    ("Gemini_Generated_Image_of95w8of95w8of95.png", "Focus, aim, and release. Archery sessions in full swing. 🎯"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.png", "Mastering the elements in our survival workshop. 🔥"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.png", "New tactical delivery! The hive is expanding. 🔫"),
    ("Gemini_Generated_Image_q74buoq74buoq74b.png", "Forest combat: Strategy is everything. 🌲"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.png", "Neon nights at the indoor arena. 🌈"),
    ("Gemini_Generated_Image_hunw61hunw61hunw.png", "Celebrating a hard-earned victory at sunset! 🙌"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.png", "Our home for the summer: Stouthall Country Mansion. 🏴󠁧󠁢󠁷󠁬󠁳󠁿"),
    ("Gemini_Generated_Image_xz9er1xz9er1xz9e.png", "Cracking codes and solving mysteries indoors. 🧠"),
    ("Gemini_Generated_Image_vv49c1vv49c1vv49.png", "Teamwork makes the dream work in the sports hall. 🏗️"),
    ("Gemini_Generated_Image_olevawolevawolev.png", "Outdoor logic puzzles testing the limits. 🧩"),
    ("Gemini_Generated_Image_cueiazcueiazcuei.png", "The final race across the estate grounds! 🏃")
]

# 3. UI STYLING
st.markdown("""
    <style>
    .fb-logo { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; font-size: 28px; letter-spacing: -1px; }
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .stat-bar { background-color: #f0f2f5; padding: 10px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 4px; margin-bottom: 15px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 15px; border-radius: 8px; margin-bottom: 5px; font-weight: bold; }
    .motto { color: #adb9d3; font-weight: bold; font-size: 22px; text-align: center; display: block; margin-top: 20px; letter-spacing: 3px; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; display: block; }
    .quote-box { border-left: 5px solid #adb9d3; background-color: #f9f9f9; padding: 10px; margin-bottom: 10px; font-style: italic; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# 4. HEADER
st.markdown('<div class="nav-bar"><span class="fb-logo">fakebook</span><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    # UPDATED LOGO
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business Hub:</b> Swansea.<br><b>Activity Site:</b> Stouthall Country Mansion.</div>', unsafe_allow_html=True)
    
    # Followers You Know
    st.markdown('<div class="section-header">Followers You Know</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box" style="font-size: 12px; color: #606770;">👥 <b>Gareth Evans</b>, <b>Bethan Jones</b> and 42 other friends like this.</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Newsletter Signup", placeholder="email@example.com", key="side_nl")
    if st.button("Subscribe"): st.toast("Welcome to the Hive! 🐝")

    with st.expander("Message Us"):
        st.text_input("Your Name", key="side_msg_n")
        if st.button("Send"): st.success("Message Sent!")

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1: # INFO & REVIEWS
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">Blast Hive offers unforgettable experiences at Stouthall Mansion. <br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        with st.expander("⭐ Leave a Review"):
            r_n = st.text_input("Name")
            r_s = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_t = st.text_area("Experience?")
            if st.button("Post Review"):
                if r_n and r_t:
                    st.session_state.user_reviews.insert(0, {"name": r_n, "stars": r_s, "text": r_t})
                    st.rerun()

        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">{r["stars"]} "{r["text"]}" - {r["name"]}</div>', unsafe_allow_html=True)

    # --- TAB 2: 55 UNIQUE POSTS ---
    with tab_posts:
        st.markdown('<div class="section-header">Recent Activity</div>', unsafe_allow_html=True)
        
        # Build 55 unique items
        campaign_feed = []
        for i in range(55):
            if i < len(all_media):
                campaign_feed.append(all_media[i])
            else:
                # Randomly recycling text for filler posts to reach 55+
                txt = random.choice([
                    "Another day of adventure at the mansion! Check out our August schedule.",
                    "Limited slots left for the next Adrenaline Weekend. Don't miss out!",
                    "Professional staff and top-tier equipment. That's the Blast Hive promise.",
                    "Rainy weather? Our indoor hall at Stouthall has you covered.",
                    "Join 1,400+ other followers and become part of the hive today!"
                ])
                campaign_feed.append((None, txt))

        for i, (img, txt) in enumerate(campaign_feed):
            st.markdown(f'<div class="post-card">{txt}</div>', unsafe_allow_html=True)
            if img: st.image(img, width=420)
            c1, c2 = st.columns([1, 4])
            if c1.button(f"👍 {st.session_state.post_likes[i]}", key=f"feed_pl_{i}"):
                st.session_state.post_likes[i] += 1; st.rerun()
            if c2.button("🔗 Share", key=f"feed_ps_{i}"): st.success("📢 Shared to your timeline!")

    with tab3: # BOOKING & RECEIPT LOGIC
        st.markdown('<div class="section-header">Book Your Adventure - £54.99</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Choose Event:", list(event_data.keys()))
            dt = st.selectbox("Choose Date:", event_data[evt])
            if st.button("Confirm Details"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "receipt_confirm"; st.rerun()
        
        elif st.session_state.booking_step == "receipt_confirm":
            st.warning("Do you require a digital receipt?")
            col1, col2 = st.columns(2)
            if col1.button("Yes, Send Receipt to Gmail"): 
                st.session_state.booking_step = "receipt_sent"; st.rerun()
            if col2.button("No Receipt, Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

        elif st.session_state.booking_step == "receipt_sent":
            st.success("📩 Receipt sent to *******@gmail.com!")
            if st.button("Back to Hub"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    with tab5: # EXPANDED FAQs
        st.markdown('<div class="section-header">Frequently Asked Questions</div>', unsafe_allow_html=True)
        faqs = [
            ("Where is the site?", "Head office Swansea, but ALL events are held at Stouthall Mansion."),
            ("What if it rains?", "We move to the indoor arena at Stouthall."),
            ("What is the cost?", "£54.99 per person for all activities."),
            ("Are staff qualified?", "Yes, all staff are Enhanced DBS checked and First Aid trained."),
            ("Do you offer group discounts?", "Yes, groups of 10+ receive a 10% discount."),
            ("What should I bring?", "Water, snacks, and a change of clothes if it's wet!"),
            ("Is there parking?", "Yes, there is free parking available on-site at Stouthall."),
            ("Is there an age limit?", "Activities are designed for ages 12–17."),
            ("How long do sessions last?", "Typical sessions run for approximately 4 hours.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
