FROM node:latest

WORKDIR /usr/app

COPY package*.json ./
COPY yarn.lock ./

RUN yarn

COPY . .

EXPOSE 3000

CMD ["npm", "start"]