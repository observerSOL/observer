<p align="center">
  <img src="https://i.ibb.co/9H44Ns3L/68747470733a2f2f692e696d6775722e636f6d2f494b797a5136542e706e67.png" width="180">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/aimclub/open-source-ops/43bb283758b43d75ec1df0a6bb4ae3eb20066323/badges/ITMO_badge_rus.svg">
  <img src="https://camo.githubusercontent.com/5d2a77363705f731c82a241eed1d9238bea2f5922ebf54e4db25e1a36fc84f5b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c616e672d72752d7265642e737667">
</p>
<p align="center">
  <img src="https://i.pinimg.com/736x/d7/2c/59/d72c59c8b66c325973d85a6e1527f294.jpg" width="180">
</p>

<h1 align="center"> Observer Bot</h1>

<p align="center">
  Анализ безопасности транзакций в сети Solana через Telegram
</p>

<p align="center">
  <a href="https://t.me/observerprojectbot">Открыть бота</a>
</p>

---

## Description

**Observer Bot** — инструмент для анализа транзакций в сети Solana.

Бот позволяет быстро проверить транзакцию по Signature и выявить потенциально опасные действия без необходимости вручную анализировать блокчейн-данные.

---

## Features

- Анализ транзакций по Signature  
- Получение данных через Solana RPC  
- Оценка риска (LOW / MEDIUM / HIGH)  
- Анализ логов транзакции  

---

## Usage

1. Откройте Telegram-бота  
   https://t.me/observerprojectbot  

2. Выполните команду:

    `/start`

3. Отправьте Signature:

    `5h6xBEauJ3PK6exampleSignature`

4. Получите результат:

    🛡 Отчет безопасности  
    Риск: MEDIUM 🟡  
    Баллы: 2  

---

## Risk Levels

    LOW    - угроз не обнаружено  
    MEDIUM - есть подозрительные действия  
    HIGH   - высокий риск  

---

## Installation

Клонирование:

    git clone https://github.com/mrnftsol2011/observer.git
    cd observer

Установка зависимостей:

    pip install -r requirements.txt

---

## Configuration

Создайте файл `.env`:

    BOT_TOKEN=your_telegram_bot_token
    RPC_URL=https://api.mainnet-beta.solana.com

---

## Run

Запуск:

    python src/main.py

---

## Example

Вход:

    Signature:
    3v9Kpexample123

Выход:

    🛡 Отчет безопасности  
    Риск: HIGH 🔴  
    Баллы: 5  

---

## Architecture

    src/main.py              - Telegram-бот  
    src/engine/analyzer.py   - анализ транзакций  

---

## Requirements

    Python 3.10+
    aiogram
    solana-rpc
---

---

## 📬 Contacts

Если у вас возникли вопросы или предложения, вы можете связаться с автором проекта:

**Yuriychak Semyon**  
✉️ Email: [yuriychak_semyon@mail.ru](mailto:yuriychak_semyon@mail.ru)
