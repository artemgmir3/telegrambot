import telebot
from telebot import types

bot = telebot.TeleBot('7934318212:AAFN_ozz5ycCGf3UolgwuNt_We8G3mHh9CU')


# ——— Translations ——————————————————————————————————————————————
translations = {
    'menu': {
        'services':                 {'en': "Services",                                          'ru': "Услуги",                                     'by': "Паслугі"},
        'contacts':                 {'en': "Contacts",                                          'ru': "Контакты",                                   'by': "Кантакты"},
        'sign_up':                  {'en': "Leave a request",                                   'ru': "Оставить заявку",                            'by': "Пакінуць заяўку"},
        'back':                     {'en': "Back",                                              'ru': "Назад",                                      'by': "Назад"},
        'restoration':              {'en': "Restoration of accounting records",                 'ru': "Восстановление бухгалтерского учета",        'by': "Аднаўленне бухгалтарскага ўліку"},
        'maintaining_accounting':   {'en': "Setting up and maintaining accounting records",     'ru': "Постановка и ведение бухгалтерского учета",  'by': "Пастаноўка і вядзенне бухгалтарскага ўліку"},
        'personnel_accounting':     {'en': "Personnel accounting",                              'ru': "Кадровый учет",                              'by': "Кадравы ўлік"},
        'submission_of_reports':    {'en': "Preparation and submission of reports",             'ru': "Подготовка и сдача отчетности",              'by': "Падрыхтоўка і здача справаздачнасці"},
        'document_development':     {'en': "Document development",                              'ru': "Разработка документов",                      'by': "Распрацоўка дакументаў"},
        'consulting':               {'en': "Consulting",                                        'ru': "Консультирование",                           'by': "Кансультаванне"},
    },
    'messages': {
        'choose_lang':              {'en': "Please choose your language", 
                                     'ru': "Пожалуйста, выберите язык",
                                     'by': "Калі ласка, абярыце мову"},
        'start':                    {'en': "<b>Bilanx Outsourcing Company</b> provides professional services in the field of <b>accounting</b> for businesses of any scale.\nOur specialists have deep knowledge and many years of experience, which allows us to solve problems of varying complexity efficiently and on time.\nWe support companies in all tax systems and work with all types of activities.\n\n<b>Bilanx is a reliable foundation for developing your business.</b>",                    
                                     'ru': "<b>Аутсорсинговая компания «Bilanx»</b> предоставляет профессиональные услуги в области <b>бухгалтерского учета</b> для бизнеса любого масштаба.\nНаши специалисты обладают глубокими знаниями и многолетним опытом, что позволяет нам качественно и в срок решать задачи различной сложности.\nМы сопровождаем компании на всех системах налогообложения и работаем со всеми видами деятельности.\n\n<b>«Bilanx» — надежная основа для развития вашего бизнеса.</b>",
                                     'by': "<b>Аўтсорсінгавая кампанія «Bilanx»</b> прадастаўляе прафесійныя паслугі ў галіне бухгалтарскага ўліку для бізнесу любога маштабу. Нашы спецыялісты валодаюць глыбокімі ведамі і шматгадовым вопытам, што дазваляе нам якасна і ў тэрмін вырашаць задачы рознай складанасці. дзейнасці. \n\n<b>«Bilanx» - надзейная аснова для развіцця вашага бізнесу.</b>"},
        'what_interest':            {'en': "What are you interested in?", 
                                     'ru': "Что Вас интересует?",
                                     'by': "Што Вас цікавіць?",},
        'services':                 {'en': "Please select a service",               
                                     'ru': "Пожалуйста, выберите услугу",
                                     'by': "Калі ласка, абярыце паслугу"},
        'contacts':                 {'en': '<b>Phone number</b>\n+375 (44) 724-78-27\n\n<b>E-mail address</b>\ninfo@bilanx.by\n\n<b>Address</b>\n<a href="https://yandex.by/maps/-/CHrqNI9v">220004, Minsk, Pobediteley Ave., 11, floor 12, office 1205</a>\n\n<b>Instagram</b>\n<a href="https://www.instagram.com/bilanx.by?igsh=b3Z0YngwdHpwdTZy">bilanx.by</a>\n\n<b>Telegram</b>\n<a href="tg://user?id=8153630729">@bilanxby</a>\n\n<b>TikTok</b>\n<a href="https://www.tiktok.com/@bilanxby">bilanxby</a>', 
                                     'ru': '<b>Номер телефона</b>\n+375 (44) 724-78-27\n\n<b>Адрес электронной почты</b>\ninfo@bilanx.by\n\n<b>Адрес</b>\n<a href="https://yandex.by/maps/-/CHrqNI9v">220004, г. Минск, пр-т Победителей, д. 11, этаж 12, офис 1205</a>\n\n<b>Инстаграм</b>\n<a href="https://www.instagram.com/bilanx.by?igsh=b3Z0YngwdHpwdTZy">bilanx.by</a>\n\n<b>Телеграм</b>\n<a href="tg://user?id=8153630729">@bilanxby</a>\n\n<b>ТикТок</b>\n<a href="https://www.tiktok.com/@bilanxby">bilanxby</a>',
                                     'by': '<b>Нумар тэлефона</b>\n+375 (44) 724-78-27\n\n<b>Адрас электроннай пошты</b>\ninfo@bilanx.by\n\n<b>Адрас</b>\n<a href="https://yandex.by/maps/-/CHrqNI9v">220004, г. Мінск, пр-т. Пераможцаў, д. 11, паверх 12, офіс 1205</a>\n\n<b>Інстаграм</b>\n<a href="https://www.instagram.com/bilanx.by?igsh=b3Z0YngwdHpwdTZy">bilanx.by</a>\n\n<b>Тэлеграм</b>\n<a href="tg://user?id=8153630729">@bilanxby</a>\n\n<b>ЦікТок</b>\n<a href="https://www.tiktok.com/@bilanxby">bilanxby</a>'},
        'enter_something':          {'en': "Please provide your name, email address, contact phone number, link to your Telegram profile, and a detailed description of the expected scope of work.",   
                                     'ru': "Просим указать Ваше имя, адрес электронной почты, контактный номер телефона, ссылку на профиль в Telegram, а также предоставить подробное описание предполагаемого объема работ.",
                                     'by': "Просім указаць Ваша імя, адрас электроннай пошты, кантактны нумар тэлефона, спасылку на профіль у Telegram, а таксама прадставіць падрабязнае апісанне меркаванага аб'ёму работ."},
        'last_message':             {'en': "Your application has been accepted. We will contact you shortly!",     
                                     'ru': "Ваша заявка принята. Мы свяжемся с Вами в ближайшее время!",
                                     'by': "Ваша заяўка прынята. Мы звяжамся з Вамі ў бліжэйшы час!"},
        'restoration':              {'en': "<b>Accounting restoration</b>\n\nA set of measures aimed at bringing accounting documentation and accounting data into compliance with current legislation. We restore lost or distorted primary documents, correct errors in reporting, form missing accounting registers, restore tax and accounting records for past periods. As a result, you receive a complete, reliable and legally correct accounting base that meets the requirements of tax authorities and accounting standards.\n\n<b>From 50 BYN/month</b>",
                                     'ru': "<b>Восстановление бухгалтерского учета</b>\n\nКомплекс мероприятий, направленных на приведение бухгалтерской документации и учетных данных в соответствие с действующим законодательством. Мы восстанавливаем утерянные или искаженные первичные документы, корректируем ошибки в отчетности, формируем недостающие регистры учета, восстанавливаем налоговый и бухгалтерский учет за прошлые периоды. В результате вы получаете полную, достоверную и юридически корректную бухгалтерскую базу, соответствующую требованиям налоговых органов и стандартам бухгалтерского учета.\n\n<b>От 50 BYN/мес.</b>",
                                     'by': "<b>Аднаўленне бухгалтарскага ўліку</b>\n\nКомплекс мерапрыемстваў, накіраваных на прывядзенне бухгалтарскай дакументацыі і ўліковых дадзеных у адпаведнасць з дзеючым заканадаўствам. Мы аднаўляем згубленыя або скажоныя першасныя дакументы, карэктуем памылкі ў справаздачнасці, фармуем адсутныя рэгістры ўліку, аднаўляем падатковы і бухгалтарскі ўлік за мінулыя перыяды. У выніку вы атрымліваеце поўную, дакладную і юрыдычна карэктную бухгалтарскую базу, якая адпавядае патрабаванням падатковых органаў і стандартам бухгалтарскага ўліку.\n\n<b>Ад 50 BYN/мес.</b>"},
        'maintaining_accounting':   {'en': "<b>Setting up and maintaining accounting</b>\n\nProfessional organization and support of enterprise accounting «from scratch» or at any stage of its activity. We ensure correct accounting in accordance with the specifics of your business. We carry out full and timely accounting and tax accounting on all tax systems (simplified tax system, general tax system, etc.) and for all types of activities. We guarantee the accuracy of calculations, compliance with all legal requirements and preparation of the necessary reporting within the established deadlines.\n\n<b>From 100 BYN/month</b>",          
                                     'ru': "<b>Постановка и ведение бухгалтерского учета</b>\n\nПрофессиональная организация и сопровождение бухгалтерии предприятия «с нуля» или на любой стадии его деятельности. Мы обеспечиваем корректную постановку учета в соответствии с особенностями вашего бизнеса. Осуществляем полное и своевременное ведение бухгалтерского и налогового учета на всех системах налогообложения (УСН, ОСН и др.) и для всех видов деятельности. Гарантируем точность расчетов, соблюдение всех требований законодательства и подготовку необходимой отчетности в установленные сроки.\n\n<b>От 100 BYN/мес.</b>",
                                     'by': "<b>Падрыхтоўка і здача справаздачнасці</b>\n\nПрафесійная паслуга па фарміраванні, праверцы і своечасовай падачы ўсёй неабходнай бухгалтарскай, падатковай і статыстычнай справаздачнасці. Мы рыхтуем справаздачы ў адпаведнасці з патрабаваннямі заканадаўства і індывідуальнымі асаблівасцямі вашай дзейнасці, у тым ліку дэкларацыі па ПДВ, прыбытку, падатку на даходы фізічных асоб, страхавыя ўзносы, бухгалтарскую (фінансавую) справаздачнасць і справаздачы ў органы статыстыкі. Кантралюем карэктнасць разлікаў і выкананне тэрмінаў падачы, што дазваляе пазбегнуць штрафаў, даналічэнняў і прэтэнзій з боку кантралюючых органаў. Забяспечваем поўнае суправаджэнне працэсу — ад збору зыходных дадзеных да пацверджання паспяховай здачы справаздачнасці.\n\n<b>Ад 50 BYN/справаздача</b>"},
        'personnel_accounting':     {'en': "<b>Personnel records</b>\n\nA range of services for the preparation, maintenance and storage of documentation related to labor relations in an organization. We undertake full support of personnel records management: we keep records of employees, draw up employment contracts, orders for hiring, transfer and dismissal, vacation schedules, personal cards and other necessary documents. We ensure compliance with all labor legislation. Our approach allows us to minimize personnel risks, increase the transparency of personnel management processes and ensure legal protection for both the employer and employees.\n\n<b>From 10 BYN/doc.</b>",          
                                     'ru': "<b>Кадровый учет</b>\n\nКомплекс услуг по оформлению, ведению и хранению документации, связанной с трудовыми отношениями в организации. Мы берем на себя полное сопровождение кадрового делопроизводства: ведем учет сотрудников, оформляем трудовые договоры, приказы о приеме, переводе и увольнении, графики отпусков, личные карточки и другие необходимые документы. Обеспечиваем соблюдение всех норм трудового законодательства. Наш подход позволяет минимизировать кадровые риски, повысить прозрачность процессов управления персоналом и обеспечить юридическую защиту как работодателя, так и работников.\n\n<b>От 10 BYN/док.</b>",
                                     'by': "<b>Кадравы ўлік</b>\n\nКомплекс паслуг па афармленні, вядзенні і захоўванні дакументацыі, звязанай з працоўнымі адносінамі ў арганізацыі. Мы бярэм на сябе поўнае суправаджэнне кадравага справаводства: вядзем улік супрацоўнікаў, афармляем працоўныя дамовы, загады аб прыёме, перакладзе і звальненні, графікі адпачынкаў, асабістыя карткі і іншыя неабходныя дакументы. Забяспечваем выкананне ўсіх норм працоўнага заканадаўства. Наш падыход дазваляе мінімізаваць кадравыя рызыкі, павысіць празрыстасць працэсаў кіравання персаналам і забяспечыць юрыдычную абарону як працадаўцы, так і работнікаў.\n\n<b>Ад 10 BYN/док.</b>"},
        'submission_of_reports':    {'en': "<b>Preparation and submission of reports</b>\n\nA professional service for the formation, verification and timely submission of all necessary accounting, tax and statistical reports. We prepare reports in accordance with the requirements of the law and the individual characteristics of your activities, including declarations on VAT, profit, personal income tax, insurance premiums, accounting (financial) statements and reports to statistical authorities. We control the correctness of calculations and compliance with filing deadlines, which allows you to avoid fines, additional charges and claims from regulatory authorities. We provide full support for the process - from collecting initial data to confirming the successful submission of reports.\n\n<b>From 50 BYN / report</b>",          
                                     'ru': "<b>Подготовка и сдача отчетности</b>\n\nПрофессиональная услуга по формированию, проверке и своевременной подаче всей необходимой бухгалтерской, налоговой и статистической отчетности. Мы готовим отчеты в соответствии с требованиями законодательства и индивидуальными особенностями вашей деятельности, включая декларации по НДС, прибыли, налогу на доходы физических лиц, страховые взносы, бухгалтерскую (финансовую) отчетность и отчеты в органы статистики. Контролируем корректность расчетов и соблюдение сроков подачи, что позволяет избежать штрафов, доначислений и претензий со стороны контролирующих органов. Обеспечиваем полное сопровождение процесса — от сбора исходных данных до подтверждения успешной сдачи отчетности.\n\n<b>От 50 BYN/отчет</b>",
                                     'by': "<b>Падрыхтоўка і здача справаздачнасці</b>\n\nППрафесійная паслуга па фарміраванні, праверцы і своечасовай падачы ўсёй неабходнай бухгалтарскай, падатковай і статыстычнай справаздачнасці. Мы рыхтуем справаздачы ў адпаведнасці з патрабаваннямі заканадаўства і індывідуальнымі асаблівасцямі вашай дзейнасці, у тым ліку дэкларацыі па ПДВ, прыбытку, падатку на даходы фізічных асоб, страхавыя ўзносы, бухгалтарскую (фінансавую) справаздачнасць і справаздачы ў органы статыстыкі. Кантралюем карэктнасць разлікаў і выкананне тэрмінаў падачы, што дазваляе пазбегнуць штрафаў, даналічэнняў і прэтэнзій з боку кантралюючых органаў. Забяспечваем поўнае суправаджэнне працэсу — ад збору зыходных дадзеных да пацверджання паспяховай здачы справаздачнасці.\n\n<b>Ад 50 BYN/справаздача</b>"},
        'document_development':     {'en': "<b>Document development</b>\n\nA service for preparing documents necessary for the effective and legal operation of a company. We develop accounting policies for the purposes of accounting and tax accounting, regulations on documents and document flow, job descriptions, regulations, orders, regulations on remuneration, bonuses, business trips and other internal acts. All documents are drawn up taking into account current legislation, the specifics of your activities and the structure of the organization. Properly executed internal documents ensure order in management, reduce legal risks and help to successfully pass inspections by regulatory authorities.\n\n<b>From 25 BYN/doc.</b>",          
                                     'ru': "<b>Разработка документов</b>\n\nУслуга по подготовке документов, необходимых для эффективной и законной деятельности компании. Мы разрабатываем учетную политику для целей бухгалтерского и налогового учета, положения о документах и документообороте, должностные инструкции, регламенты, приказы, положения об оплате труда, премировании, командировках и другие внутренние акты. Все документы составляются с учетом действующего законодательства, специфики вашей деятельности и структуры организации. Грамотно оформленные внутренние документы обеспечивают порядок в управлении, снижают юридические риски и помогают успешно пройти проверки контролирующих органов.\n\n<b>От 25 BYN/док.</b>",
                                     'by': "<b>Распрацоўка дакументаў</b>\n\nПаслуга па падрыхтоўцы дакументаў, неабходных для эфектыўнай і законнай дзейнасці кампаніі. Мы распрацоўваем уліковую палітыку для мэт бухгалтарскага і падатковага ўліку, палажэнні аб дакументах і дакументазвароце, службовыя інструкцыі, рэгламенты, загады, палажэнні аб аплаце працы, прэміраванні, камандзіроўках і іншыя ўнутраныя акты. Усе дакументы складаюцца з улікам дзейнага заканадаўства, спецыфікі вашай дзейнасці і структуры арганізацыі. Пісьменна аформленыя ўнутраныя дакументы забяспечваюць парадак ва ўпраўленні, зніжаюць юрыдычныя рызыкі і дапамагаюць паспяхова прайсці праверкі кантралюючых органаў.\n\n<b>Ад 25 BYN/док.</b>"},
        'consulting':               {'en': "<b>Consulting</b>\n\nProfessional consulting on accounting and personnel records. We provide qualified explanations on complex and controversial situations, help to correctly apply the norms of legislation. We consult on accounting of transactions, preparation of reports, changes in the tax system, documentation, settlements with personnel and interaction with regulatory authorities. Support can be provided both on a one-time basis and on an ongoing basis. Our recommendations help to make informed management decisions and ensure the stability of the company's financial and accounting system.\n\n<b>From 50 BYN/hour.</b>",          
                                     'ru': "<b>Консультирование</b>\n\nПрофессиональный консалтинг по вопросам бухгалтерского и кадрового учета. Мы предоставляем квалифицированные разъяснения по сложным и спорным ситуациям, помогаем правильно применять нормы законодательства. Консультируем по вопросам учета операций, подготовки отчетности, изменения системы налогообложения, ведения документации, расчетов с персоналом и взаимодействия с контролирующими органами. Поддержка может оказываться как в разовом формате, так и на постоянной основе. Наши рекомендации помогают принимать обоснованные управленческие решения и обеспечивают стабильность финансовой и учетной системы компании.\n\n<b>От 50 BYN/час.</b>",
                                     'by': "<b>Кансультаванне</b>\n\nПрафесійны кансалтынг па пытаннях бухгалтарскага і кадравага ўліку. Мы даем кваліфікаваныя тлумачэнні па складаных і спрэчных сітуацыях, дапамагаем правільна прымяняць нормы заканадаўства. Кансультуем па пытаннях уліку аперацый, падрыхтоўкі справаздачнасці, змены сістэмы падаткаабкладання, вядзенні дакументацыі, разлікаў з персаналам і ўзаемадзеянні з кантралюючымі органамі. Падтрымка можа аказвацца як у разавым фармаце, так і на сталай аснове. Нашы рэкамендацыі дапамагаюць прымаць абгрунтаваныя кіраўнічыя рашэнні і забяспечваюць стабільнасць фінансавай і ўліковай сістэмы кампаніі.\n\n<b>Ад 50 BYN/гадзіну.</b>"},
    }
}


