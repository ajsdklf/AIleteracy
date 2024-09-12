import streamlit as st
from openai import OpenAI 
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Update the CSS for better styling and visibility
st.markdown("""
<style>
    .main-title {
        font-size: 3.5rem;
        color: lightyellow;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.8rem;
        color: lightblue;
        text-align: center;
        margin-bottom: 2rem;
    }
    .highlight-box {
        background-color: #f8f9fa;
        border-left: 5px solid #3498db;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .highlight-title {
        color: #1a1a1a;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .highlight-content {
        color: #333333;
    }
    .btn-learn-more {
        background-color: #3498db;
        color: white;
        padding: 0.5rem 1rem;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
        margin: 0.5rem 0;
        cursor: pointer;
        border-radius: 4px;
    }
    .section-title {
        font-size: 2.2rem;
        color: #ff6600;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .team-member {
        font-size: 1.3rem;
        color: black;
        margin-bottom: 1rem;
        padding: 15px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
        border-left: 5px solid #6600cc;
    }
    .team-member:hover {
        transform: translateY(-5px);
    }
    .description {
        font-size: 1.2rem;
        color: #333333;
        line-height: 1.8;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content .stRadio > label {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }
    .sidebar .sidebar-content .stRadio > label:hover {
        background-color: #e9ecef;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("<h1 style='text-align: center; color: #0066cc;'>메뉴</h1>", unsafe_allow_html=True)
menu = st.sidebar.radio("", ["홈", "우리의 미션", "우리가 하는 일", "우리 팀", "연락하기"], format_func=lambda x: f"📌 {x}")

# 팀 멤버 정보
team_members = [
    {"name": "강지민", "role": "AI 연구원", "description": "인공지능 알고리즘 개발 전문가"},
    {"name": "고정훈", "role": "UX 디자이너", "description": "사용자 중심 인터페이스 설계"},
    {"name": "한예지", "role": "데이터 과학자", "description": "데이터 분석 및 시각화 전문가"},
    {"name": "김영운", "role": "프로젝트 매니저", "description": "프로젝트 조정 및 리소스 관리"},
    {"name": "김한울", "role": "교육 컨텐츠 개발자", "description": "AI 교육 자료 제작"}
]

if menu == "홈":
    # 메인 제목
    st.markdown("<h1 class='main-title'>에이아이다움</h1>", unsafe_allow_html=True)

    # 부제목
    st.markdown("<p class='subtitle'>인공지능 기술 정보 격차 해소를 위한 혁신적인 플랫폼</p>", unsafe_allow_html=True)

    # 간단한 소개
    st.write("""
    에이아이다움은 모든 사람이 인공지능 기술을 쉽게 이해하고 활용할 수 있도록 돕는 혁신적인 교육 플랫폼입니다. 
    우리는 AI 기술 정보 격차를 해소하고, 더 포용적인 디지털 미래를 만들어가는 것을 목표로 합니다.
    """)

    # 주요 특징 소개
    st.subheader("에이아이다움의 주요 특징")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <p class="highlight-title">🎓 맞춤형 학습 경험</p>
            <p class="highlight-content">AI 기반 추천 시스템으로 개인화된 학습 경로를 제공합니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <p class="highlight-title">🌐 접근성 높은 플랫폼</p>
            <p class="highlight-content">누구나 쉽게 이용할 수 있는 직관적인 인터페이스를 제공합니다.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <p class="highlight-title">🛠️ 실시간 AI 도구 지원</p>
            <p class="highlight-content">AI 도구 탐색 및 실시간 질의응답 시스템을 제공합니다.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
            <p class="highlight-title">🤝 포용적 커뮤니티</p>
            <p class="highlight-content">다양한 배경의 사람들이 함께 학습하고 성장하는 환경을 조성합니다.</p>
        </div>
        """, unsafe_allow_html=True)

    # 행동 유도
    st.markdown("### 에이아이다움과 함께 AI의 세계를 탐험해보세요")
    st.write("우리의 혁신적인 플랫폼을 통해 AI 기술을 쉽고 재미있게 학습할 수 있습니다.")


    # 최근 업데이트 또는 뉴스
    st.subheader("최근 소식")
    st.info("🎉 새로운 AI 기초 강좌가 오픈되었습니다! '초보자를 위한 머신러닝 입문' 코스를 지금 확인해보세요.")

elif menu == "우리의 미션":
    # 미션 선언문
    st.markdown("<h2 class='section-title'>우리의 미션</h2>", unsafe_allow_html=True)
    st.info(
        "에이아이다움은 인공지능 기술 정보 격차 해소에 전념하고 있습니다. "
        "우리는 모든 사람이 사회적 배경, 교육 수준, 또는 기술 전문성에 관계없이 인공지능 기술을 이해하고 활용할 수 있어야 한다고 믿습니다. "
        "우리의 목표는 급속도로 발전하는 인공지능 세계에서 모든 개인이 자신감을 가지고 참여할 수 있도록 포용적이고 접근 가능한 교육 자원과 실용적인 도구를 제공하는 것입니다."
    )

