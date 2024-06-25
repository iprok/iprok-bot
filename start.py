#!/usr/bin/env python3
import asyncio
import uvloop

from pyrogram import Client

#mydev
#chat_id=-1002149471190

#poker
chat_id=-1002080270918

uvloop.install()

app = Client("my_account")

async def main():
    async with app:

#        await app.send_message("me", "Hi!")
#        await app.send_message(-1002149471190, "Hi!")
        await app.send_poll(chat_id, "Покер, четверг, Belelusso (бул. Руски, 7). 18:30", ["Да, буду в 18:30-19:00", "Да, буду в 19:00-19:15", "Да, буду еще позже или не знаю когда", "Не буду \\ Хочу увидеть результаты"],is_anonymous=False)
        await app.send_poll(chat_id, "Настолки, пятница, Belelusso (бул. Руски, 7). 19:00", ["Да, предпочитаю Манчкин", "Да, предпочитаю Bang", "Да, предпочитаю Dixit", "Да, предпочитаю Покер", "Да, предпочитаю Мафию", "Да, нет предпочтений", "Не буду \\ Хочу увидеть результаты"],is_anonymous=False)



@app.on_message()
async def hello(client, message):
    print(await client.get_me(),message)

#app.run()
app.run(main())
