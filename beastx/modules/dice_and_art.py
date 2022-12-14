from telethon.tl.types import InputMediaDice

from . import *
# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
DICE_E_MOJI = "🎲"
BALL_E_MOJI = "🏀"
# EMOJI CONSTANTS


@beast.on(beastx_cmd(pattern=f"({DART_E_MOJI}|{DICE_E_MOJI}|{BALL_E_MOJI}) ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except:
            pass


CMD_HELP.update(
    {
        "diceandart": "**Diceandart**\
\n\n**Syntax : **`.🏀`\
\n**Usage :** Creates a basket ball game.\
\n\n**Syntax : **`.🎲`\
\n**Usage :** Creates a dice game.\
\n\n**Syntax : **`.🎯`\
\n**Usage :** Creates a dart game. ."
    }
)
