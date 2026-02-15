⚖️ Discord Bot Hệ Thống Kiện Tự Động

Bot Discord giúp quản lý đơn kiện trong server một cách tự động và chuyên nghiệp.

🚀 Tính Năng
📄 1. Gửi Đơn Kiện

Lệnh:

/kien


Người dùng sẽ cung cấp:

👤 Người kiện

👤 Người bị kiện

📜 Luật khác (nếu có)

⏰ Thời gian xảy ra

📝 Trình bày tình huống

📸 Bằng chứng (link ảnh/video)

Sau khi gửi thành công, bot sẽ:

Tạo ID ngẫu nhiên cho đơn kiện

Gửi embed vào kênh chỉ định

Trả ID cho người gửi

✅ 2. Duyệt Đơn Kiện (Staff)

Lệnh:

/duyetkien <ID>


Tìm đơn kiện theo ID

Đổi màu embed sang xanh

Đổi tiêu đề thành:

✅ ĐƠN KIỆN ĐÃ ĐƯỢC DUYỆT

📋 3. Cập Nhật Kết Quả

Lệnh:

/ketqua <ID> <Kết quả>


Đổi tiêu đề thành:

📋 KẾT QUẢ ĐƠN KIỆN


Thêm trường:

📌 Kết Quả: (Đạt / Không đạt / nội dung khác)

📌 4. Hướng Dẫn Sử Dụng

Lệnh:

/cachdung


Hiển thị hướng dẫn cho:

Người chơi

Staff

⚙️ Cài Đặt
1️⃣ Yêu Cầu

Python 3.10+

discord.py 2.3+

Cài thư viện:

pip install -U discord.py

2️⃣ Cấu Hình

Trong file bot, chỉnh sửa:

TOKEN = "YOUR_TOKEN"
GUILD_ID = YOUR_GUILD_ID
CHANNEL_ID = YOUR_CHANNEL_ID


TOKEN → Token bot từ Discord Developer Portal

GUILD_ID → ID server

CHANNEL_ID → ID kênh nhận đơn kiện

3️⃣ Chạy Bot
python bot.py


Nếu thành công sẽ hiện:

✅ Bot online & slash synced

🔒 Quyền Cần Thiết

Bot cần các quyền:

View Channel

Send Messages

Embed Links

Read Message History

Manage Messages (để chỉnh sửa embed khi duyệt)

📦 Cấu Trúc Hệ Thống

Đơn kiện được lưu dưới dạng Embed

Mỗi đơn có ID ngẫu nhiên 6 chữ số

Staff quản lý trực tiếp bằng cách chỉnh sửa embed

Không dùng database (quản lý qua lịch sử tin nhắn)

🛠 Nâng Cấp Có Thể Thêm

Giới hạn chỉ Staff mới được duyệt

Lưu ID vào file JSON

Thêm hệ thống thống kê

Thêm phân quyền theo role

Tự động ping staff khi có đơn mới

👨‍💻 Tác Giả

Bot được xây dựng bằng discord.py
Hệ thống quản lý kiện tự động cho server roleplay / game.
