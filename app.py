import streamlit as st
import os

st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# --- CSS FOR UI ---
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; }
    .search-box { background-color: white; padding: 5px; border-radius: 2px; color: #333; width: 200px; font-size: 14px; font-weight: bold; border: 1px solid #ccc; }
    .sub-nav { display: flex; gap: 2px; margin-top: 10px; }
    .tab { background-color: #e9ebee; padding: 5px 20px; border: 1px solid #ccd0d5; font-size: 13px; color: #4b4f56; }
    .active-tab { background-color: white; border-bottom: 1px solid white; font-weight: bold; }
    .section-header { background-color: #adb9d3; color: white; padding: 5px 10px; font-weight: bold; font-size: 14px; margin-top: 15px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.5; color: #1c1e21; }
    .activity-item { border-bottom: 1px solid #f0f2f5; padding: 8px 0; font-size: 12px; color: #606770; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
    <div class="nav-bar">
        <b>takebook</b>
        <div style="display:flex; gap:15px; align-items:center;">
            <span>Profile</span>
            <span>Inbox</span>
            <span>Friends</span>
            <div class="search-box">Blast Hive 🔍</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.2])

with col_left:
    # Logo Logic
    image_path = "image_83c146.jpg"
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.warning("⚠️ Logo file 'image_83c146.jpg' not detected on GitHub.")

    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content-box">
            <b>Business name:</b> Blast Hive.<br><br>
            <b>Location:</b> Bishop Gore School, Swansea, Sketty.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Groups</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content-box">
            <b>Recently visited</b><br><br>
            ⛰️ Swansea Outdoors Enthusiasts<br>
            🏹 Archery & Airsoft Wales<br>
            🛡️ Medieval Reenactment South
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Events</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content-box">
            <b>Recent</b><br>
            Bushcraft Day! — ages 12-17 in Stouthall. 1st – 8th April.<br><br>
            Medieval Day! — ages 5-12 in Stouthall. 17 – 19th February.<hr>
            <b>Upcoming</b><br>
            Target Day! — ages 14-17 in Stouthall. 4-11th August.
        </div>
        """, unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="sub-nav"><div class="tab">Wall</div><div class="tab active-tab">Info</div><div class="tab">Photos</div></div>', unsafe_allow_html=True)
    
    # --- STATUS UPDATE BOX ---
    with st.container():
        st.markdown("""
            <div class="content-box" style="margin-top:10px; border-bottom:none;">
                <b>Update Status</b><br>
                Upcoming event! We would like to welcome you to Blast Hive’s very own Target Day! We will be hosting these in Stouthall from the 4th – 11th August. This includes a full range package with archery, airsoft and many more for the small and fair price of £54.99! We will see you there. Ready, Aim, BLAST!
            </div>
            """, unsafe_allow_html=True)
        
        if st.button("Share Post", use_container_width=False):
            st.success("✅ Post shared to Blast Hive's timeline!")
    
    st.write("Recent Activity")
    st.markdown("""
        <div class="content-box">
            <div class="activity-item">✔ Updated business location to Bishop Gore School.</div>
            <div class="activity-item">📅 Added a new event: Target Day!</div>
            <div class="activity-item">⭐ Received a 5-star review from a local parent.</div>
        </div>
        """, unsafe_allow_html=True)

    # --- ABOUT SECTION ---
    st.markdown('<div class="section-header">About your business</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content-box">
            We are Blast Hive, an all-inclusive company that offers exciting days out for the young people in our area. 
            We are based in Swansea and have offered days put that include a wild bushcraft day, competitive team sports day 
            and even a thrilling murder mystery day full of brain boggling puzzles. We offer the fairest prices we possibly 
            can in order for your children and you young people to have the most unforgettable days. We cannot wait to see 
            you guys have fun at our next exciting events. We hope to see you there, when you’re ready, READY, AIM, BLAST!
        </div>
        """, unsafe_allow_html=True)

    # --- LIKES SECTION ---
    st.markdown('<div class="section-header">Likes</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content-box">
            👍 Adventure Sports Monthly<br>
            👍 Swansea Youth Services<br>
            👍 Stouthall Country Mansion
        </div>
        """, unsafe_allow_html=True)
    
    # --- QUOTES SECTION ---
    st.markdown('<div class="section-header">Quotes</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content-box">
            <i>"The best weekend my son has ever had. Highly recommend the Bushcraft day!"</i> — <b>Local Parent</b><br><br>
            <i>"Ready, Aim, BLAST!"</i> — <b>The Blast Hive Team</b>
        </div>
        """, unsafe_allow_html=True)
