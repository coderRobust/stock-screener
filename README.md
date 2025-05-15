# Stock Market Screener & Alert System

A FastAPI-based screener to fetch top stock performers with scheduled alerts using Celery and Redis.

## Features
- Real-time stock fetching using Yahoo Finance
- FastAPI endpoint for top tickers
- Scheduled tasks via Celery for daily alerts
- MongoDB integration for persistence
- Chart generation via Matplotlib

## Run Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Run the API

uvicorn api.main:app --reload

3.Start Redis server (if not running)
 redis-server

4.Run Celery worker
 celery -A tasks.celery_tasks worker --loglevel=info
