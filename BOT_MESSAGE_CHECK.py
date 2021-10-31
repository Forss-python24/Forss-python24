from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton
import Telegram_reply_texts as texts
from ast import literal_eval

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

def KeyboardMarkup(*args, one_time_keyboard=False):
    kb = []
    x = 0

    while x < len(args):
            
        kb.append([KeyboardButton(args[x])])
        x += 1
    
    kb_markup = ReplyKeyboardMarkup(kb, resize_keyboard=True, one_time_keyboard=one_time_keyboard)

    return kb_markup

def message_check(bot, update, context):

    if update.message.text == "السلام عليكم":

        bot.sendMessage(chat_id=update.effective_chat.id, text="<b>و عليكم السلام ! ،\n اكتب '/' لمعرفة الاوامر المتاحة!</b>", timeout=5
        , parse_mode="HTML")
        bot.sendMessage(chat_id=update.effective_chat.id, text="👋", timeout=5)

    else :
        bot.sendMessage(chat_id=update.effective_chat.id, timeout=5,
        text="<b>اسف انا لا افهمك! ، اكتب '/' لمعرفة الاوامر المتاحة</b>", parse_mode="HTML")

        bot.sendMessage(chat_id=update.effective_chat.id, timeout=5,
        text="🤔")

def query_check_departments(bot, update, context, query):

    match(query):

        case "departments" :

            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("مساعده 🔍", callback_data="help")],
            [InlineKeyboardButton("القسم العام 📚", callback_data="GD")],
            [InlineKeyboardButton("قسم الميكانيكا  ⚙️", callback_data="ME"),InlineKeyboardButton("قسم الطاقات المتجدده ♻️", callback_data="RE")],
            [InlineKeyboardButton("قسم المدني  🏛", callback_data="CV"),InlineKeyboardButton("قسم الكهرباء ⚡️", callback_data="EL")],
            [InlineKeyboardButton("قسم المعماري 🎨", callback_data="AR"),InlineKeyboardButton("قسم الحاسوب 💻", callback_data="CM")],
            [InlineKeyboardButton("قسم الكيمياء 🧪", callback_data="CH"),InlineKeyboardButton("قسم علم المواد 🔬", callback_data="MA")]
            ]

            update.callback_query.edit_message_text(text="<b>اختر القسم المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")


        case "GD" :

            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                    [InlineKeyboardButton("ميكانيكا 1", callback_data="mech1"),
                        InlineKeyboardButton("كيمياء عامة", callback_data="gen_chem")],
                        [InlineKeyboardButton("فيزياء 1", callback_data="physics_1"),
                        InlineKeyboardButton("فيزياء 2", callback_data="physics_2")],
                    [InlineKeyboardButton("رياضة 1", callback_data="math1"),
                        InlineKeyboardButton("رياضة 2", callback_data="math2")],
                        [InlineKeyboardButton("رياضة 3", callback_data="math3"),
                        InlineKeyboardButton("الاحصاء و الاحتمالات", callback_data="statitcs")],
                        [InlineKeyboardButton("اتصال فعال", callback_data="effectiveCOM")],
                        [InlineKeyboardButton("المزيد", callback_data="more")],
                        [InlineKeyboardButton("النتيجة 📩", url="https://omu.edu.ly/results/fgeneral.php")],
            ]

            update.callback_query.edit_message_text(text="<b>اختر الماده المناسبة: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "ME" :     

            update.callback_query.answer(timeout=5)

            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                    [InlineKeyboardButton(" ميكانيكا 2 (ديناميكا)", callback_data="mech2"),
                        InlineKeyboardButton("اقتصاد هندسي", callback_data="eng_economics")],
                        [InlineKeyboardButton("ديناميكا حرارية 1", callback_data="thermo1"),
                        InlineKeyboardButton("ديناميكا حرارية 2", callback_data="thermo2")],
                        [InlineKeyboardButton("النتيجة 📩", url="https://omu.edu.ly/results/fmech.php")],
            ]

            update.callback_query.edit_message_text(text="<b>اختر الماده المناسبة: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "RE" :
            
            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                    [InlineKeyboardButton(" ميكانيكا 2 (ديناميكا)", callback_data="mech2"),
                        InlineKeyboardButton("ادارة و اقتصاد هندسي", callback_data="eng_economics")],
                        [InlineKeyboardButton("ديناميكا حرارية 1", callback_data="thermo1"),
                        InlineKeyboardButton("ديناميكا حرارية 2", callback_data="thermo2")],
                        [InlineKeyboardButton("Biomass", callback_data="biomass"),
                        InlineKeyboardButton("Fluid Mechanics 1", callback_data="fluid1")],
                        [InlineKeyboardButton("Solar PV", callback_data="solar"),
                        InlineKeyboardButton("Heat Transfer 1", callback_data="heat1")],
                        [InlineKeyboardButton("النتيجة 📩", url="https://omu.edu.ly/results/fsree.php")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الماده المناسبة: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "CV" :
            
            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                    [InlineKeyboardButton(" ميكانيكا 2 (ديناميكا)", callback_data="mech2"),
                        InlineKeyboardButton("ادارة و اقتصاد هندسي", callback_data="eng_economics")],
                        [InlineKeyboardButton("النتيجة 📩", url="https://omu.edu.ly/results/fcivil.php")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الماده المناسبة: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "EL" :
            
            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                        [InlineKeyboardButton("ادارة و اقتصاد هندسي", callback_data="eng_economics")],
                        [InlineKeyboardButton("النتيجة 📩", url="https://omu.edu.ly/results/felec.php")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الماده المناسبة: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
            
        case "AR" :
            
            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                    [InlineKeyboardButton("النتيجة 📩", url="https://omu.edu.ly/results/farch.php")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الماده المناسبة: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
        
        case "CM" :
            
            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                       [InlineKeyboardButton("دوائر كهربائية 1", callback_data="circuits1")],
                       [InlineKeyboardButton("Digital II", callback_data="digital2")],
                       [InlineKeyboardButton("دوائر كهربائية 3", callback_data="circuits3")],
                    [InlineKeyboardButton("النتيجة 📩", url="https://omu.edu.ly/results/fcomp.php")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الماده المناسبة: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "CH" :
            
            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                        [InlineKeyboardButton("اقتصاد هندسي", callback_data="eng_economics")],
                        [InlineKeyboardButton("النتيجة 📩", url="https://omu.edu.ly/results/fchem.php")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الماده المناسبة: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "MA" :
            
            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                        [InlineKeyboardButton("اقتصاد هندسي", callback_data="eng_economics")],
                        [InlineKeyboardButton("النتيجة 📩", url="https://omu.edu.ly/results/fsci.php")],
            ]
        
            update.callback_query.edit_message_text(text="<b>اختر الماده المناسبة: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

def query_check_General_subjects(bot, update, context, query):
    
    match(query):

        case "effectiveCOM":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                        [InlineKeyboardButton("Lecture Notes (9/2021).pdf", callback_data="Communication skills lecture notes updated  sep 2021.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mech1":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                        [InlineKeyboardButton("Engineering mechanics statics 14th edition by hibbeler.pdf", callback_data="Engineering mechanics statics 14th edition by hibbeler.pdf")],
                            [InlineKeyboardButton("Chapter 2.pdf", callback_data="Chapter 2.pdf")],
                            [InlineKeyboardButton("Chapter 3.pdf", callback_data="Chapter 3.pdf")],
                            [InlineKeyboardButton("Chapter 4.pdf", callback_data="Chapter 4.pdf")],
                            [InlineKeyboardButton("Chapter 5.pdf", callback_data="Chapter 5.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "gen_chem":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                        [InlineKeyboardButton("Chemistry by raymond chang.pdf", callback_data="Chemistry by raymond chang.pdf")]
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "physics_1":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                       [InlineKeyboardButton("فيزياء 1.pdf", callback_data="فيزياء 1.pdf")]
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "physics_2":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                        [InlineKeyboardButton("فيزياء 2 (من شبتر 16).pdf", callback_data="فيزياء 2 (من شبتر 16).pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "math1":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                        [InlineKeyboardButton("رياضة 1 (من شبتر 3 الى 6).pdf", callback_data="رياضة 1 (من شبتر 3 الى 6).pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "math2":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                        [InlineKeyboardButton("Unit-One.pdf", callback_data="Unit-One.pdf")],
                        [InlineKeyboardButton("Unit-Two.pdf", callback_data="Unit-Two.pdf")],
                        [InlineKeyboardButton("Unit-Three.pdf", callback_data="Unit-Three.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "math3":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                        [InlineKeyboardButton("Part1-Matrices.pdf", callback_data="Part1-Matrices.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "statitcs":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                        [InlineKeyboardButton("Probability and Statistics for Engineers Part1.pdf", callback_data="Probability and Statistics for Engineers_ Part1.pdf")],
                        [InlineKeyboardButton("Probability and Statistics for Engineers Part2 Lec2.pdf", callback_data="Probability and Statistics for Engineers Part2 Lec2.pdf")],
                        [InlineKeyboardButton("Probability and Statistics for Engineers Part2 Lec3.pdf", callback_data="Probability and Statistics for Engineers Part2 Lec3.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")


        case "more":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="GD")],
                        [InlineKeyboardButton("امتحانات سابقة رياضة 1 📃", callback_data="Math1PrevExams")],
                        [InlineKeyboardButton("حلول تمارين الرياضة 📝", callback_data="Math1Solved")],
                        [InlineKeyboardButton("واجبات الاحصاء و الاحتمالات 📄", callback_data="statisticsHM")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
        
        case "statisticsHM":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="more")],
                        [InlineKeyboardButton("Statistics and Probability HW1.pdf", callback_data="Statistics and Probability _HW1.pdf")],
                        [InlineKeyboardButton("Statistics and Probability HW2.pdf", callback_data="Statistics and Probability _HW2.pdf")],
                        [InlineKeyboardButton("Statistics and Probability HW3.pdf", callback_data="Statistics and Probability _HW3.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "Math1PrevExams":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="more")],
                        [InlineKeyboardButton("GS101Mid19.pdf", callback_data="GS101Mid19.pdf")],
                        [InlineKeyboardButton("GS101Mid18.pdf", callback_data="GS101Mid18.pdf")],
                        [InlineKeyboardButton("101Mid17.pdf", callback_data="101Mid17.pdf")],
                        [InlineKeyboardButton("101FinalExam.pdf", callback_data="101FinalExam.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "Math1Solved":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="more")],
                       [InlineKeyboardButton("Exercise1", callback_data="mathEX1"),
                       InlineKeyboardButton("Exercise2", callback_data="mathEX2")],
                       [InlineKeyboardButton("Exercise3", callback_data="mathEX3"),
                       InlineKeyboardButton("Exercise4", callback_data="mathEX4")],
                       [InlineKeyboardButton("Exercise5", callback_data="mathEX5"),
                       InlineKeyboardButton("Exercise6", callback_data="mathEX6")],
                       [InlineKeyboardButton("Exercise7", callback_data="mathEX7"),
                       InlineKeyboardButton("Exercise8", callback_data="mathEX8")],
                       [InlineKeyboardButton("Exercise9", callback_data="mathEX9"),
                       InlineKeyboardButton("Exercise10", callback_data="mathEX10")],
                       [InlineKeyboardButton("Exercise11", callback_data="mathEX11"),
                       InlineKeyboardButton("Exercise12", callback_data="mathEX12")],
                       [InlineKeyboardButton("Exercise13", callback_data="mathEX13"),
                       InlineKeyboardButton("Exercise14", callback_data="mathEX14")],
                       [InlineKeyboardButton("Exercise15", callback_data="mathEX15")],

                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
        
        #mathematics solved sol.

        case "mathEX1":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions1a.pdf", callback_data="Solutions1a.pdf"),
                       InlineKeyboardButton("Solutions1b.pdf", callback_data="Solutions1b.pdf")],
                       [InlineKeyboardButton("Solutions1c.pdf", callback_data="Solutions1c.pdf"),
                       InlineKeyboardButton("Solutions1d.pdf", callback_data="Solutions1d.pdf")],
                       [InlineKeyboardButton("Solutions1e.pdf", callback_data="Solutions1e.pdf"),
                       InlineKeyboardButton("Solutions1f.pdf", callback_data="Solutions1f.pdf")],
                       [InlineKeyboardButton("Solutions1g.pdf", callback_data="Solutions1g.pdf"),
                       InlineKeyboardButton("Solutions1h.pdf", callback_data="Solutions1h.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX2":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions2a.pdf", callback_data="Solutions2a.pdf"),
                       InlineKeyboardButton("Solutions2b.pdf", callback_data="Solutions2b.pdf")],
                       [InlineKeyboardButton("Solutions2c.pdf", callback_data="Solutions2c.pdf"),
                       InlineKeyboardButton("Solutions2d.pdf", callback_data="Solutions2d.pdf")],
                       [InlineKeyboardButton("Solutions2e.pdf", callback_data="Solutions2e.pdf"),
                       InlineKeyboardButton("Solutions2f.pdf", callback_data="Solutions2f.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX3":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions3a.pdf", callback_data="Solutions3a.pdf"),
                       InlineKeyboardButton("Solutions3b.pdf", callback_data="Solutions3b.pdf")],
                       [InlineKeyboardButton("Solutions3c.pdf", callback_data="Solutions3c.pdf"),
                       InlineKeyboardButton("Solutions3d.pdf", callback_data="Solutions3d.pdf")],
                       [InlineKeyboardButton("Solutions3e.pdf", callback_data="Solutions3e.pdf"),
                       InlineKeyboardButton("Solutions3f.pdf", callback_data="Solutions3f.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX4":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions4a.pdf", callback_data="Solutions4a.pdf"),
                       InlineKeyboardButton("Solutions4b.pdf", callback_data="Solutions4b.pdf")],
                       [InlineKeyboardButton("Solutions4c.pdf", callback_data="Solutions4c.pdf"),
                       InlineKeyboardButton("Solutions4d.pdf", callback_data="Solutions4d.pdf")],
                       [InlineKeyboardButton("Solutions4e.pdf", callback_data="Solutions4e.pdf"),
                       InlineKeyboardButton("Solutions4f.pdf", callback_data="Solutions4f.pdf")],
                       [InlineKeyboardButton("Solutions4g.pdf", callback_data="Solutions4g.pdf"),
                       InlineKeyboardButton("Solutions4h.pdf", callback_data="Solutions4h.pdf")],
                       [InlineKeyboardButton("Solutions4i.pdf", callback_data="Solutions4i.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX5":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions5a.pdf", callback_data="Solutions5a.pdf"),
                       InlineKeyboardButton("Solutions5b.pdf", callback_data="Solutions5b.pdf")],
                       [InlineKeyboardButton("Solutions5c.pdf", callback_data="Solutions5c.pdf"),
                       InlineKeyboardButton("Solutions5d.pdf", callback_data="Solutions5d.pdf")],
                       [InlineKeyboardButton("Solutions5e.pdf", callback_data="Solutions5e.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX6":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions6a.pdf", callback_data="Solutions6a.pdf"),
                       InlineKeyboardButton("Solutions6b.pdf", callback_data="Solutions6b.pdf")],
                       [InlineKeyboardButton("Solutions6c.pdf", callback_data="Solutions6c.pdf"),
                       InlineKeyboardButton("Solutions6d.pdf", callback_data="Solutions6d.pdf")],
                       [InlineKeyboardButton("Solutions6e.pdf", callback_data="Solutions6e.pdf"),
                       InlineKeyboardButton("Solutions6f.pdf", callback_data="Solutions6f.pdf")],
                       [InlineKeyboardButton("Solutions6g.pdf", callback_data="Solutions6g.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX7":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions7a.pdf", callback_data="Solutions7a.pdf"),
                       InlineKeyboardButton("Solutions7b.pdf", callback_data="Solutions7b.pdf")],
                       [InlineKeyboardButton("Solutions7c.pdf", callback_data="Solutions7c.pdf"),
                       InlineKeyboardButton("Solutions7d.pdf", callback_data="Solutions7d.pdf")],
                       [InlineKeyboardButton("Solutions7e.pdf", callback_data="Solutions7e.pdf"),
                       InlineKeyboardButton("Solutions7f.pdf", callback_data="Solutions7f.pdf")],
                       [InlineKeyboardButton("Solutions7g.pdf", callback_data="Solutions7g.pdf"),
                       InlineKeyboardButton("Solutions7h.pdf", callback_data="Solutions7h.pdf")],
                       [InlineKeyboardButton("Solutions7i.pdf", callback_data="Solutions7i.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX8":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions8a.pdf", callback_data="Solutions8a.pdf"),
                       InlineKeyboardButton("Solutions8b.pdf", callback_data="Solutions8b.pdf")],
                       [InlineKeyboardButton("Solutions8c.pdf", callback_data="Solutions8c.pdf"),
                       InlineKeyboardButton("Solutions8d.pdf", callback_data="Solutions8d.pdf")],
                       [InlineKeyboardButton("Solutions8e.pdf", callback_data="Solutions8e.pdf"),
                       InlineKeyboardButton("Solutions8f.pdf", callback_data="Solutions8f.pdf")],
                       [InlineKeyboardButton("Solutions8g.pdf", callback_data="Solutions8g.pdf"),
                       InlineKeyboardButton("Solutions8h.pdf", callback_data="Solutions8h.pdf")],
                       [InlineKeyboardButton("Solutions8i.pdf", callback_data="Solutions8i.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX9":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions9a.pdf", callback_data="Solutions9a.pdf"),
                       InlineKeyboardButton("Solutions9b.pdf", callback_data="Solutions9b.pdf")],
                       [InlineKeyboardButton("Solutions9c.pdf", callback_data="Solutions9c.pdf"),
                       InlineKeyboardButton("Solutions9d.pdf", callback_data="Solutions9d.pdf")],
                       [InlineKeyboardButton("Solutions9e.pdf", callback_data="Solutions9e.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX10":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions10a.pdf", callback_data="Solutions10a.pdf"),
                       InlineKeyboardButton("Solutions10b.pdf", callback_data="Solutions10b.pdf")],
                       [InlineKeyboardButton("Solutions10c.pdf", callback_data="Solutions10c.pdf"),
                       InlineKeyboardButton("Solutions10d.pdf", callback_data="Solutions10d.pdf")],
                       [InlineKeyboardButton("Solutions10e.pdf", callback_data="Solutions10e.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX11":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions11a.pdf", callback_data="Solutions11a.pdf"),
                       InlineKeyboardButton("Solutions11b.pdf", callback_data="Solutions11b.pdf")],
                       [InlineKeyboardButton("Solutions11c.pdf", callback_data="Solutions11c.pdf"),
                       InlineKeyboardButton("Solutions11d.pdf", callback_data="Solutions11d.pdf")],
                       [InlineKeyboardButton("Solutions11e.pdf", callback_data="Solutions11e.pdf"),
                       InlineKeyboardButton("Solutions11f.pdf", callback_data="Solutions11f.pdf")],
                       [InlineKeyboardButton("Solutions11g.pdf", callback_data="Solutions11g.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX12":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions12a.pdf", callback_data="Solutions12a.pdf"),
                       InlineKeyboardButton("Solutions12b.pdf", callback_data="Solutions12b.pdf")],
                       [InlineKeyboardButton("Solutions12c.pdf", callback_data="Solutions12c.pdf"),
                       InlineKeyboardButton("Solutions12d.pdf", callback_data="Solutions12d.pdf")],
                       [InlineKeyboardButton("Solutions12e.pdf", callback_data="Solutions12e.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX13":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions13a.pdf", callback_data="Solutions13a.pdf"),
                       InlineKeyboardButton("Solutions13b.pdf", callback_data="Solutions13b.pdf")],
                       [InlineKeyboardButton("Solutions13c.pdf", callback_data="Solutions13c.pdf"),
                       InlineKeyboardButton("Solutions13d.pdf", callback_data="Solutions13d.pdf")],
                       [InlineKeyboardButton("Solutions13e.pdf", callback_data="Solutions13e.pdf"),
                       InlineKeyboardButton("Solutions13f.pdf", callback_data="Solutions13f.pdf")],
                       [InlineKeyboardButton("Solutions13g.pdf", callback_data="Solutions13g.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX14":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions14a.pdf", callback_data="Solutions14a.pdf"),
                       InlineKeyboardButton("Solutions14b.pdf", callback_data="Solutions14b.pdf")],
                       [InlineKeyboardButton("Solutions14c.pdf", callback_data="Solutions14c.pdf"),
                       InlineKeyboardButton("Solutions14d.pdf", callback_data="Solutions14d.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "mathEX15":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="Math1Solved")],
                       [InlineKeyboardButton("Solutions15a.pdf", callback_data="Solutions15a.pdf"),
                       InlineKeyboardButton("Solutions15b.pdf", callback_data="Solutions15b.pdf")],
                       [InlineKeyboardButton("Solutions15c.pdf", callback_data="Solutions15c.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

def query_check_common_subjects(bot, update, context, query):

    match(query):

        case "mech2":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                        [InlineKeyboardButton("Lec # 1.pdf", callback_data="Lec # 1.pdf")],
                            [InlineKeyboardButton("Lec # 2.pdf", callback_data="Lec # 2.pdf")],
                            [InlineKeyboardButton("Lec # 3.pdf", callback_data="Lec # 3.pdf")],
                            [InlineKeyboardButton("Lec # 4.pdf", callback_data="Lec # 4.pdf")],
                            [InlineKeyboardButton("Lec # 5.pdf", callback_data="Lec # 5.pdf")],
                ]
                
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "eng_economics":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                        [InlineKeyboardButton("Engineering Economy 7th Ed.pdf", callback_data="Engineering_Economy_7th_Ed.pdf")],
                            [InlineKeyboardButton("Chapter1.ppt", callback_data="Chapter1.ppt")],
                            [InlineKeyboardButton("Chapter2.ppt", callback_data="Chapter2.ppt")],
                            [InlineKeyboardButton("مسائل", callback_data="ecoExample")],
                ]

            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "ecoExample":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="eng_economics")],
                        [InlineKeyboardButton("Economics Engineering problems Ch2.ppt", callback_data="Economics-Engineering problems-Ch2-.ppt")],
                ]

            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "thermo1":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                    [InlineKeyboardButton("أ.محمد يونس", callback_data="Thermo1Moh"),
                        InlineKeyboardButton("أ.علي آدم", callback_data="Thermo1Adam")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر المحاضر: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "thermo2":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="departments")],
                    [InlineKeyboardButton("أ.محمد يونس", callback_data="Thermo2Moh"),
                        InlineKeyboardButton("أ.علي آدم", callback_data="Thermo2Adam")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر المحاضر: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

def query_check_RE(bot, update, context, query):

    match(query):

        case "biomass":

            update.callback_query.answer(timeout=5)


            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="RE")],
                    [InlineKeyboardButton("أ.احمد بالخير", callback_data="AHMEDbio")]
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر المحاضر: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "fluid1":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="RE")],
                    [InlineKeyboardButton("Fundamentals of Fluid Mechanics 7th_Edition 2013 Munson.pdf", callback_data="Fundamentals_of_Fluid_Mechanics_7th_Edition.pdf")]
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "solar":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="RE")],
                    [InlineKeyboardButton("سالم بورجعة", callback_data="solarSALEM")],
                        [InlineKeyboardButton("حسن عزوز", callback_data="solarHASAN")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر المحاضر: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
        
        case "heat1":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="RE")],
                    [InlineKeyboardButton("Fundamentals of Heat and Mass Transfer 7th Edition.pdf", callback_data="Fundamentals_of_Heat_and_Mass_Transfer_7th_Edition.pdf")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

def query_check_CM(bot, update, context, query):

    match(query):

        case "circuits1":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="CM")],
                    [InlineKeyboardButton("Fundamentals of Electric Circuits 5th Ed (المرجع)", callback_data="Fundamentals of Electric Circuits (5th Ed)(gnv64).pdf")],
                    [InlineKeyboardButton("W1 Basic Laws1", callback_data="W1_Basic Laws1 (1).pdf")],
                    [InlineKeyboardButton("W1 INTRO", callback_data="W1_INTRO.pdf")],
                    [InlineKeyboardButton("W2 LAWS", callback_data="W2_LAWS.pdf")],
                    [InlineKeyboardButton("W3 RESISTORS", callback_data="W3_RESISTORS.pdf")],
                    [InlineKeyboardButton("W4-5 METHOD OF ANALYSIS", callback_data="W4-5_METHOD OF ANALYSIS.pdf")],
                    [InlineKeyboardButton("W5 Thevenin Norton Theorem 1", callback_data="W5_Thevenin _ Norton Theorem-1.pdf")],
                    [InlineKeyboardButton("W6-7 THEOREMS", callback_data="W6-7_THEOREMS.pdf")],
                    [InlineKeyboardButton("W7-8 1st ORDER", callback_data="W7-8_1st ORDER.pdf")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")
            
        case "circuits3":
            
            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="CM")],
                    [InlineKeyboardButton("Chapter1.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter1.pdf"),
                     InlineKeyboardButton("Chapter2.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter2.pdf")],
                    [InlineKeyboardButton("Chapter3.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter3.pdf"),
                     InlineKeyboardButton("Chapter4.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter4.pdf")],
                    [InlineKeyboardButton("Chapter5.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter5.pdf"),
                     InlineKeyboardButton("Chapter6.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter6.pdf")],
                    [InlineKeyboardButton("Chapter7.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter7.pdf"),
                     InlineKeyboardButton("Chapter8.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter8.pdf")],
                    [InlineKeyboardButton("Chapter9.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter9.pdf"),
                     InlineKeyboardButton("Chapter10.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter10.pdf")],
                    [InlineKeyboardButton("Chapter11.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter11.pdf"),
                     InlineKeyboardButton("Chapter12.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter12.pdf")],
                    [InlineKeyboardButton("Chapter13.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter13.pdf"),
                     InlineKeyboardButton("Chapter14.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter14.pdf")],
                    [InlineKeyboardButton("Chapter15.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter15.pdf"),
                     InlineKeyboardButton("Chapter16.pdf", callback_data="Electronic_Devices_and_Circuit_Theory_10thEd_Chapter16.pdf")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

        case "digital2":

            update.callback_query.answer(timeout=5)
            
            buttons = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="CM")],
                    [InlineKeyboardButton("Digital ll (المحاضرة الاولى).pdf", callback_data="Digital ll c.pdf")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), parse_mode="HTML")

def Docter_checker(bot, update, context, query):

    match(query):

        case "Thermo1Moh":

            update.callback_query.answer(timeout=5)

            buttons1 = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="thermo1")],
                    [InlineKeyboardButton("thermodynamics-ch1.pdf", callback_data="thermodynamics-ch1.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch2.pdf", callback_data="thermodynamics-ch2.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch3.pdf", callback_data="thermodynamics-ch3.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch4.pdf", callback_data="thermodynamics-ch4.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch5.pdf", callback_data="thermodynamics-ch5.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch6.pdf", callback_data="thermodynamics-ch6.pdf")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons1), parse_mode="HTML")

        case "Thermo1Adam":
            
            update.callback_query.answer(timeout=5)

            buttons2 = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="thermo1")],
                    [InlineKeyboardButton("Chapter01.ppt", callback_data="Chapter01.ppt")],
                    [InlineKeyboardButton("Chapter02.ppt", callback_data="Chapter02.ppt")],
                    [InlineKeyboardButton("Chapter03.ppt", callback_data="Chapter03.ppt")],
                    [InlineKeyboardButton("Chapter04.ppt", callback_data="Chapter04.ppt")],
                    [InlineKeyboardButton("Chapter05.ppt", callback_data="Chapter05.ppt")],
                    [InlineKeyboardButton("Chapter06.ppt", callback_data="Chapter06.ppt")],
                    [InlineKeyboardButton("Chapter07.ppt", callback_data="Chapter07.ppt")]
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons2), parse_mode="HTML")
        
        case "Thermo2Adam":
            
            update.callback_query.answer(timeout=5)

            buttons3 = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="thermo2")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons3), parse_mode="HTML")


        case "Thermo2Moh":
            
            update.callback_query.answer(timeout=5)

            buttons4 = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="thermo2")],
                    [InlineKeyboardButton("thermodynamics-ch7.pdf", callback_data="thermodynamics-ch7.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch8.pdf", callback_data="thermodynamics-ch8.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch9.pdf", callback_data="thermodynamics-ch9.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch10.pdf", callback_data="thermodynamics-ch10.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch11.pdf", callback_data="thermodynamics-ch11.pdf")],
                    [InlineKeyboardButton("thermodynamics-ch12.pdf", callback_data="thermodynamics-ch12.pdf")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons4), parse_mode="HTML")
    
        case "solarSALEM":

            update.callback_query.answer(timeout=5)
        
            buttons5 = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="solar")],
                        [InlineKeyboardButton("Chap 1 PV.pdf", callback_data="Chap 1 PV.pdf")],
                        [InlineKeyboardButton("Chap 2.1 PV.pdf", callback_data="Chap 2.1 PV.pdf")],
                        [InlineKeyboardButton("Chap 2.2 Basics of Photovoltaics.pdf", callback_data="Chap 2.2_Basics of Photovoltaics.pdf")],
                        [InlineKeyboardButton("Chap 3.1.pdf", callback_data="Chap 3.1.pdf")],
                        [InlineKeyboardButton("Chap 3.2.pdf", callback_data="Chap 3.2.pdf")],
                        [InlineKeyboardButton("Chap 3.3.pdf", callback_data="Chap 3.3.pdf")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons5), parse_mode="HTML")

        case "solarHASAN":

            update.callback_query.answer(timeout=5)
        
            buttons6 = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="solar")],
                        [InlineKeyboardButton("Chap 1 PV.pdf", callback_data="Chap 1 PV.pdf")],
                        [InlineKeyboardButton("Chap 2.1 PV.pdf", callback_data="Chap 2.1 PV.pdf")],
                        [InlineKeyboardButton("Chap 2.2 Basics of Photovoltaics.pdf", callback_data="Chap 2.2_Basics of Photovoltaics.pdf")],
                        [InlineKeyboardButton("Chap 3.1.pdf", callback_data="Chap 3.1.pdf")],
                        [InlineKeyboardButton("Chap 3.2.pdf", callback_data="Chap 3.2.pdf")],
                        [InlineKeyboardButton("Chap 3.3.pdf", callback_data="Chap 3.3.pdf")],
                        [InlineKeyboardButton("Solar.pptx", callback_data="solar.pptx")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons6), parse_mode="HTML")

        case "AHMEDbio":

            update.callback_query.answer(timeout=5)


            buttons7 = [[InlineKeyboardButton("الرجوع ⬅️", callback_data="biomass")],
                        [InlineKeyboardButton("Biomass Eneergy 1.pptx", callback_data="Biomass Eneergy 1.pptx")],
                        [InlineKeyboardButton("Biomass Eneergy 2.pptx", callback_data="Biomass Eneergy 2.pptx")],
                        [InlineKeyboardButton("Biomass Eneergy 3.pptx", callback_data="Biomass Eneergy 3.pptx")],
                        [InlineKeyboardButton("Biomass Eneergy 4.pptx", callback_data="Biomass Eneergy 4NEW new.pptx")],
            ]
            
            update.callback_query.edit_message_text(text="<b>اختر الملف المناسب: ⤵️</b>", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons7), parse_mode="HTML")

