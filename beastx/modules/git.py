import asyncio

from telethon import events

from . import *

@beast.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "githubs":

        await event.edit(input_str)

        animation_chars = [
            "https://github.com/msy1717/Beast-X",
            "https://github.com/msy1717/Beast-X",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 2])


CMD_HELP.update(
    {
        "git": "**Git**\
\n\n**Syntax : **`.githubs`\
\n**Usage :** Provides repository link."
    }
)
