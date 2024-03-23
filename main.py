from fastapi import FastAPI
from database import create_tables,delete_tables
from contextlib import asynccontextmanager
from router import router as tasks_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print('база очищена')
    await create_tables()
    print('база готова')
    yield
    # Clean up the ML models and release the resources
    print('Выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
