
import streamlit as st
import requests
from config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
from bs4 import BeautifulSoup

# 1 네이버 API를 호출하여 뉴스 검색 결과를 가져오는 get_news( ) 함수 정의
def get_news(query, display=10):
    # 2 네이버 API를 호출하여 url 생성
    url = f"https://openapi.naver.com/v1/search/news.json?query={query}&display={display}"
    headers = {
        'X-Naver-Client-Id': NAVER_CLIENT_ID,
        'X-Naver-Client-Secret': NAVER_CLIENT_SECRET
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 3 문자열에서 HTML 태그를 제거하는 strip_html_tags( ) 함수 정의
def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# 4 스트림릿 애플리케이션의 메인 실행 함수
def main():
    # 5 앱 제목 설정 및 검색어 입력 필드 생성
    st.title("네이버 뉴스 검색")
    query = st.text_input("검색어를 입력하세요")

    # 6 검색 버튼 생성 및 클릭 시 뉴스 데이터를 가져와 결과 출력
    if st.button("검색"):
        news_data = get_news(query)
        if news_data:
            st.write("검색 결과:")
            # 7 뉴스 데이터 항목을 순회하여 제목과 설명을 HTML 태그 없이 출력
            for item in news_data['items']:
                title = strip_html_tags(item['title'])
                description = strip_html_tags(item['description'])
                st.write(f"- [{title}]({item['link']})<br>{description}", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
