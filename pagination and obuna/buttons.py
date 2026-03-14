from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db import rasmlar


def menyu(cnt):
    buttons = InlineKeyboardBuilder()
    if cnt > 1:
        buttons.add(InlineKeyboardButton(text=f"orqaga", callback_data=f"page_{cnt-1}"))
    buttons.add(InlineKeyboardButton(text=f"{cnt}", callback_data="page", style="danger"))
    if cnt < len(rasmlar) - 1:
        buttons.add(InlineKeyboardButton(text="oldinga", callback_data=f"page_{cnt+1}"))
    return buttons.as_markup()


obuna = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kanal", url="https://t.me/rajabov_flow")],
        [InlineKeyboardButton(text='Tekshirish', callback_data="tek")]
    ]
)