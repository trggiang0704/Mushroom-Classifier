# 🍄 Mushroom-Classifier với Flask & ID3
## 📌 Giới thiệu

Đây là một ứng dụng web đơn giản để dự đoán nấm ăn được hay nấm độc dựa trên mô hình ID3.
Người dùng chọn các thuộc tính quan trọng của nấm (mùi, màu mũ, màu phiến) trên giao diện web → hệ thống dự đoán và hiển thị kết quả ngay trên màn hình.

## 🛠️ Công nghệ và công cụ sử dụng
Thành phần	Công nghệ sử dụng
Ngôn ngữ lập trình	Python 3
Web framework	Flask
Machine Learning	ID3 (Decision Tree)
Frontend	HTML, CSS (thuần)
Template engine	Jinja2 (tích hợp Flask)
## 🧠 Logic & hoạt động

Người dùng chọn các thuộc tính của nấm: odor (mùi), cap-color (màu mũ), gill-color (màu phiến).

Flask backend nhận dữ liệu và dự đoán dựa trên cây quyết định ID3 đã được huấn luyện.

Kết quả trả về:

e → Nấm ăn được (Edible)

p → Nấm độc (Poisonous)

Trường hợp không xác định → cảnh báo UNKNOWN

Các lựa chọn của người dùng vẫn giữ nguyên trên form sau khi submit.

## 🎨 Giao diện

🔹 Form chọn thuộc tính nấm

<img width="978" height="604" alt="image" src="https://github.com/user-attachments/assets/1a39ca88-6e9d-45aa-b9b2-32ee5fabe009" />

🔹 Kết quả dự đoán

<img width="880" height="611" alt="image" src="https://github.com/user-attachments/assets/594ce291-5f9d-4b3f-9768-ec2fc6c149b7" />

## 🚀 Khởi chạy ứng dụng

```bash
1. Tạo môi trường ảo
python -m venv .venv

2. Kích hoạt môi trường ảo
Windows:
.venv\Scripts\activate
macOS/Linux:
source .venv/bin/activate

3. Cài đặt thư viện
pip install -r requirements.txt

4. Chạy ứng dụng Flask
python app.py

5. Mở trình duyệt
http://127.0.0.1:5000
```

## 💡 Ghi chú

Mô hình đã được huấn luyện trên 3 feature quan trọng: odor, cap-color, gill-color.

Có thể mở rộng: thêm nhiều feature, lưu lịch sử dự đoán, cải thiện giao diện, thêm tooltip giải thích ý nghĩa của các giá trị.

Nếu muốn truy cập từ thiết bị khác trong cùng mạng LAN, sửa trong app.py:

app.run(host="0.0.0.0", port=5000, debug=True)