def query_file_sender(bot, update, context, query):

        if "pdf" in query:
            update.callback_query.answer(timeout=5)
            bot.sendDocument(chat_id=update.effective_chat.id, timeout=5, document=search_files(query))

        elif "ppt" in query:
            update.callback_query.answer(timeout=5)
            bot.sendDocument(chat_id=update.effective_chat.id, timeout=5, document=search_files(query))
        
        elif "pptx" in query:
            update.callback_query.answer(timeout=5)
            bot.sendDocument(chat_id=update.effective_chat.id, timeout=5, document=search_files(query))
        
        elif "rar" in query:
            update.callback_query.answer(timeout=5)
            bot.sendDocument(chat_id=update.effective_chat.id, timeout=5, document=search_files(query))

def query_check(bot, update, context, query):

    match(query):

        case "admin" :
                
            update.callback_query.answer("هذا الخيار قيد التطوير", show_alert=True, timeout=5)

        case "help" :
            
            update.callback_query.answer(timeout=5)

            buttons = [[InlineKeyboardButton("الموقع 🌐", url=texts.Website_lnk)],
            [InlineKeyboardButton("قائمة المسؤولين 👤", callback_data="admin" ),
            InlineKeyboardButton("الاقسام 📁", callback_data="departments")]]

            update.callback_query.edit_message_text(parse_mode="HTML", timeout=5,
            reply_markup=InlineKeyboardMarkup(buttons), text=f"<b>مرحبا {update.effective_chat.first_name}❕ 👋\n\n🔸 هذه قائمة المساعده 🔍 ، انقر على احدى الخيارات:</b>\n\n\n<b>🔹 الموقع</b> ➖> <u>الموقع الرسمي لكلية الهندسة جامعة عمر المختار</u>\n\n<b>🔹 الاقسام</b> ➖> <u>الاقسام الموجوده</u>\n\n<b>🔹 قائمة المسؤولين</b> ➖> <u>اوامر خاصة للمسؤولين </u>(قيد التطوير)")

    query_check_departments(bot, update, context, query)
    query_check_General_subjects(bot, update, context, query)
    query_check_common_subjects(bot, update, context, query)
    query_check_RE(bot, update, context, query)
    query_check_CM(bot, update, context, query)
    Docter_checker(bot, update, context, query)
    query_file_sender(bot, update, context, query)

    