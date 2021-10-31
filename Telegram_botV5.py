import telegram
import telegram.ext
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.callbackqueryhandler import CallbackQueryHandler
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.filters import Filters
from telegram.ext.messagehandler import MessageHandler
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.update import Update
from BOT_MESSAGE_CHECK import message_check, query_check 
import Telegram_reply_texts as texts
from ast import literal_eval
from json import dumps
from time import sleep
import logging


logging.basicConfig(filename="bot_log_file.log", level=logging.INFO,
format="%(asctime)s-%(levelname)s-%(message)s", encoding="utf-8")

token = open("api_token.txt", "r").read()

bot =  telegram.Bot(token)

updater = telegram.ext.Updater(token, use_context=True, workers=10, request_kwargs={'read_timeout': 2, 'connect_timeout': 2})

disp = updater.dispatcher

def KeyboardMarkup(*args, one_time_keyboard=False):
    kb = []
    x = 0

    while x < len(args):
            
        kb.append([telegram.KeyboardButton(args[x])])
        x += 1
    
    kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True, one_time_keyboard=one_time_keyboard)

    return kb_markup

def file_manager(fileName, fileID):

    file_dict = {}
    fileName = fileName
    fileID = fileID
    file_dict.update({fileName : fileID})

    dict = open("FileResults.txt", mode='r', encoding="utf-8")
    dict = dict.read()
    dict = str(dict).split('\n')
    dict = list(dict)
    i = True

    
    for line in dict :
        
        try:
            line = literal_eval(line)
        except SyntaxError:
            pass
        
        for key1 in line:
            pass
            for key2 in file_dict:
                pass
                if  key1 == key2:
                    i = False
                    break
            
            if not i:
                break
        if not i:
            break

    if i :
            with open("FileResults.txt", "a", encoding="utf-8") as file:
                
                file.write(dumps(file_dict) + "\n", )
                file.close()

def search_files(usr_message):

    usr_message = str(usr_message)

    file = open("FileResults.txt", encoding="utf-8").read()
    file = list(str(file).split("\n"))

    for line in file:

        try:
            line = literal_eval(line)
        except SyntaxError:
            pass
        for key in line:
            
            if key == usr_message:
                return line[key]

def start(update:Update, context:CallbackContext):

    logging.info(f"[+]{update.message.from_user.first_name} {update.message.from_user.last_name} (@{update.message.from_user.username}) SENT A MESSAGE ({update.message.text})")

    button = [[InlineKeyboardButton("مساعده 🔍", callback_data="help")]]

    bot.sendMessage(chat_id=update.effective_chat.id, parse_mode="HTML", timeout=5,
    text=texts.start, reply_markup=InlineKeyboardMarkup(button))

def help(update:Update, context:CallbackContext):

    logging.info(f"[+]{update.message.from_user.first_name} {update.message.from_user.last_name} (@{update.message.from_user.username}) SENT A MESSAGE ({update.message.text})")

    buttons = [[InlineKeyboardButton("الموقع 🌐", url=texts.Website_lnk)],
        [InlineKeyboardButton("قائمة المسؤولين 👤", callback_data="admin"),
         InlineKeyboardButton("الاقسام 📁", callback_data="departments")]]

    bot.sendMessage(chat_id=update.effective_chat.id, parse_mode="HTML", timeout=5,
        reply_markup=InlineKeyboardMarkup(buttons), text=f"<b>مرحبا {update.effective_chat.first_name}❕ 👋\n\n🔸 هذه قائمة المساعده 🔍 ، انقر على احدى الخيارات:</b>\n\n\n<b>🔹 الموقع</b> ➖> <u>الموقع الرسمي لكلية الهندسة جامعة عمر المختار</u>\n\n<b>🔹 الاقسام</b> ➖> <u>الاقسام الموجوده</u>\n\n<b>🔹 قائمة المسؤولين</b> ➖> <u>اوامر خاصة للمسؤولين </u>(قيد التطوير)")

