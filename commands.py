#!/usr/bin/env python3
# Copyright (C) @A_l_i_y_e_v_d_i
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nIam Kanallarda və Qruplarda musiqi ifa edən MusicPlayer 24*7.\n\nMən hətta Səsli Söhbətinizdə Youtube Canlı yayımını da edə bilərəm.\və Aşağıdakı mənbə kodundan Öz botunuzu yerləşdirə bilərsiniz.\n\nMövcud əmrlər haqqında bilmək üçün /kömək et düyməsini basın.</b>"
HELP = """
**Ümumi Əmrlər:**
/play **[song name]/[yt link]**: Audio fayla cavab verin.
/dplay **[song name]:** Deezer-dən musiqi çalın.
/yplay: YouTube pleylistinin bütün mahnılarını oxutmaq üçün.
/splay <code>song name</code> Jio Saavn-dan mahnı oxumaq və ya
<code>/splay -a album name</code> jiosaavn albomundan bütün mahnıları səsləndirmək və ya
/cplay <channel istifadəçi adı və ya kanal id> telegram kanalından musiqi oxutmaq üçün.
/player:  Cari ifa olunan mahnını göstərin.
/upload: Cari ifa olunan mahnını audio fayl kimi yükləyir.
/help: Əmrlər üçün yardım göstərin.
/playlist: Pleylist göstərir

**Admin Əmrləri**:
**/skip** [n] ...  Cari və ya n olduğu yerdə keçin >= 2.
**/cplay** Kanalın musiqi fayllarından musiqi çalın.
**/yplay** YouTube pleylistindən musiqi çalın.
**/join**  Səsli söhbətə qoşulun.
**/leave**  Cari səsli söhbəti tərk edin.
**/shuffle** Pleylistləri qarışdırın.
**/vc**  Hansı VC-nin qoşulduğunu yoxlayın.
**/stop**  oynamağı dayandırın.
**/radio** Radioya başlayın.
**/stopradio** Radio axını dayandırır.
**/clearplaylist** Pleylistini silin.
**/export** Gələcək istifadə üçün cari pleylisti ixrac edin.
**/import** Əvvəllər ixrac edilmiş pleylisti idxal edin.
**/replay**  Əvvəldən oynayın.
**/clean** İstifadə edilməmiş RAW PCM fayllarını silin.
**/pause** Oynamağa fasilə verin.
**/resume** Oynamağa davam edin.
**/volume** Səs səviyyəsini dəyişdirin(0-200).
**/mute**  VC-də səssiz.
**/unmute**  VC-də səsi açın.
**/restart**  Botu yeniləyir və yenidən işə salır.
"""




@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("🔥 Source Code 🔥", url='https://github.com/ZauteKm/MusicPlayer'),
    ],
    [
        InlineKeyboardButton('👥 Group', url='https://t.me/iZaute/5'),
        InlineKeyboardButton('Channel 📢', url='https://t.me/iZaute/6'),
    ],
    [
        InlineKeyboardButton('🆘 Help & Commands 🆘', callback_data='help'),

    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton("🇦🇿🇦🇿🇦🇿", url='..'),
        ],
        [
            InlineKeyboardButton('👥 qrup', url='https://t.me/iron_Blood_Gurup/5'),
            InlineKeyboardButton('kanal 📢', url='https://t.me/Nexus_Bots/6'),
        ],
        [
            InlineKeyboardButton('🇦🇿🇦🇿🇦🇿🇦🇿', '),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await mp.delete(message)
