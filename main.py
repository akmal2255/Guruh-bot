import logging
import asyncio
from aiogram.types import Message, ChatPermissions
from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, and_f
from config import bot_token
import time

logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token)
dp = Dispatcher()



@dp.message(CommandStart())
async def StartBot(message: Message):
    await message.answer("Assalomu alaykum")


@dp.message(F.chat.type =='supergroup', and_f(F.text=="yozma", F.reply_to_message))
async def YozmaBot(message: Message):
    id = message.reply_to_message.from_user.id
    huquq = ChatPermissions(can_send_messages=False)
    await message.chat.restrict(id, huquq)
    await message.answer(f"guruhga yozmang\n{message.reply_to_message.from_user.full_name}")


@dp.message(F.chat.type =='supergroup', and_f(F.text=="yoz", F.reply_to_message))
async def YozBot(message: Message):
    id = message.reply_to_message.from_user.id
    huquq = ChatPermissions(can_send_messages=True)
    await message.chat.restrict(id, huquq)
    await message.answer(f"guruhga Yozavering\n{message.reply_to_message.from_user.full_name}")





@dp.message(F.chat.type == "supergroup",and_f(F.text == "ban", F.reply_to_message))
async def get_bann_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.ban_sender_chat(user_id)
   await message.answer(f"Siz guruhdan haydaldingiz\n ❌ {message.reply_to_message.from_user.full_name}")



@dp.message(F.chat.type == "supergroup",and_f(F.text == "unban", F.reply_to_message))
async def get_unbann_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.unban_sender_chat(user_id)
   await message.answer(f"Siz endi guruhga qo'shila olasiz\n 🆗 {message.reply_to_message.from_user.full_name}")





@dp.message(F.chat.type == "supergroup", F.new_chat_members)
async def AddPerson(message:Message):
    for new in message.new_chat_members:
        await message.answer(f"Guruhga xush kelibsiz bro\n{new.full_name}")

@dp.message(F.chat.type == "supergroup", F.left_chat_member)
async def AddPerson(message:Message):
    await message.answer(f"guruhga kelib turing biz sizni soginamiz\n{message.left_chat_member.full_name}")



# @dp.message(F.chat.type=="supergroup")
# async def GuruhBot(message: Message):
#     id = message.from_user.id
#     huquq = ChatPermissions(can_send_messages=False)
#     await message.chat.restrict(id, huquq)
#     # reklama = ["https://t.me/", 't.me/', 'https://']
#     name = message.chat.title
#     ty = message.chat.type
#     # xabar = message.text
#     # for i in reklama:
#     #     if xabar.startswith(i):
#     #         await message.delete()
#     #         await message.answer("reklama yubormang")
#     time.sleep(5)
#     huquq = ChatPermissions(can_send_messages=True)
#     await message.chat.restrict(id, huquq)    
#     await message.answer(f"Biz sizni eshtamiz\n{name}\n{ty}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")