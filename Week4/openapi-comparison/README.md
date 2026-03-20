# OpenAPI vs API Blueprint vs RAML vs TypeSpec Comparison

Dự án này thực hiện thiết kế một API quản lý sách (Simple Books API) bằng 4 ngôn ngữ mô tả API (ADLs) phổ biến nhằm so sánh ưu nhược điểm của từng loại dựa trên các tiêu chí cụ thể.

---

## 📂 Danh sách các thư mục tài liệu

### 1. [OpenAPI (YAML)](./openapi/)

- **Ngôn ngữ nền tảng:** YAML / JSON - Cấu trúc dữ liệu chặt chẽ.
- **Trải nghiệm người dùng:** Tập trung vào Machine-centric, hỗ trợ tự động hóa cao. Dễ tương tác qua giao diện Swagger UI.
- **Tính module hóa:** Tốt qua `components/schemas`.
- **Hệ sinh thái:** **Dẫn đầu**. Hỗ trợ Swagger UI, OpenAPI Generator và hầu hết các công cụ API hiện nay.

### 2. [API Blueprint](./API_Blueprint/)

- **Ngôn ngữ nền tảng:** Markdown - Định dạng văn bản phổ biến.
- **Trải nghiệm người dùng:** **Thân thiện nhất với con người**. Phù hợp để thảo luận và làm tài liệu hướng dẫn.
- **Tính module hóa:** Tốt qua `Data Structures`.
- **Hệ sinh thái:** Khá tốt với các công cụ như Aglio (render UI) và Dredd (testing).

### 3. [RAML](./RAML/)

- **Ngôn ngữ nền tảng:** YAML-based - Phân cấp tài nguyên rõ ràng.
- **Trải nghiệm người dùng:** Cân bằng giữa cấu trúc logic và khả năng đọc hiểu. Nhìn rõ cây tài nguyên (Resource tree).
- **Tính module hóa:** **Xuất sắc** nhờ tư duy hướng đối tượng (`Types`, `Traits`, `Libraries`).
- **Hệ sinh thái:** Mạnh trong mảng doanh nghiệp lớn.

### 4. [TypeSpec](./TypeSec/)

- **Ngôn ngữ nền tảng:** TypeScript-like - Sử dụng cú pháp mã nguồn.
- **Trải nghiệm người dùng:** **Rất tốt cho lập trình viên** với sự hỗ trợ của IDE (Intellisense, Type-checking).
- **Tính module hóa:** Cực mạnh qua `namespace`, `interface`, `decorators`.
- **Hệ sinh thái:** Linh hoạt, có thể biên dịch (emit) ra OpenAPI để tận dụng các công cụ sẵn có.

## 🛠️ Quy trình tự động hóa đã thực hiện

Dự án này đã thực hiện demo thực tế quy trình "Design-First" thông qua tự động hóa:

1.  **OpenAPI ➔ Code & UI:**
    - Sử dụng `openapi-generator-cli` để tạo server Flask tự động trong thư mục `openapi/server-code/`.
    - Tích hợp **Swagger UI** trực tiếp vào ứng dụng để hiển thị tài liệu tương tác.
2.  **API Blueprint ➔ UI & Contract Testing:**
    - Sử dụng `Aglio` để render tài liệu định dạng HTML đẹp mắt.
    - Sử dụng **Dredd** để thực hiện kiểm thử thực tế giữa thiết kế và server Flask (`server.py`).
3.  **RAML ➔ UI & Server:**
    - Sử dụng `raml2html` để sinh giao diện tài liệu.
4.  **TypeSpec ➔ OpenAPI Transformation:**
    - Sử dụng `tsp compile` để biên dịch mã nguồn TypeSpec (TypeScript-like) sang chuẩn OpenAPI 3.0, giúp tận dụng tối đa sức mạnh của toàn bộ hệ sinh thái OpenAPI.


