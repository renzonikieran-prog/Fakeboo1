import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# 1. Memory Management (Session State)
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = []
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(20, 950) for _ in range(100)]

# 2. CORRECTED DATE MAPPING
event_data = {
    "Target Day": ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th August"],
    "Adrenaline Weekend": ["12th", "13th", "14th", "18th", "19th August"],
    "Ultimate Challenge Day": ["6th", "7th", "11th", "20th August"],
    "Social Play Fest": ["9th", "10th", "15th", "16th August"],
    "Extreme Impact Day": ["4th", "5th", "17th", "22nd August"],
    "Skill Switch Experience": ["8th", "14th", "21st", "23rd August"]
}

# 3. VERIFIED GALLERY DATA (Accurate Image Mapping)
posters = [
    ("target_day.jpg", "Target Day Poster"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend Poster"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Poster"),
    ("social_play_fest.jpg", "Social Play Fest Poster"),
    ("extreme_impact.jpg", "Extreme Impact Poster"),
    ("skill_switch.jpg", "Skill Switch Poster"),
    ("https://images.unsplash.com/photo-1511191988486-3d24285e61f4?w=800", "Archery Target & Bow"),
    ("https://images.unsplash.com/photo-1526491109672-74740652b963?w=800", "Survival Campfire"),
    ("https://images.unsplash.com/photo-1599586120429-48281b6f0ece?w=800", "Tactical Laser Gear"),
    ("https://images.unsplash.com/photo-1511949863663-92c5c06cc0bb?w=800", "Outdoor Victory Celebration"),
    ("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800", "Stouthall Mansion Grounds"),
    ("https://images.unsplash.com/photo-1517164850305-99a3e65bb47e?w=800", "Team Logic Challenge")
]