def departments(update:Update, context:CallbackContext):

    logging.info(f"[+]{update.message.from_user.first_name} {update.message.from_user.last_name} (@{update.message.from_user.username}) SENT A MESSAGE ({update.message.text})")

    buttons = [[InlineKeyboardButton("مساعده 🔍", callback_data="help")],
    [InlineKeyboardButton("القسم العام 📚", callback_data="GD")],
    [InlineKeyboardButton("قسم الميكانيكا  ⚙️", callback_data="ME"),InlineKeyboardButton("قسم الطاقات المتجدده ♻️", callback_data="RE")],
    [InlineKeyboardButton("قسم المدني  🏛", callback_data="CV"),InlineKeyboardButton("قسم الكهرباء ⚡️", callback_data="EL")],
    [InlineKeyboardButton("قسم المعماري 🎨", callback_data="AR"),InlineKeyboardButton("قسم الحاسوب 💻", callback_data="CM")],
    [InlineKeyboardButton("قسم الكيمياء 🧪", callback_data="CH"),InlineKeyboardButton("قسم علم المواد 🔬", callback_data="MA")]
    ]

    bot.sendMessage(chat_id=update.effective_chat.id, text="<b>اختر القسم المناسب: ⤵️</b>", timeout=5,
    reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

def textHandler(update:Update, context:CallbackContext):

    logging.info(f"[+]{update.message.from_user.first_name} {update.message.from_user.last_name} (@{update.message.from_user.username}) SENT A MESSAGE ({update.message.text})")

    message_check(bot, update, context)

def queryhandler(update:Update, context:CallbackContext):

    try : 
        
        query = update.callback_query.data

        logging.info(f"[+]{update.callback_query.from_user.first_name} {update.callback_query.from_user.last_name} (@{update.callback_query.from_user.username}) SENT A QUERY ({query})")

        query_check(bot, update, context, query)
       

    except (telegram.error.TimedOut, telegram.error.BadRequest, telegram.error.NetworkError) as e:

        print("AN ERROR OCCURED = ", e)
        if str(e).lower() == "timed out":

            logging.warning("[!]QUERY HANDLER ERROR TIMED OUT")
            print("\n[!]QUERY HANDLER ERROR TIMED OUT")
            

        elif str(e).lower() == "bad request":

            logging.warning("[!]QUERY HANDLER ERROR COULD NOT FIND MESSAGE TO DELETE")
            print("\n[!]QUERY HANDLER ERROR COULD NOT FIND MESSAGE TO DELETE")
    
def photoHandler(update:Update, context:CallbackContext):
    
    logging.info(f"[+]{update.message.from_user.first_name} {update.message.from_user.last_name} (@{update.message.from_user.username}) SENT A PHOTO")

    bot.sendMessage(chat_id=update.effective_chat.id, timeout=5,
        text="<b>اسف انا لا افهم الصور! ، اكتب '/' لمعرفة الاوامر المتاحة</b>", parse_mode="HTML")

    bot.sendMessage(chat_id=update.effective_chat.id, timeout=5,
        text="🤔")

def voiceHandler(update:Update, context:CallbackContext):

    logging.info(f"[+]{update.message.from_user.first_name} {update.message.from_user.last_name} (@{update.message.from_user.username}) SENT A VOICE MESSAGE")

    bot.sendMessage(chat_id=update.effective_chat.id, timeout=5,
        text="<b>اسف انا لا افهم الرسائل الصوتية! ، اكتب '/' لمعرفة الاوامر المتاحة</b>", parse_mode="HTML")

    bot.sendMessage(chat_id=update.effective_chat.id, timeout=5,
        text="🤔")

def stickerHandler(update:Update, context:CallbackContext):

    logging.info(f"[+]{update.message.from_user.first_name} {update.message.from_user.last_name} (@{update.message.from_user.username}) SENT A STICKER")

    bot.sendMessage(chat_id=update.effective_chat.id, timeout=5,
        text="<b>اسف انا لا افهم الملصقات! ، اكتب '/' لمعرفة الاوامر المتاحة</b>", parse_mode="HTML")

    bot.sendMessage(chat_id=update.effective_chat.id, timeout=5,
        text="🤔")
    
def documentHandler(update:Update, context:CallbackContext):

    logging.info(f"[+]{update.message.from_user.first_name} {update.message.from_user.last_name} (@{update.message.from_user.username}) SENT A DOCUMENT ({update.message.document.file_name})")
    
    file_manager(update.message.document.file_name, update.message.document.file_id)

    bot.sendMessage(chat_id=update.effective_chat.id, parse_mode="HTML", timeout=5,
    text="<b>تم استلام الملف، سيتم مراجعتها من قبل المطور!\n للمزيد من التفاصيل قم بمراسلة المطور \n@Firas_Alawami</b>")





def error(update:Update, context:CallbackContext):

    print(f"Update {update} caused error {context.error}")
            
        
def main():

    ###Handlers###

    #Command Handlers
    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("help", help))
    disp.add_handler(CommandHandler("Departments", departments))

    #Message Handlers
    disp.add_handler(MessageHandler(Filters.text, textHandler))
    disp.add_handler(MessageHandler(Filters.photo, photoHandler))
    disp.add_handler(MessageHandler(Filters.voice, voiceHandler))
    disp.add_handler(MessageHandler(Filters.sticker, stickerHandler))
    disp.add_handler(MessageHandler(Filters.document, documentHandler))

    #CallbackQuery Handlers
    disp.add_handler(CallbackQueryHandler(queryhandler))


    print("\nTelegram bot V5 is running....\tVIEW LOG FILE FOR MORE INFO\n")

    try:
        disp.add_error_handler(error)

        updater.start_polling(timeout=5)
        updater.idle()
    except (telegram.error.NetworkError) as e:

        print(f"A NETWORK ERROR OCCURED {e}")    




    
main()

