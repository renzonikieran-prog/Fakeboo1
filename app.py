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
if "post_likes" not in st.session_state:
    st.session_state.post_likes = [random.randint(45, 950) for _ in range(100)]
if "ui_color" not in st.session_state:
    st.session_state.ui_color = "#adb9d3" # Default project blue

# 2. EVENT DATA
event_data = {
    "Target Day": ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th August"],
    "Adrenaline Weekend": ["12th", "13th", "14th", "18th", "19th August"],
    "Ultimate Challenge Day": ["6th", "7th", "11th", "20th August"],
    "Social Play Fest": ["9th", "10th", "15th", "16th August"],
    "Extreme Impact Day": ["4th", "5th", "17th", "22nd August"],
    "Skill Switch Experience": ["8th", "14th", "21st", "23rd August"]
}

# 3. VERIFIED GALLERY DATA (Using your cinematic images)
posters = [
    ("target_day.jpg", "Target Day Poster"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend Poster"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Poster"),
    ("social_play_fest.jpg", "Social Play Fest Poster"),
    ("extreme_impact.jpg", "Extreme Impact Poster"),
    ("skill_switch.jpg", "Skill Switch Poster"),
    ("Gemini_Generated_Image_lpugatlpugatlpug.jpg", "Stouthall Mansion Grounds"),
    ("Gemini_Generated_Image_of95w8of95w8of95.jpg", "Outdoor Archery Action"),
    ("Gemini_Generated_Image_4nwpmx4nwpmx4nwp.jpg", "Indoor Archery Arena"),
    ("Gemini_Generated_Image_fqzz3rfqzz3rfqzz.jpg", "Bushcraft Skills"),
    ("Gemini_Generated_Image_sbz4c8sbz4c8sbz4.jpg", "Tactical Laser Equipment"),
    ("Gemini_Generated_Image_q74buoq74buoq74b.jpg", "Outdoor Laser Tag"),
    ("Gemini_Generated_Image_g2yanmg2yanmg2ya.jpg", "Indoor Neon Arena"),
    ("Gemini_Generated_Image_hunw61hunw61hunw.jpg", "Victory Celebration"),
    ("Gemini_Generated_Image_xz9er1xz9er1xz9e.jpg", "Logic Puzzle Challenge"),
    ("Gemini_Generated_Image_vv49c1vv49c1vv49.jpg", "Indoor Team Games"),
    ("Gemini_Generated_Image_olevawolevawolev.jpg", "Outdoor Physical Puzzles"),
    ("Gemini_Generated_Image_cueiazcueiazcuei.jpg", "Outdoor Team Challenge")
]

# --- 4. SIDEBAR (Customization & Connectivity) ---
with st.sidebar:
    st.title("Project Controls")
    
    # Palette Selection
    theme_preset = st.selectbox("Theme Preset", ["Standard", "Hot Dog Theme", "Holiday (Winter)", "Holiday (Summer)"])
    
    # Specific color choice from palette
    picked_color = st.color_picker("Custom Accent Color", st.session_state.ui_color)
    if picked_color != st.session_state.ui_color:
        st.session_state.ui_color = picked_color
        st.rerun()

    st.divider()
    # Functional Connectivity Buttons
    st.subheader("Integrations")
    if st.button("Connect Email"):
        st.toast("Email account linked.")
    if st.button("Connect Calendar"):
        st.toast("Project calendar synced.")

# --- 5. UI STYLING ---
st.markdown(f"""
    <style>
    .nav-bar {{ background-color: {st.session_state.ui_color}; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; margin-bottom: 20px;}}
    .section-header {{ background-color: {st.session_state.ui_color}; color: white; padding: 8px 12px; font-weight: bold; font-size: 14px; margin-top: 15px; border-radius: 2px; }}
    .content-box {{ border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }}
    .motto {{ color: {st.session_state.ui_color}; font-weight: bold; font-size: 22px; text-align: center; display: block; margin-top: 20px; letter-spacing: 3px; }}
    </style>
    """, unsafe_allow_html=True)

# --- 6. HEADER & LAYOUT ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><div style="background-color: white; color: #333; padding: 2px 10px; border-radius: 2px;">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("Gemini_Generated_Image_lpugatlpugatlpug.jpg"):
        st.image("Gemini_Generated_Image_lpugatlpugatlpug.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business Hub:</b> Swansea.<br><b>Activity Site:</b> Stouthall Country Mansion.</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab_posts, tab2, tab3, tab4, tab5 = st.tabs(["📄 Info", "📰 Posts", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings", "❓ FAQ"])

    with tab1:
        st.markdown('<div class="section-header">About Blast Hive</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="content-box">We are Blast Hive. All activities take place at the <b>Stouthall Country Mansion</b>.<br><span class="motto">READY, AIM, BLAST!</span></div>', unsafe_allow_html=True)

    with tab_posts:
        # Full 35-post marketing campaign feed
        st.markdown('<div class="section-header">35-Post Activity Feed</div>', unsafe_allow_html=True)
        images_avail = [p[0] for p in posters if os.path.exists(p[0])]
        for i in range(35):
            st.markdown(f'<div class="content-box"><b>Update #{i+1}</b>: Join us at Stouthall for our next event!</div>', unsafe_allow_html=True)
            if images_avail:
                st.image(images_avail[i % len(images_avail)], width=400)
            st.divider()

    with tab2: # Evidence Gallery
        cols = st.columns(3)
        for i, (img, title) in enumerate(posters):
            with cols[i % 3]:
                if os.path.exists(img):
                    st.image(img, use_container_width=True, caption=title)
