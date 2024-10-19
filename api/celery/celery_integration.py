import uvicorn
from celery import AsyncResult
import celery
from fastapi import FastAPI

app = FastAPI()


@app.post("/task/")
def run_task(x: int, y: int):
    task = celery.send_task("add", args=[x, y])
    return {"task_id": task.id}


@app.get("/task/{task_id}")
def get_task_result(task_id: str):
    result = AsyncResult(task_id, app=celery)
    if result.state == "SUCCESS":
        return {"status": "SUCCESS", "result": result.result}
    return {"status": result.state}


if __name__ == "__main__":
    uvicorn.run("celery_integration:app", host="127.0.0.1", port=8000, reload=True)
