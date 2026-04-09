# Hướng dẫn sinh Client SDK từ OpenAPI

Để tự động sinh mã nguồn Client (ví dụ bằng ngôn ngữ Python) từ file `openapi.yaml`, bạn có thể sử dụng công cụ OpenAPI Generator.

## Bước 1: Chạy lệnh sinh code

Mở terminal tại thư mục chứa file `openapi.yaml` (yêu cầu máy đã cài Node.js để chạy lệnh `npx`) và sử dụng lệnh sau:

```bash
npx @openapitools/openapi-generator-cli generate -i openapi.yaml -g python -o client-code
```

**Giải thích các tham số:**

- `-i openapi.yaml`: Tên file đặc tả OpenAPI của bạn.
- `-g python`: Tên ngôn ngữ/framework muốn sinh client. Bạn có thể thay bằng `javascript`, `typescript-axios`, `java`, v.v.
- `-o client-code`: Tên thư mục đầu ra để lưu mã nguồn tự động sinh.

## Bước 2: Cài đặt thư viện Client vừa sinh

Di chuyển vào thư mục vừa được tạo và dùng `pip` để cài đặt nó như một thư viện Python thông thường:

```bash
cd client-code
pip install .
```

## Bước 3: Sử dụng trong code của bạn

Sau khi cài đặt thành công, bạn có thể tạo một file Python (vd: `demo.py`) và gọi API như sau:

```python
import openapi_client

# Cấu hình địa chỉ server thực tế đang chạy
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)

# Gọi hàm từ Client
with openapi_client.ApiClient(configuration) as api_client:
    api_instance = openapi_client.BooksApi(api_client)
    try:
        response = api_instance.books_get()
        print(response)
    except Exception as e:
        print("Lỗi:", e)
```

> **Lưu ý:** Client sinh ra chỉ chứa code logic để gửi và nhận request, không bao gồm giao diện người dùng (UI). Để xem các tài liệu hướng dẫn cực kỳ chi tiết cho từng API, bạn có thể mở các file Markdown trong thư mục `client-code/docs/`.
