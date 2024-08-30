import aiohttp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp
from dotenv import load_dotenv
import os

# .env fayldan o'zgaruvchilarni yuklash
load_dotenv()

# Asosiy API URL'ni .env fayldan olish
BASE_API_URL = os.getenv("API_URL")

# API dan ma'lumotlarni olish
async def fetch_data(endpoint):
    url = f"{BASE_API_URL}/{endpoint}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# "Arnasoy tumani" deb yozilganda qo'ng'iroq
@dp.message_handler(text="Arnasoy tumani")
async def bot_start(message: types.Message):
    data = await fetch_data("arnasoytumani/")

    # BOLIM_NOMI qiymatlarini guruhlash
    bolim_dict = {}
    for item in data:
        bolim_nomi = item.get('BOLIM_NOMI', 'N/A')
        if bolim_nomi not in bolim_dict:
            bolim_dict[bolim_nomi] = []
        bolim_dict[bolim_nomi].append(item)

    keyboard = InlineKeyboardMarkup(row_width=1)
    for bolim_nomi in bolim_dict.keys():
        button = InlineKeyboardButton(bolim_nomi, callback_data=f"show_{bolim_nomi.replace(' ', '_')}")
        keyboard.add(button)

    await message.answer("Tanlang:", reply_markup=keyboard)

# Tugmani bosilganda ma'lumotlarni ko'rsatish
@dp.callback_query_handler(lambda c: c.data.startswith('show_'))
async def process_callback(callback_query: types.CallbackQuery):
    bolim_nomi = callback_query.data.split('_', 1)[1].replace('_', ' ')

    # Ma'lumotlarni qayta olish va guruhlash
    data = await fetch_data("arnasoytumani/")  # Endpointni yangilang agar kerak bo'lsa
    bolim_items = [item for item in data if item.get('BOLIM_NOMI', 'N/A') == bolim_nomi]

    if bolim_items:
        for item in bolim_items:
            response_text = (
                f"ID: {item.get('id', 'N/A')}\n"
                f"INN: {item.get('INN', 'N/A')}\n"
                f"COATO: {item.get('COATO', 'N/A')}\n"
                f"TASHKILOT_NOMI: {item.get('TASHKILOT_NOMI', 'N/A')}\n"
                f"OKED: {item.get('OKED', 'N/A')}\n"
                f"COOGU: {item.get('COOGU', 'N/A')}\n"
                f"BOLIM_NOMI: {item.get('BOLIM_NOMI', 'N/A')}\n"
                f"LAVOZIM: {item.get('LAVOZIM', 'N/A')}\n"
                f"BOSH_ISH_ORIN_BIRLIGI: {item.get('BOSH_ISH_ORIN_BIRLIGI', 'N/A')}\n"
                f"NSKZ: {item.get('NSKZ', 'N/A')}\n"
                f"TELERAQAM1: {item.get('TELERAQAM1', 'N/A')}\n"
                f"TELERAQAM2: {item.get('TELERAQAM2', 'N/A')}\n"
                f"POCHTA_MANZIL: {item.get('POCHTA_MANZIL', 'N/A')}\n"
                f"BUDGET_0_XUSUSIY_1: {item.get('BUDGET_0_XUSUSIY_1', 'N/A')}\n"
                f"MAOSH: {item.get('MAOSH', 'N/A')}\n"
                f"LAVOZIMGA_QOYILGAN_TALABLAR: {item.get('LAVOZIMGA_QOYILGAN_TALABLAR', 'N/A')}\n"
                f"SOXA: {item.get('SOXA', 'N/A')}\n"
                f"XUDUD: {item.get('XUDUD', 'N/A')}"
            )
            await callback_query.message.answer(response_text)
    else:
        await callback_query.message.answer("Ma'lumot topilmadi.")
