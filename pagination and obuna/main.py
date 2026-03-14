import logging
import asyncio
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from config import token, Kanal_id
from aiogram.filters import CommandStart
from buttons import menyu, obuna
from db import rasmlar
from chanal import ChekSubChannel, ChekSubChannel1


logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
bot = Bot(token=token)


@dp.message(CommandStart())
async def StartBot1(message: Message):
    user_status = await bot.get_chat_member(Kanal_id, message.from_user.id)
    # if user_status.status in ['creator', 'administrator', 'member']:
    #     await message.answer_photo(photo="https://t3.ftcdn.net/jpg/10/23/17/04/360_F_1023170496_zQqTluLQsqFBAkxk2veiOdhZsU8RHsUT.jpg", caption="Rasmlar", reply_markup=menyu(cnt=1))
    # else:
    #     await message.answer("kanalga obuna bo'ling", reply_markup=obuna)





@dp.message(ChekSubChannel())
async def TekBot(message: Message):
    await message.answer("kanalga obuna bo'ling", reply_markup=obuna)

@dp.message()
async def EchoBot(message: Message):
    await message.copy_to(message.from_user.id)


@dp.callback_query(ChekSubChannel1())
async def TekBot(call:CallbackQuery):
    await call.message.answer("kanalga obuna bo'ling", reply_markup=obuna)


@dp.callback_query(F.data == 'tek')
async def ObunTek(call: CallbackQuery):
    await call.answer("obuna bo'lgansiz", show_alert=True)


@dp.callback_query(F.data)
async def PaginationBot(call: CallbackQuery):
    user_status = await bot.get_chat_member(Kanal_id, call.from_user.id)
    if user_status.status in ['creator', 'administrator', 'member']:
        xabar = call.data.split("_")
        print(xabar)
        if len(xabar) == 2:
            await call.message.edit_media(InputMediaPhoto(media=rasmlar[int(xabar[-1])], caption=f"Rasmlar {xabar[-1]}"), reply_markup=menyu(int(xabar[-1])))
    else:
        await call.message.answer("kanalga obuna bo'ling", reply_markup=obuna)

    


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")