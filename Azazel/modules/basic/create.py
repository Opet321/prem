# if you can read this, this meant you use code from Ubot | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Ubot and Ram doesn't care about credit
# at least we are know as well
# who Ubot and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Ubot | Ram Team
from pyrogram import Client, filters
from pyrogram.types import Message
from . import *
from ubotlibs.ubot.helper import edit_or_reply



@Ubot(["buat"], "")
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.reply(f"**buat gc => Untuk Membuat Grup, buat ch => Untuk Mebuat Channel**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.edit("`Processing...`")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"**Successfully Created Telegram Group: [{group_name}]({link.invite_link})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"**Successfully Created Telegram Channel: [{group_name}]({link.invite_link})**",
            disable_web_page_preview=True,
        )




add_command_help(
    "Buat",
    [
        [f"buat gc atau ch", "Membuat Channel atau Group"],
    ],
)