def tr(section, key, lang):
    return translations[section][key].get(lang, translations[section][key]['en'])




# ——— In-memory user language store —————————————————————————————
user_langs = {}




# ——— Keyboards ———————————————————————————————————————————————
def language_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add("Русский","Беларуская","English" )
    return kb


def create_main_menu(lang):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        types.KeyboardButton(tr('menu','services', lang)),
        types.KeyboardButton(tr('menu','contacts', lang)),
        types.KeyboardButton(tr('menu','sign_up',  lang)),
    )
    return kb






def create_back_menu(lang):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(tr('menu','back', lang)))
    return kb


def create_services_menu(lang):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(tr('menu','restoration', lang)),
           types.KeyboardButton(tr('menu','maintaining_accounting', lang)),
           types.KeyboardButton(tr('menu','personnel_accounting', lang)),
           types.KeyboardButton(tr('menu','submission_of_reports', lang)),
           types.KeyboardButton(tr('menu','document_development', lang)),
           types.KeyboardButton(tr('menu','consulting', lang)),
           types.KeyboardButton(tr('menu','back', lang)),
           )
    return kb





# ——— Handlers ———————————————————————————————————————————————
@bot.message_handler(commands=['start'])
def cmd_start(msg):
    bot.send_message(
        msg.chat.id,
        f"{translations['messages']['choose_lang']['ru']}\n{translations['messages']['choose_lang']['by']}\n{translations['messages']['choose_lang']['en']}",
        reply_markup=language_menu()
    )


