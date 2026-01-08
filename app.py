import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# Memory Management
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
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 20px; border-radius: 8px; margin-bottom: 10px; border-bottom: none; border-bottom-left-radius: 0; border-bottom-right-radius: 0;}
    .post-actions { border: 1px solid #dddfe2; background-color: #f9f9f9; padding: 10px; border-radius: 8px; border-top: none; border-top-left-radius: 0; border-top-right-radius: 0; margin-bottom: 20px; display: flex; gap: 10px; }
    .quote-box { font-style: italic; color: #4b4f56; border-left: 4px solid #adb9d3; padding-left: 12px; margin-bottom: 15px; }
    .price-tag { color: #2e7d32; font-size: 24px; font-weight: bold; margin: 10px 0; }
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
    
    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Send Message"):
        c_name = st.text_input("Name")
        if st.button("Submit"): st.success(f"Sent! Thanks {c_name}.")

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    # --- TAB 1: INFO ---
    with tab1:
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b><br>Followers</div><div class="stat-item"><b>920</b><br>Reviews</div><div class="stat-item"><b>4.9 ⭐</b><br>Rating</div></div>', unsafe_allow_html=True)
        with st.expander("⭐ Add a Review"):
            rev_name = st.text_input("Your Name")
            rev_text = st.text_area("Your Review")
            if st.button("Post Review"):
                st.session_state.user_reviews.insert(0, {"name": rev_name, "text": rev_text})
                st.rerun()
        st.markdown('<div class="section-header">About Us</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company offering exciting days out in Swansea...</div>', unsafe_allow_html=True)
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">"{r["text"]}" - {r["name"]} (Latest)</div>', unsafe_allow_html=True)

    # --- TAB: POSTS (With Share Pop-up) ---
    with tab_posts:
        st.markdown('<div class="section-header">Recent Updates</div>', unsafe_allow_html=True)
        
        feed_posts = [
            ("The Target Day equipment has just arrived! Who's ready for some Airsoft? 🔫", 0),
            ("Check out this view from our Sketty indoor facility. Rain can't stop the fun! 🌧️", 1),
            ("New 'Skill Switch' puzzles are being tested. They are brain-bogglers! 🧩", 2)
        ]

        for text, p_idx in feed_posts:
            st.markdown(f'<div class="post-card">{text}</div>', unsafe_allow_html=True)
            
            col_act1, col_act2 = st.columns([1, 4])
            with col_act1:
                if st.button(f"👍 {st.session_state.post_likes[p_idx]} Likes", key=f"post_like_{p_idx}"):
                    st.session_state.post_likes[p_idx] += 1
                    st.rerun()
            with col_act2:
                if st.button(f"🔗 Share", key=f"share_{p_idx}"):
                    st.toast("Link copied to clipboard!")
                    st.success("📢 Post Shared successfully to your profile!")

    # --- TAB 2: PHOTOS ---
    with tab2:
        if st.session_state.photo_index is None:
            st.markdown('<div class="section-header">Event Gallery</div>', unsafe_allow_html=True)
            g_cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with g_cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                        if st.button(f"View {title}", key=f"gal_{i}"):
                            st.session_state.photo_index = i
                            st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(posters[idx][0], use_container_width=True)
            if st.button(f"❤️ {st.session_state.photo_likes[idx]} Likes", key=f"photo_like_{idx}"):
                st.session_state.photo_likes[idx] += 1
                st.rerun()
            
            c1, c2, c3 = st.columns(3)
            if c1.button("⬅ Prev"): st.session_state.photo_index = (idx-1)%len(posters); st.rerun()
            if c2.button("Next ➡"): st.session_state.photo_index = (idx+1)%len(posters); st.rerun()
            if c3.button("❌ Close", type="primary"): st.session_state.photo_index = None; st.rerun()

    # --- TAB 3: BOOK NOW ---
    with tab3:
        st.markdown('<div class="section-header">Make a Booking</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Select Activity:", list(event_data.keys()))
            dt = st.selectbox("Choose Date:", event_data[evt])
            st.markdown(f'<div class="price-tag">Price: £54.99 per person</div>', unsafe_allow_html=True)
            if st.button("Confirm Booking"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}", "price": "£54.99"}
                st.session_state.booking_step = "confirm"; st.rerun()
        elif st.session_state.booking_step == "confirm":
            st.success(f"Booking Registered: {st.session_state.temp_booking['event']}")
            if st.button("Yes, Send Receipt"): st.session_state.booking_step = "receipt"; st.rerun()
        elif st.session_state.booking_step == "receipt":
            st.info("📩 Receipt sent to ***********@gmail.com")
            if st.button("Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    # --- TAB 4: MY BOOKINGS ---
    with tab4:
        st.markdown('<div class="section-header">Active Bookings</div>', unsafe_allow_html=True)
        if not st.session_state.my_bookings: st.info("No bookings found.")
        else:
            for i, b in enumerate(st.session_state.my_bookings):
                st.markdown(f'<div class="content-box">🎯 <b>{b["event"]}</b><br>📅 Date: {b["date"]}<br>🆔 ID: {b["id"]}</div>', unsafe_allow_html=True)
                if st.button(f"Cancel {b['id']}", key=f"del_{i}"):
                    st.session_state.my_bookings.pop(i); st.rerun()

    # --- TAB 5: FAQ ---
    with tab5:
        st.markdown('<div class="section-header">FAQ</div>', unsafe_allow_html=True)
        st.markdown("""<div class="content-box"><b>Is equipment provided?</b><br>Yes! Gear and insurance are included in the £54.99 price.</div>""", unsafe_allow_html=True)
