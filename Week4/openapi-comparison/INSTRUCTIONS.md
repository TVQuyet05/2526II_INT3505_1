# Hướng dẫn bài tập: So sánh các định dạng đặc tả API

Tài liệu này mô tả mục đích, yêu cầu và phương pháp thực hiện bài tập so sánh các ngôn ngữ thiết kế API (API Description Languages - ADLs).

## 1. Mục đích

- Làm quen với các tiêu chuẩn thiết kế API phổ biến hiện nay: OpenAPI (Swagger), API Blueprint, RAML và TypeSpec.
- Hiểu được sự khác biệt về cú pháp, khả năng tái sử dụng và hệ sinh thái công cụ của từng định dạng.
- Trải nghiệm quy trình "Design-First": Thiết kế API trước khi viết code logic.
- Thực hành việc tự động hóa trong phát triển phần mềm (sinh code và sinh test từ tài liệu).

## 2. Yêu cầu bài tập

- **Nội dung:** Thiết kế API cho một ứng dụng quản lý thư viện (Simple Books API) bao gồm 5 endpoints cơ bản:
  1. `GET /books`: Lấy danh sách toàn bộ sách.
  2. `POST /books`: Thêm một cuốn sách mới.
  3. `GET /books/{id}`: Lấy thông tin chi tiết một cuốn sách.
  4. `PUT /books/{id}`: Cập nhật thông tin sách.
  5. `DELETE /books/{id}`: Xóa một cuốn sách.
- **Cấu trúc thư mục:** Tạo thư mục `openapi-comparison`, bên trong chia thành các thư mục con cho mỗi định dạng: `openapi`, `API_Blueprint`, `RAML`, `TypeSec`.
- **Tài liệu:** Mỗi thư mục con phải chứa file đặc tả tương ứng và một file `README.md` hướng dẫn cách cài đặt/chạy các công cụ liên quan.

## 3. Phương pháp so sánh

Các định dạng được so sánh dựa trên các tiêu chí sau:

- **Ngôn ngữ nền tảng:** YAML (OpenAPI, RAML), Markdown (Blueprint), hay TypeScript-like (TypeSpec).
- **Trải nghiệm người dùng:** Độ dễ đọc cho con người vs. độ dễ phân tích cho máy móc.
- **Tính module hóa:** Khả năng định nghĩa lại các kiểu dữ liệu (Schemas/Types) và tái sử dụng chúng.
- **Hệ sinh thái công cụ:** Khả năng hỗ trợ sinh giao diện (Swagger UI), sinh mã nguồn (Code Generator) và kiểm thử (Mock Server/Testing).

## 4. Demo thực tế (Code, Test & UI)

Bài tập thực hiện demo thực tế việc chuyển đổi từ tài liệu sang ứng dụng cho từng định dạng:

- **OpenAPI (Swagger):**
  - **Sinh Code:** Sử dụng `openapi-generator-cli` để sinh ra server Flask tự động trong thư mục `openapi/server-code/`.
  - **UI:** Tích hợp `Swagger UI` trực tiếp vào ứng dụng Flask để hiển thị tài liệu tương tác.
- **API Blueprint:**
  - **UI:** Sử dụng `Aglio` để biên dịch file `.apib` sang giao diện HTML tĩnh.
  - **Contract Testing:** Sử dụng `Dredd` để chạy kiểm thử tự động, so sánh phản hồi thực tế của server Flask (`server.py`) với các ví dụ trong tài liệu.
- **RAML:**
  - **UI:** Sử dụng `raml2html` để tạo tài liệu API từ file `.raml`.
  - **Server:** Viết `server.py` bằng Flask khớp với các kiểu dữ liệu và endpoints định nghĩa trong RAML.
- **TypeSpec (TSP):**
  - **Biên dịch:** Sử dụng `tsp compile` để chuyển đổi mã nguồn TypeSpec sang chuẩn **OpenAPI 3.0**.
  - **Ưu điểm:** Tận dụng tối đa khả năng kiểm tra lỗi (Type-checking) ngay khi thiết kế, đảm bảo tính nhất quán của dữ liệu.

**Kết quả:** Hệ thống chứng minh khả năng "Single Source of Truth" - từ một file thiết kế duy nhất có thể sinh ra Tài liệu, Mã nguồn và các bộ Test tự động.
