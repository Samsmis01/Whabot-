
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token
TOKEN = "7561812092:AAEAKm4zOgUPTy5qnE3tiSyJ06cie9fHC-c"

# Start function to send a welcome message
async def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    logger.info(f"User {username} with ID {user_id} started the bot.")

    welcome_text = """
    🔰 Bienvenue ! Je suis un bot🤖 programmé par Brother_Sam pour exécuter ces tâches automatiquement pour lui 🌹. Voici les options suivantes⬇️
    ------------------------------------------------
    ➡️ Contactme📩
    ➡️ Rejoins-nous sur WhatsApp📩
    ➡️ Follow me on Instagram📸
    ➡️ Follow me on Twitter (X)🐦
    ➡️ add me👻💌
    -------------------------------------------------
    🛃 Avant d'utiliser ce bot, après avoir complété toutes les tâches, cliquez sur ✅ Jᴏɪɴᴇᴅ!
    """

    # Create buttons
    keyboard = [
        [InlineKeyboardButton("➡️ Contact me", url="https://wa.me/0846005684")],
        [InlineKeyboardButton("➡️ Rejoins-nous sur WhatsApp", url="https://chat.whatsapp.com/DngmyuX5dzY1uCvdUvThKl")],
        [InlineKeyboardButton("➡️ Follow me on Instagram", url="https://www.instagram.com/samsmis01/")],
        [InlineKeyboardButton("➡️ Follow me on Twitter (X)", url="https://x.com/HARMONIE0994?t=Iuy4b3b2NPH66eqXvP9z2w&s=09")],
        [InlineKeyboardButton("➡️ Add me", url="https://www.facebook.com/profile.php?id=100076495286591")],
        [InlineKeyboardButton("✅ cliquez ici 🌻!", callback_data="joined")]
    ]

    # Attach keyboard to buttons
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Handler for "✅ cliquez ici !" button response
async def joined_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Merci d'avoir rejoint tous les groupes et chaînes ! 🎉 Vous pouvez maintenant démarrer une discussion avec mon maître Brother_Sam👻 soyez cool envers lui😉.")

# Main function to start the bot
def main():
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(joined_callback))

    # Start polling (blocking call)
    application.run_polling()

if __name__ == '__main__':
    main()
