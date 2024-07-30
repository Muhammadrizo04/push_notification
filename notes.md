uvicorn push_notification.asgi:application --host 0.0.0.0 --port 8000 --workers 4 --log-level debug --reload
uvicorn push_notification.asgi:application --port 8000 --workers 4 --log-level debug --reload
