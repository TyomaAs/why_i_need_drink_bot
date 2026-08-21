import sys


# Require Python 3.10+ because python-telegram-bot uses modern typing features
if sys.version_info < (3, 10):
    raise ImportError(
        "python-telegram-bot requires Python 3.10+. "
        "Select a newer interpreter in VS Code or run the script with Python 3.11."
    )

try:
    from telegram import Update, ReplyKeyboardMarkup, BotCommand  # type: ignore[import]
    from telegram.ext import (  # type: ignore[import]
        ApplicationBuilder,
        CommandHandler,
        MessageHandler,
        ContextTypes,
        filters,
    )
except ImportError as e:
    raise ImportError(
        "Missing dependency: python-telegram-bot is required. "
        "Install it with `pip install python-telegram-bot` or select an interpreter that has it installed."
    ) from e

__all__ = [
    "Update",
    "ReplyKeyboardMarkup",
    "BotCommand",
    "ApplicationBuilder",
    "CommandHandler",
    "MessageHandler",
    "ContextTypes",
    "filters",
]
