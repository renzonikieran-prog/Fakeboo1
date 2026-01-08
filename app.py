import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# Core Memory (Session State)
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = []
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(5, 250) for _ in range(25)]

# --- DATA MAPPING ---
event_data = {
    "Target Day": ["4th", "5th", "6th", "7th August"],
    "Adrenaline Weekend": ["12th", "13th", "14th August"],
    "Ultimate Challenge Day": ["6th", "11th August"],
    "Social Play Fest": ["9th", "15th August"],
    "Extreme Impact Day": ["4th", "17th August"],
    "Skill Switch Experience": ["8th", "14th August"]
}

# --- UI STYLING ---
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .stat-bar { background-color: #f0f2f5; padding: 10px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 4px; margin-bottom: 15px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
    .quote-box { font-style: italic; color: #4b4f56; border-left: 4px solid #adb9d3; padding-left: 12px; margin-bottom: 15px; }
    .price-tag { color: #2e7d32; font-size: 26px; font-weight: bold; margin-bottom: 10px; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 12px; font-size: 15px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business:</b> Blast Hive.<br><b>Location:</b> Swansea, Sketty.<br><b>Backup:</b> Indoor facility at Stouthall.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Newsletter Signup", placeholder="email@example.com", key="news_email")
    if st.button("Subscribe"): st.toast("Welcome to the Hive! 🐝")

    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Send us a message"):
        st.text_input("Name", key="msg_name")
        st.text_area("Message", key="msg_body")
        if st.button("Send"): st.success("Message Sent!")

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    # --- TAB 1: INFO & REVIEWS ---
    with tab1:
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        
        # FIXED: Add Review Section
        st.markdown('<div class="section-header">Customer Reviews</div>', unsafe_allow_html=True)
        with st.expander("⭐ Leave a Review"):
            r_name = st.text_input("Name", key="rev_n")
            r_stars = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_text = st.text_area("Your Review", key="rev_t")
            if st.button("Submit Review"):
                if r_name and r_text:
                    st.session_state.user_reviews.insert(0, {"name": r_name, "stars": r_stars, "text": r_text})
                    st.rerun()

        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">{r["stars"]} "{r["text"]}" - {r["name"]} (Latest)</div>', unsafe_allow_html=True)
        
        st.markdown("""
            <div class="quote-box">⭐⭐⭐⭐⭐ "The Target Day was the highlight of our summer. Highly recommend!" - Sarah J.</div>
            <div class="quote-box">⭐⭐⭐⭐⭐ "So glad they have the backup facility at Stouthall, the rain didn't stop us!" - Mark T.</div>
            <div class="quote-box">⭐⭐⭐⭐ "Great value for £54.99. All equipment was top tier." - Gareth P.</div>
        """, unsafe_allow_html=True)

    # --- TAB 2: POSTS WITH IMAGES ---
    with tab_posts:
        st.markdown('<div class="section-header">Community Feed</div>', unsafe_allow_html=True)
        
        posts = [
            ("New laser gear is ready for action! 🔫", "https://images.unsplash.com/photo-1599586120429-48281b6f0ece"),
            ("Cooking over the fire at our bushcraft session! 🌲", "https://images.unsplash.com/photo-1506332800446-0fb3df09358a"),
            ("Don't forget, if it rains we head to Stouthall! 🌧️", None),
            ("Check out the focus on the archery range today! 🏹", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b")
        ]
        
        for i, (text, img) in enumerate(posts):
            with st.container():
                st.markdown(f'<div class="post-card">{text}</div>', unsafe_allow_html=True)
                if img: st.image(img, use_container_width=True)
                c_l, c_r = st.columns([1, 4])
                if c_l.button(f"👍 {st.session_state.post_likes[i]}", key=f"pl_{i}"):
                    st.session_state.post_likes[i] += 1; st.rerun()
                if c_r.button("🔗 Share", key=f"ps_{i}"): st.success("📢 Shared to profile!")

    # --- TAB 3: BOOKING & RECEIPT ---
    with tab3:
        st.markdown('<div class="section-header">Book Your Day Out</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Select Event:", list(event_data.keys()))
            dt = st.selectbox("Select Date:", event_data[evt])
            st.markdown('<div class="price-tag">Total: £54.99</div>', unsafe_allow_html=True)
            if st.button("Confirm Booking"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "receipt_ask"; st.rerun()
        
        elif st.session_state.booking_step == "receipt_ask":
            st.warning("Booking confirmed! Would you like a receipt?")
            if st.button("Yes, send to *******@gmail.com"):
                st.success("📩 Receipt sent to *******@gmail.com!")
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"
            if st.button("No receipt, just finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    # --- TAB 4: MY BOOKINGS ---
    with tab4:
        st.markdown('<div class="section-header">My Active Schedule</div>', unsafe_allow_html=True)
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} <br>📅 {b["date"]} <br>🆔 {b["id"]}</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"can_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()

    # --- TAB 5: FAQ ---
    with tab5:
        st.markdown('<div class="section-header">Frequently Asked Questions</div>', unsafe_allow_html=True)
        st.markdown("""<div class="content-box">
            <span class="faq-q">What is the backup plan for bad weather?</span>
            <p>We move all activities to our dedicated <b>indoor facility at Stouthall</b>.</p>
            <span class="faq-q">Is all equipment provided?</span>
            <p>Yes! Every booking includes gear, insurance, and professional instruction.</p>
            <span class="faq-q">Can I cancel my booking?</span>
            <p>Yes, you can use the 'My Bookings' tab to manage or cancel your slots.</p>
            <span class="faq-q">What age is this for?</span>
            <p>Most events are designed for ages 12-17.</p>
        </div>""", unsafe_allow_html=True)
