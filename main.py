import requests
import time

user_id = input("Введи tg user id: ")
url = f"https://advert-app.com/rocket/seenAd/{user_id}"

while True:
    try:
        response = requests.get(url, timeout=1)
        print(f"Запрос: Статус-код {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    time.sleep(3)  # Пауза в 1 секунду между запросами
