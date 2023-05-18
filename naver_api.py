from config import Config
import requests

#네이버 지도 API로 경로 정보 가져오는 함수
def get_route(start_lat, start_lng, end_lat, end_lng):
    #naver map api 
    naver_client_id = Config.NAVER_CLIENT_ID
    naver_client_secret = Config.NAVER_CLIENT_SECRET

    headers = {
        "X-NCP-APIGW-API-KEY-ID": naver_client_id,
        "X-NCP-APIGW-API-KEY": naver_client_secret
    }

    params = {
        "start": f"{start_lng},{start_lat}",
        "goal": f"{end_lng},{end_lat}"
    }

    response = requests.get(Config.NAVER_OPEN_API, headers=headers, params=params)
    return response.json()
