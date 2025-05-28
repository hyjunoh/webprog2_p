import requests

SERVER_URL = 'http://220.149.232.226:10017/'

def get_data_from_server():
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            print("서버로부터 성공적으로 응답을 받았습니다.")
            print("------------------------------------")
            print("응답 내용 (Content):")
            print(response.text)
            print("------------------------------------")
        else:
            print(f"요청 실패: 서버가 상태 코드 {response.status_code}를 반환했습니다.")
            print(f"응답 내용: {response.text}")
    except requests.exceptions.ConnectionError:
        print(f"연결 실패: {SERVER_URL} 에 접속할 수 없습니다.")
        print("app_01.py 서버가 실행 중인지 확인해주세요.")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")

if __name__ == '__main__':
    print(f"{SERVER_URL} 에 접속을 시도합니다...")
    get_data_from_server()
