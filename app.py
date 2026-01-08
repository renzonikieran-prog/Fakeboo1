import streamlit as st

st.set_page_config(layout="wide", page_title="Takebook")

# --- ADVANCED CSS FOR FACEBOOK UI ---
st.markdown("""
    <style>
    /* Top Navigation Bar */
    .nav-bar {
        background-color: #4267B2;
        padding: 10px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: white;
        border-radius: 4px;
        margin-bottom: 20px;
    }
    .nav-links {
        display: flex;
        gap: 20px;
        font-size: 14px;
    }
    .search-box {
        background-color: white;
        padding: 5px 10px;
        border-radius: 2px;
        color: #8d949e;
        width: 250px;
    }

    /* Profile Header Area */
    .profile-tabs {
        display: flex;
        justify-content: center;
        gap: 2px;
        margin-bottom: 20px;
    }
    .tab-button {
        background-color: #e9ebee;
        padding: 10px 30px;
        border: 1px solid #ccd0d5;
        color: #4b4f56;
        font-weight: bold;
    }
    .tab-active {
        background-color: white;
        border-bottom: none;
    }

    /* Sidebar Boxes */
    .sidebar-title {
        background-color: #adb9d3;
        color: white;
        padding: 5px 10px;
        font-weight: bold;
        font-size: 14px;
        margin-top: 15px;
    }
    .sidebar-content {
        border: 1px solid #dddfe2;
        background-color: white;
        padding: 15px;
        min-height: 50px;
    }

    /* Feed Posts */
    .feed-post {
        background-color: white;
        border: 1px solid #dddfe2;
        padding: 20px;
        margin-bottom: 10px;
        min-height: 80px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. THE TOP NAV BAR ---
st.markdown("""
    <div class="nav-bar">
        <div style="font-size: 24px; font-weight: bold;">takebook</div>
        <div class="nav-links">
            <span>Profile</span>
            <span>Letters</span>
            <span>Friends</span>
            <div class="search-box">Search... 🔍</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 2. LAYOUT COLUMNS ---
col_left, col_mid = st.columns([1, 2.5])

with col_left:
    # Profile Picture Placeholder (The "Blast Hive" area)
    st.image("https://via.placeholder.com/150", width=150) # Replace with your logo later
    
    st.markdown('<div class="sidebar-title">Basic Information</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-content"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-title">Groups</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-content" style="height:150px;"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-title">Events</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-content"></div>', unsafe_allow_html=True)

with col_mid:
    # Navigation Tabs (Info, Web, Photos)
    st.markdown("""
        <div class="profile-tabs">
            <div class="tab-button">Info</div>
            <div class="tab-button tab-active">Web</div>
            <div class="tab-button">Photos</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("**Recent Activity**")
    st.divider()
    
    # The Feed
    st.markdown('<div class="feed-post"></div>', unsafe_allow_html=True)
    st.markdown('<div class="feed-post"></div>', unsafe_allow_html=True)
    st.markdown('<div class="feed-post"></div>', unsafe_allow_html=True)
    st.markdown('<div class="feed-post"></div>', unsafe_allow_html=True)
    st.markdown('<div class="feed-post"></div>', unsafe_allow_html=True)