elif menu == "우리가 하는 일":
    st.markdown("<h2 class='section-title'>우리가 하는 일</h2>", unsafe_allow_html=True)
    
    st.info("에이아이다움은 AI 기술 정보 격차 해소를 위해 다음과 같은 혁신적인 솔루션을 개발하고 있습니다.")

    with st.expander("🎓 AI 기반 맞춤형 학습 추천 시스템"):
        st.subheader("목표")
        st.write("사용자의 AI 이해 수준과 학습 목표에 맞춘 맞춤형 학습 자료를 추천하는 시스템을 구축합니다.")
        
        st.subheader("주요 기능")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**RAG 모델 활용**")
            st.write("사용자의 관심 주제에 대해 최신 학습 자료를 검색하고 추천합니다.")
        with col2:
            st.markdown("**AI 진단 테스트**")
            st.write("사용자의 이해도를 평가하고 맞춤형 학습 경로를 제시합니다.")
        
        st.success("OpenAI API를 활용하여 비용 효율적으로 개발할 계획입니다.")

    with st.expander("🌐 직관적이고 접근성 높은 플랫폼 설계"):
        st.subheader("목표")
        st.write("다양한 연령층과 배경의 사용자가 쉽게 접근하고 이용할 수 있는 학습 플랫폼을 설계합니다.")
        
        st.subheader("주요 특징")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**사용자 친화적 UI/UX**")
            st.write("간단한 네비게이션과 조절 가능한 텍스트 크기")
        with col2:
            st.markdown("**다중 플랫폼 지원**")
            st.write("웹과 모바일 모두 지원")
        with col3:
            st.markdown("**지속적인 개선**")
            st.write("사용자 피드백 기반 UI/UX 개선")
        
        st.info("Streamlit을 사용해 프로토타입을 개발하고, 다양한 사용자 그룹을 대상으로 사용성 테스트를 실시할 예정입니다.")

    with st.expander("🛠️ AI 도구 탐색 및 실시간 지원 시스템"):
        st.subheader("목표")
        st.write("사용자가 AI 도구와 기술을 탐색하고, 실시간으로 질문을 하고 답변을 받을 수 있는 시스템을 개발합니다.")
        
        st.subheader("주요 기능")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**AI 도구 설명서 및 사례 제공**")
            st.write("다양한 AI 도구의 사용법, 사례, 기능 등을 상세히 설명하는 콘텐츠")
        with col2:
            st.markdown("**실시간 지원 챗봇**")
            st.write("GPT 기반 AI 챗봇을 통한 실시간 질의응답 시스템")
        
        st.success("RAG 구조를 도입하여 사용자 질문에 대해 관련 학습 자료를 검색하고 실시간으로 적합한 답변을 생성합니다.")

    st.markdown("<h3 class='section-title'>우리의 비전</h3>", unsafe_allow_html=True)
    st.write("에이아이다움은 이러한 혁신적인 솔루션을 통해 모든 사람이 AI 기술을 쉽게 이해하고 활용할 수 있는 세상을 만들어가고 있습니다. 우리의 노력이 더 포용적이고 공평한 디지털 미래를 향한 길을 열어갈 것입니다.")

elif menu == "우리 팀":
    # 팀 멤버
    st.markdown("<h2 class='section-title'>우리 팀</h2>", unsafe_allow_html=True)
    
    # 사이드바에 팀 멤버 선택 옵션 추가
    selected_member = st.sidebar.selectbox("팀 멤버 상세 정보", [member["name"] for member in team_members])
    
    # 팀 멤버 그리드 표시
    cols = st.columns(3)
    for i, member in enumerate(team_members):
        with cols[i % 3]:
            st.markdown(f"""
            <div class='team-member'>
                <h3 style='color: #333333;'>{member['name']}</h3>
                <p style='color: #666666;'><strong>{member['role']}</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    # 선택된 팀 멤버의 상세 정보 표시
    st.markdown("<h3 class='section-title'>팀 멤버 상세 정보</h3>", unsafe_allow_html=True)
    selected_info = next((member for member in team_members if member["name"] == selected_member), None)
    if selected_info:
        st.markdown(f"""
        <div style='background-color: #f0f0f0; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
            <h4 style='color: #0066cc;'>{selected_info['name']}</h4>
            <p style='color: #009933; font-weight: bold;'>{selected_info['role']}</p>
            <p style='color: #333333;'>{selected_info['description']}</p>
        </div>
        """, unsafe_allow_html=True)

    # 행동 촉구
    st.markdown("<h2 class='section-title'>우리의 미션에 동참하세요</h2>", unsafe_allow_html=True)
    st.success(
        "당신이 인공지능 전문가이든 이제 막 관심을 갖기 시작했든, 우리 커뮤니티에는 당신을 위한 자리가 있습니다. "
        "함께하면, 우리는 인공지능 기술 정보 격차를 해소하고 모든 이에게 공평한 기회가 주어지는 더 포용적인 디지털 미래를 만들 수 있습니다."
    )

elif menu == "연락하기":
    # 연락 양식
    st.markdown("<h2 class='section-title'>연락하기</h2>", unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("이름")
        email = st.text_input("이메일")
        message = st.text_area("메시지")
        submitted = st.form_submit_button("보내기")
        if submitted:
            st.balloons()
            st.success("메시지를 보내주셔서 감사합니다. 곧 연락 드리겠습니다!")