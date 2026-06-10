import streamlit as st
import streamlit.components.v1 as components
import pathlib

st.set_page_config(
    page_title="AI 지능형 CCTV 범죄 예방 시스템",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit 기본 UI 완전 제거
st.markdown("""
<style>
    .stApp { background: #050b18; }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    /* iframe 자체의 여백 제거 */
    .stCustomComponentV1 { border: none !important; }
    iframe { border: none !important; display: block; }
</style>
""", unsafe_allow_html=True)

# HTML 파일 읽기 (pathlib으로 안전하게)
html_file = pathlib.Path(__file__).parent / "index.html"

try:
    html_content = html_file.read_text(encoding="utf-8")
    # Streamlit 내부 스크롤을 위해 height를 뷰포트 기준으로 설정
    # scrolling=True 로 iframe 내부에서 스크롤 가능하게 함
    components.html(
        html_content,
        height=850,    # 뷰포트 높이와 유사하게
        scrolling=True  # ← 핵심: iframe 내 스크롤 허용
    )
except FileNotFoundError:
    st.error(f"❌ index.html 파일을 찾을 수 없습니다: {html_file}")
    st.info("app.py와 같은 폴더에 index.html 파일이 있는지 확인해주세요.")
