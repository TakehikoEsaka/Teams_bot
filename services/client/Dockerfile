FROM node:14.5-alpine

WORKDIR /app

RUN apk update && \
    yarn global add @vue/cli

# COPY package.json ./

RUN yarn install

COPY . .

# Production
# RUN npm install -g http-server
# RUN ROOT_API=http://localhost:5011 npm run build
# CMD [ "http-server", "dist" ]

# Development 
# CMD [ "npm", "run", "dev"]
# serve打てない時はvue-cli入っているかpackage.json要確認
CMD ["yarn", "serve"]