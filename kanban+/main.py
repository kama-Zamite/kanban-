from fastapi import FastAPI

app = FastAPI(title='kanbanAPI')


@app.get('/')
def home():
    return {'msg': 'bem-vindo ao kanbanAPI'}
