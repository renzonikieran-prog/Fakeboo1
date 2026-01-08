import streamlit as st
import os

st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# --- CSS FOR UI ---
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; }
    .search-box { background-color: white; padding: 5px; border-radius: 2px; color: #333; width: 200px; font-size: 14px; font-weight: bold; border: 1px solid #ccc; }
    .section-header { background-color: #adb9d3; color: white; padding: 5px 10px; font-weight: bold; font-size: 14px; margin-top: 15px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.5; color: #1c1e21; }
    .photo-container { border: 1px solid #dddfe2; background-color: white; padding: 10px; margin-bottom: 20px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:15px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div class="search-box">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

# --- 2. LAYOUT ---
col_left, col_right = st.columns([1, 2.2])

with col_left:
    # Logo
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business name:</b> Blast Hive.<br><b>Location:</b> Bishop Gore School, Swansea, Sketty.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Events</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Upcoming</b><br>Target Day! — ages 14-17 in Stouthall. 4-11th August.</div>', unsafe_allow_html=True)

with col_right:
    # Navigation Tabs
    tab1, tab2 = st.tabs(["📄 Info", "🖼️ Photos"])

    with tab1:
        # Status Box
        st.markdown('<div class="content-box" style="margin-top:10px;"><b>Update Status</b><br>Upcoming event! Target Day at Stouthall from 4th–11th August. £54.99! Ready, Aim, BLAST!</div>', unsafe_allow_html=True)
        if st.button("Share Post"):
            st.success("✅ Shared to Timeline!")

        st.markdown('<div class="section-header">About your business</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company that offers exciting days out for the young people in our area. We are based in Swansea and have offered days put that include a wild bushcraft day, competitive team sports day and even a thrilling murder mystery day full of brain boggling puzzles. We offer the fairest prices we possibly can in order for your children and you young people to have the most unforgettable days. We cannot wait to see you guys have fun at our next exciting events. We hope to see you there, when you’re ready, READY, AIM, BLAST!</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-header">Quotes</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box"><i>"Ready, Aim, BLAST!"</i> — The Blast Hive Team</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="section-header">Event Gallery</div>', unsafe_allow_html=True)
        
        # Grid for Photos
        g_col1, g_col2 = st.columns(2)
        
        images = [
            ("adrenaline_weekend.jpg", "Adrenaline Weekend"),
            ("ultimate_challenge.jpg", "Ultimate Challenge"),
            ("social_play_fest.jpg", "Social Play Fest"),
            ("extreme_impact.jpg", "Extreme Impact"),
            ("skill_switch.jpg", "Skill Switch Experience")
        ]
        
        for i, (img, title) in enumerate(images):
            target_col = g_col1 if i % 2 == 0 else g_col2
            with target_col:
                st.markdown(f'<div class="photo-container">', unsafe_allow_html=True)
                if os.path.exists(img):
                    st.image(img, caption=title, use_container_width=True)
                else:
                    st.warning(f"File {img} not found.")
                st.markdown('</div>', unsafe_allow_html=True)
