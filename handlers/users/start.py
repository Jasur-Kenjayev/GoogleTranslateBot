import logging
import sqlite3

from aiogram import types
from data.config import CHANNELS
from keyboards.inline.subscription import check_button
from loader import bot, dp, db
from utils.misc import subscription
from keyboards.inline.tarjimonkeyboard import categoryMenu
from aiogram.types import ParseMode
from data.config import ADMINS

@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    ###
    status = await subscription.check(user_id=message.from_user.id, channel=CHANNELS[0])
    if status:
        name = message.from_user.full_name
        try:
        	db.add_user(id=message.from_user.id, name=name)
        except sqlite3.IntegrityError as err:
        	pass
        await message.answer("<i>Tarjima qilish uchun kerakli tilni tanlang!</i>",reply_markup=categoryMenu)
        count = db.count_users()[0]
        msg = f"*{message.from_user.full_name} 💡Bazaga Yangi 👤Foydalanuvchi ➕Qo'shildi. Bazada {count} ta Foydalanuvchi Bor✅*"
        await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode=ParseMode.MARKDOWN)
    else:
    ###
        channels_format = str()
        for channel in CHANNELS:
            chat = await bot.get_chat(channel)
            invite_link = await chat.export_invite_link()
            # logging.info(invite_link)
            channels_format += f"<b>📡 Kanal:</b> <a href='{invite_link}'>{chat.title}</a>\n"

        await message.answer(f"<b>🤖 Botdan to'liq fodalanish uchub quyidagi kanalga obuna bo'ling👇</b>\n\n"
                             f"{channels_format}",
                             reply_markup=check_button,
                             disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>✅ {channel.title} Kanaliga obuna bo'lgansiz botan to'liq foydalanish uchun /start bosing👇\n\n/start /start /start\n/start /start /start</b>"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>❌ {channel.title} Kanaliga obuna bo'lmagansiz. </b>"
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)
