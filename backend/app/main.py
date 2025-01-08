import webbrowser
import uvicorn
from fastapi import FastAPI
from .core.config import settings
from .api.main import api_router

app = FastAPI(title=settings.PROJECT_NAME,
              )

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import threading

    def run():
        uvicorn.run(app, host="127.0.0.1", port=8000)

    threading.Thread(target=run).start()
    webbrowser.open("http://127.0.0.1:8000/docs")