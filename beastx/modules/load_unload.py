from beastx.utils import load_module, remove_plugin
from . import *

@beast.on(beastx_cmd(pattern="load ?(.*)", outgoing=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        try:
            remove_plugin(shortname)
        except:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(
            f"Could not load {shortname} because of the following error.\n{str(e)}"
        )


@beast.on(beastx_cmd(pattern="unload ?(.*)", outgoing=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        remove_plugin(shortname)
        await event.edit(f"Unloaded {shortname} successfully")
    except Exception as e:
        await event.edit(
            "Successfully unload {shortname}\n{}".format(shortname, str(e))
        )