@bot.message_handler(func=lambda m: m.text in ("English", "Русский","Беларуская"))
def set_language(msg):
 if msg.text == "English":
    lang = 'en'
 elif msg.text == "Русский":
    lang = 'ru'
 elif msg.text == "Беларуская":
    lang = 'by'
 user_langs[msg.chat.id] = lang
 bot.send_message(
        msg.chat.id,
        tr('messages','start', lang),
        reply_markup=create_main_menu(lang),parse_mode="html"
    )


@bot.message_handler(func=lambda m: True, content_types=['text'])
def text_handler(msg):
    lang = user_langs.get(msg.chat.id, 'en')
    text = msg.text.strip().lower()

    if text == tr('menu','back', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','what_interest', lang),
                         reply_markup=create_main_menu(lang))


    elif text == tr('menu','services', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','services', lang),
                         reply_markup=create_services_menu(lang))


    elif text == tr('menu','contacts', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','contacts', lang),
                         reply_markup=create_main_menu(lang), parse_mode='html')


    elif text == tr('menu','consulting', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','consulting', lang),
                         reply_markup=create_services_menu(lang), parse_mode="html")


    elif text == tr('menu','document_development', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','document_development', lang),
                         reply_markup=create_services_menu(lang), parse_mode="html")


    elif text == tr('menu','restoration', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','restoration', lang),
                         reply_markup=create_services_menu(lang), parse_mode="html")


    elif text == tr('menu','maintaining_accounting', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','maintaining_accounting', lang),
                         reply_markup=create_services_menu(lang), parse_mode="html")


    elif text == tr('menu','personnel_accounting', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','personnel_accounting', lang),
                         reply_markup=create_services_menu(lang), parse_mode="html")


    elif text == tr('menu','submission_of_reports', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','submission_of_reports', lang),
                         reply_markup=create_services_menu(lang), parse_mode="html")


    elif text == tr('menu','sign_up', lang).lower():
        bot.send_message(msg.chat.id,
                         tr('messages','enter_something', lang),
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, forward)



    else:
        bot.send_message(msg.chat.id,
                         tr('messages','what_interest', lang),
                         reply_markup=create_main_menu(lang))

def forward(msg):
    lang = user_langs.get(msg.chat.id, 'en')
    bot.forward_message(chat_id='-4756139137',
                        from_chat_id=msg.chat.id,
                        message_id=msg.message_id)
    bot.send_message(msg.chat.id,
                     tr('messages','last_message', lang),
                     reply_markup=create_main_menu(lang))

bot.infinity_polling()
