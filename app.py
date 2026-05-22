import streamlit as st
import streamlit.components.v1 as components

# 화면 전체를 넓게 쓰기 위한 설정
st.set_page_config(layout="wide")

# HTML 코드를 큰따옴표 3개(""")로 안전하게 감쌉니다.
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>30~40만원대 블랙박스 추천 (2026 상반기 기준)</title>
    <style>
        body {
            font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background-color: #f4f7f6;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        .summary {
            background: #e8f4fd;
            border-left: 5px solid #3498db;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 4px;
        }
        .summary h2 {
            margin: 0 0 10px 0;
            color: #2980b9;
            font-size: 1.4em;
        }
        .summary p {
            margin: 0;
            font-size: 1.05em;
        }
        .item-card {
            border: 1px solid #e1e8ed;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            background: #fafafa;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .item-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.08);
            background: #ffffff;
        }
        .rank {
            display: inline-block;
            background: #e74c3c;
            color: white;
            font-weight: bold;
            padding: 4px 10px;
            border-radius: 4px;
            margin-right: 10px;
            font-size: 0.9em;
        }
        .item-title {
            font-size: 1.3em;
            font-weight: bold;
            color: #2c3e50;
            margin-top: 0;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            border-bottom: 1px solid #ecf0f1;
            padding-bottom: 12px;
        }
        .specs {
            margin: 0;
            padding: 0;
            list-style: none;
        }
        .specs li {
            margin-bottom: 10px;
            display: flex;
            align-items: flex-start;
        }
        .specs strong {
            min-width: 110px;
            color: #34495e;
        }
        .specs span {
            flex: 1;
        }
        .highlight {
            color: #c0392b;
            font-weight: bold;
        }
        .btn {
            display: inline-block;
            margin-top: 15px;
            padding: 8px 16px;
            background-color: #3498db;
            color: #ffffff !important;
            text-decoration: none;
            border-radius: 4px;
            font-weight: bold;
            font-size: 0.9em;
            transition: background-color 0.3s ease;
        }
        .btn:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="summary">
            <h2>💡 핵심 요약 (결론)</h2>
            <p>최근 6개월(2025년 하반기~2026년 상반기) 빅데이터 및 소비자 리뷰를 분석한 결과, <strong>30~40만 원대 예산</strong>으로 <strong>최상위 화질, 모바일 다이렉트 연동, 그리고 확실한 A/S망</strong>을 모두 충족하는 실사용 만족도 최우수 5개 모델입니다.</p>
        </div>

        <div class="item-card">
            <div class="item-title"><span class="rank">1위</span> 아이나비 QXD1 PLUS (64GB)</div>
            <ul class="specs">
                <li><strong>예상 가격:</strong> <span>약 39~42만 원대</span></li>
                <li><strong>녹화 화질:</strong> <span>전후방 QHD. Vision AI 탑재로 야간, 악천후, 고속 주행 시 <span class="highlight">번호판 보정 식별력 압도적 1위</span>.</span></li>
                <li><strong>모바일 연동:</strong> <span>전용 동글/커넥티드를 통한 고속 Wi-Fi 직접 연결 및 주차 충격 원격 움짤(GIF) 알림 지원.</span></li>
                <li><strong>A/S 및 리뷰:</strong> <span>프리미엄 하이엔드 시장 판매량 및 리뷰 평점 1위. 직영 프리미엄 스토어 운영으로 대면 A/S 및 사후 관리가 가장 확실함.</span></li>
            </ul>
            <a href="https://search.shopping.naver.com/search/all?query=아이나비+QXD1+PLUS" class="btn" target="_blank">상세 정보 및 가격 확인</a>
        </div>

        <div class="item-card">
            <div class="item-title"><span class="rank">2위</span> 파인뷰 X600 4K (128GB + 출장장착 패키지)</div>
            <ul class="specs">
                <li><strong>예상 가격:</strong> <span>약 33~35만 원대</span></li>
                <li><strong>녹화 화질:</strong> <span>전방 <span class="highlight">4K UHD</span> / 후방 QHD. 동급 예산 대비 가장 선명하고 넓은 물리적 해상도 제공.</span></li>
                <li><strong>모바일 연동:</strong> <span>5GHz 고속 Wi-Fi 모듈 탑재로 4K 대용량 영상도 스마트폰으로 끊김 없이 매우 빠르게 다운로드 가능.</span></li>
                <li><strong>A/S 및 리뷰:</strong> <span>4K 지원 모델 중 실사용자 가성비 만족도 최고점. 촘촘한 공식 서비스 지정점 및 대리점망 운영.</span></li>
            </ul>
            <a href="https://search.shopping.naver.com/search/all?query=파인뷰+X600+4K" class="btn" target="_blank">상세 정보 및 가격 확인</a>
        </div>

        <div class="item-card">
            <div class="item-title"><span class="rank">3위</span> 만도 Z10 4K (64GB)</div>
            <ul class="specs">
                <li><strong>예상 가격:</strong> <span>약 32~34만 원대</span></li>
                <li><strong>녹화 화질:</strong> <span>전방 4K UHD. 만도 독자적인 애니세이프(AnySafe) 기술로 강한 충격 시 영상 누락 방지 성능 탁월.</span></li>
                <li><strong>모바일 연동:</strong> <span>Wi-Fi 동글을 통한 전용 스마트폰 앱 실시간 영상 확인 및 다운로드 즉시 지원.</span></li>
                <li><strong>A/S 및 리뷰:</strong> <span>여름철 발열에 강한 내구성으로 호평. 오프라인 '만도플라자'를 통한 신속한 대면 A/S 처리 접근성 우수.</span></li>
            </ul>
            <a href="https://search.shopping.naver.com/search/all?query=만도+Z10+4K" class="btn" target="_blank">상세 정보 및 가격 확인</a>
        </div>

        <div class="item-card">
            <div class="item-title"><span class="rank">4위</span> 아이나비 QXD8000 mini (128GB + 커넥티드 패키지)</div>
            <ul class="specs">
                <li><strong>예상 가격:</strong> <span>약 32~35만 원대</span></li>
                <li><strong>녹화 화질:</strong> <span>전후방 QHD. 소니 스타비스 센서 적용으로 빛이 적은 야간 주행 화질 우수.</span></li>
                <li><strong>모바일 연동:</strong> <span>빌트인 Wi-Fi 및 커넥티드 기능을 통해 모바일 앱에서 차량 상태를 직관적으로 바로 확인 가능.</span></li>
                <li><strong>A/S 및 리뷰:</strong> <span>시야를 가리지 않는 '초소형 룸미러 뒤 밀착 디자인'으로 리뷰 만족도가 높음. 아이나비 전국 직영 센터망 100% 활용.</span></li>
            </ul>
            <a href="https://search.shopping.naver.com/search/all?query=아이나비+QXD8000+mini" class="btn" target="_blank">상세 정보 및 가격 확인</a>
        </div>

        <div class="item-card">
            <div class="item-title"><span class="rank">5위</span> 파인뷰 LXQ600 POWER (128GB)</div>
            <ul class="specs">
                <li><strong>예상 가격:</strong> <span>약 31~33만 원대</span></li>
                <li><strong>녹화 화질:</strong> <span>전후방 QHD. Auto 나이트 비전 적용으로 조도에 따라 자동으로 밝기 최적화.</span></li>
                <li><strong>모바일 연동:</strong> <span>5GHz 고속 Wi-Fi 지원으로 스마트폰 다이렉트 연결 및 SNS 영상 공유 용이.</span></li>
                <li><strong>A/S 및 리뷰:</strong> <span>1.5초 초고속 부팅과 초저전력 주차 녹화(최장 7개월 대기) 기능으로 실용성 리뷰 최상. 2년 무상 A/S 정책 및 탄탄한 장착점 연계.</span></li>
            </ul>
            <a href="https://search.shopping.naver.com/search/all?query=파인뷰+LXQ600+POWER" class="btn" target="_blank">상세 정보 및 가격 확인</a>
        </div>
    </div>
</body>
</html>
"""

# Streamlit 화면에 바로 렌더링 (스크롤 및 높이 넉넉하게 설정)
components.html(html_code, height=1200, scrolling=True)
