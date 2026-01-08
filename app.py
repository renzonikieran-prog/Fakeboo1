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
    st.session_state.post_likes = [random.randint(20, 600) for _ in range(60)]

# --- DATA MAPPING ---
event_data = {
    "Target Day": ["4th", "5th August"],
    "Adrenaline Weekend": ["12th", "13th August"],
    "Ultimate Challenge Day": ["6th", "11th August"],
    "Social Play Fest": ["9th August"],
    "Extreme Impact Day": ["17th August"],
    "Skill Switch Experience": ["14th August"]
}

# Expanded Photos (Posters + Real Action)
posters = [
    ("target_day.jpg", "Target Day Poster"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend Poster"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Poster"),
    ("social_play_fest.jpg", "Social Play Fest Poster"),
    ("extreme_impact.jpg", "Extreme Impact Poster"),
    ("skill_switch.jpg", "Skill Switch Poster"),
    ("https://images.unsplash.com/photo-1599586120429-48281b6f0ece", "Laser Tag Strategy"),
    ("https://images.unsplash.com/photo-1506332800446-0fb3df09358a", "Bushcraft Fire Skills"),
    ("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b", "Archery Focus"),
    ("https://images.unsplash.com/photo-1511949863663-92c5c06cc0bb", "End of Day Celebration"),
    ("https://images.unsplash.com/photo-1517164850305-99a3e65bb47e", "Logic Puzzle Teamwork"),
    ("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b", "Stouthall Estate Grounds"),
    ("https://images.unsplash.com/photo-1516627145497-ae6968895b74", "Obstacle Course"),
    ("https://images.unsplash.com/photo-1533227268408-a7647dd0d936", "Outdoor Leadership")
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
    .motto { color: #adb9d3; font-weight: bold; font-size: 20px; text-align: center; display: block; margin-top: 15px; text-transform: uppercase; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 12px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Head Office:</b> Swansea.<br><b>Main Activity Site:</b> Stouthall Country Mansion.<br><b>Wet Weather:</b> Indoor facility at Stouthall.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Enter Email", key="news_email", placeholder="updates@gmail.com")
    if st.button("Subscribe"):
        st.toast("Welcome to the Hive! 🐝")

    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Message Us"):
        st.text_input("Your Name", key="side_n")
        if st.button("Send Message"): st.success("Sent! We'll reply soon.")

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    # --- TAB 1: INFO & AUTO-REVIEWS ---
    with tab1:
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company offering exciting days out for young people. Based in Swansea, <b>all activities take place at the historic Stouthall Country Mansion</b>. We provide unforgettable experiences including bushcraft, team sports, and thrilling murder mystery days. We offer the fairest prices so young people can have the most unforgettable days. We cannot wait to see you at our next event!<br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        with st.expander("⭐ Post a Review"):
            r_name = st.text_input("Name")
            r_stars = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_text = st.text_area("Review Content")
            if st.button("Post"):
                if r_name and r_text:
                    st.session_state.user_reviews.insert(0, {"name": r_name, "stars": r_stars, "text": r_text})
                    st.rerun()

        st.markdown('<div class="section-header">Recent Customer Feedback</div>', unsafe_allow_html=True)
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">{r["stars"]} "{r["text"]}" - {r["name"]} (Latest)</div>', unsafe_allow_html=True)
        # Base Generated Reviews
        st.markdown("""
            <div class="quote-box">⭐⭐⭐⭐⭐ "The Target Day at Stouthall was fantastic. The instructors really know their stuff." - Local Parent</div>
            <div class="quote-box">⭐⭐⭐⭐⭐ "My group loved the Skill Switch day. The puzzles were genuinely hard!" - Youth Leader</div>
            <div class="quote-box">⭐⭐⭐⭐ "Great value for money. Safety was clearly the top priority." - Swansea School Trip</div>
        """, unsafe_allow_html=True)

    # --- TAB: POSTS (More content + Better scaling) ---
    with tab_posts:
        posts_data = [
            ("The view from the Stouthall manor house this morning. Archery starts in 10 mins! 🏹", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b"),
            ("New gear has arrived! These laser tags are high-spec and ready for Adrenaline Weekend. 🔫", "https://images.unsplash.com/photo-1599586120429-48281b6f0ece"),
            ("Bushcraft mastery: Watching the team light their first fire at Stouthall. 🔥", "https://images.unsplash.com/photo-1506332800446-0fb3df09358a"),
            ("Cloudy day? No problem. The Stouthall indoor arena is ready. 🌧️", None),
            ("Team celebration after a logic puzzle victory! 🧩", "https://images.unsplash.com/photo-1511949863663-92c5c06cc0bb"),
            ("Who's ready for next week's Target Day? Slots are 95% full. 🐝", None)
        ]
        for i, (txt, img) in enumerate(posts_data):
            st.markdown(f'<div class="post-card">{txt}</div>', unsafe_allow_html=True)
            if img: st.image(img, width=450)
            col1, col2 = st.columns([1, 4])
            if col1.button(f"👍 {st.session_state.post_likes[i]}", key=f"f_l_{i}"):
                st.session_state.post_likes[i] += 1; st.rerun()
            if col2.button("🔗 Share", key=f"f_s_{i}"): st.success("📢 Post Shared!")

    # --- TAB 2: PHOTOS (Scroll/Nav Fixed) ---
    with tab2:
        if st.session_state.photo_index is None:
            cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with cols[i % 3]:
                    st.image(img, use_container_width=True)
                    if st.button(f"View {title}", key=f"v_g_{i}"):
                        st.session_state.photo_index = i; st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(posters[idx][0], width=550, caption=posters[idx][1])
            c1, c2, c3 = st.columns(3)
            if c1.button("⬅ Previous"): st.session_state.photo_index = (idx-1)%len(posters); st.rerun()
            if c2.button("Next ➡"): st.session_state.photo_index = (idx+1)%len(posters); st.rerun()
            if c3.button("❌ Close"): st.session_state.photo_index = None; st.rerun()

    # --- TAB 3: BOOKING ---
    with tab3:
        st.markdown('<div class="section-header">Book Your Adventure - £54.99</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Event:", list(event_data.keys()))
            dt = st.selectbox("Date:", event_data[evt])
            if st.button("Book Now"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "receipt_confirm"; st.rerun()
        
        elif st.session_state.booking_step == "receipt_confirm":
            st.warning("Booking Confirmed! Send receipt to *******@gmail.com?")
            if st.button("Yes, Send Receipt"): st.session_state.booking_step = "receipt_sent"; st.rerun()
            if st.button("No Receipt, Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

        elif st.session_state.booking_step == "receipt_sent":
            st.success("📩 Receipt sent to *******@gmail.com!")
            if st.button("Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    # --- TAB 4: MY BOOKINGS ---
    with tab4:
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]}</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"c_b_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()

    # --- TAB 5: FAQ (Significantly expanded) ---
    with tab5:
        st.markdown('<div class="section-header">Detailed FAQ</div>', unsafe_allow_html=True)
        faqs = [
            ("Where exactly are the activities?", "Head office is Swansea, but every activity is at the Stouthall Country Mansion estate."),
            ("What is the rain policy?", "We don't cancel! We move to our large indoor facility at Stouthall."),
            ("Is lunch included?", "Water and fruit are provided, but please bring a packed lunch."),
            ("What should I wear?", "Sturdy footwear (boots/trainers) and comfortable clothes you don't mind getting dirty."),
            ("Is there an age limit?", "We specialize in ages 12-17."),
            ("Are staff qualified?", "Yes, all staff are DBS checked and First Aid trained.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
