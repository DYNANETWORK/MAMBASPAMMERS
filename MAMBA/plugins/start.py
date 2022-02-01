import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from MAMBA import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, BOT10, BOT11, BOT12, BOT13, BOT14, BOT15, BOT16, BOT17, BOT18, BOT19,BOT20, BOT21, BOT22, BOT23, BOT24, BOT25, BOT26, BOT27, BOT28, BOT29, BOT30, BOT31, BOT32, BOT33, BOT34, BOT35, BOT36, BOT37, BOT38, BOT39, BOT40, BOT41, BOT42, BOT43, BOT44, BOT45, BOT46, BOT47, BOT48, BOT49, BOT50, BOT51, BOT52, BOT53, BOT54, BOT55, BOT56, BOT57, BOT58, BOT59, BOT60, ALIVE_PIC, OWNER_ID

MAMBA_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/a8a793a8716bdcc923fd3.jpg"

MAMBA_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/MAMBA_NETWORK")
        ],
        [
        Button.url("• ᴍᴀɪɴᴛᴀɪɴ ʙʏ •", "https://t.me/BLACKMAMBA_OFFICIAL")
        ]
        ]
               
MAMBAX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/MAMBA_NETWORK"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/MAMBA_X_SUPPORT")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/SUKHPL443/MAMBASPAMMERS")
        ]
        ]
        
        
#USERS 


@BOT0.on(events.NewMessage(pattern="/start"))
@BOT1.on(events.NewMessage(pattern="/start"))
@BOT2.on(events.NewMessage(pattern="/start"))
@BOT3.on(events.NewMessage(pattern="/start"))
@BOT4.on(events.NewMessage(pattern="/start"))
@BOT5.on(events.NewMessage(pattern="/start"))
@BOT6.on(events.NewMessage(pattern="/start"))
@BOT7.on(events.NewMessage(pattern="/start"))
@BOT8.on(events.NewMessage(pattern="/start"))
@BOT9.on(events.NewMessage(pattern="/start"))
@BOT10.on(events.NewMessage(pattern="/start"))
@BOT11.on(events.NewMessage(pattern="/start"))
@BOT12.on(events.NewMessage(pattern="/start"))
@BOT13.on(events.NewMessage(pattern="/start"))
@BOT14.on(events.NewMessage(pattern="/start"))
@BOT15.on(events.NewMessage(pattern="/start"))
@BOT16.on(events.NewMessage(pattern="/start"))
@BOT17.on(events.NewMessage(pattern="/start"))
@BOT18.on(events.NewMessage(pattern="/start"))
@BOT19.on(events.NewMessage(pattern="/start"))
@BOT20.on(events.NewMessage(pattern="/start"))
@BOT21.on(events.NewMessage(pattern="/start"))
@BOT22.on(events.NewMessage(pattern="/start"))
@BOT23.on(events.NewMessage(pattern="/start"))
@BOT24.on(events.NewMessage(pattern="/start"))
@BOT25.on(events.NewMessage(pattern="/start"))
@BOT26.on(events.NewMessage(pattern="/start"))
@BOT27.on(events.NewMessage(pattern="/start"))
@BOT28.on(events.NewMessage(pattern="/start"))
@BOT29.on(events.NewMessage(pattern="/start"))
@BOT30.on(events.NewMessage(pattern="/start"))
@BOT31.on(events.NewMessage(pattern="/start"))
@BOT33.on(events.NewMessage(pattern="/start"))
@BOT33.on(events.NewMessage(pattern="/start"))
@BOT34.on(events.NewMessage(pattern="/start"))
@BOT35.on(events.NewMessage(pattern="/start"))
@BOT36.on(events.NewMessage(pattern="/start"))
@BOT37.on(events.NewMessage(pattern="/start"))
@BOT38.on(events.NewMessage(pattern="/start"))
@BOT39.on(events.NewMessage(pattern="/start"))
@BOT40.on(events.NewMessage(pattern="/start"))
@BOT41.on(events.NewMessage(pattern="/start"))
@BOT42.on(events.NewMessage(pattern="/start"))
@BOT43.on(events.NewMessage(pattern="/start"))
@BOT44.on(events.NewMessage(pattern="/start"))
@BOT45.on(events.NewMessage(pattern="/start"))
@BOT46.on(events.NewMessage(pattern="/start"))
@BOT47.on(events.NewMessage(pattern="/start"))
@BOT48.on(events.NewMessage(pattern="/start"))
@BOT49.on(events.NewMessage(pattern="/start"))
@BOT50.on(events.NewMessage(pattern="/start"))
@BOT51.on(events.NewMessage(pattern="/start"))
@BOT52.on(events.NewMessage(pattern="/start"))
@BOT53.on(events.NewMessage(pattern="/start"))
@BOT54.on(events.NewMessage(pattern="/start"))
@BOT55.on(events.NewMessage(pattern="/start"))
@BOT56.on(events.NewMessage(pattern="/start"))
@BOT57.on(events.NewMessage(pattern="/start"))
@BOT58.on(events.NewMessage(pattern="/start"))
@BOT59.on(events.NewMessage(pattern="/start"))
@BOT60.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       MAMBABot = await event.client.get_me()
       bot_id = MAMBABot.first_name
       bot_username = MAMBABot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheMAMBA = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheMAMBA,
                  MAMBA_IMG,
                  caption=ownermsg, 
                  buttons=MAMBA_Button)
       else:
            await event.client.send_file(TheMAMBA,
                  MAMBA_IMG,
                  caption=usermsg, 
                  buttons=MAMBAX_Button)
                
