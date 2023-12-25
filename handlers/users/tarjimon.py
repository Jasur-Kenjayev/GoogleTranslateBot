import logging
from loader import dp
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.inline.tarjimonkeyboard import categoryMenu
from keyboards.inline.back import Back
from aiogram.dispatcher import FSMContext
from states.statee import new

translator = Translator()

@dp.callback_query_handler(text_contains="backs",state=new)
async def backs(call: CallbackQuery,state: FSMContext):
	await state.finish()
	await call.message.answer("<i>Tarjima qilish uchun kerakli tilni tanlang!</i>",reply_markup=categoryMenu)
	
	
@dp.callback_query_handler(text_contains="uzen")
async def uzen(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzen.set()

@dp.message_handler(state=new.uzen)
async def enuzz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='en')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)

@dp.callback_query_handler(text_contains="enuz")
async def enuz(call: CallbackQuery):
    await call.message.answer("<i>✏️Enter text to translate....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.enuz.set()

@dp.message_handler(state=new.enuz)
async def enuzz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='en', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="ruuz")
async def ruuzz(call: CallbackQuery):
    await call.message.answer("<i>✏️Введите текст для перевода....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.ruuz.set()

@dp.message_handler(state=new.ruuz)
async def ruuz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='ru', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="uzru")
async def uzruu(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzru.set()

@dp.message_handler(state=new.uzru)
async def uzru(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='ru')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="uzge")
async def uzde(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzge.set()

@dp.message_handler(state=new.uzge)
async def deuz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='de')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="geuz")
async def geruz(call: CallbackQuery):
    await call.message.answer("<i>✏️Geben Sie den zu übersetzenden Text ein....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.geuz.set()

@dp.message_handler(state=new.geuz)
async def uzger(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='de', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="aruz")
async def aruz(call: CallbackQuery):
    await call.message.answer("<i>✏️ أدخل نصًا للترجمة....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.aruz.set()

@dp.message_handler(state=new.aruz)
async def uzar(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='ar', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="uzar")
async def uzarb(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzar.set()

@dp.message_handler(state=new.uzar)
async def arbuz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='ar')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)

@dp.callback_query_handler(text_contains="uztur")
async def uztr(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uztur.set()

@dp.message_handler(state=new.uztur)
async def truz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='tr')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)

@dp.callback_query_handler(text_contains="turuz")
async def truzb(call: CallbackQuery):
    await call.message.answer("<i>✏️Çevirmek için metni girin....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.turuz.set()

@dp.message_handler(state=new.turuz)
async def uzbtr(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='tr', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="hiuz")
async def hiuz(call: CallbackQuery):
    await call.message.answer("<i>️ ✏️अनुवाद करने के लिए टेक्स्ट दर्ज करें....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.hiuz.set()

@dp.message_handler(state=new.hiuz)
async def uzhi(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='hi', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)

@dp.callback_query_handler(text_contains="uzhi")
async def uzhin(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzhi.set()

@dp.message_handler(state=new.uzhi)
async def hinuz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='hi')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="uzfr")
async def uzfr(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzfr.set()

@dp.message_handler(state=new.uzfr)
async def fruz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='fr')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="fruz")
async def fruzb(call: CallbackQuery):
    await call.message.answer("<i>✏️Entrez le texte à traduire....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.fruz.set()

@dp.message_handler(state=new.fruz)
async def uzbfr(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='fr', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)

@dp.callback_query_handler(text_contains="chsmuz")
async def zhcnuz(call: CallbackQuery):
    await call.message.answer("<i>✏️输入要翻译的文字....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.chsmuz.set()

@dp.message_handler(state=new.chsmuz)
async def zhcn_uz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='zh-cn', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="uzchsm")
async def zhcn_uzb(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzchsm.set()

@dp.message_handler(state=new.uzchsm)
async def zhcn_uzb(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='zh-cn')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="uzchtr")
async def zhtw_uz(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzchtr.set()

@dp.message_handler(state=new.uzchtr)
async def uz_zhtw(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='zh-tw')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)

@dp.callback_query_handler(text_contains="chtruz")
async def zhtw_uzb(call: CallbackQuery):
    await call.message.answer("<i>✏️輸入要翻譯的文字....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.chtruz.set()

@dp.message_handler(state=new.chtruz)
async def uzb_zhtw(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='zh-tw', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="tjuz")
async def tguz(call: CallbackQuery):
    await call.message.answer("<i>✏️Барои тарҷума матнро ворид кунед....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.tjuz.set()

@dp.message_handler(state=new.tjuz)
async def uztg(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='tg', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="uztj")
async def uz_tg(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uztj.set()

@dp.message_handler(state=new.uztj)
async def tg_uz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='tg')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)

@dp.callback_query_handler(text_contains="uzkg")
async def uzky(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzkg.set()

@dp.message_handler(state=new.uzkg)
async def kyuz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='ky')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="kguz")
async def ky_uz(call: CallbackQuery):
    await call.message.answer("<i>✏️Котормо үчүн текстти киргизүү үчүн....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.kguz.set()

@dp.message_handler(state=new.kguz)
async def uz_ky(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='ky', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="kouz")
async def kouz(call: CallbackQuery):
    await call.message.answer("<i>✏️번역할 텍스트를 입력하세요....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.kouz.set()

@dp.message_handler(state=new.kouz)
async def uzko(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='ko', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="uzko")
async def uz_ko(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzko.set()

@dp.message_handler(state=new.uzko)
async def ko_uz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='ko')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)

@dp.callback_query_handler(text_contains="uzka")
async def uzkk(call: CallbackQuery):
    await call.message.answer("<i>✏️Tarjima qilish uchun matin kiriting....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.uzka.set()

@dp.message_handler(state=new.uzka)
async def kkuz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='uz', dest='kk')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)
	
@dp.callback_query_handler(text_contains="kauz")
async def uz_kk(call: CallbackQuery):
    await call.message.answer("<i>✏️Аудару үшін мәтінді енгізіңіз....</i>",reply_markup=Back)
    await call.message.delete()
    await call.answer(cache_time=60)
    await new.kauz.set()

@dp.message_handler(state=new.kauz)
async def kk_uz(message: Message,state: FSMContext):
	text = message.text
	translated = translator.translate(text, src='kk', dest='uz')
	await message.reply(f"<b>{translated.text}</b>",reply_markup=Back)


