# Đánh giá API (backend/server.py)

Tài liệu này liệt kê các API hiện có trong `backend/server.py`, phân tích các lỗi vi phạm nguyên tắc thiết kế RESTful và đề xuất phương án cải thiện.

## 1. Danh sách API hiện tại

| Method   | Endpoint             | Mô tả                                                                           |
| :------- | :------------------- | :------------------------------------------------------------------------------ |
| `GET`    | `/new_conversation`  | Tạo một cuộc hội thoại mới.                                                     |
| `POST`   | `/chat`              | Gửi tin nhắn và nhận phản hồi từ bot. Payload: `{"conversation_id", "message"}` |
| `GET`    | `/history`           | Lấy lịch sử tin nhắn. Param: `conversation_id`                                  |
| `GET`    | `/all_conversations` | Lấy danh sách tất cả các cuộc hội thoại.                                        |
| `DELETE` | `/conversation`      | Xóa cuộc hội thoại và agent. Payload: `{"conversation_id"}`                     |

## 2. Các lỗi trong nguyên tắc thiết kế

### 2.1. Vi phạm chuẩn RESTful (Resource Naming & HTTP Methods)

Code hiện tại đang thiết kế theo phong cách RPC (Remote Procedure Call) thay vì RESTful.

- **Sử dụng sai HTTP Method:**
  - `GET /new_conversation`: Sử dụng `GET` để thực hiện hành động tạo dữ liệu (Create) là sai nguyên tắc. `GET` phải là phương thức an toàn (safe) và không làm thay đổi trạng thái server.
- **Đặt tên URL chứa động từ:**
  - Các endpoint như `new_conversation`, `chat`, `history`, `all_conversations` mô tả hành động thay vì tài nguyên. RESTful nên sử dụng danh từ (Resource).
- **DELETE với Request Body:**
  - API `DELETE /conversation` yêu cầu body JSON. Mặc dù không bị cấm hoàn toàn, nhưng nhiều client/proxy sẽ loại bỏ body của request DELETE. Định danh tài nguyên cần xóa nên nằm trên URL.

### 2.2. Vấn đề về Kiến trúc (State Management & Scalability)

- **Lưu trữ state trong bộ nhớ (In-memory State):**
  - Biến toàn cục `active_agent = {}` lưu trữ instance của Agent trong RAM.
  - **Hệ quả:** Hệ thống không thể mở rộng (scale). Khi chạy nhiều worker hoặc nhiều server, `active_agent` không được chia sẻ. User kết nối vào worker A sẽ không tìm thấy agent nếu request sau đó rơi vào worker B. Agent nên được thiết kế stateless hoặc khôi phục trạng thái từ Database/Redis cho mỗi request.

### 2.3. Cấu trúc Code

- **Hardcoded Imports:** Sử dụng `sys.path.append` để sửa đường dẫn import là một "bad practice", gây khó khăn cho việc đóng gói, kiểm thử và bảo trì.

## 3. Đề xuất sửa lỗi (Refactoring)

Chuyển đổi sang cấu trúc RESTful chuẩn hướng tài nguyên (`/conversations`):

| Hành động            | API Hiện tại             | API Đề xuất (RESTful)               | Ghi chú                                      |
| :------------------- | :----------------------- | :---------------------------------- | :------------------------------------------- |
| Tạo hội thoại        | `GET /new_conversation`  | `POST /conversations`               | Trả về ID của hội thoại mới tạo.             |
| Lấy danh sách        | `GET /all_conversations` | `GET /conversations`                | Trả về danh sách tóm tắt.                    |
| Lấy chi tiết/Lịch sử | `GET /history`           | `GET /conversations/{id}/messages`  | Lấy danh sách tin nhắn của hội thoại `{id}`. |
| Gửi tin nhắn (Chat)  | `POST /chat`             | `POST /conversations/{id}/messages` | Tạo một message mới trong hội thoại.         |
| Xóa hội thoại        | `DELETE /conversation`   | `DELETE /conversations/{id}`        | Xóa tài nguyên hội thoại `{id}`.             |

**Cải thiện Code:**

- Loại bỏ `active_agent` global dictionary. Tải lại context từ DB mỗi khi xử lý request chat.
- Sử dụng biến môi trường hoặc cấu trúc package chuẩn để xử lý import.
