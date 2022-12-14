from PyLyrics import *
from . import *

@beast.on(beastx_cmd(pattern="singer (.*)"))
async def _(event):
    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)

    try:
        song = input_str.split("-")
        if len(song) == 1:
            await event.edit("Usage: .singer Duman - Haberin Yok Ölüyorum")
        else:
            await event.edit("🔍︎Searching lyrics By Fire-x")
            lyrics = PyLyrics.getLyrics(song[0].strip(), song[1].strip()).split("\n")
            lyric_message = f"Singing {song[0].strip()} from {song[1].strip()} 🎙"
            lyric_message += "\n\n" + "\n".join(lyrics)
            try:
                await event.edit(lyric_message)
            except:
                # TODO: send as file
                logger.info(lyric_message)
    except ValueError:
        await event.edit("Song not found")
