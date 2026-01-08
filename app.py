import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# Memory Management for GlizzyGPT 2.0 Features
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = []
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(5, 250) for _ in range(20)]
if "photo_likes" not in st.session_state:
    st.session_state.photo_likes = [random.randint(50, 400) for _ in range(12)]

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
    ("target_day.jpg", "Target Day Poster"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend Poster"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Day Poster"),
    ("social_play_fest.jpg", "Social Play Fest Poster"),
    ("extreme_impact.jpg", "Extreme Impact Day Poster"),
    ("skill_switch.jpg", "Skill Switch Experience Poster"),
    ("https://images.unsplash.com/photo-1506332800446-0fb3df09358a", "Bushcraft Skills Action"),
    ("https://images.unsplash.com/photo-1599586120429-48281b6f0ece", "Laser Tag Teamwork"),
    ("https://images.unsplash.com/photo-1551632811-561732d1e306", "Forest Survival Training"),
    ("https://images.unsplash.com/photo-1517164850305-99a3e65bb47e", "Team Puzzle Challenge"),
    ("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b", "Archery Practice"),
    ("https://images.unsplash.com/photo-1511949863663-92c5c06cc0bb", "Victory Celebration")
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
    
    # Newsletter
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Email:", placeholder="your@email.com")
    if st.button("Subscribe"):
        st.toast("Welcome to the Hive! 🐝")

    # Contact Form
    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Message Us"):
        c_name = st.text_input("Name", key="c_name")
        if st.button("Send Message"):
            st.success(f"Sent! Thanks {c_name}.")

    # Likes Section
    st.markdown('<div class="section-header">Likes</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box">👍 Adventure Wales<br>👍 Gower Activity Centres<br>👍 Swansea Youth Hub</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    # --- TAB 1: INFO ---
    with tab1:
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        
        # Add Review Logic
        with st.expander("⭐ Add a Review"):
            r_name = st.text_input("Your Name")
            r_stars = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_text = st.text_area("Your Review")
            if st.button("Post Review"):
                if r_name and r_text:
                    st.session_state.user_reviews.insert(0, {"name": r_name, "stars": r_stars, "text": r_text})
                    st.rerun()

        st.markdown('<div class="section-header">About Us</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company offering exciting days out in Swansea...</div>', unsafe_allow_html=True)
        
        # Quotes and Reviews Feed
        st.markdown('<div class="section-header">Reviews & Quotes</div>', unsafe_allow_html=True)
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">{r["stars"]} "{r["text"]}" - {r["name"]} (Latest)</div>', unsafe_allow_html=True)
        st.markdown('<div class="quote-box">⭐⭐⭐⭐⭐ "Best summer activity company in Swansea!" - Parent Review</div>', unsafe_allow_html=True)

    # --- TAB: POSTS (20 Posts) ---
    with tab_posts:
        st.markdown('<div class="section-header">Recent Updates</div>', unsafe_allow_html=True)
        feed = ["Target Day gear is here! 🔫", "Sketty indoor ready! 🌧️", "New puzzles today! 🧩", "Teamwork wins! 🙌", "Sept Bushcraft! 🌲", "Free hoodies for groups! 👕", "Check the video! 📹", "Extreme Impact full! 🏃", "Lost bottle found! 🍼", "Ready, Aim, BLAST! 🐝", "Archery open! 🏹", "Prep for Challenge! 🛠️", "Starts at 10 AM! 🕙", "Sketty mural done! 🎨", "Action shots! 📸", "Welcome Gethin! 👋", "Crack the Case! 🕵️", "Thanks Bishop Gore! 🏫", "Winter Adrenaline! ❄️", "Swansea Memories! 🏴󠁧󠁢󠁷󠁬󠁳󠁿"]
        for i, text in enumerate(feed):
            st.markdown(f'<div class="post-card">{text}</div>', unsafe_allow_html=True)
            l_col, s_col = st.columns([1, 4])
            if l_col.button(f"👍 {st.session_state.post_likes[i]}", key=f"post_l_{i}"):
                st.session_state.post_likes[i] += 1
                st.rerun()
            if s_col.button(f"🔗 Share", key=f"post_s_{i}"):
                st.success("📢 Post Shared successfully!")

    # --- TAB 2: PHOTOS (Scaled) ---
    with tab2:
        if st.session_state.photo_index is None:
            g_cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with g_cols[i % 3]:
                    st.image(img, use_container_width=True)
                    if st.button(f"View {title}", key=f"view_{i}"):
                        st.session_state.photo_index = i
                        st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(posters[idx][0], use_container_width=True)
            if st.button(f"❤️ {st.session_state.photo_likes[idx]} Likes"):
                st.session_state.photo_likes[idx] += 1
                st.rerun()
            if st.button("❌ Close Gallery"):
                st.session_state.photo_index = None
                st.rerun()

    # --- TAB 3: BOOK NOW (£54.99) ---
    with tab3:
        st.markdown('<div class="section-header">Booking - £54.99</div>', unsafe_allow_html=True)
        evt = st.selectbox("Activity:", list(event_data.keys()))
        dt = st.selectbox("Date:", event_data[evt])
        if st.button("Confirm Booking"):
            st.session_state.my_bookings.append({"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"})
            st.info("📩 Receipt sent to ***********@gmail.com")
            st.rerun()

    # --- TAB 4: MY BOOKINGS ---
    with tab4:
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]} (ID: {b["id"]})</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"can_{i}"):
                st.session_state.my_bookings.pop(i)
                st.rerun()

    # --- TAB 5: FAQ (More content) ---
    with tab5:
        st.markdown('<div class="section-header">Frequently Asked Questions</div>', unsafe_allow_html=True)
        faqs = [("Gear included?", "Yes, in the £54.99 price."), ("Rain?", "We move to Sketty indoor facilities."), ("Age?", "12-17 usually."), ("Discounts?", "Groups of 10+."), ("Safe?", "DBS checked staff."), ("Food?", "Bring a packed lunch.")]
        for q, a in faqs:
            st.markdown(f'<p class="faq-q">{q}</p><p>{a}</p>', unsafe_allow_html=True)
