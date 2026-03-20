# OpenAPI Generator - Python Flask Server

Hướng dẫn nhanh cách cài đặt công cụ sinh code và chạy server từ file `openapi.yaml`.

## 🛠️ 1. Cài đặt OpenAPI Generator CLI

Để sử dụng lệnh `openapi-generator-cli`, bạn cần cài đặt nó thông qua Node.js (npm):

```powershell
# Cài đặt toàn cục
npm install @openapitools/openapi-generator-cli -g

# Kiểm tra cài đặt
openapi-generator-cli version
```

## 🚀 2. Cách sinh code từ file YAML

Nếu bạn muốn tạo lại thư mục code từ file thiết kế:

```powershell
openapi-generator-cli generate -i openapi.yaml -g python-flask -o ./server-code
```

## 🏃 3. Cách chạy Server trên Localhost

Sau khi đã có thư mục `server-code`, hãy thực hiện các bước sau:

### Bước 1: Di chuyển vào thư mục code

```powershell
cd server-code
```

### Bước 2: Cài đặt thư viện (Dependencies)

_Khuyên dùng môi trường ảo (venv) trước khi cài._

```powershell
pip install -r requirements.txt
```

### Bước 3: Khởi chạy Server

Server mặc định sẽ chạy trên cổng **8080**.

```powershell
python -m openapi_server
```

### Bước 4: Kiểm tra kết quả

Mở trình duyệt và truy cập các đường dẫn sau:

- **Tài liệu API (Swagger UI):** [http://localhost:8080/ui/](http://localhost:8080/ui/)
- **Dữ liệu Spec (JSON):** [http://localhost:8080/openapi.json](http://localhost:8080/openapi.json)

---

## 📝 Lưu ý:

- File logic thực tế nằm trong: `openapi_server/controllers/books_controller.py`.
- Các model dữ liệu nằm trong: `openapi_server/models/`.
