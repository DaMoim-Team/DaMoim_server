import mysql.connector
from config_DB import Config_DB

#데이터베이스 연결, count 초기화 기능

# 데이터베이스 연결 함수
def create_db_connection():
    connection = mysql.connector.connect(
        host=Config_DB.HOST,
        port=Config_DB.PORT,
        user=Config_DB.USER,
        password=Config_DB.PASSWORD,
        database=Config_DB.DATABASE
    )

    return connection

# 데이터베이스 연결 종료 함수
def close_db_connection(connection, cursor):
    cursor.close()
    connection.close()


#데이터베이스 연결
def get_data_from_database():
    connection = create_db_connection()
    cursor = connection.cursor()

    #locations 테이블 데이터 가져오기
    cursor.execute("SELECT * FROM locations")
    data_locations = cursor.fetchall()

    #timeranking 테이블 데이터 가져오기
    cursor.execute("SELECT * FROM timeranking")
    data_timeranking = cursor.fetchall()
    
    # 연결 및 커서 닫기
    close_db_connection(connection, cursor)

    #locaitons 딕셔너리 형태로 만들기
    data_dicts_locations = []
    for row in data_locations:
        data_dict = {
            "id": row[0],
            "cctv_id": row[1],
            "count_catch": row[2],
            "count_cleanup": row[3],
            "latitude": float(row[4]),
            "longitude": float(row[5])
        }
        data_dicts_locations.append(data_dict)

    #timeranking 딕셔너리 형태로 만들기기
    data_dicts_timeranking = []
    for row in data_timeranking:
        data_dict = {
            "time_range": row[0],
            "most": row[1],
            "top_count": row[2]
        }
        data_dicts_timeranking.append(data_dict)

    #리턴
    return data_dicts_locations, data_dicts_timeranking


#count_cleanup 직접 초기화
def reset_count_cleanup(selected_topics):
    connection = create_db_connection()
    cursor = connection.cursor()

    for topic in selected_topics:
        # 테이블 수정 쿼리문 작성 및 실행
        sql_query = f"UPDATE locations SET count_cleanup = 0 WHERE cctv_id = '{topic}'"
        cursor.execute(sql_query)

    # 변경사항 커밋
    connection.commit()

    # 커서 닫기 및 연결 종료
    close_db_connection(connection, cursor)

#count_catch 자동 초기화
def reset_count_catch():
    connection = create_db_connection()
    cursor = connection.cursor()

    # 테이블 수정 쿼리문 작성 및 실행
    sql_query = "UPDATE locations SET count_catch = 0"
    cursor.execute(sql_query)

    # 변경사항 커밋, 커서 닫기 및 연결 종료
    connection.commit()
    close_db_connection(connection, cursor)

    print("count_catch has been reset.")
