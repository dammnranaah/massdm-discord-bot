# 📬 MassDM Bot

MassDM is a simple Discord bot that allows server administrators to **send a direct message (DM) to all members** in a server.
It’s lightweight, easy to use, and includes basic error handling to avoid crashing when a DM fails.

> ⚠️ **Warning:** Use responsibly. Sending unsolicited DMs can violate Discord’s Terms of Service and may get your bot or server penalized.

---

## ✨ Features

* Mass DM all members in a server.
* Skips bots automatically.
* Sends messages safely with a delay to reduce rate-limiting issues.
* Basic permission check: Only administrators can send mass messages.
* Handles exceptions if a message fails to send.

---

## 📦 Commands

### `!massdm <message>`

* Sends a DM containing `<message>` to all members in the server (excluding bots).
* Only usable by users with administrator permissions.

Example usage:

```
!massdm Hello everyone! Don't forget our event tonight.
```

---

## ⚙️ Setup

1. **Clone or download the bot code**

```bash
git clone https://github.com/yourusername/massdm-bot.git
cd massdm-bot
```

2. **Install dependencies**

```bash
pip install discord.py asyncio
```

3. **Add your bot token** in the code:

```python
bot.run('YOUR_BOT_TOKEN')
```

4. **Run the bot**

```bash
python bot.py
```

---

## ⚡ How it Works

* The bot logs in using your bot token.
* When a server administrator uses `!massdm <message>`, the bot loops through all members and sends the DM individually.
* It automatically skips bots and the bot itself.
* A small delay (`asyncio.sleep(1)`) helps prevent hitting Discord’s rate limits.

---

## 🛡️ Permissions

* The command checks if the user has **administrator permissions**.
* Only admins can use `!massdm` to prevent abuse.

---
