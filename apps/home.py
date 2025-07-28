import streamlit as st
import requests
import json
from pathlib import Path
import tempfile
import os
from services.speech_recognition import MockSpeechRecognitionService

def home_page():
    """홈 화면을 표시합니다."""
    st.title("🎵 음성인식 서비스")
    st.markdown("파일을 업로드하거나 YouTube URL을 입력하여 음성인식을 시작하세요.")

    # 탭 생성
    tab1, tab2 = st.tabs(["📁 파일 업로드", "📺 YouTube URL"])

    with tab1:
        st.header("파일 업로드")
        uploaded_file = st.file_uploader(
            "음성 파일을 선택하세요",
            type=['mp3', 'wav', 'm4a', 'flac'],
            help="지원 형식: MP3, WAV, M4A, FLAC"
        )

        if uploaded_file is not None:
            st.success(f"파일이 업로드되었습니다: {uploaded_file.name}")

            # 파일 정보 표시
            file_size = len(uploaded_file.getvalue()) / 1024 / 1024  # MB
            st.info(f"파일 크기: {file_size:.2f} MB")

            # 처리 버튼
            if st.button("🎯 음성인식 시작", key="upload_process"):
                process_audio_file(uploaded_file)

    with tab2:
        st.header("YouTube URL")
        youtube_url = st.text_input(
            "YouTube URL을 입력하세요",
            placeholder="https://www.youtube.com/watch?v=...",
            help="YouTube 동영상 URL을 입력하세요"
        )

        if youtube_url:
            st.success("URL이 입력되었습니다.")

            # 처리 버튼
            if st.button("🎯 음성인식 시작", key="youtube_process"):
                process_youtube_url(youtube_url)

def process_audio_file(uploaded_file):
    """업로드된 오디오 파일을 처리합니다."""
    with st.spinner("음성인식 처리 중..."):
        try:
            # 임시 파일로 저장
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name

            # 음성인식 서비스 호출
            speech_service = st.session_state.get('speech_service', MockSpeechRecognitionService())
            result = speech_service.recognize_audio_file(tmp_file_path)

            # 임시 파일 삭제
            os.unlink(tmp_file_path)

            if result:
                st.success("음성인식이 완료되었습니다!")
                display_results(result)
            else:
                st.error("음성인식 처리 중 오류가 발생했습니다.")

        except Exception as e:
            st.error(f"파일 처리 중 오류가 발생했습니다: {str(e)}")

def process_youtube_url(youtube_url):
    """YouTube URL을 처리합니다."""
    with st.spinner("YouTube 동영상 처리 중..."):
        try:
            # 음성인식 서비스 호출
            speech_service = st.session_state.get('speech_service', MockSpeechRecognitionService())
            result = speech_service.recognize_youtube_url(youtube_url)

            if result:
                st.success("음성인식이 완료되었습니다!")
                display_results(result)
            else:
                st.error("YouTube 동영상 처리 중 오류가 발생했습니다.")

        except Exception as e:
            st.error(f"YouTube 처리 중 오류가 발생했습니다: {str(e)}")

def display_results(result):
    """결과를 표시합니다."""
    st.subheader("📝 음성인식 결과")

    # 결과 텍스트
    st.text_area("인식된 텍스트", result["text"], height=200)

    # 신뢰도
    confidence = result["confidence"]
    st.metric("신뢰도", f"{confidence:.1%}")

    # 처리 시간
    if "duration" in result:
        st.info(f"처리 시간: {result['duration']}")

    # 단어별 상세 정보 (있는 경우)
    if "words" in result and result["words"]:
        st.subheader("🔍 단어별 상세 정보")
        words_data = []
        for word_info in result["words"]:
            words_data.append({
                "단어": word_info["word"],
                "시작 시간": f"{word_info['start']:.1f}s",
                "종료 시간": f"{word_info['end']:.1f}s",
                "신뢰도": f"{word_info['confidence']:.1%}"
            })

        st.dataframe(words_data, use_container_width=True)

    # 다운로드 버튼
    if st.button("📥 결과 다운로드"):
        download_results(result)

def download_results(result):
    """결과를 다운로드합니다."""
    # 텍스트 파일로 다운로드
    text_content = result["text"]
    st.download_button(
        label="📄 텍스트 파일 다운로드",
        data=text_content,
        file_name="speech_recognition_result.txt",
        mime="text/plain"
    )

    # JSON 파일로 다운로드 (상세 정보 포함)
    json_content = json.dumps(result, ensure_ascii=False, indent=2)
    st.download_button(
        label="📊 JSON 파일 다운로드",
        data=json_content,
        file_name="speech_recognition_result.json",
        mime="application/json"
    )