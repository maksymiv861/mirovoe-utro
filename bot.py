  ```python
     import os
     from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
     from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

     # Define callback data for the main menu and submenu options
     MENU, DATE_SELECTION = range(2)

     # Define main menu options
     main_menu_buttons = [
         [InlineKeyboardButton("Лучшие моменты", callback_data='highlights')],
         [InlineKeyboardButton("Розыгрыши и подарки", callback_data='giveaways')],
         [InlineKeyboardButton("Гости и интервью", callback_data='guests')],
         [InlineKeyboardButton("Гороскоп", callback_data='horoscope')]
     ]

     # Define submenu options with dates (example dates)
     date_buttons = [
         [InlineKeyboardButton("2024-07-28", callback_data='2024-07-28')],
         [InlineKeyboardButton("2024-07-29", callback_data='2024-07-29')],
         [InlineKeyboardButton("2024-07-30", callback_data='2024-07-30')],
         [InlineKeyboardButton("Назад", callback_data='back')]
     ]

     def start(update: Update, context: CallbackContext) -> None:
         """Send a message with four inline buttons attached."""
         keyboard = main_menu_buttons
         reply_markup = InlineKeyboardMarkup(keyboard)
         update.message.reply_text('Добро пожаловать на утреннее шоу "Мировое утро"! Выберите категорию:', reply_markup=reply_markup)

     def button(update: Update, context: CallbackContext) -> None:
         """Handle button press events."""
         query = update.callback_query
         query.answer()
         
         if query.data == 'back':
             keyboard = main_menu_buttons
             query.edit_message_text('Выберите категорию:', reply_markup=InlineKeyboardMarkup(keyboard))
         elif query.data in ['highlights', 'giveaways', 'guests', 'horoscope']:
             # Here we simulate date selection menu
             context.user_data['category'] = query.data
             keyboard = date_buttons
             query.edit_message_text('Выберите дату:', reply_markup=InlineKeyboardMarkup(keyboard))
         elif query.data in ['2024-07-28', '2024-07-29', '2024-07-30']:
             # Simulate sending audio or video file
             send_media(query.data, query, context)
         else:
             query.edit_message_text("Неизвестная команда")

     def send_media(date: str, query, context: CallbackContext) -> None:
         """Send an audio or video file based on the date and category selected."""
         category = context.user_data.get('category', 'highlights')
         
         # Placeholder logic to send a file
         if category == 'highlights':
             query.edit_message_text(f'Отправляю лучшие моменты за {date}')
             # context.bot.send_audio(chat_id=query.message.chat_id, audio=open('path_to_audio.mp3', 'rb'))
         elif category == 'giveaways':
             query.edit_message_text(f'Отправляю информацию о розыгрышах и подарках за {date}')
             # context.bot.send_audio(chat_id=query.message.chat_id, audio=open('path_to_audio.mp3', 'rb'))
         elif category == 'guests':
             query.edit_message_text(f'Отправляю гости и интервью за {date}')
             # context.bot.send_video(chat_id=query.message.chat_id, video=open('path_to_video.mp4', 'rb'))
         elif category == 'horoscope':
             query.edit_message_text(f'Отправляю гороскоп за {date}')
             # context.bot.send_audio(chat_id=query.message.chat_id, audio=open('path_to_audio.mp3', 'rb'))

     def main() -> None:
         """Run the bot."""
         token = "6997178327:AAFa2n18AoJGL0IjmULZbfkayRdJV0FW81Y"
         updater = Updater(token)
         
         updater.dispatcher.add_handler(CommandHandler('start', start))
         updater.dispatcher.add_handler(CallbackQueryHandler(button))
         
         updater.start_polling()
         updater.idle()

     if __name__ == '__main__':
         main()
     ```
