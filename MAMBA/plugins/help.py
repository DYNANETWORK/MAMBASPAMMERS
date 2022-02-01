from MAMBA import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from MAMBA import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/a8a793a8716bdcc923fd3.jpg"

MAMBA_Help = "🔥 ʍǟʍɮǟ ֆքǟʍʍɛʀֆ 🔥\n\n"
 
MAMBA_Help += f"_ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ʍǟʍɮǟ ֆքǟʍʍɛʀֆ ɮօȶ__\n\n"

MAMBA_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

MAMBA_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots \n `.addecho` - to addecho \n `.rmecho` - To remove Echo \n `.addsudo` - To add sudo user using spam bot \n\n"
 
MAMBA_Help += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"

MAMBA_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
MAMBA_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

MAMBA_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"

MAMBA_Help += f" .mambaspam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"

MAMBA_Help += f"© @BLACKMAMBA_OFFICIAL\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=MAMBA_Help,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/MAMBA_NETWORK")
        ] 
        ]
        )                                                         
