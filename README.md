# nguyenphuochau-iot-matma

Đồ án môn Bảo mật IoT - Đề tài 36

ĐỀ CƯƠNG CHI TIẾT TIỂU LUẬN LẦN 01

**1. Thông tin chung

Tên đề tài: Đề tài 36 - Vai trò của mật mã trong bảo mật IoT

Sinh viên thực hiện: Nguyễn Phước Hậu - 231A010774

Mã học phần: INT4410 (Bảo mật IoT)

Link kho lưu trữ (GitHub): [https://github.com/Qvk5/nguyenphuochau-iot-matma](https://github.com/Qvk5/nguyenphuochau-iot-matma)

**2. Lý do chọn đề tài**

Trong hệ sinh thái Internet of Things (IoT), dữ liệu cảm biến thường xuyên được truyền tải qua các môi trường mạng không an toàn. Các thiết bị IoT có đặc thù tài nguyên hạn chế (CPU yếu, RAM thấp), dẫn đến việc áp dụng các giao thức bảo mật tiêu chuẩn gặp nhiều khó khăn. Việc triển khai sai mật mã (như sử dụng thuật toán tự chế, mã hóa cứng khóa bí mật) diễn ra rất phổ biến. Do đó, việc nghiên cứu vai trò của mật mã để đảm bảo ba yếu tố cốt lõi: Tính bí mật (Confidentiality), Tính toàn vẹn (Integrity) và Xác thực (Authentication) là vô cùng cấp thiết nhằm xây dựng nền tảng IoT an toàn.

**3. Mục tiêu đề tài**

Mục tiêu 1: Trình bày và phân biệt rõ vai trò của 4 kỹ thuật mật mã cốt lõi trong không gian IoT: Mã hóa (Encryption), Băm (Hash), Xác thực thông điệp (MAC/HMAC), và Chữ ký số (Digital Signature).

Mục tiêu 2: Viết mã nguồn (code) mô phỏng thực tế quá trình áp dụng Hash và HMAC để bảo vệ tính toàn vẹn của dữ liệu cảm biến (định dạng JSON).

Mục tiêu 3: Phân tích các lỗi triển khai mật mã phổ biến trong thực tế (hard-code key, không xoay vòng khóa định kỳ) và đề xuất biện pháp khắc phục dựa trên chuẩn OWASP ISVS.

**4. Phạm vi nghiên cứu**

Môi trường thực nghiệm: Chạy lab cục bộ (Localhost) trên máy tính cá nhân.

Ngôn ngữ & Dữ liệu: Sử dụng ngôn ngữ Python để mô phỏng. Dữ liệu đầu vào là các payload JSON giả lập thông số môi trường (Nhiệt độ, Độ ẩm, Device ID).

Trọng tâm kỹ thuật: Tập trung vào bảo vệ luồng dữ liệu (Payload) ở lớp ứng dụng thông qua Hash (SHA-256) và HMAC, kết hợp nghiên cứu lý thuyết từ các thư viện Mbed TLS và TinyCrypt, không đi sâu vào việc nạp firmware vật lý (flashing).

**5. Phương pháp thực hiện**

Nghiên cứu tài liệu (Desk Research): Phân tích kiến trúc mật mã từ các mã nguồn mở được chỉ định (Mbed-TLS, TinyCrypt) và tiêu chuẩn kiểm thử bảo mật OWASP ISVS.

Mô phỏng thực hành (Lab/Demo): Viết script đóng vai trò thiết bị IoT (Client) tạo dữ liệu và sinh mã HMAC; viết script đóng vai trò Server để nhận, tính toán lại và xác thực mã HMAC.

Phân tích đối chứng: Đánh giá kết quả sinh ra từ log hệ thống giữa hai trường hợp: Dữ liệu hợp lệ và Dữ liệu đã bị kẻ tấn công (MITM) thay đổi.

**6. Danh sách sản phẩm dự kiến (Deliverables)**

Để đáp ứng chuẩn đầu ra của đồ án, nhóm cam kết sẽ hoàn thiện các minh chứng sau trên GitHub:

Sơ đồ luồng dữ liệu: Biểu đồ minh họa cụ thể khi nào dùng TLS, khi nào dùng HMAC cho payload, và khi nào dùng chữ ký số cho firmware.

Mã nguồn (Source Code): Script Python (hmac_sensor_demo.py) thực hiện băm và xác thực dữ liệu cảm biến.

Log/Hình ảnh minh chứng: Ảnh chụp màn hình Terminal thể hiện 2 kịch bản: Giao tiếp thành công (Verification OK) và Phát hiện can thiệp dữ liệu (Verification Failed).

Bảng phân tích rủi ro: Bảng tổng hợp các lỗi triển khai mật mã phổ biến và cách phòng chống.
