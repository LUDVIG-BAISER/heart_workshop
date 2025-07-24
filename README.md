1) Скачать репозиторий на комьютер.

    git clone https://github.com/https://github.com/LUDVIG-BAISER/heart_workshop.git

2) Перейти в папку с проектом

   cd heart_workshop

4) В папке с проектом активировать виртуальное окружение.
   
   source .venv/bin/activate          # для Linux/macOS
   
   .venv\Scripts\activate               # для Windows

5) Установить зависимости

   pip install -r requirements.txt

6) Активировать FastAPI сервер.

     uvicorn app.main:app --reload

Будет доступен пользовательсий интерфейс для ввода данных и получения предсказания:

Адрес сервера: http://127.0.0.1:8000 или http://localhost:8000

Документация : http://127.0.0.1:8000/docs

ВНИМАНИЕ! Данный сервис не предназначен для получения реальных предсказаний о состоянии здоровья!

ЭТО ВСЕГО ЛИШЬ ДЕМОНСТРАЦИЯ ПРОЕКТА! 
<img width="1269" height="822" alt="image" src="https://github.com/user-attachments/assets/e6dc6a47-3319-499e-9cb1-eaa25b2550d1" />


7) Либо воспользоваться скриптом для получения предсказания

   python prediction.py --input heart_test.csv

   
