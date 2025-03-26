# Python Telegram Bot on Vercel

A production-ready Telegram bot running on Vercel's serverless infrastructure. Built with Django and python-telegram-bot.

## Features

- 🚀 Serverless deployment on Vercel
- 🔒 Secure webhook handling
- 📝 Comprehensive error handling and logging
- ⚡ Fast response times
- 🔄 Automatic webhook setup

## Available Commands

- `/start` - Start the bot and get a welcome message
- `/help` - Show available commands
- `/echo <text>` - Echo back your message
- `/status` - Check bot status

## One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fasonmotivation%2Ftelegram-bot-vercel-python&env=TOKEN&envDescription=Telegram%20Bot%20Token&envLink=https%3A%2F%2Fcore.telegram.org%2Fbots%23creating-a-new-bot&envValue=7970579536:AAHOWQDir-ule9h5WxP2UagXFAL3AlON9UY)

## Manual Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```
   TOKEN=your_telegram_bot_token
   webhook=https://your-vercel-url.vercel.app/webhook
   ```
4. Deploy to Vercel:
   ```bash
   vercel
   ```
5. Set up the webhook:
   ```
   https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://your-vercel-url.vercel.app/webhook
   ```

## Environment Variables

- `TOKEN` - Your Telegram Bot Token (required)
- `webhook` - Your Vercel deployment URL (required)
- `PYTHONUNBUFFERED` - Set to "1" for better logging

## Notes

- Environment variable names are case-sensitive
- The webhook URL must end with `/webhook`
- Make sure your bot token is kept secure
- The bot uses Python 3.10 runtime on Vercel

## Error Handling

The bot includes comprehensive error handling:
- Logs all errors with stack traces
- Sends user-friendly error messages
- Maintains webhook connection
- Handles malformed requests

## Contributing

Feel free to submit issues and enhancement requests!

