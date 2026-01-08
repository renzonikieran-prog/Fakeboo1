import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Fakebook")

# 1. Memory Management (Session State) - FIXED ATTRIBUTE ERROR
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = [
        {"name": "Liam W.", "stars": "⭐⭐⭐⭐⭐", "text": "Best laser tag experience in Wales! Professional staff and amazing gear."},
        {"name": "Chloe M.", "stars": "⭐⭐⭐⭐", "text": "Really enjoyed the bushcraft, great for team building."},
        {"name": "Dan R.", "stars": "⭐⭐⭐⭐⭐", "text": "The puzzles at Stouthall were brain-melters. Loved the challenge!"},
        {"name": "Sian T.", "stars": "⭐⭐⭐⭐⭐", "text": "Stouthall Mansion is the perfect backdrop for these activities."}
    ]
# Ensure post_likes is a dictionary and initialized
if "post_likes" not in st.session_state:
    st.session_state.post_likes = {i: random.randint(45, 1200) for i in range(60)}

# 2. DATA MAPPING (Posters .jpg | Activities .png)
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
    ("Gemini_Generated_Image_cueiazcueiazcuei.png", "Outdoor Team Challenge")
]

# 3. UI STYLING
st.markdown("""
    <style>
    .fb-logo { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; font-size: 28px; letter-spacing: -1px; }
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); }
    .motto { color: #adb9d3; font-weight: bold; font-size: 22px; text-align: center; display: block; margin-top: 20px; letter-spacing: 3px; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; display: block; }
    .quote-box { border-left: 5px solid #adb9d3; background-color: #f9f9f9; padding: 10px; margin-bottom: 10px; font-style: italic; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# 4. HEADER
st.markdown('<div class="nav-bar"><span class="fb-logo">fakebook</span><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Hub:</b> Swansea.<br><b>Site:</b> Stouthall Country Mansion.<br><b>Weather:</b> All-weather indoor arena available.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Followers You Know</div>', unsafe_allow_html=True)
    f_col1, f_col2 = st.columns([1, 4])
    with f_col1:
        if os.path.exists("image_83c146.jpg"): st.image("image_83c146.jpg", width=40)
    with f_col2:
        st.markdown('<div style="font-size: 11px; color: #606770;"><b>Gareth Evans</b> and 42 others like this.</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    # --- TAB 1: ABOUT & REVIEWS ---
    with tab1:
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">Blast Hive is South Wales\' premier adventure company. Based at the historic <b>Stouthall Country Mansion</b>, we provide high-intensity activity days including <b>Survival Skills, Tactical Laser Tag, Archery, and Elite Team Challenges</b>. <br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">Community Reviews</div>', unsafe_allow_html=True)
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">{r["stars"]} "{r["text"]}" - {r["name"]}</div>', unsafe_allow_html=True)

    # --- TAB 2: 55+ SEPARATED POSTS ---
    with tab_posts:
        for i in range(55):
            st.markdown('<div class="post-card">', unsafe_allow_html=True)
            txt = "Join us at Stouthall Mansion for an action-packed session! Book your August slot today."
            img = None
            if i < len(posters):
                img, txt = posters[i][0], posters[i][1]
            
            st.write(txt)
            if img and os.path.exists(img):
                st.image(img, width=450)
            
            # FAST LIKE BUTTON LOGIC
            likes = st.session_state.post_likes.get(i, 0)
            if st.button(f"👍 {likes} Likes", key=f"lk_btn_{i}"):
                st.session_state.post_likes[i] = likes + 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # --- TAB 3: PHOTO GALLERY ---
    with tab2:
        if st.session_state.photo_index is None:
            cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                        if st.button(f"View {title}", key=f"gal_open_{i}"):
                            st.session_state.photo_index = i
                            st.rerun()
        else:
            idx = st.session_state.photo_index
            st.image(posters[idx][0], use_container_width=True, caption=posters[idx][1])
            if st.button("❌ Close Gallery"):
                st.session_state.photo_index = None
                st.rerun()

    # --- TAB 4/5: BOOKINGS & CANCELLATIONS ---
    with tab3:
        st.markdown('<div class="section-header">New Booking - £54.99</div>', unsafe_allow_html=True)
        evt = st.selectbox("Activity:", ["Target Day", "Adrenaline Weekend", "Ultimate Challenge Day", "Social Play Fest", "Extreme Impact Day", "Skill Switch Experience"])
        dt = st.selectbox("Date:", ["4th August", "5th August", "10th August", "15th August"])
        if st.button("Reserve Slot"):
            st.session_state.my_bookings.append({"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"})
            st.success("Reserved! Receipt sent to connected email.")

    with tab4:
        st.markdown('<div class="section-header">Your Scheduled Events</div>', unsafe_allow_html=True)
        if not st.session_state.my_bookings:
            st.info("No active bookings.")
        else:
            for i, b in enumerate(st.session_state.my_bookings):
                st.markdown(f'<div class="content-box">🎯 <b>{b["event"]}</b><br>Date: {b["date"]} | ID: {b["id"]}</div>', unsafe_allow_html=True)
                if st.button(f"Cancel {b['id']}", key=f"can_booking_{i}"):
                    st.session_state.my_bookings.pop(i)
                    st.rerun()

    with tab5: # FAQs
        faqs = [
            ("Where is the site?", "HQ is Swansea, but ALL events are held at Stouthall Mansion."),
            ("What if it rains?", "We use our indoor arena at Stouthall."),
            ("What is the cost?", "£54.99 per person for all activities."),
            ("Are staff qualified?", "Yes, Enhanced DBS checked and First Aid trained."),
            ("Do you offer group discounts?", "Yes, groups of 10+ receive a 10% discount.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
