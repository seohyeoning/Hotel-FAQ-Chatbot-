# Hotel-FAQ-Chatbot
## 🏨 프로젝트 소개
Hotel FAQ Chatbot은 호텔 관련 질문에 빠르고 정확하게 응답하는 인공지능 챗봇입니다. Doc2Vec 모델을 사용하여 질문의 의미를 분석합니다.

## ✨ 주요 기능
- **빠른 모델 로딩:** Doc2Vec 모델을 전역 변수로 한 번만 로드하여 속도 개선
- **Corpus 데이터 캐싱:** `st.session_state`에 Corpus 데이터를 캐싱하여 반복 로딩 방지
- **최적화된 HTML 렌더링:** 채팅 업데이트 시에만 HTML 문자열을 재구성하여 렌더링 지연 최소화
- **자연어 이해:** 사용자의 질문에 대한 가장 유사한 답변을 선택해 응답
- **직관적인 UI:** 사용자와 챗봇의 대화가 말풍선 형태로 표시됨

## 🛠️ 사용된 기술
- **프로그래밍 언어:** Python
- **프레임워크 및 라이브러리:**
  - Streamlit: 사용자 인터페이스 구현
  - Gensim: Doc2Vec 모델 사용
  - NLTK: 텍스트 토큰화 및 전처리
  - Scikit-Learn: 코사인 유사도 계산

## 💾 설치 및 실행 방법
### 1. 필수 사전 조건
- Python 3.8 이상 설치
- 필요한 Python 라이브러리 설치

```bash
pip install streamlit nltk gensim scikit-learn
```

### 2. NLTK 데이터 다운로드
```python
import nltk
nltk.download('punkt')
```

### 3. 프로젝트 실행
```bash
streamlit run chatbot.py
```

## 📂 프로젝트 디렉토리 구조
```plaintext
hotel-chatbot
├── chatbot.py
├── models
│   └── doc2vec.bin
└── data
    ├── [Dataset] Module27(ans).txt
    └── [Dataset] Module27(ques).txt
```

## 💡 기여 방법
1. 레포지토리를 포크합니다.
2. 새로운 브랜치를 생성합니다: `git checkout -b feature-branch`
3. 수정 사항을 커밋합니다: `git commit -m 'Add new feature'`
4. 브랜치에 푸시합니다: `git push origin feature-branch`
5. Pull Request를 생성합니다.

## 📜 라이선스
이 프로젝트는 MIT 라이선스에 따라 배포됩니다.


## 📝 추가적인 설명
- 이 챗봇은 호텔 고객의 자주 묻는 질문(FAQ)에 응답하도록 설계되었습니다.
- 향후 기능 추가 계획으로는 다국어 지원 및 음성 인식 기능이 포함될 예정입니다.

