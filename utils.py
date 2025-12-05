import requests
import datetime
from zoneinfo import ZoneInfo  # Python 3.9 이상 필요

def get_online_time():
    try:
        response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Seoul', timeout=5)
        if response.status_code == 200:
            data = response.json()
            local_datetime_str = data['datetime']
            return datetime.datetime.fromisoformat(local_datetime_str)
        else:
            raise Exception("시간 서버 응답 오류")
    except Exception as e:
        print(f"온라인 시간 가져오기 실패: {e}")
        return None