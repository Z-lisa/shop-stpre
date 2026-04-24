# 书店商城 - 前后端一体化 Dockerfile
# 一个容器同时启动前端和后端

# 例如
FROM python:3.11-slim

WORKDIR /app

RUN sed -i 's|http://deb.debian.org|https://mirrors.aliyun.com|g' /etc/apt/sources.list.d/debian.sources && \
    apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/uploads

RUN npm config set registry https://registry.npmmirror.com

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

RUN npm install -g serve

COPY backend/requirements.txt ./backend/
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --no-cache-dir -r backend/requirements.txt

COPY backend/app/ ./app/
COPY backend/init_db.py ./

ENV PYTHONPATH=/app
ENV APP_ENV=production
ENV DATABASE_URL=sqlite:///./book_shop.db
ENV UPLOAD_DIR=/app/uploads

EXPOSE 3000 8000

CMD sh -c "python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 & serve -s dist -l 3000"
