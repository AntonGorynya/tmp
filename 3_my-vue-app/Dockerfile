FROM node:22-bullseye-slim as frontend
WORKDIR /usr/app/frontend
COPY . .
RUN npm install
EXPOSE 5173
RUN npm run dev