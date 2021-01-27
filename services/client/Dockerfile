FROM node:13.7.0-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

# RUN npm update vue-template-compiler

COPY . .

RUN ROOT_API=http://localhost:5011 npm run build

EXPOSE 8080

CMD [ "http-server", "dist" ]
