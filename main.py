import requests
import time

url = "https://advert-app.com/rocket/seenAd/5609089582"

while True:
    try:
        response = requests.get(url, timeout=1)
        print(f"Запрос: Статус-код {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    time.sleep(3)  # Пауза в 1 секунду между запросами
