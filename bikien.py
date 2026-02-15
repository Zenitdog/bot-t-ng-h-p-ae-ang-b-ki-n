import discord
from discord import app_commands
from discord.ext import commands
import random

TOKEN = "MTQ2NjQyNjMwNTcyMDQ4NDA5MA.GpGBT4.zf4Z3OvpDZHnkapd_33uywMXjwA8KxmKYh--pU"
GUILD_ID = 1466420983681515531
CHANNEL_ID = 1466435508824571924  # kênh nhận đơn kiện

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# ================== READY ==================
@bot.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)
    print("✅ Bot online & slash synced")

# ================== /KIEN ==================
@bot.tree.command(name="kien", description="Gửi đơn kiện", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(
    nguoi_kien="Tên người kiện",
    nguoi_bi_kien="Tên người bị kiện",
    luat_khac="Nếu là luật khác, hãy nêu rõ",
    thoi_gian="Thời gian xảy ra vụ việc",
    tinh_huong="Trình bày rõ tình huống",
    bang_chung="Link hình ảnh / video"
)
async def kien(
    interaction: discord.Interaction,
    nguoi_kien: str,
    nguoi_bi_kien: str,
    vi_pham: str,
    luat_khac: str,
    thoi_gian: str,
    tinh_huong: str,
    bang_chung: str
):
    channel = bot.get_channel(CHANNEL_ID)

    don_id = random.randint(100000, 999999)

    embed = discord.Embed(
        title="📄 ĐƠN KIỆN MỚI",
        color=discord.Color.red()
    )
    embed.add_field(name="👤 Người kiện", value=nguoi_kien, inline=False)
    embed.add_field(name="👤 Người bị kiện", value=nguoi_bi_kien, inline=False)
    embed.add_field(name="📜 Luật khác", value=luat_khac, inline=False)
    embed.add_field(name="⏰ Thời gian", value=thoi_gian, inline=False)
    embed.add_field(name="📝 Tình huống", value=tinh_huong, inline=False)
    embed.add_field(name="📸 Bằng chứng", value=bang_chung, inline=False)

    embed.set_footer(text=f"ID ĐƠN KIỆN: {don_id}")

    await channel.send(embed=embed)
    await interaction.response.send_message(
        f"✅ Đã gửi đơn kiện!\n🆔 ID đơn: `{don_id}`",
        ephemeral=True
    )

# ================== /DUYETKIEN ==================
@bot.tree.command(name="duyetkien", description="Duyệt đơn kiện theo ID", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(id_don="ID của đơn kiện")
async def duyetkien(interaction: discord.Interaction, id_don: int):
    channel = bot.get_channel(CHANNEL_ID)

    async for msg in channel.history(limit=100):
        if not msg.embeds:
            continue

        embed = msg.embeds[0]

        if not embed.footer or not embed.footer.text:
            continue

        if str(id_don) in embed.footer.text:
            new_embed = embed.copy()
            new_embed.color = discord.Color.green()
            new_embed.title = "✅ ĐƠN KIỆN ĐÃ ĐƯỢC DUYỆT"

            await msg.edit(embed=new_embed)
            await interaction.response.send_message(
                f"✅ Đã duyệt đơn kiện ID `{id_don}`",
                ephemeral=True
            )
            return

    await interaction.response.send_message(
        "❌ Không tìm thấy đơn kiện với ID này!",
        ephemeral=True
    )

# ================== /CACHDUNG ==================
@bot.tree.command(name="cachdung", description="Hướng dẫn sử dụng hệ thống kiện", guild=discord.Object(id=GUILD_ID))
async def cachdung(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📌 HƯỚNG DẪN SỬ DỤNG HỆ THỐNG KIỆN",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="👤 Người chơi",
        value=(
            "• Dùng lệnh `/kien`\n"
            "• Điền đầy đủ thông tin\n"
            "• Sau khi gửi sẽ nhận được **ID đơn kiện**"
        ),
        inline=False
    )

    embed.add_field(
        name="🛡️ Staff",
        value=(
            "• Dùng lệnh `/duyetkien <ID>`\n"
            "• Khi duyệt xong, đơn kiện sẽ **đổi sang màu xanh**"
        ),
        inline=False
    )

    embed.set_footer(text="Hệ thống kiện tự động")

    await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.tree.command(name="ketqua", description="Xem kết quả đơn kiện", guild=discord.Object(id=GUILD_ID))
@app_commands.describe(
    id_don="ID của đơn kiện",
    ket_qua="Kết quả của đơn kiện (Đạt/Không đạt)"
)
async def ketqua(
    interaction: discord.Interaction,
    id_don: int,
    ket_qua: str
):
    channel = bot.get_channel(CHANNEL_ID)

    async for msg in channel.history(limit=100):
        if not msg.embeds:
            continue

        embed = msg.embeds[0]

        if not embed.footer or not embed.footer.text:
            continue

        if str(id_don) in embed.footer.text:
            new_embed = embed.copy()
            new_embed.color = discord.Color.gold()
            new_embed.title = "📋 KẾT QUẢ ĐƠN KIỆN"
            new_embed.add_field(name="📌 Kết Quả", value=ket_qua, inline=False)

            await msg.edit(embed=new_embed)
            await interaction.response.send_message(
                f"✅ Đã cập nhật kết quả đơn kiện ID `{id_don}`",
                ephemeral=True
            )
            return

    await interaction.response.send_message(
        "❌ Không tìm thấy đơn kiện với ID này!",
        ephemeral=True
    )

bot.run(TOKEN)

