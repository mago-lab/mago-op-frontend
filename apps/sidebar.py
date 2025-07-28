import streamlit as st

def sidebar_header():
    """사이드바 헤더를 표시합니다."""
    st.sidebar.title("🎵 음성인식 서비스")
    st.sidebar.markdown("---")

def create_navigation():
    """네비게이션 메뉴를 생성합니다."""
    st.sidebar.markdown("### 📋 메뉴")

    # 홈 버튼
    home_clicked = st.sidebar.button("🏠 홈", key="home_btn")

    # 서비스 선택
    st.sidebar.markdown("### 🔧 서비스")
    service_options = ["음성인식", "자막 생성", "음성 분석"]
    selected_service = st.sidebar.selectbox("서비스를 선택하세요", service_options)

    # 로그아웃 버튼
    st.sidebar.markdown("---")
    logout_clicked = st.sidebar.button("🚪 로그아웃", key="logout_btn")

    return home_clicked, selected_service, logout_clicked