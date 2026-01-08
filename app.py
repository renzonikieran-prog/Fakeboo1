import streamlit as st
import os
import random

# --- SYSTEM INITIALIZATION ---
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []

# --- DATA MAPPING ---
event_data = {
    "Target Day": ["4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th August"],
    "Adrenaline Weekend": ["12th", "13th", "14th", "18th", "19th"],
    "Ultimate Challenge Day": ["6th", "7th", "11th", "20th"],
    "Social Play Fest": ["9th", "10th", "15th", "16th"],
    "Extreme Impact Day": ["4th", "5th", "17th", "22th"],
    "Skill Switch Experience": ["8th", "14th", "21st", "23rd"]
}

posters = [
    ("target_day.jpg", "Target Day"),
    ("adrenaline_weekend.jpg", "Adrenaline Weekend"),
    ("ultimate_challenge.jpg", "Ultimate Challenge Day"),
    ("social_play_fest.jpg", "Social Play Fest"),
    ("extreme_impact.jpg", "Extreme Impact Day"),
    ("skill_switch.jpg", "Skill Switch Experience")
]

# --- UI STYLING ---
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; border-radius: 4px; }
    .search-box { background-color: white; padding: 5px; border-radius: 2px; color: #333; width: 220px; font-size: 14px; font-weight: bold; border: 1px solid #ccc; }
    .section-header { background-color: #adb9d3; color: white; padding: 6px 12px; font-weight: bold; font-size: 14px; margin-top: 18px; border-radius: 2px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.6; color: #1c1e21; margin-bottom: 12px; border-radius: 4px; }
    .faq-q { font-weight: bold; color: #adb9d3; margin-top: 10px; font-size: 14px; }
    .faq-a { margin-bottom: 10px; border-bottom: 1px solid #f0f2f5; padding-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:20px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div class="search-box">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.3])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business:</b> Blast Hive.<br><b>Location:</b> Swansea, Sketty.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Message the Team</div>', unsafe_allow_html=True)
    with st.expander("Click to open contact form"):
        u_name = st.text_input("Your Name")
        u_msg = st.text_area("Your Question")
        if st.button("Send Message"):
            st.success(f"Thanks {u_name}, we'll get back to you soon!")

    st.markdown('<div class="section-header">Join the Hive</div>', unsafe_allow_html=True)
    email_sub = st.text_input("Newsletter Email:", placeholder="your@email.com")
    if st.button("Subscribe"):
        st.toast("Welcome to the Hive! 🐝")

with col_right:
    tab1, tab2, tab3, tab4 = st.tabs(["📄 Info", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings"])

    with tab1:
        st.markdown('<div class="section-header">About Your Business</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company... [Full Text Applied]</div>', unsafe_allow_html=True)
        
        # EXPANDED FAQ SECTION
        st.markdown('<div class="section-header">Frequently Asked Questions (FAQ)</div>', unsafe_allow_html=True)
        st.markdown("""<div class="content-box">
            <p class="faq-q">Is food and drink included?</p>
            <p class="faq-a">We provide light refreshments (water and fruit), but we ask all attendees to bring a packed lunch for full-day events.</p>
            
            <p class="faq-q">What happens if the weather is bad?</p>
            <p class="faq-a">Most activities go ahead in light rain (it's Wales, after all!). For extreme weather, we switch to our indoor backup facilities in Sketty.</p>
            
            <p class="faq-q">Do you offer group discounts?</p>
            <p class="faq-a">Yes! For bookings of 10 or more people, please use the contact form on the left for a custom quote.</p>
            
            <p class="faq-q">Is there a pick-up/drop-off service?</p>
            <p class="faq-a">Parents are responsible for transport to the meeting point, but we provide a supervised "Stay and Play" zone for 30 mins before and after the event.</p>
            
            <p class="faq-q">Are your activities safe for beginners?</p>
            <p class="faq-a">Absolutely. All events start with a full safety briefing and "skill-builder" session to ensure everyone is comfortable.</p>
        </div>""", unsafe_allow_html=True)

        st.markdown('<div class="section-header">Safety & Accessibility</div>', unsafe_allow_html=True)
        st.markdown("""<div class="content-box">
            ✅ Enhanced DBS Checked Staff<br>
            ✅ First Aid Trained Leaders<br>
            ✅ Inclusive Activity Planning
        </div>""", unsafe_allow_html=True)

    # ... [Rest of the Photo/Booking code remains same as previous master version] ...