# 4. UI STYLING
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .stat-bar { background-color: #f0f2f5; padding: 10px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 4px; margin-bottom: 15px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 15px; border-radius: 8px; margin-bottom: 5px; font-weight: bold; }
    .motto { color: #adb9d3; font-weight: bold; font-size: 22px; text-align: center; display: block; margin-top: 20px; letter-spacing: 3px; }
    .price-tag { color: #2e7d32; font-size: 26px; font-weight: bold; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# 5. HEADER
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business HQ:</b> Swansea.<br><b>Activity Site:</b> Stouthall Country Mansion.<br><b>Wet Weather:</b> Indoor arena at Stouthall.</div>', unsafe_allow_html=True)
    
    # Newsletter Box
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Newsletter Signup", placeholder="email@example.com", key="sidebar_nl")
    if st.button("Subscribe"): st.toast("Welcome to the Hive! 🐝")

    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Message Us"):
        st.text_input("Your Name", key="side_msg_n")
        if st.button("Send"): st.success("Sent!")

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    # --- TAB 1: INFO ---
    with tab1:
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company offering exciting days out for young people. While we are based in Swansea, <b>all activities take place at the Stouthall Country Mansion</b>. We provide unforgettable experiences including bushcraft, team sports, and murder mystery days full of brain-boggling puzzles. We offer fair prices so young people can have unforgettable days. We cannot wait to see you at our next event!<br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        with st.expander("⭐ Leave a Review"):
            r_n = st.text_input("Name")
            r_s = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_t = st.text_area("How was your experience?")
            if st.button("Post Review"):
                if r_n and r_t:
                    st.session_state.user_reviews.insert(0, {"name": r_n, "stars": r_s, "text": r_t})
                    st.rerun()

        st.markdown('<div class="section-header">Community Feedback</div>', unsafe_allow_html=True)
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">{r["stars"]} "{r["text"]}" - {r["name"]} (Latest)</div>', unsafe_allow_html=True)
        st.markdown('<div class="quote-box">⭐⭐⭐⭐⭐ "The Target Day at Stouthall was fantastic. Professional staff and great gear." - Sarah J.</div>', unsafe_allow_html=True)

    # --- TAB 2: POSTS (35 POSTS WITH ACCURATE IMAGES) ---
    with tab_posts:
        st.markdown('<div class="section-header">Stouthall Activity Feed</div>', unsafe_allow_html=True)
        
        # Defining 35 posts with varied images and text
        posts_content = [
            ("Archery range set up at Stouthall! Who is going for the bulls-eye today? 🏹", "https://images.unsplash.com/photo-1511191988486-3d24285e61f4?w=600"),
            ("Survival mastery: Learning the ancient art of fire lighting at Stouthall. 🔥", "https://images.unsplash.com/photo-1526491109672-74740652b963?w=600"),
            ("Our high-spec laser tags are sanitized and ready for the weekend. 🔫", "https://images.unsplash.com/photo-1599586120429-48281b6f0ece?w=600"),
            ("Victory celebration! Everyone crushed the Adrenaline Challenge. 🙌", "https://images.unsplash.com/photo-1511949863663-92c5c06cc0bb?w=600"),
            ("Logic puzzles in full swing under the Stouthall mansion trees. 🧠", "https://images.unsplash.com/photo-1517164850305-99a3e65bb47e?w=600"),
            ("The Mansion grounds provide the best terrain for team games. 🏴󠁧󠁢󠁷󠁬󠁳󠁿", "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600"),
            ("Reminder: Rainy forecast? We move to the Stouthall Indoor Arena! 🌧️", None),
            ("Check out this bulls-eye grouping! Pure focus. 🎯", "https://images.unsplash.com/photo-1511191988486-3d24285e61f4?w=600"),
            ("Bushcraft skills: Building shelters that actually stay dry. 🏕️", "https://images.unsplash.com/photo-1526491109672-74740652b963?w=600"),
            ("Clean gear is happy gear. Sanitizing units for tomorrow. 🧼", None),
            ("Ready, Aim, BLAST! See you all for Friday Fest. 🐝", None)
        ]
        filler_posts = ["Special discounts for groups of 10+!", "New puzzles added to Skill Switch.", "Staff training day complete!", "Sunset over the Stouthall estate."]
        for i in range(len(posts_content), 35):
            posts_content.append((random.choice(filler_posts), None))

        for i, (txt, img) in enumerate(posts_content):
            st.markdown(f'<div class="post-card">{txt}</div>', unsafe_allow_html=True)
            if img: st.image(img, width=420)
            c1, c2 = st.columns([1, 4])
            if c1.button(f"👍 {st.session_state.post_likes[i]}", key=f"feed_pl_{i}"):
                st.session_state.post_likes[i] += 1; st.rerun()
            if c2.button("🔗 Share", key=f"feed_ps_{i}"): st.success("📢 Post Shared!")

    # --- TAB 3: PHOTOS (Gallery Nav Fixed) ---
    with tab2:
        if st.session_state.photo_index is None:
            cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with cols[i % 3]:
                    st.image(img, use_container_width=True)
                    if st.button(f"View {title}", key=f"v_gal_{i}"):
                        st.session_state.photo_index = i; st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(posters[idx][0], width=550, caption=posters[idx][1])
            c1, c2, c3 = st.columns(3)
            if c1.button("⬅ Previous"): st.session_state.photo_index = (idx-1)%len(posters); st.rerun()
            if c2.button("Next ➡"): st.session_state.photo_index = (idx+1)%len(posters); st.rerun()
            if c3.button("❌ Close Gallery"): st.session_state.photo_index = None; st.rerun()

    # --- TAB 4: BOOKING & RECEIPT ---
    with tab3:
        st.markdown('<div class="section-header">Book Your Adventure - £54.99</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            evt = st.selectbox("Choose Event:", list(event_data.keys()))
            dt = st.selectbox("Choose Date:", event_data[evt])
            if st.button("Confirm Details"):
                st.session_state.temp_booking = {"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"}
                st.session_state.booking_step = "receipt_confirm"; st.rerun()
        
        elif st.session_state.booking_step == "receipt_confirm":
            st.warning("Booking Saved! Do you require a receipt?")
            if st.button("Yes, Send to *******@gmail.com"): st.session_state.booking_step = "receipt_sent"; st.rerun()
            if st.button("No Receipt, Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

        elif st.session_state.booking_step == "receipt_sent":
            st.success("📩 Receipt sent to *******@gmail.com!")
            if st.button("Return to Booking"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    # --- TAB 5: MY BOOKINGS ---
    with tab4:
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]}</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"cb_del_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()

    # --- TAB 6: FAQ ---
    with tab5:
        st.markdown('<div class="section-header">FAQ</div>', unsafe_allow_html=True)
        faqs = [
            ("Where is the site?", "Head office Swansea, but ALL events are held at Stouthall Mansion."),
            ("What if it rains?", "We move to the indoor arena at Stouthall."),
            ("What is the cost?", "£54.99 per person for all activities."),
            ("Are staff qualified?", "Yes, all staff are Enhanced DBS checked and First Aid trained.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
