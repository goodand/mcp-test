# 서버 코드 예시 - 이 코드를 weather_server.py로 저장
# weather_server.py

from mcp.server.fastmcp import FastMCP

# 서버 인스턴스 생성
mcp = FastMCP("Weather Server", json_response=True)

# 날씨 데이터 (실제로는 API 호출)
WEATHER_DATA = {
    "서울": {"temp": 15, "condition": "맑음", "humidity": 45},
    "부산": {"temp": 18, "condition": "흐림", "humidity": 60},
    "제주": {"temp": 20, "condition": "비", "humidity": 80},
}

@mcp.tool()
def get_weather(city: str) -> dict:
    """도시의 날씨 정보를 조회합니다"""
    if city in WEATHER_DATA:
        return WEATHER_DATA[city]
    return {"error": f"{city}의 날씨 정보를 찾을 수 없습니다"}

@mcp.tool()
def get_temperature(city: str) -> str:
    """도시의 온도를 조회합니다"""
    if city in WEATHER_DATA:
        return f"{city}의 현재 온도: {WEATHER_DATA[city]['temp']}°C"
    return f"{city}의 온도 정보를 찾을 수 없습니다"

@mcp.resource("weather://{city}")
def weather_resource(city: str) -> str:
    """날씨 리소스를 반환합니다"""
    import json
    if city in WEATHER_DATA:
        return json.dumps(WEATHER_DATA[city], ensure_ascii=False)
    return json.dumps({"error": "not found"})

@mcp.prompt()
def weather_report(city: str) -> str:
    """날씨 보고서 프롬프트를 생성합니다"""
    return f"""다음 도시의 날씨 정보를 분석하고 오늘의 활동 추천을 해주세요:

도시: {city}

분석 내용:
1. 현재 날씨 상태
2. 실외 활동 적합성
3. 준비물 추천"""

if __name__ == "__main__":
    """
    stdio 모드로 실행 (기본)
    """
    mcp.run()
