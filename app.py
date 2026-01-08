import streamlit as st

# Set page to wide mode for a desktop social media feel
st.set_page_config(layout="wide", page_title="Blast Hive - Takebook")

# --- FACEBOOK/TAKEBOOK UI STYLING ---
st.markdown("""
    <style>
    /* Top Header Bar */
    .nav-bar {
        background-color: #adb9d3;
        padding: 8px 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: white;
        font-family: Arial, sans-serif;
    }
    .nav-links {
        display: flex;
        gap: 15px;
        font-size: 14px;
        align-items: center;
    }
    .search-box {
        background-color: white;
        padding: 3px 8px;
        border: 1px solid #ddd;
        color: #8d949e;
        width: 180px;
        font-size: 12px;
    }

    /* Sub-navigation Tabs (Wall, Info, Photos) */
    .sub-nav {
        display: flex;
        gap: 2px;
        margin-top: 10px;
    }
    .tab {
        background-color: #e9ebee;
        padding: 5px 20px;
        border: 1px solid #ccd0d5;
        font-size: 13px;
        color: #4b4f56;
    }
    .active-tab {
        background-color: white;
        border-bottom: 1px solid white;
        font-weight: bold;
    }

    /* Section Headers (Blue bars from your screenshot) */
    .section-header {
        background-color: #adb9d3;
        color: white;
        padding: 4px 10px;
        font-weight: bold;
        font-size: 14px;
        margin-top: 15px;
    }
    
    /* Content Boxes */
    .content-box {
        border: 1px solid #dddfe2;
        background-color: white;
        padding: 10px;
        min-height: 40px;
        font-family: Arial, sans-serif;
        font-size: 13px;
    }
    
    /* Feed Post Cards */
    .post-card {
        background-color: white;
        border: 1px solid #dddfe2;
        padding: 15px;
        margin-bottom: 10px;
        min-height: 60px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. HEADER ---
st.markdown("""
    <div class="nav-bar">
        <div style="font-size: 20px; font-weight: bold;">takebook</div>
        <div class="nav-links">
            <span>Profile</span>
            <span>Inbox</span>
            <span>Friends</span>
            <div class="search-box">Blast Hive 🔍</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. MAIN LAYOUT ---
col_left, col_right = st.columns([1, 2.2])

with col_left:
    # Business Profile Image
    st.image("image_83c146.jpg", use_column_width=True)
    
    # Basic Information Section
    st.markdown('<div class="section-header">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"></div>', unsafe_allow_html=True)
    
    # Groups Section
    st.markdown('<div class="section-header">Groups</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box" style="height: 150px;"></div>', unsafe_allow_html=True)
    
    # Events Section
    st.markdown('<div class="section-header">Events</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box" style="height: 200px;"></div>', unsafe_allow_html=True)

with col_right:
    # Sub-tabs (Wall, Info, Photos)
    st.markdown("""
        <div class="sub-nav">
            <div class="tab">Wall</div>
            <div class="tab active-tab">Info</div>
            <div class="tab">Photos</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("") # Spacer
    
    # Update Status Box Placeholder
    st.markdown('<div class="content-box" style="border: 1px solid #ccd0d5; height: 80px;"></div>', unsafe_allow_html=True)
    
    st.markdown('<p style="font-size: 12px; color: #666; margin-top: 5px;">Recent Activity</p>', unsafe_allow_html=True)
    
    # Main Feed Posts
    st.markdown('<div class="post-card"></div>', unsafe_allow_html=True)
    st.markdown('<div class="post-card"></div>', unsafe_allow_html=True)
    st.markdown('<div class="post-card"></div>', unsafe_allow_html=True)
    
    # About Your Business Section
    st.markdown('<div class="section-header">About your business</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box" style="height: 120px;"></div>', unsafe_allow_html=True)
    
    # Likes & Quotes Section
    st.markdown('<div class="section-header">Likes</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">Quotes</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-box"></div>', unsafe_allow_html=True)
