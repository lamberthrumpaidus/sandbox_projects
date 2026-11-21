# Bot WhatsApp berbasis AI

Contoh integrasi percakapan WhatsApp dengan layanan AI.

[Profil utama](https://github.com/lamberthrumpaidus/lamberthrumpaidus) · [Indeks proyek](../../../README.md)

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
Lamberth Rumpaidus
