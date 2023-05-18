import requests
from database import get_data_from_database
from naver_api import get_route

#최적 경로 도출

#최근접 이웃 알고리즘으로 이동 경로 최소화하는 함수
def nearest_neighbor(start_latitude, start_longitude, locations):
    visited = set()
    optimal_route = []
    current_latitude, current_longitude = start_latitude, start_longitude

    #방문한 위치는 visited에 추가, 최단 거리 위치는 optimal_route 리스트에 추가
    while len(visited) < len(locations):
        min_distance = float('inf')
        next_location = None

        for location in locations:
            if location['cctv_id'] not in visited:
                distance = get_distance(current_latitude, current_longitude, location["latitude"], location["longitude"])

                # 거리가 None이 아니고, 현재 최소 거리보다 작은 경우에만 최소 거리를 업데이트
                if distance is not None and distance < min_distance:
                    min_distance = distance
                    nearest_location = location

        if nearest_location is not None:
            visited.add(nearest_location['cctv_id'])
            optimal_route.append(nearest_location)

            current_latitude, current_longitude = nearest_location["latitude"], nearest_location["longitude"]

    return optimal_route


#두 지점 사이의 거리를 계산하는 함수
def get_distance(start_lat, start_lng, end_lat, end_lng):
    route_data = get_route(start_lat, start_lng, end_lat, end_lng)

    #반환되는 거리값은 미터 단위
    if route_data.get("code") == 0:
        distance = route_data['route']['traoptimal'][0]['summary']['distance']
        return distance
    else:
        return None

#최적 경로를 계산하고 리턴
def get_optimal_route_coordinates(start_latitude, start_longitude):
    #데이터베이스에서 위경도 값 가져옴
    locations_data, _  = get_data_from_database()

    #nearest_neighbor 함수로 최적 경로 도출
    optimal_route = nearest_neighbor(start_latitude, start_longitude, locations_data)
    print("Optimal route:", optimal_route)

    optimal_route_coordinates = []

    #출발지 데이터
    start_location = {
            'cctv_id': 'start',
            'latitude': start_latitude,
            'longitude': start_longitude,
            'count_catch': 0,
            'count_cleanup': 0,
    }
    #최적 경로 리턴값에 출발지 추가
    optimal_route_coordinates.append(start_location)

    #최적 경로 인덱스에 맞춰서 기존 데이터셋 형태로 변경
    for location in optimal_route:
        coordinates = {
                'cctv_id': location["cctv_id"],
                'latitude': location["latitude"],
                'longitude': location["longitude"],
                'count_catch': location["count_catch"],
                'count_cleanup': location["count_cleanup"],
        }

        #최적 경로 리턴값에 최적 경로 데이터 추가
        optimal_route_coordinates.append(coordinates)

    print("Optimal route coordinates ok")

    #출발지+최적 경로 리턴
    return optimal_route_coordinates
