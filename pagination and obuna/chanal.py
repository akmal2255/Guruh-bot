from aiogram.filters import Filter
from config import Kanal_id
from aiogram import Bot
from aiogram.types import Message, CallbackQuery


class ChekSubChannel(Filter):
    async def __call__(self, message: Message, bot:Bot):
        user_status = await bot.get_chat_member(Kanal_id, message.from_user.id)
        if user_status.status in ['creator', 'administrator', 'member']:
            return False
        return True
    
class ChekSubChannel1(Filter):
    async def __call__(self, call: CallbackQuery, bot:Bot):
        user_status = await bot.get_chat_member(Kanal_id, call.from_user.id)
        if user_status.status in ['creator', 'administrator', 'member']:
            return False
        return True