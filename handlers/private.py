from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
      await message.reply_text(
        f"""**مرحبا انا {bn} 📢

بامكاني تشغيل الاغاني في مكالمات الكروبات 
قم برفعي  مشرف في الكروب مع البوت المساعد [اضغط هنا](https://t.me/KKFR7).

قم باضافتي الى مجموعتك لتشغيل الاغاني**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "️ المطـور ️", url="https://t.me/RRRD7")
                  ],[
                    InlineKeyboardButton(
                        " قـناة البوت ", url="https://t.me/Jmthon"
                    ),
                    InlineKeyboardButton(
                        "الـحساب المساعـد", url="https://t.me/RDRR7"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕  اضفني الى مجموعتك ➕", url="https://t.me/J0VBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** تم تفعيل البوت بنجاح ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "راسـلني", url="https://t.me/RRRD7")
                ]
            ]
        )
   )


@Client.on_message(filters.command("panel") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""** البوت يختص بتحميل والبحث عن الاغاني 🌿

ارسل يوزر البوت مع اسم الاغنيه للبحث 📢
مثال : 
@H7RBOT SAD

تستطيع تحميل الاغاني ايضا 💗
بالاوامر التاليه :
- /ytp رابط الاغنيه من اليوتيوب
- /song رابط الاغنيه من اليوتيوب

للتحكم بالاغنية داخل المكالمه الجماعيه 🔊
- /play بالرد على الاغنيه او الرابط للتشغيل
- /pause لايقاف الاغنيه موقتا داخل المكالمه
- /resume لتكمله الاغنيه المتوقفه
- /stop لايقاف البوت عن تشغيل الاغنيه
- /skip لتخطي الاغنيه الحاليه والانتقال الى الاغنيه التاليه**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📌 قنـاة الـمطور", url="https://t.me/Jmthon")
                ],[
                    InlineKeyboardButton(
                        "📢 الحساب المساعد", url="https://t.me/KKFR7"
                    )
                ]
            ]
        )
   )
