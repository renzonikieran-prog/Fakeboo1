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
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(10, 500) for _ in range(50)]

# --- DATA MAPPING ---
event_data = {
    "Target Day": ["4th", "5th August"],
    "Adrenaline Weekend": ["12th", "13th August"],
    "Ultimate Challenge Day": ["6th", "11th August"],
    "Social Play Fest": ["9th August"],
    "Extreme Impact Day": ["17th August"],
    "Skill Switch Experience": ["14th August"]
}

# ALL Posters and Real Action Shots Restored
posters = [
    ("target_day.jpg", "Target Day Poster"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend Poster"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Poster"),
    ("social_play_fest.jpg", "Social Play Fest Poster"),
    ("extreme_impact.jpg", "Extreme Impact Poster"),
    ("skill_switch.jpg", "Skill Switch Poster"),
    ("https://images.unsplash.com/photo-1599586120429-48281b6f0ece", "Laser Tag Action"),
    ("https://images.unsplash.com/photo-1506332800446-0fb3df09358a", "Bushcraft Survival"),
    ("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b", "Archery Range"),
    ("https://images.unsplash.com/photo-1511949863663-92c5c06cc0bb", "Team Celebration"),
    ("https://images.unsplash.com/photo-1517164850305-99a3e65bb47e", "Puzzle Challenge"),
    ("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b", "Stouthall Estate View")
]

# --- UI STYLING ---
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .stat-bar { background-color: #f0f2f5; padding: 10px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 4px; margin-bottom: 15px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 15px; border-radius: 8px; margin-bottom: 5px; font-weight: bold; }
    .quote-box { font-style: italic; color: #4b4f56; border-left: 4px solid #adb9d3; padding-left: 12px; margin-bottom: 15px; }
    .price-tag { color: #2e7d32; font-size: 26px; font-weight: bold; }
    .motto { color: #adb9d3; font-weight: bold; font-size: 18px; text-align: center; display: block; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Head Office:</b> Swansea.<br><b>Activity Site:</b> Stouthall Country Mansion.<br><b>Wet Weather:</b> Indoor facility at Stouthall.</div>', unsafe_allow_html=True)
    
    # Newsletter Restored
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Enter Email for updates", key="news_email")
    if st.button("Subscribe"):
        st.toast("Welcome to the Hive! 🐝")

    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Message Us"):
        st.text_input("Name", key="side_n")
        if st.button("Send"): st.success("Sent!")

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    # --- TAB 1: INFO ---
    with tab1:
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company that offers exciting days out for the young people in our area. While our head office is located in Swansea, <b>all our activities take place on the stunning grounds of Stouthall</b>. We provide unforgettable experiences including bushcraft, team sports, and thrilling murder mystery days. We offer the fairest prices possible so that young people can have the most unforgettable days. We cannot wait to see you at our next event!<br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        with st.expander("⭐ Leave a Review"):
            r_name = st.text_input("Name")
            r_stars = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_text = st.text_area("Review")
            if st.button("Submit"):
                if r_name and r_text:
                    st.session_state.user_reviews.insert(0, {"name": r_name, "stars": r_stars, "text": r_text})
                    st.rerun()

        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">{r["stars"]} "{r["text"]}" - {r["name"]} (Latest)</div>', unsafe_allow_html=True)

    # --- TAB: POSTS (Significantly More Content) ---
    with tab_posts:
        st.markdown('<div class="section-header">Recent Community Updates</div>', unsafe_allow_html=True)
        posts_data = [
            ("The archery range at Stouthall is looking perfect this morning! 🏹", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b"),
            ("New laser gear has been delivered to our Swansea office and is heading to Stouthall today! 🔫", "https://images.unsplash.com/photo-1599586120429-48281b6f0ece"),
            ("Reminder: If the weather turns, we head straight to the indoor facility at Stouthall. 🌧️", None),
            ("Bushcraft skills in full swing. Fire making is an essential skill! 🔥", "https://images.unsplash.com/photo-1506332800446-0fb3df09358a"),
            ("Big shoutout to the group from last Saturday! Absolute legends. 🙌", None),
            ("The Stouthall mansion provides the perfect backdrop for our Murder Mystery days. 🕵️", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b"),
            ("Ready, Aim, BLAST! Who is joining us this weekend? 🐝", None)
        ]
        for i, (txt, img) in enumerate(posts_data):
            st.markdown(f'<div class="post-card">{txt}</div>', unsafe_allow_html=True)
            if img: st.image(img, width=450)
            col1, col2 = st.columns([1, 4])
            if col1.button(f"👍 {st.session_state.post_likes[i]}", key=f"feed_l_{i}"):
                st.session_state.post_likes[i] += 1; st.rerun()
            if col2.button("🔗 Share", key=f"feed_s_{i}"):
                st.success("📢 Post Shared!")

    # --- TAB 2: PHOTOS (All Posters & Action) ---
    with tab2:
        if st.session_state.photo_index is None:
            cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with cols[i % 3]:
                    st.image(img, use_container_width=True)
                    if st.button(f"View {title}", key=f"gal_v_{i}"):
                        st.session_state.photo_index = i; st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(posters[idx][0], width=550, caption=posters[idx][1])
            if st.button("❌ Close Gallery"): st.session_state.photo_index = None; st.rerun()

    # --- TAB 3: BOOKING ---
    with tab3:
        st.markdown('<div class="section-header">Book Your Stouthall Adventure</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Activity:", list(event_data.keys()))
            dt = st.selectbox("Date:", event_data[evt])
            st.markdown('<div class="price-tag">Total: £54.99</div>', unsafe_allow_html=True)
            if st.button("Confirm Details"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "receipt_confirm"; st.rerun()
        
        elif st.session_state.booking_step == "receipt_confirm":
            st.warning("Booking Saved! Do you require a receipt?")
            if st.button("Yes, Send to *******@gmail.com"):
                st.session_state.booking_step = "receipt_sent"; st.rerun()
            if st.button("No Receipt, Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

        elif st.session_state.booking_step == "receipt_sent":
            st.success("📩 Receipt sent to *******@gmail.com!")
            if st.button("Return to Booking"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    # --- TAB 4: MY BOOKINGS ---
    with tab4:
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]}</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"del_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()

    # --- TAB 5: FAQ ---
    with tab5:
        st.markdown('<div class="section-header">FAQ</div>', unsafe_allow_html=True)
        st.write("<b>Why is your office in Swansea but activities at Stouthall?</b><br>Our management team is based in the city, but Stouthall offers the perfect rural terrain for adventure!", unsafe_allow_html=True)
        st.write("<b>What happens in a downpour?</b><br>We move to our massive indoor facility at Stouthall.", unsafe_allow_html=True)
