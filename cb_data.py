from botbtns import *

API_ID = 16514976
API_HASH = '40bd8634b3836468bb2fb7eafe39d81a'

TOKEN = '5661363625:AAEyBehhT25zbPnkWnAc_n15gCWKlseez6c'


@app.on_callback_query(filters.regex('about_data'))
async def query_handler(_, query):
    name = query.from_user.first_name
    await query.message.edit(
        text=f'<b>{about_txt}</b>'.format(name), reply_markup=about_btns, disable_web_page_preview=True)


@app.on_callback_query(filters.regex('back_data'))
async def back_handler(_, query):
    name = query.from_user.first_name
    await query.message.edit(text=start_msg_txt.format(name), reply_markup=start_btns, disable_web_page_preview=True)

@app.on_callback_query(filters.regex('help_data'))
async def back_handler(_, query):
    name = query.from_user.first_name
    await query.message.edit(text=commands.format(name), reply_markup=about_btns, disable_web_page_preview=True)


@app.on_callback_query(filters.regex('connect_api'))
async def connect_handler(_, query):
    await query.message.edit(
        text=connect_txt, reply_markup=connect_btns, disable_web_page_preview=True)
