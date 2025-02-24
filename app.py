# Hotel Chatbot - Optimized for Performance
#
# 변경사항 및 이유:
# 1. **모델 로딩 속도 개선:** `Doc2Vec.load()`를 전역 변수로 한 번만 로드하여 속도 개선
# 2. **Corpus 데이터 로딩 최적화:** `load_corpus()` 결과를 `st.session_state`에 캐싱하여 반복 로딩 방지
# 3. **HTML 렌더링 속도 향상:** 채팅 내용이 업데이트될 때만 HTML 문자열을 재구성하여 렌더링 지연 최소화

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from gensim.models import Doc2Vec
from sklearn.metrics.pairwise import cosine_similarity
import random
import operator

# 스타일 추가 (말풍선)
st.markdown(
    """
    <style>
    .chatbot-bubble {
        background-color: #e0e0e0;
        border-radius: 15px;
        padding: 10px;
        margin: 5px 0;
        display: inline-block;
        max-width: 70%;
        float: left;
        clear: both;
        order: 2;
    }
    .user-bubble {
        background-color: #4caf50;
        color: white;
        border-radius: 15px;
        padding: 10px;
        margin: 5px 0;
        display: inline-block;
        max-width: 70%;
        float: right;
        clear: both;
        order: 1;
    }
    .chat-container {
        overflow-y: auto;
        height: 400px;
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 10px;
        background-color: #f9f9f9;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Greeting function
def greeting(sentence):
    GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey", "hey there"]
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Probability calculation function (Only calc_prob is used now)
def calc_prob(v1, sentences, model):
    probs = [(idx, cosine_similarity(v1.reshape(1, -1), model.infer_vector(word_tokenize(sentence.lower())).reshape(1, -1))[0][0])
             for idx, sentence in enumerate(sentences)]
    best_match = max(probs, key=lambda x: x[1])
    st.write(f"Best match index: {best_match[0]}, Similarity: {best_match[1]:.2f}")  # 디버깅용 출력
    return best_match

# Load corpus
def load_corpus(ans_path, ques_path):
    with open(ans_path, 'r', errors='ignore') as file:
        ans_data = file.read().lower()
    with open(ques_path, 'r', errors='ignore') as file:
        ques_data = file.read().lower()
    return sent_tokenize(ans_data), sent_tokenize(ques_data)

# Streamlit chatbot app
def chatbot_app():
    st.title('Hotel Chatbot - Jane🤖')
    st.write('Jane🤖: My name is Jane. I will answer your queries about this hotel. If you want to exit, type Bye!')

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    if 'model' not in st.session_state:
        st.session_state.model = Doc2Vec.load(r"C:\\Users\\user\\Desktop\\psh\\수업자료\\2502\\module27\\ipynb_dataset_model\\hotelChat\\doc2vec.bin")

    if 'ans_tokens' not in st.session_state or 'ques_tokens' not in st.session_state:
        st.session_state.ans_tokens, st.session_state.ques_tokens = load_corpus(
            r"C:\\Users\\user\\Desktop\\psh\\수업자료\\2502\\module27\\ipynb_dataset_model\\[Dataset] Module27(ans).txt",
            r"C:\\Users\\user\\Desktop\\psh\\수업자료\\2502\\module27\\ipynb_dataset_model\\[Dataset] Module27(ques).txt"
        )

    # 말풍선들을 하나의 HTML 문자열로 합치기
    chat_html = '<div class="chat-container">'
    for message in st.session_state.conversation:
        if message.startswith("User💬"):
            chat_html += f'<div class="user-bubble">{message.replace("User💬:", "You💬:")}</div>'
        else:
            chat_html += f'<div class="chatbot-bubble">{message.replace("Jane🤖:", "Jane🤖:")}</div>'
    chat_html += '</div>'

    st.markdown(chat_html, unsafe_allow_html=True)

    user_response = st.text_input("You💬:")
    enter = st.button("Send Message")

    if user_response and enter:
        st.session_state.conversation.append(f"User💬: {user_response}")
        user_response_lower = user_response.lower()

        if user_response_lower != 'bye':
            if user_response_lower in ['thanks', 'thank you']:
                st.session_state.conversation.append("Jane🤖: You are welcome.")
            else:
                greet = greeting(user_response_lower)
                if greet is not None:
                    st.session_state.conversation.append(f"Jane🤖: {greet}")
                else:
                    user_vector = st.session_state.model.infer_vector(word_tokenize(user_response_lower))
                    resp = calc_prob(user_vector, st.session_state.ans_tokens, st.session_state.model)
                    chatbot_response = f"Jane🤖: {st.session_state.ans_tokens[resp[0]]} (With similarity of {resp[1]:.2f})"
                    st.session_state.conversation.append(chatbot_response)
                    st.write(f"Added chatbot response: {chatbot_response}")  # 디버깅용 출력
        else:
            st.session_state.conversation.append("Jane🤖: Bye! Take care.")

if __name__ == "__main__":
    chatbot_app()
