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
    st.session_state.user_reviews = []
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(45, 950) for _ in range(100)]

# 2. DATE MAPPING
event_data = {
    "Target Day": ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th August"],
    "Adrenaline Weekend": ["12th", "13th", "14th", "18th", "19th August"],
    "Ultimate Challenge Day": ["6th", "7th", "11th", "20th August"],
    "Social Play Fest": ["9th", "10th", "15th", "16th August"],
    "Extreme Impact Day": ["4th", "5th", "17th", "22nd August"],
    "Skill Switch Experience": ["8th", "14th", "21st", "23rd August"]
}

# 3. GALLERY DATA (Posters .jpg | Activity Images .png)
posters = [
    ("target_day.jpg", "Target Day Poster"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend Poster"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Poster"),
    ("social_play_fest.jpg", "Social Play Fest Poster"),
    ("extreme_impact.jpg", "Extreme Impact Poster"),
    ("skill_switch.jpg", "Skill Switch Poster"),
    ("Gemini_Generated_Image_wdo2rzwdo2rzwdo2.png", "Archery Field Setup"),
    ("Gemini_Generated_Image_of95w8of95w8of95.png", "Outdoor Archery Action"),
    ("Gemini_Generated_Image_4nwpmx4nwpmx4nwp.png", "Indoor Archery Arena"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.png", "Survival Campfire"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.png", "Tactical Laser Gear"),
    ("Gemini_Generated_Image_q74buoq74buoq74b.png", "Outdoor Laser Tag Action"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.png", "Indoor Neon Arena"),
    ("Gemini_Generated_Image_hunw61hunw61hunw.png", "Outdoor Victory Celebration"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.png", "Stouthall Mansion Site"),
    ("Gemini_Generated_Image_xz9er1xz9er1xz9e.png", "Indoor Team Logic Challenge"),
    ("Gemini_Generated_Image_vv49c1vv49c1vv49.png", "Indoor Cooperative Games"),
    ("Gemini_Generated_Image_olevawolevawolev.png", "Outdoor Physical Puzzles"),
    ("Gemini_Generated_Image_cueiazcueiazcuei.png", "Outdoor Team Competition")
]

# 4. UI STYLING
st.markdown("""
    <style>
    .fb-logo { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; font-size: 28px; letter-spacing: -1px; }
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .stat-bar { background-color: #f0f2f5; padding: 10px; display: flex; justify-content: space-around; border: 1px solid #dddfe2; border-radius: 4px; margin-bottom: 15px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); font-weight: bold; }
    .motto { color: #adb9d3; font-weight: bold; font-size: 22px; text-align: center; display: block; margin-top: 20px; letter-spacing: 3px; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; display: block; }
    </style>
    """, unsafe_allow_html=True)

# 5. HEADER
st.markdown('<div class="nav-bar"><span class="fb-logo">fakebook</span><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    # UPDATED LOGO
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business Hub:</b> Swansea.<br><b>Activity Site:</b> Stouthall Country Mansion.<br><b>Standard Rate:</b> £54.99 per person.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Newsletter Signup", placeholder="email@example.com", key="side_nl")
    if st.button("Subscribe"): st.toast("Welcome to the Hive! 🐝")

    st.markdown('<div class="section-header">Contact Our Team</div>', unsafe_allow_html=True)
    with st.expander("Message Us"):
        st.text_input("Your Name", key="side_msg_n")
        if st.button("Send"): st.success("Message Sent!")

    st.markdown('<div class="section-header">Followers You Know</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box" style="font-size: 11px; color: #606770;">👥 <b>Gareth Evans</b> and 42 others like this.</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1: # INFO
        st.markdown('<div class="stat-bar"><div class="stat-item"><b>1.4k</b> Followers</div><div class="stat-item"><b>920</b> Reviews</div><div class="stat-item"><b>4.9 ⭐</b> Rating</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company offering exciting days out for young people at Stouthall Mansion. <br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        with st.expander("⭐ Leave a Review"):
            r_n = st.text_input("Name")
            r_s = st.select_slider("Rating", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"], value="⭐⭐⭐⭐⭐")
            r_t = st.text_area("How was your experience?")
            if st.button("Post Review"):
                if r_n and r_t:
                    st.session_state.user_reviews.insert(0, {"name": r_n, "stars": r_s, "text": r_t})
                    st.rerun()
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="content-box">{r["stars"]} "{r["text"]}" - {r["name"]}</div>', unsafe_allow_html=True)

    with tab_posts: # 55 UNIQUE POSTS
        st.markdown('<div class="section-header">Recent Activity</div>', unsafe_allow_html=True)
        captions = [
            "The range is ready at Stouthall! 🏹", "Mastering fire lighting skills. 🔥", 
            "Tactical gear checked and ready. 🔫", "Victory celebration! 🙌",
            "Indoor arena looking great today. 🌈", "Team strategy in action. 🧠"
        ]
        for i in range(55):
            st.markdown('<div class="post-card">', unsafe_allow_html=True)
            cap = captions[i % len(captions)]
            st.write(cap)
            if i < len(posters) and os.path.exists(posters[i][0]):
                st.image(posters[i][0], width=450)
            c1, c2 = st.columns([1, 4])
            if c1.button(f"👍 {st.session_state.post_likes[i]}", key=f"feed_pl_{i}"):
                st.session_state.post_likes[i] += 1
                st.rerun()
            if c2.button("🔗 Share", key=f"feed_ps_{i}"): st.success("📢 Post Shared!")
            st.markdown('</div>', unsafe_allow_html=True)

    with tab2: # PHOTOS
        if st.session_state.photo_index is None:
            cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                        if st.button(f"View {title}", key=f"gal_v_{i}"):
                            st.session_state.photo_index = i
                            st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(posters[idx][0], use_container_width=True, caption=posters[idx][1])
            if st.button("❌ Close Gallery"):
                st.session_state.photo_index = None
                st.rerun()

    with tab3: # BOOKING
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
            if col1.button("Yes, Send Receipt"): st.session_state.booking_step = "receipt_sent"; st.rerun()
            if col2.button("No, Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()
        elif st.session_state.booking_step == "receipt_sent":
            st.success("📩 Receipt sent to *******@gmail.com!")
            if st.button("Finish"):
                st.session_state.my_bookings.append(st.session_state.temp_booking)
                st.session_state.booking_step = "select"; st.rerun()

    with tab4: # MY BOOKINGS
        for i, b in enumerate(st.session_state.my_bookings):
            st.markdown(f'<div class="content-box">🎯 {b["event"]} - {b["date"]}</div>', unsafe_allow_html=True)
            if st.button(f"Cancel {b['id']}", key=f"del_b_{i}"):
                st.session_state.my_bookings.pop(i); st.rerun()

    with tab5: # FAQ
        faqs = [
            ("Where is the site?", "All events are held at Stouthall Mansion."),
            ("What if it rains?", "We use our indoor arena at Stouthall."),
            ("What is the cost?", "£54.99 per person.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
