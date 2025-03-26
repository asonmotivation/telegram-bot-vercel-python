import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from os import getenv
import json

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}! 👋\n\n"
        "I'm your Telegram bot running on Vercel!\n"
        "Use /help to see available commands."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/echo <text> - Echo back your message\n"
        "/status - Check bot status"
    )
    await update.message.reply_text(help_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check bot status."""
    await update.message.reply_text("✅ Bot is running normally!")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors."""
    logger.error(f"Update {update} caused error: {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "Sorry, something went wrong. Please try again later."
        )

async def bot_tele(text):
    """Main bot function to handle incoming updates."""
    try:
        # Create application
        application = (
            Application.builder()
            .token(getenv("TOKEN"))
            .build()
        )

        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help))
        application.add_handler(CommandHandler("echo", echo))
        application.add_handler(CommandHandler("status", status))
        
        # Add error handler
        application.add_error_handler(error_handler)

        # Set webhook
        webhook_url = getenv("webhook")
        if webhook_url:
            await application.bot.set_webhook(url=webhook_url)
            logger.info(f"Webhook set to {webhook_url}")

        # Process the update
        if text:
            await application.update_queue.put(
                Update.de_json(data=json.loads(text), bot=application.bot)
            )

        # Start application
        async with application:
            await application.start()
            await application.stop()

    except Exception as e:
        logger.error(f"Error in bot_tele: {str(e)}")
        raise