class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
I am <a href=https://t.me/{}>{}</a>, 

You can use me for mainly download movies , And also I have many more features like add filters, fetch movies info from imdb and other sources.My creaters are also planning for add many more features for me.

ඔබට ප්‍රධාන වශයෙන් චිත්‍රපට download කිරිම සඳහා මාව භාවිතා කළ හැක,තවද සමූහවල filters  එකතු කිරීම , imdb සහ වෙනත් මූලාශ්‍රවලින් චිත්‍රපට තොරතුරු ලබා ගැනීම වැනි තවත් බොහෝ විශේෂාංග මා සතුව ඇත.ඒ වගේම මගේ නිර්මාණකරුවන් මා වෙනුවෙන් තවත් බොහෝ විශේෂාංග එකතු කිරීමට සැලසුම් කරමින් සිටිති.
 

꧁༒☬𝓐𝓭𝓭 𝓶𝓮 𝓽𝓸 𝔂𝓸𝓾𝓻 𝓰𝓻𝓸𝓾𝓹𝓼 𝓪𝓷𝓭 𝓼𝓮𝓮 𝓶𝔂 𝓹𝓸𝔀𝓮𝓻𝓼☬༒꧂

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­ """
    HELP_TXT = """Hi {}
These buttons will be help you to know more about me,

පහත බටන් මා පිළිබදව අවබෝධයක් ලබා ගැනීම සදහා උදව් වනු ඇත.

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­
"""
    ABOUT_TXT = """🔘 I am {}
🔘 My creters are <a href=https://t.me/slofficialcommunity>SLOFFICIAL</a>
🔘 I am using Pyrogram library.
🔘 My language is python.
🔘 I am stored in MONGO DB.
🔘 I was built in RAILWAY.

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­
"""
    SOURCE_TXT = """<b>NOTE:</b>
- Xandria is a copied source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Xandra should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Xandria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/xandria_roBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.
 
 <a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
    STATUS_TXT = """🟡 Total files: <code>{}</code>
🟡 Total users: <code>{}</code>
🟡 Total chats: <code>{}</code>
🟡 Used storage: <code>{}</code> 𝙼𝚒𝙱
🟡 Free storage: <code>{}</code> 𝙼𝚒𝙱

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}

<a href=https://t.me/slofficialmain> ‌‌‌‌©️ＳＬＯＦＦＩＣＩＡＬ ­</a> ­"""
