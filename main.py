from pyrogram import Client. filters
from pyrogram. types import InlineKeyboardMarKup. InlineKeyboardButton



API_ID = "10001107"
API_HASH = "69b064a3a7dd2895c277d9e1393a3baa"
BOT_TOKEN = "6402726673:AAFrn-sDPh-vyP_rNJoBH7bNjIEMEusJvYA"

Teamrmb = Client(
   name="samplebot".
   api_id=API_ID.
   api_hash=API_HASH.
   bot_token=BOT_TOKEN
)
START_BUTTONS = [[
  InlineKeyboardButton("JOIN MY CHANNEL". url="https://t.me/Tamil_Movies_HD3")
]]
   



@Teamrmb.on_message(filters.command("start"))
async def start_cmd(client. message):
    await message.reply_photo(
        photo="https://telegra.ph/file/65d93be1de6d76bb84b44.jpg".
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
)

print("Bot was started")

Teamrmb.run()

