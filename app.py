import streamlit as st
import os

st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# --- INITIALIZE SESSION STATE ---
if "photo_index" not in st.session_state:
    st.session_state.photo_index = None
if "booking_step" not in st.session_state:
    st.session_state.booking_step = "select"
if "my_bookings" not in st.session_state:
    st.session_state.my_bookings = []

# Data mapping from your posters
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

# --- CSS FOR UI ---
st.markdown("""
    <style>
    .nav-bar { background-color: #adb9d3; padding: 10px; display: flex; justify-content: space-between; align-items: center; color: white; }
    .search-box { background-color: white; padding: 5px; border-radius: 2px; color: #333; width: 200px; font-size: 14px; font-weight: bold; border: 1px solid #ccc; }
    .section-header { background-color: #adb9d3; color: white; padding: 5px 10px; font-weight: bold; font-size: 14px; margin-top: 15px; }
    .content-box { border: 1px solid #dddfe2; background-color: white; padding: 15px; font-size: 13px; line-height: 1.5; color: #1c1e21; }
    .thumbnail-box { border: 1px solid #dddfe2; padding: 5px; text-align: center; background-color: white; border-radius: 5px; cursor: pointer; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="nav-bar"><b>takebook</b><div style="display:flex; gap:15px; align-items:center;"><span>Profile</span><span>Inbox</span><span>Friends</span><div class="search-box">Blast Hive 🔍</div></div></div>', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 2.2])

with col_left:
    if os.path.exists("image_83c146.jpg"):
        st.image("image_83c146.jpg", use_container_width=True)
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"><b>Business name:</b> Blast Hive.<br><b>Location:</b> Bishop Gore School, Swansea, Sketty.</div>', unsafe_allow_html=True)

with col_right:
    tab1, tab2, tab3, tab4 = st.tabs(["📄 Info", "🖼️ Photos", "🎟️ Book Now!", "📅 My Bookings"])

    # --- TAB 1: INFO ---
    with tab1:
        st.markdown('<div class="section-header">About your business</div>', unsafe_allow_html=True)
        st.markdown('<div class="content-box">We are Blast Hive, an all-inclusive company that offers exciting days out for the young people in our area. We are based in Swansea and have offered days put that include a wild bushcraft day, competitive team sports day and even a thrilling murder mystery day full of brain boggling puzzles. We offer the fairest prices we possibly can in order for your children and you young people to have the most unforgettable days. We cannot wait to see you guys have fun at our next exciting events. We hope to see you there, when you’re ready, READY, AIM, BLAST!</div>', unsafe_allow_html=True)

    # --- TAB 2: PHOTOS (Interactive Gallery) ---
    with tab2:
        if st.session_state.photo_index is None:
            st.markdown('<div class="section-header">Event Gallery (Click to Enlarge)</div>', unsafe_allow_html=True)
            g_cols = st.columns(3)
            for i, (img, title) in enumerate(posters):
                with g_cols[i % 3]:
                    if os.path.exists(img):
                        st.image(img, use_container_width=True)
                        if st.button(f"View {title}", key=f"thumb_{i}"):
                            st.session_state.photo_index = i
                            st.rerun()
        else:
            # Enlarged View
            idx = st.session_state.photo_index
            st.image(posters[idx][0], use_container_width=True)
            
            c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
            with c1:
                if st.button("⬅ Previous"):
                    st.session_state.photo_index = (idx - 1) % len(posters)
                    st.rerun()
            with c2:
                if st.button("Next ➡"):
                    st.session_state.photo_index = (idx + 1) % len(posters)
                    st.rerun()
            with c4:
                if st.button("❌ Close Gallery", type="primary"):
                    st.session_state.photo_index = None
                    st.rerun()

    # --- TAB 3: BOOK NOW ---
    with tab3:
        st.markdown('<div class="section-header">Book Your Experience</div>', unsafe_allow_html=True)
        if st.session_state.booking_step == "select":
            event_name = st.selectbox("Choose an event:", list(event_data.keys()))
            date_choice = st.selectbox("Select a date from the poster:", event_data[event_name])
            st.write("### Total: £54.99")
            if st.button("Confirm Booking"):
                st.session_state.last_booking = {"event": event_name, "date": date_choice}
                st.session_state.booking_step = "ask_receipt"
                st.rerun()

        elif st.session_state.booking_step == "ask_receipt":
            st.success(f"✅ Successfully booked {st.session_state.last_booking['event']}!")
            st.write("Would you like a receipt?")
            r1, r2 = st.columns(2)
            if r1.button("Yes"):
                st.session_state.my_bookings.append(st.session_state.last_booking)
                st.session_state.booking_step = "receipt_sent"
                st.rerun()
            if r2.button("No"):
                st.session_state.my_bookings.append(st.session_state.last_booking)
                st.session_state.booking_step = "select"
                st.rerun()

        elif st.session_state.booking_step == "receipt_sent":
            st.info("📩 Email sent to *********@gmail.com")
            if st.button("Thank you!"):
                st.session_state.booking_step = "select"
                st.rerun()

    # --- TAB 4: MY BOOKINGS (With Cancel Feature) ---
    with tab4:
        st.markdown('<div class="section-header">Your Confirmed Bookings</div>', unsafe_allow_html=True)
        if not st.session_state.my_bookings:
            st.write("You haven't booked any events yet!")
        else:
            for i, b in enumerate(st.session_state.my_bookings):
                with st.container():
                    st.markdown(f"""
                    <div class="content-box">
                        🎯 <b>Event:</b> {b['event']}<br>
                        📅 <b>Date:</b> {b['date']}<br>
                        💰 <b>Status:</b> Paid (£54.99)
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Cancel {b['event']}", key=f"cancel_{i}"):
                        st.session_state.my_bookings.pop(i)
                        st.rerun()
