import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from ubotlibs.ubot.helper import edit_or_reply, ReplyCheck
from ubotlibs.ubot.utils import extract_user
from . import *

@Ubot(["jamet"], "")
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await message.reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "**WOII**")
    await asyncio.sleep(1.5)
    await xx.edit("**JAMET**")
    await asyncio.sleep(1.5)
    await xx.edit("**CUMA MAU BILANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH SO ASIK**")
    await asyncio.sleep(1.5)
    await xx.edit("**EMANG KENAL?**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH REPLY**")
    await asyncio.sleep(1.5)
    await xx.edit("**KITA BUKAN KAWAN**")
    await asyncio.sleep(1.5)
    await xx.edit("**GASUKA PC ANJING**")
    await asyncio.sleep(1.5)
    await xx.edit("**BOCAH KAMPUNG**")
    await asyncio.sleep(1.5)
    await xx.edit("**MENTAL TEMPE**")
    await asyncio.sleep(1.5)
    await xx.edit("**LEMBEK NGENTOT🔥**")


@Ubot(["ywc"], "")
async def ywc(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ok sama sama",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["pp"], "")
async def toxicpp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["dp"], "")
async def toxicdp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["so"], "")
async def toxicso(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["nb"], "")
async def toxicnb(client: Client, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MAEN BOT MULU ALAY NGENTOTT, KESANNYA NORAK GOBLOK!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["met"], "")
async def toxicmet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["war"], "")
async def toxicwer(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN.",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["wartai"], "")
async def toxicwartai(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["kismin"], "")
async def toxickismin(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["ded"], "")
async def toxicded(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["sokab"], "")
async def toxicsokab(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["gembel"], "")
async def toxicgembel(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["cuih"], "")
async def toxiccuih(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["dih"], "")
async def toxicdih(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["gc"], "")
async def toxicgcs(client: Client, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["skb"], "")
async def toxicskb(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Ubot(["virtual"], "")
async def toxicvirtual(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "**OOOO**")
    await asyncio.sleep(1.5)
    await xx.edit("**INI YANG VIRTUAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**YANG KATANYA SAYANG BANGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TAPI TETEP AJA DI TINGGAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**NI INGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**APALAGI OMONGANNYA**")
    await asyncio.sleep(1.5)
    await xx.edit("**BHAHAHAHA**")
    await asyncio.sleep(1.5)
    await xx.edit("**KASIAN MANA MASIH MUDA**")


add_command_help(
    "Toxic",
    [
        ["jamet", "Menghina Jamet telegram"],
        ["pp", "Menghina Jamet telegram yang ga pake foto profil."],
        ["dp", "Menghina Jamet muka hina!"],
        ["so", "Ngeledek orang sokab."],
        ["nb", "Ngeledek orang norak baru pake bot."],
        ["skb", "Ngeledek orang sokab versi 2."],
        ["met", "Ngeledek si jamet caper."],
        ["war", "Ngeledek orang so keras ngajak war."],
        ["wartai", "Ngeledek orang so ketrigger ngajak cod minta sharelok."],
        ["kismin", "Ngeledek orang kismin so jagoan di tele."],
        ["ded", "Nyuruh orang mati aja goblok wkwk."],
        ["sokab", "Ngeledek orang so kenal so dekat padahal kga kenal goblok."],
        ["gembel", "Ngeledek bapaknya si jamet."],
        ["cuih", "Ngeludahin keluarganya satu satu wkwk."],
        ["dih", "Ngeledek anak haram."],
        ["gc", "Ngeledek gc sampah."],
    ],
)
