import streamlit as st

# Set page to wide mode to mimic a desktop browser layout
st.set_page_config(layout="wide")

# --- CUSTOM CSS FOR THE FACEBOOK LOOK ---
st.markdown("""
    <style>
    /* Main Header Bar */
    .main-header {
        background-color: #4267B2;
        padding: 10px;
        color: white;
        font-size: 24px;
        font-weight: bold;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    /* Section Headers */
    .section-box {
        background-color: #f0f2f5;
        padding: 10px;
        border-radius: 8px;
        border-left: 5px solid #4267B2;
        margin-bottom: 10px;
    }
    /* Post/Feed Cards */
    .post-card {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #ddd;
        margin-bottom: 15px;
        height: 100px; /* Placeholder height */
    }
    </style>
    """, unsafe_allow_html=True)

# --- BLUE HEADER BAR ---
st.markdown('<div class="main-header">takebook</div>', unsafe_allow_html=True)

# --- LAYOUT: SIDEBAR AND MAIN FEED ---
# Creating two columns: Left (Info) and Right (Recent Activity)
col1, col2 = st.columns([1, 2])

with col1:
    # Sidebar/Left Column Information
    st.markdown('<div class="section-box"><b>Basic Information</b></div>', unsafe_allow_html=True)
    st.info("") # Placeholder for your text
    
    st.markdown('<div class="section-box"><b>Groups</b></div>', unsafe_allow_html=True)
    st.text_area("Group List", value="", height=100, label_visibility="collapsed")
    
    st.markdown('<div class="section-box"><b>Events</b></div>', unsafe_allow_html=True)
    st.info("") # Placeholder for your text

with col2:
    # Main Feed / Recent Activity
    st.subheader("Recent Activity")
    
    # Placeholder Post Cards (Empty containers for your future text)
    st.markdown('<div class="post-card"></div>', unsafe_allow_html=True)
    st.markdown('<div class="post-card"></div>', unsafe_allow_html=True)
    st.markdown('<div class="post-card"></div>', unsafe_allow_html=True)
    st.markdown('<div class="post-card"></div>', unsafe_allow_html=True)
