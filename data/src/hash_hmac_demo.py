import json
import hashlib
import hmac

# 1. Khởi tạo Khóa bí mật (Secret Key) dùng chung giữa Thiết bị và Server
SECRET_KEY = b'MySuperSecretKeyIoT2026'

# 2. Đọc dữ liệu từ cảm biến
payload = {
    "device_id": "sensor_esp32_01",
    "temperature": 26.5,
    "humidity": 60,
    "timestamp": "2026-07-10T12:00:00Z"
}

# Chuyển JSON thành chuỗi string để tính toán
payload_string = json.dumps(payload, separators=(',', ':'))
payload_bytes = payload_string.encode('utf-8')

# ==========================================
# KỊCH BẢN 1: TẠO HASH VÀ HMAC HỢP LỆ (THIẾT BỊ GỬI)
# ==========================================
print("--- BƯỚC 1: THIẾT BỊ GỬI DỮ LIỆU ---")

# Tính mã Băm (Hash - SHA256)
hash_sha256 = hashlib.sha256(payload_bytes).hexdigest()
print(f"[+] Mã Hash (SHA-256) của dữ liệu: {hash_sha256}")

# Tính mã Xác thực thông điệp (HMAC-SHA256)
hmac_signature = hmac.new(SECRET_KEY, payload_bytes, hashlib.sha256).hexdigest()
print(f"[+] Chữ ký HMAC gửi đi: {hmac_signature}\n")

# ==========================================
# KỊCH BẢN 2: SERVER KIỂM TRA DỮ LIỆU HỢP LỆ
# ==========================================
print("--- BƯỚC 2: SERVER XÁC THỰC (KỊCH BẢN HỢP LỆ) ---")
# Server dùng SECRET_KEY tính lại HMAC trên dữ liệu nhận được
server_hmac = hmac.new(SECRET_KEY, payload_bytes, hashlib.sha256).hexdigest()

if hmac.compare_digest(hmac_signature, server_hmac):
    print("[SUCCESS] Xác thực thành công (Verification OK). Dữ liệu toàn vẹn!\n")
else:
    print("[FAILED] Xác thực thất bại!\n")

# ==========================================
# KỊCH BẢN 3: SERVER KIỂM TRA DỮ LIỆU BỊ KẺ GIAN SỬA ĐỔI
# ==========================================
print("--- BƯỚC 3: SERVER XÁC THỰC (KỊCH BẢN BỊ TẤN CÔNG MAN-IN-THE-MIDDLE) ---")
# Kẻ tấn công sửa nhiệt độ từ 26.5 thành 99.9
fake_payload_string = payload_string.replace("26.5", "99.9")
fake_payload_bytes = fake_payload_string.encode('utf-8')

# Server tính lại HMAC với dữ liệu giả mạo
server_fake_hmac = hmac.new(SECRET_KEY, fake_payload_bytes, hashlib.sha256).hexdigest()

if hmac.compare_digest(hmac_signature, server_fake_hmac):
    print("[SUCCESS] Xác thực thành công!\n")
else:
    print("[FAILED] Xác thực thất bại (Verification Failed). Dữ liệu đã bị thay đổi!")
    print(f"   -> HMAC của Server tính ra: {server_fake_hmac}")
    print(f"   -> Khác hoàn toàn với HMAC ban đầu: {hmac_signature}")
