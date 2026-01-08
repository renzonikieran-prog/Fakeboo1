import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# Memory Management for Interactive Features
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = []
if "photo_likes" not in st.session_state:
    st.session_state.photo_likes = [random.randint(50, 200) for _ in range(6)]
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(10, 100) for _ in range(3)]

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
    .section-header { background-color: #adb9d3; color: white; padding: 6px 12px; font-weight: bold; font-size: 14px; margin-top: 18px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .stat-bar { background-color: #f0f2f5; padding: 10px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 4px; margin-bottom: 15px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 20px; border-radius: 8px; margin-bottom: 10px; }
    .quote-box { font-style: italic; color: #4b4f56; border-left: 4px solid #adb9d3; padding-left: 12px; margin-bottom: 15px; }
    .price-tag { color: #2e7d32; font-size: 24px; font-weight: bold; margin: 10px 0; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; font-size: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business:</b> Blast Hive.<br><b>Location:</b> Swansea, Sketty.</div>', unsafe_allow_html=True)
    
    # Newsletter Section
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    email_sub = st.text_input("Newsletter Email:", placeholder="your@email.com")
    if st.button("Subscribe"):
        st.toast("Welcome to the Hive! 🐝")

    # Contact Team Section
    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Send us a message"):
        c_name = st.text_input("Your Name")
        c_msg = st.text_area("Question")
        if st.button("Submit Message"):
            st.success(f"Thanks {c_name}! Message sent.")

    st.markdown('<div class="section-header">Likes</div>', unsafe_allow_html=True)
    st.markdown("""<div class="content-box">👍 Adventure Sports Wales<br>👍 Gower Activity Centres<br>👍 Swansea Youth Hub</div>""", unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    # --- TAB 1: INFO ---
    with tab1:
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b><br>Followers</div><div class="stat-item"><b>920</b><br>Reviews</div><div class="stat-item"><b>4.9 ⭐</b><br>Rating</div></div>', unsafe_allow_html=True)
        with st.expander("⭐ Add a Review"):
            rev_name = st.text_input("Name", key="rev_n")
            rev_text = st.text_area("Review", key="rev_t")
            if st.button("Post Review"):
                st.session_state.user_reviews.insert(0, {"name": rev_name, "text": rev_text})
                st.rerun()
        
        st.markdown('<div class="section-header">About Us</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company offering exciting days out in Swansea...</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">Reviews & Quotes</div>', unsafe_allow_html=True)
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">"{r["text"]}" - {r["name"]} (Latest)</div>', unsafe_allow_html=True)
        st.markdown('<div class="quote-box">"Best summer activity company in Swansea!" - Parent Review</div>', unsafe_allow_html=True)

    # --- TAB: POSTS ---
    with tab_posts:
        st.markdown('<div class="section-header">Recent Updates</div>', unsafe_allow_html=True)
        feed = [("Target Day gear is here! Ready for Airsoft? 🔫", 0), ("Our indoor backup in Sketty is ready for rain! 🌧️", 1)]
        for text, p_idx in feed:
            st.markdown(f'<div class="post-card">{text}</div>', unsafe_allow_html=True)
            c_l, c_r = st.columns([1, 4])
            if c_l.button(f"👍 {st.session_state.post_likes[p_idx]}", key=f"pl_{p_idx}"):
                st.session_state.post_likes[p_idx] += 1
                st.rerun()
            if c_r.button(f"🔗 Share", key=f"ps_{p_idx}"):
                st.toast("Link copied!")
                st.success("📢 Post Shared successfully!")

    # --- TAB 2: PHOTOS ---
    with tab2:
        if st.session_state.photo_index is None:
            st.markdown('<div class="section-header">Gallery</div>', unsafe_allow_html=True)
            g_cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with g_cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                        if st.button(f"View {title}", key=f"gv_{i}"):
                            st.session_state.photo_index = i
                            st.rerun()
        else:
            # Scaled Down Enlarged View
            l_b, mid, r_b = st.columns([1, 1.5, 1])
            with mid:
                idx = st.session_state.photo_index
                st.image(posters[idx][0], use_container_width=True)
                if st.button(f"❤️ {st.session_state.photo_likes[idx]} Likes", key=f"phl_{idx}"):
                    st.session_state.photo_likes[idx] += 1
                    st.rerun()
                c1, c2, c3 = st.columns(3)
                if c1.button("⬅ Prev"): st.session_state.photo_index = (idx-1)%len(posters); st.rerun()
                if c2.button("Next ➡"): st.session_state.photo_index = (idx+1)%len(posters); st.rerun()
                if c3.button("❌ Close", type="primary"): st.session_state.photo_index = None; st.rerun()

    # --- TAB 3: BOOK NOW ---
    with tab3:
        st.markdown('<div class="section-header">Booking</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Activity:", list(event_data.keys()))
            dt = st.selectbox("Date:", event_data[evt])
            st.markdown('<div class="price-tag">Price: £54.99</div>', unsafe_allow_html=True)
            if st.button("Confirm"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "confirm"; st.rerun()
        elif st.session_state.booking_step == "confirm":
            st.success("Registered!")
            if st.button("Send Receipt"): st.session_state.booking_step = "receipt"; st.rerun()
        elif st.session_state.booking_step == "receipt":
            st.info("📩 Sent to ***********@gmail.com")
            if st.button("Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    # --- TAB 4: MY BOOKINGS ---
    with tab4:
        st.markdown('<div class="section-header">My Schedule</div>', unsafe_allow_html=True)
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]} (ID: {b["id"]})</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"can_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()

    # --- TAB 5: FAQ ---
    with tab5:
        st.markdown('<div class="section-header">FAQ</div>', unsafe_allow_html=True)
        st.markdown("""<div class="content-box"><p class="faq-q">Is gear included?</p><p>Yes, all gear is in the £54.99 price.</p><p class="faq-q">What if it rains?</p><p>We use indoor facilities in Sketty.</p></div>""", unsafe_allow_html=True)
