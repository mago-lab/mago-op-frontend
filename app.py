#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- SATURN
# AUTHORS:
# Sukbong Kwon (Galois)

import streamlit as st
from apps.sidebar import sidebar_header, create_navigation
from apps.home import home_page
from services.speech_recognition import MockSpeechRecognitionService
from config.style import apply_custom_style

# 페이지 설정
st.set_page_config(
    page_title="음성인식 서비스",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 커스텀 스타일 적용
apply_custom_style()

# 세션 상태 초기화
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

if 'selected_service' not in st.session_state:
    st.session_state.selected_service = "음성인식"

if 'speech_service' not in st.session_state:
    st.session_state.speech_service = MockSpeechRecognitionService()

def main():
    """메인 애플리케이션 함수"""

    # 사이드바 헤더
    sidebar_header()

    # 네비게이션
    home_clicked, selected_service, logout_clicked = create_navigation()

    # 페이지 상태 업데이트
    if home_clicked:
        st.session_state.current_page = "home"
        st.rerun()

    if logout_clicked:
        st.session_state.current_page = "home"
        st.session_state.selected_service = "음성인식"
        st.rerun()

    # 선택된 서비스 업데이트
    if selected_service != st.session_state.selected_service:
        st.session_state.selected_service = selected_service
        st.rerun()

    # 메인 콘텐츠
    if st.session_state.current_page == "home":
        home_page()

    # 서비스별 페이지 (향후 확장 가능)
    elif st.session_state.current_page == "service":
        st.title(f"🔧 {st.session_state.selected_service}")
        st.info(f"{st.session_state.selected_service} 서비스 페이지입니다. 현재는 홈 화면에서 모든 기능을 사용할 수 있습니다.")

if __name__ == '__main__':
    main()
