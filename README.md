# 🎵 음성인식 서비스

Streamlit 기반의 음성인식 웹 애플리케이션입니다. 파일 업로드와 YouTube URL을 통해 음성인식 서비스를 제공합니다.

## ✨ 주요 기능

- **파일 업로드**: MP3, WAV, M4A, FLAC 형식의 오디오 파일 업로드
- **YouTube URL**: YouTube 동영상 URL을 통한 음성인식
- **실시간 처리**: 음성인식 결과를 실시간으로 확인
- **결과 다운로드**: 텍스트 및 JSON 형식으로 결과 다운로드
- **단어별 상세 정보**: 각 단어의 시작/종료 시간과 신뢰도 표시

## 🚀 설치 및 실행

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 애플리케이션 실행

```bash
streamlit run app.py
```

### 3. 브라우저에서 접속

```
http://localhost:8501
```

## 📁 프로젝트 구조

```
mago-op-frontend/
├── app.py                 # 메인 애플리케이션
├── requirements.txt       # Python 의존성
├── README.md             # 프로젝트 설명
├── apps/
│   ├── sidebar.py        # 사이드바 네비게이션
│   └── home.py          # 홈 화면
├── services/
│   └── speech_recognition.py  # 음성인식 서비스
└── config/
    └── style.py         # UI 스타일 설정
```

## 🎯 사용법

### 1. 파일 업로드

1. 사이드바에서 "🏠 홈" 버튼 클릭
2. "📁 파일 업로드" 탭 선택
3. 음성 파일 선택 (MP3, WAV, M4A, FLAC)
4. "🎯 음성인식 시작" 버튼 클릭
5. 결과 확인 및 다운로드

### 2. YouTube URL

1. "📺 YouTube URL" 탭 선택
2. YouTube 동영상 URL 입력
3. "🎯 음성인식 시작" 버튼 클릭
4. 결과 확인 및 다운로드

## 🔧 설정

### 환경 변수

실제 음성인식 API를 사용하려면 다음 환경 변수를 설정하세요:

```bash
export SPEECH_RECOGNITION_API_URL="http://your-api-server:8000/api/speech"
export SPEECH_RECOGNITION_API_KEY="your-api-key"
```

### API 서비스 변경

`services/speech_recognition.py`에서 `MockSpeechRecognitionService`를 실제 API 서비스로 변경:

```python
# MockSpeechRecognitionService 대신 SpeechRecognitionService 사용
speech_service = SpeechRecognitionService(
    api_url="http://your-api-server:8000/api/speech",
    api_key="your-api-key"
)
```

## 🎨 UI 특징

- **반응형 디자인**: 다양한 화면 크기에 최적화
- **직관적인 인터페이스**: 사용하기 쉬운 탭 기반 레이아웃
- **실시간 피드백**: 처리 상태와 결과를 실시간으로 표시
- **다양한 다운로드 옵션**: 텍스트 및 JSON 형식 지원

## 🔮 향후 계획

- [ ] 실제 음성인식 API 연동
- [ ] 다국어 지원
- [ ] 배치 처리 기능
- [ ] 사용자 인증 시스템
- [ ] 처리 히스토리 관리

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 🤝 기여

버그 리포트나 기능 제안은 이슈를 통해 제출해 주세요.