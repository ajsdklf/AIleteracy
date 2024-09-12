import streamlit as st
from openai import OpenAI 
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 더 나은 스타일링을 위한 사용자 정의 CSS
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        color: #4A4A4A;
        text-align: center;
        margin-bottom: 2rem;
    }
    .subtitle {
        font-size: 1.5rem;
        color: #6A6A6A;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-title {
        font-size: 2rem;
        color: #4A4A4A;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .team-member {
        font-size: 1.2rem;
        color: #4A4A4A;
        margin-bottom: 0.5rem;
    }
    .description {
        font-size: 1.1rem;
        color: #6A6A6A;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# 메인 제목
st.markdown("<h1 class='main-title'>에이아이다움</h1>", unsafe_allow_html=True)

# 부제목
st.markdown("<p class='subtitle'>인공지능 문해력 격차 해소</p>", unsafe_allow_html=True)

# 미션 선언문
st.markdown("<h2 class='section-title'>우리의 미션</h2>", unsafe_allow_html=True)
st.markdown(
    "<p class='description'>"
    "에이아이다움에서는 인공지능 기술 문해력 격차 해소에 전념하고 있습니다. "
    "우리는 모든 사람이 배경이나 기술 전문성 수준에 관계없이 인공지능 기술을 이해하고 참여할 수 있는 기회를 가져야 한다고 믿습니다. "
    "우리의 목표는 개인이 빠르게 진화하는 인공지능 세계를 탐색할 수 있도록 포용적이고 접근 가능한 자원과 도구를 만드는 것입니다."
    "</p>", 
    unsafe_allow_html=True
)

# 우리가 하는 일
st.markdown("<h2 class='section-title'>우리가 하는 일</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("🎓 **교육 자료**")
    st.markdown("인공지능 개념에 대한 이해하기 쉬운 가이드와 튜토리얼을 개발합니다.")

with col2:
    st.markdown("🛠️ **대화형 도구**")
    st.markdown("인공지능 기능을 시연하는 사용자 친화적인 애플리케이션을 만듭니다.")

st.markdown("🌐 **커뮤니티 구축**")
st.markdown("인공지능 학습과 토론을 위한 지원적인 커뮤니티를 육성합니다.")

# 팀 멤버
st.markdown("<h2 class='section-title'>우리 팀</h2>", unsafe_allow_html=True)
team_members = ["강지민", "고정훈", "한예지", "김영운", "김한울"]
for member in team_members:
    st.markdown(f"<p class='team-member'>• {member}</p>", unsafe_allow_html=True)

# 행동 촉구
st.markdown("<h2 class='section-title'>우리의 미션에 동참하세요</h2>", unsafe_allow_html=True)
st.markdown(
    "<p class='description'>"
    "당신이 인공지능 전문가이든 이제 막 여정을 시작했든, 우리 커뮤니티에는 당신을 위한 자리가 있습니다. "
    "함께, 우리는 인공지능 문해력 격차를 해소하고 더 포용적인 미래를 만들 수 있습니다."
    "</p>", 
    unsafe_allow_html=True
)

# 연락 양식 (자리 표시자)
st.markdown("<h2 class='section-title'>연락하기</h2>", unsafe_allow_html=True)
name = st.text_input("이름")
email = st.text_input("이메일")
message = st.text_area("메시지")
if st.button("보내기"):
    st.success("메시지를 보내주셔서 감사합니다. 곧 연락 드리겠습니다!")