import requests
import json
import os
from typing import Dict, Optional

class SpeechRecognitionService:
    """음성인식 API 서비스 클래스"""

    def __init__(self, api_url: str = None, api_key: str = None):
        self.api_url = api_url or os.getenv("SPEECH_RECOGNITION_API_URL", "http://localhost:8000/api/speech")
        self.api_key = api_key or os.getenv("SPEECH_RECOGNITION_API_KEY", "")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def recognize_audio_file(self, file_path: str, language: str = "ko") -> Optional[Dict]:
        """오디오 파일을 음성인식합니다."""
        try:
            with open(file_path, 'rb') as audio_file:
                files = {'audio': audio_file}
                data = {'language': language}

                response = requests.post(
                    f"{self.api_url}/recognize",
                    files=files,
                    data=data,
                    headers={"Authorization": f"Bearer {self.api_key}"}
                )

                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"API 호출 실패: {response.status_code} - {response.text}")
                    return None

        except Exception as e:
            print(f"음성인식 처리 중 오류: {str(e)}")
            return None

    def recognize_youtube_url(self, youtube_url: str, language: str = "ko") -> Optional[Dict]:
        """YouTube URL을 음성인식합니다."""
        try:
            data = {
                "youtube_url": youtube_url,
                "language": language
            }

            response = requests.post(
                f"{self.api_url}/youtube",
                json=data,
                headers=self.headers
            )

            if response.status_code == 200:
                return response.json()
            else:
                print(f"YouTube API 호출 실패: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"YouTube 음성인식 처리 중 오류: {str(e)}")
            return None

    def get_processing_status(self, task_id: str) -> Optional[Dict]:
        """처리 상태를 확인합니다."""
        try:
            response = requests.get(
                f"{self.api_url}/status/{task_id}",
                headers=self.headers
            )

            if response.status_code == 200:
                return response.json()
            else:
                print(f"상태 확인 실패: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"상태 확인 중 오류: {str(e)}")
            return None

# 모의 API 응답을 위한 클래스
class MockSpeechRecognitionService:
    """테스트용 모의 음성인식 서비스"""

    def __init__(self):
        pass

    def recognize_audio_file(self, file_path: str, language: str = "ko") -> Dict:
        """모의 오디오 파일 음성인식"""
        return {
            "text": "안녕하세요. 이것은 음성인식 테스트 결과입니다. 실제 API가 연결되면 실제 음성이 인식됩니다.",
            "confidence": 0.95,
            "duration": "00:02:30",
            "language": language,
            "words": [
                {"word": "안녕하세요", "start": 0.0, "end": 1.2, "confidence": 0.98},
                {"word": "이것은", "start": 1.3, "end": 2.1, "confidence": 0.94},
                {"word": "음성인식", "start": 2.2, "end": 3.5, "confidence": 0.96},
                {"word": "테스트", "start": 3.6, "end": 4.2, "confidence": 0.92}
            ]
        }

    def recognize_youtube_url(self, youtube_url: str, language: str = "ko") -> Dict:
        """모의 YouTube URL 음성인식"""
        return {
            "text": "YouTube 동영상의 음성인식 결과입니다. 실제 API가 연결되면 YouTube 동영상의 음성이 인식됩니다.",
            "confidence": 0.92,
            "duration": "00:05:15",
            "language": language,
            "youtube_url": youtube_url,
            "words": [
                {"word": "YouTube", "start": 0.0, "end": 0.8, "confidence": 0.95},
                {"word": "동영상의", "start": 0.9, "end": 1.8, "confidence": 0.90},
                {"word": "음성인식", "start": 1.9, "end": 3.2, "confidence": 0.94}
            ]
        }

    def get_processing_status(self, task_id: str) -> Dict:
        """모의 처리 상태"""
        return {
            "task_id": task_id,
            "status": "completed",
            "progress": 100,
            "result": "처리가 완료되었습니다."
        }