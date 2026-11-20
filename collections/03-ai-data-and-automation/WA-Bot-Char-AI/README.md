# WhatsApp Bot (Auto Chat AI)

This WhatsApp bot integrates AI from **Character.AI** for auto chatting. It supports both private and group chats, using mentions as a prefix for group conversations.

## Features
- AI powered by [Character.AI](https://character.ai)
- Supports private & group chats
- Rest API: [https://api.maelyn.tech](https://api.maelyn.tech)

## Installation
```bash
$ apt update && apt upgrade -y
$ apt install nodejs git
$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
$ source ~/.nvm/nvm.sh
$ nvm install 20
$ nvm use 20
$ node -v
$ git clone https://github.com/lamberthrumpaidus/WA-Bot-Char-AI.git
$ cd WA-Bot-Char-AI
$ npm install
$ npm install pm2
$ node . # Get session
$ ctrl + c
$ pm2 start index.js --name bot
```

## Authors
[lamberthrumpaidus](https://github.com/lamberthrumpaidus)
