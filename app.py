import streamlit as st
import streamlit.components.v1 as components

# 블랙박스 추천 HTML 코드
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>40~50만원대 하이엔드 블랙박스 추천</title>
    <h1 style="text-align: center;">40~50만원대 하이엔드 블랙박스 추천</h1>
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://search.shopping.naver.com/search/all?query=아이나비+퀀텀3+4K" target="_blank" style="padding: 10px 20px; background-color: #3498db; color: white; text-decoration: none; border-radius: 5px;">아이나비 퀀텀3 4K 검색하기</a>
    </div>
</head>
<body>
</body>
</html>
"""

# Streamlit 화면에 바로 렌더링 (화면 너비에 맞게 출력)
components.html(html_code, height=900, scrolling=True)
