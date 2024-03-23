from python: 3.12-slim
COPY . .
RUN pip install -r fastapi.txt
cmd ['uvicorn','main:app','--host','0.0.0.0','--port','80']