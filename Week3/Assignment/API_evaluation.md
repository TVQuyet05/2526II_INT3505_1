# Đánh giá API (server.py)

Tài liệu này liệt kê các API hiện có trong `server.py`, phân tích các lỗi vi phạm nguyên tắc thiết kế RESTful và đề xuất phương án cải thiện.

## 1. Danh sách API hiện tại

| Method   | Endpoint             | Mô tả                                                                           |
| :------- | :------------------- | :------------------------------------------------------------------------------ |
| `GET`    | `/new_conversation`  | Tạo một cuộc hội thoại mới.                                                     |
| `POST`   | `/chat`              | Gửi tin nhắn và nhận phản hồi từ bot. Payload: `{"conversation_id", "message"}` |
| `GET`    | `/history`           | Lấy lịch sử tin nhắn. Param: `conversation_id`                                  |
| `GET`    | `/all_conversations` | Lấy danh sách tất cả các cuộc hội thoại.                                        |
| `DELETE` | `/conversation`      | Xóa cuộc hội thoại và agent. Payload: `{"conversation_id"}`                     |

## 2. Các lỗi trong nguyên tắc thiết kế


Code hiện tại đang thiết kế theo phong cách RPC (Remote Procedure Call) thay vì RESTful.

- **Sử dụng sai HTTP Method:**
  - `GET /new_conversation`: Sử dụng `GET` để thực hiện hành động tạo dữ liệu (Create) là sai nguyên tắc. `GET` phải là phương thức an toàn (safe) và không làm thay đổi trạng thái server.
- **Đặt tên URL chứa động từ:**
  - Các endpoint như `new_conversation`, `chat`, `history`, `all_conversations` mô tả hành động thay vì tài nguyên. RESTful nên sử dụng danh từ (Resource).
- **DELETE với Request Body:**
  - API `DELETE /conversation` yêu cầu body JSON. Mặc dù không bị cấm hoàn toàn, nhưng nhiều client/proxy sẽ loại bỏ body của request DELETE. Định danh tài nguyên cần xóa nên nằm trên URL.



## 3. Đề xuất sửa lỗi (Refactoring)

Chuyển đổi sang cấu trúc RESTful chuẩn hướng tài nguyên:

| Hành động            | API Hiện tại             | API Đề xuất (RESTful)               | Ghi chú                                      |
| :------------------- | :----------------------- | :---------------------------------- | :------------------------------------------- |
| Tạo hội thoại        | `GET /new_conversation`  | `POST /conversations`               | Trả về ID của hội thoại mới tạo.             |
| Lấy danh sách        | `GET /all_conversations` | `GET /conversations`                | Trả về danh sách hội thoại.                    |
| Lấy chi tiết/Lịch sử | `GET /history`           | `GET /conversations/{id}/messages`  | Lấy danh sách tin nhắn của hội thoại `{id}`. |
| Gửi tin nhắn (Chat)  | `POST /chat`             | `POST /conversations/{id}/messages` | Tạo một message mới trong hội thoại.         |
| Xóa hội thoại        | `DELETE /conversation`   | `DELETE /conversations/{id}`        | Xóa tài nguyên hội thoại `{id}`.             |

