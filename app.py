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
        {"name": "Liam W.", "stars": "⭐⭐⭐⭐⭐", "text": "Best laser tag experience in Wales! Professional staff."},
        {"name": "Chloe M.", "stars": "⭐⭐⭐⭐", "text": "Really enjoyed the bushcraft session."},
        {"name": "Dan R.", "stars": "⭐⭐⭐⭐⭐", "text": "The puzzles at Stouthall were brain-melters. Loved it!"}
    ]
if "post_likes" not in st.session_state:
    st.session_state.post_likes = {i: random.randint(45, 1200) for i in range(60)}

# 2. CAMPAIGN CONTENT STRATEGY (Deep Narratives)
campaign_narratives = [
    ("Skills Spotlight: Mastering the Spark", "Gemini_Generated_Image_fqzz3rfqzz3rfqzz.png", "Bushcraft isn't just about survival; it's about discipline. Today's group mastered friction-fire lighting under the Stouthall canopy. 🔥 #SurvivalSkills #BlastHive"),
    ("Poster Reveal: Target Day 2026", "target_day.jpg", "The arrows are fletched and the targets are set. Our most popular event, Target Day, returns this August. Will you take the gold? 🏹 #Archery #Stouthall"),
    ("Tactical Intel: The New Gear", "Gemini_Generated_Image_sbz4c8sbz4c8sbz4.png", "Our armory just got an upgrade. Precision sensors and long-range optics are now standard for all Laser Tag sessions. Come test the tech. 🔫 #TacticalLaser #Gaming"),
    ("Mansion Grounds: A Hidden Gem", "Gemini_Generated_Image_lpugatlpugatlpug.png", "A quick look at our HQ. Stouthall Mansion provides over 30 acres of woodland and lawns, making it the premier activity site in South Wales. 🏴󠁧󠁢󠁷󠁬󠁳󠁿 #VisitWales #OutdoorEducation"),
    ("Pricing Update: All-Inclusive Value", None, "High-intensity adventure shouldn't break the bank. Our flat rate of £54.99 covers all equipment, instruction, and activities for the full day. 💸 #FairPrice #BlastHive"),
    ("Arena Action: Neon Nights", "Gemini_Generated_Image_g2yanmg2yanmg2ya.png", "When the sun goes down, the lights come up. Our indoor neon arena ensures the 'Blast' never stops, regardless of the weather. 🌈 #IndoorFun"),
    ("Strategy Session: Team Logic", "Gemini_Generated_Image_xz9er1xz9er1xz9e.png", "Teamwork makes the dream work. These puzzle crates require high-level communication and logic to unlock. Are your friends up to the task? 🧠 #EscapeRoom #Teamwork"),
    ("The Ultimate Challenge", "ultimate_challenge.jpg", "6 Activities. 1 Winner. The Ultimate Challenge Day is the final test of stamina and skill. Booking is now open for August! 🎟️"),
    ("Safety First: Professional Standards", None, "Did you know? All Blast Hive lead instructors are Enhanced DBS checked and First Aid trained. Safety is our foundation. ✅ #Professionalism"),
    ("Action Shot: Precision Archery", "Gemini_Generated_Image_of95w8of95w8of95.png", "The sound of the arrow hitting the straw—perfection. Join us this weekend for an intensive archery clinic. 🎯 #ArcheryLife")
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

    st.markdown('<div class="section-header">Followers You Know</div>', unsafe_allow_html=True)
    f_col1, f_col2 = st.columns([1, 4])
    with f_col1:
        if os.path.exists("image_83c146.jpg"): st.image("image_83c146.jpg", width=40)
    with f_col2:
        st.markdown('<div style="font-size: 11px; color: #606770;"><b>Gareth Evans</b> and 42 others like this.</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1: # ABOUT & REVIEWS
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="content-box">Blast Hive is South Wales\' premier adventure company. Operating from the historic 30-acre <b>Stouthall Country Mansion</b>, we provide all-inclusive adventure days for just <span class="price-tag">£54.99</span> per person. <br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">Community Reviews</div>', unsafe_allow_html=True)
        for r in st.session_state.user_reviews:
            st.markdown(f'<div class="quote-box">{r["stars"]} "{r["text"]}" - {r["name"]}</div>', unsafe_allow_html=True)

    # --- TAB 2: 55+ DEEP CONTENT POSTS ---
    with tab_posts:
        for i in range(55):
            st.markdown('<div class="post-card">', unsafe_allow_html=True)
            narrative = campaign_narratives[i % len(campaign_narratives)]
            title, img, body = narrative
            st.markdown(f"**{title}**")
            st.write(body)
            if img and os.path.exists(img):
                st.image(img, width=450)
            likes = st.session_state.post_likes.get(i, 0)
            if st.button(f"👍 {likes} Likes", key=f"lk_btn_{i}"):
                st.session_state.post_likes[i] = likes + 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    with tab3: # BOOKING & PRICE LOGIC
        st.markdown('<div class="section-header">Book Your Adventure - £54.99</div>', unsafe_allow_html=True)
        evt = st.selectbox("Activity:", ["Target Day", "Adrenaline Weekend", "Ultimate Challenge Day", "Social Play Fest", "Extreme Impact Day", "Skill Switch Experience"])
        dt = st.selectbox("Date:", ["4th August", "5th August", "10th August", "15th August"])
        if st.button("Reserve Slot"):
            st.session_state.my_bookings.append({"event": evt, "date": dt, "id": f"BH-{random.randint(1000, 9999)}"})
            st.success("Reserved! Receipt sent to connected email.")

    with tab5: # FAQs
        st.markdown('<div class="section-header">Frequently Asked Questions</div>', unsafe_allow_html=True)
        faqs = [
            ("Where is the site?", "HQ is Swansea, but ALL events are held at Stouthall Mansion."),
            ("What if it rains?", "We use our indoor arena at Stouthall."),
            ("What is the cost?", "The flat rate is £54.99 per person for all activities."),
            ("Are staff qualified?", "Yes, Enhanced DBS checked and First Aid trained.")
        ]
        for q, a in faqs:
            st.markdown(f'<span class="faq-q">{q}</span><span>{a}</span>', unsafe_allow_html=True)
