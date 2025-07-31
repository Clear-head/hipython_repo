import pymysql

# MySQL 연결 설정
connection = pymysql.connect(
    host='localhost',  # 도커 컨테이너가 로컬에서 실행 중이므로 localhost
    port=3307,         # 도커 실행 시 매핑한 포트 (3307:3306)
    user='root',       # MySQL 사용자 이름
    password='1234',   # 도커 실행 시 설정한 루트 비밀번호
    database='mysql'   # 기본 데이터베이스 (없으면 생성한 데이터베이스 이름)
)

try:
    # 커서 생성
    with connection.cursor() as cursor:
        # SQL 쿼리 실행
        cursor.execute("SELECT VERSION()")
        # 결과 가져오기
        result = cursor.fetchone()
        print(f"MySQL 버전: {result[0]}")
        
        # 데이터베이스 목록 조회
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("데이터베이스 목록:")
        for db in databases:
            print(f"- {db[0]}")
            
finally:
    # 연결 종료
    connection.close()
