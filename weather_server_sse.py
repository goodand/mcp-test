# 클라우드 배포용 서버 코드 (SSE 지원)
# weather_server_sse.py

import os
from mcp.server.fastmcp import FastMCP

# 1. 호스트와 포트 지정 (클라우드 환경 대응)
# 클라우드(Render 등)는 PORT 환경변수로 포트를 지정해줍니다.
port = int(os.environ.get("PORT", 8000))
mcp = FastMCP("Weather Server SSE", host="0.0.0.0", port=port)

# ... (기존 Tools/Resources 코드는 단순화를 위해 생략하거나 필요시 추가) ...
# 데모를 위해 기본 데이터만 포함합니다.

WEATHER_DATA = {
    "서울": {"temp": 15, "condition": "맑음", "humidity": 45},
    "부산": {"temp": 18, "condition": "흐림", "humidity": 60},
    "제주": {"temp": 20, "condition": "비", "humidity": 80},
}

@mcp.tool()
def get_weather(city: str) -> dict:
    """도시의 날씨 정보를 조회합니다"""
    return WEATHER_DATA.get(city, {"error": "Not found"})

if __name__ == "__main__":
    # 2. 실행 모드를 'sse'로 설정
    print(f"Starting SSE server on port {port}...")
    mcp.run(transport="sse")
