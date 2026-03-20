# TypeSpec (TSP) Demo: Modern API Design

Thư mục này minh họa cách sử dụng **TypeSpec** - một ngôn ngữ thiết kế API hiện đại của Microsoft, giúp viết API spec nhanh và ít lỗi hơn so với YAML truyền thống.

## 📁 Cấu trúc thư mục

- `main.tsp`: File nguồn TypeSpec chứa định nghĩa API.
- `tsp-output/`: Thư mục chứa kết quả biên dịch (sau khi chạy lệnh compile).

---

## 🚀 1. Cài đặt môi trường

Để sử dụng TypeSpec, bạn cần có [Node.js](https://nodejs.org/) và cài đặt compiler:

```powershell
npm install -g @typespec/compiler
```

Để hỗ trợ biên dịch sang OpenAPI (Swagger), cài thêm thư viện tương ứng:

```powershell
npm install @typespec/http @typespec/rest @typespec/openapi3
```

---

## 🛠️ 2. Biên dịch (Compile)

Khác với các ADL khác, TypeSpec cần được "biên dịch" để tạo ra các định nghĩa API chuẩn (như OpenAPI 3.0).

### Lệnh biên dịch:

```powershell
tsp compile main.tsp
```

### Kết quả (Output):

Sau khi biên dịch thành công:

1. Thư mục `tsp-output/@typespec/openapi3/` sẽ được tạo ra.
2. File `openapi.yaml` (hoặc `openapi.json`) sẽ xuất hiện bên trong - đây là file bạn có thể dùng để sinh code hoặc hiển thị trên Swagger UI.

---

## ✨ 3. Tính năng nổi bật của TypeSpec

Trong 4 loại ADL được so sánh, TypeSpec vượt trội nhờ:

1.  **Code-like Syntax**: Viết API giống như viết code TypeScript/Java/C#, có khả năng kiểm tra lỗi ngay lập tức (Type-safe).
2.  **Siêu ngắn gọn**: Bạn không cần viết hàng trăm dòng YAML; TypeSpec xử lý các tác vụ lặp lại (như model reuse) cực kỳ thông minh.
3.  **Hệ sinh thái Emitter**: Một file `.tsp` có thể biên dịch ra nhiều thứ cùng lúc:
    - **OpenAPI 3.0** (cho HTTP REST API).
    - **JSON Schema** (cho validation dữ liệu).
    - **Protobuf** (cho gRPC).
4.  **Hỗ trợ IDE**: Extension trên VS Code cung cấp Intellisense mạnh mẽ, giúp designer làm việc năng suất hơn hẳn YAML.

---

## 🧪 4. Sinh Code & Test

Vì TypeSpec biên dịch ra file OpenAPI chuẩn, bạn có thể tận dụng toàn bộ hệ sinh thái của OpenAPI để:

- **Sinh Code**: Sử dụng `openapi-generator-cli`.
- **UI**: Dùng `Swagger UI` hoặc `Redoc`.
- **Test**: Dùng `Dredd` hoặc `Schemathesis`.
