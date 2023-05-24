import schedule
import time
from flask import Flask, request, jsonify
from datetime import datetime

from route import get_optimal_route_coordinates
from database import get_data_from_database, reset_count_cleanup, reset_count_catch

app = Flask(__name__)

@app.route('/data', methods=['GET'])
#최적 경로를 JSON 형식으로 반환
def get_locations():
    #출발지  위경도 
    start_latitude = 37.54804
    start_longitude = 127.03984 

    optimal_route_coordinates = get_optimal_route_coordinates(start_latitude, start_longitude)

    result = {
            'optimal_route': optimal_route_coordinates,
    }

    return jsonify(result)

@app.route('/timeranking', methods=['GET'])
#timeranking 데이터를 JSON 형식으로 반환 
def get_timeranking():
    _, timeranking_data = get_data_from_database()

    result = {
            'timeranking_data': timeranking_data
    }
    return jsonify(result)

@app.route('/update_topics', methods=['POST'])
#데이터베이스 count_cleanup 초기화 함수
def update_topics():
    #전달 받은 선택된 토픽들 저장
    data = request.get_json()
    selected_topics = data['selectedTopics']

    #선택된 토픽들 초기화 업데이트
    reset_count_cleanup(selected_topics)

    #성공 메세지 리턴
    return jsonify({"status": "success", "message": "Topics updated successfully"})

#무한 루프를 돌면서, schedule 라이브러리를 이용해 예약된 작업 수행
def run_scheduled_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)

#정해진 시간마다 데이터베이스 count_catch 초기화 
schedule.every().day.at("18:10:00").do(reset_count_catch)

# 스케줄된 작업을 실행할 별도의 스레드를 생성
import threading
task_thread = threading.Thread(target=run_scheduled_tasks)
task_thread.start()
print("----Task thread 시작----")


if __name__ == '__main__':
    app.run('0.0.0.0', port=1105, debug=True)
