from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title='Code Execution Assignment'
)


if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=9500, reload=True)


