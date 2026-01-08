import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Fakebook")

# 1. Memory Management (Session State)
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []
if "user_reviews" not in st.session_state:
    st.session_state.user_reviews = [
        {"name": "Liam W.", "stars": "⭐⭐⭐⭐⭐", "text": "Best laser tag experience in Wales!"},
        {"name": "Chloe M.", "stars": "⭐⭐⭐⭐", "text": "Really enjoyed the bushcraft session."},
        {"name": "Dan R.", "stars": "⭐⭐⭐⭐⭐", "text": "The puzzles at Stouthall were brain-melters."}
    ]
if "post_likes" not in st.session_state:
    st.session_state.post_likes = {i: random.randint(45, 1200) for i in range(60)}

# 2. CAMPAIGN CONTENT STRATEGY
campaign_narratives = [
    ("Skills Spotlight: Mastering the Spark", "Gemini_Generated_Image_fqzz3rfqzz3rfqzz.png", "Bushcraft discipline: Master fire lighting under the Stouthall canopy. 🔥 #SurvivalSkills"),
    ("Poster Reveal: Target Day 2026", "target_day.jpg", "The arrows are fletched. Target Day returns this August. 🏹 #Archery #Stouthall"),
    ("Tactical Intel: New Gear", "Gemini_Generated_Image_sbz4c8sbz4c8sbz4.png", "Precision sensors and long-range optics are now standard. 🔫 #TacticalLaser"),
    ("Mansion Grounds", "Gemini_Generated_Image_lpugatlpugatlpug.png", "Stouthall Mansion provides 30 acres of woodland. 🏴󠁧󠁢󠁷󠁬󠁳󠁿 #VisitWales"),
    ("Pricing: All-Inclusive Value", None, "High-intensity adventure for a flat rate of £54.99. 💸 #FairPrice"),
    ("Arena Action: Neon Nights", "Gemini_Generated_Image_g2yanmg2yanmg2ya.png", "The indoor neon arena ensures the Blast never stops. 🌈 #IndoorFun"),
    ("Strategy: Team Logic", "Gemini_Generated_Image_xz9er1xz9er1xz9e.png", "Unlock crates with high-level communication. 🧠 #Teamwork"),
    ("Ultimate Challenge", "ultimate_challenge.jpg", "6 Activities. 1 Winner. Booking open for August! 🎟️"),
    ("Safety First", None, "Instructors are Enhanced DBS checked and First Aid trained. ✅"),
    ("Precision Archery", "Gemini_Generated_Image_of95w8of95w8of95.png", "The sound of the arrow hitting the straw. 🎯 #ArcheryLife")
]

# 3. UI STYLING
st.markdown("""
    <style>
    .fb-logo { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; font-size: 28px; letter-spacing: -1px; }
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}
    .section-header { background-color: #adb9d3; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .post-card { border: 1px solid #dddfe2; background-color: white; padding: 20px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 1px 2px rgba(0,0,0,0.1); }
    .price-tag { color: #adb9d3; font-weight: bold; font-size: 20px; }
    .motto { color: #adb9d3; font-weight: bold; font-size: 22px; text-align: center; display: block; margin-top: 20px; letter-spacing: 3px; }
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
    st.markdown('<div class="content-box"><b>Hub:</b> Swansea.<br><b>Site:</b> Stouthall Country Mansion.<br><b>Standard Rate:</b> £54.99 per person.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    st.text_input("Newsletter Signup", placeholder="email@example.com", key="side_nl")
    if st.button("Subscribe"): st.toast("Welcome to the Hive! 🐝")

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1:
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="content-box">South Wales\' premier adventure company at <b>Stouthall Mansion</b>. All-inclusive days for <span class="price-tag">£54.99</span>.<br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">{r["stars"]} "{r["text"]}" - {r["name"]}</div>', unsafe_allow_html=True)

    with tab_posts:
        for i in range(55):
            st.markdown('<div class="post-card">', unsafe_allow_html=True)
            narrative = campaign_narratives[i % len(campaign_narratives)]
            st.markdown(f"**{narrative[0]}**")
            st.write(narrative[2])
            if narrative[1] and os.path.exists(narrative[1]):
                st.image(narrative[1], width=450)
            likes = st.session_state.post_likes.get(i, 0)
            if st.button(f"👍 {likes} Likes", key=f"lk_btn_{i}"):
                st.session_state.post_likes[i] = likes + 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    with tab3: # Booking
        st.markdown('<div class="section-header">Book Your Adventure - £54.99</div>', unsafe_allow_html=True)
        evt = st.selectbox("Activity:", ["Target Day", "Adrenaline Weekend", "Ultimate Challenge Day"])
        dt = st.selectbox("Date:", ["4th August", "5th August", "10th August"])
        if st.button("Reserve Slot"):
            st.session_state.my_bookings.append({"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"})
            st.success("Reserved! Receipt sent.")
