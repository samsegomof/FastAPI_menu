from fastapi import FastAPI
import uvicorn

app = FastAPI(debug=True)


@app.get('/')
def main_page():
    return {'API': 'Simple menu API'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
