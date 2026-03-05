# Các Mã Lỗi Trạng Thái HTTP

Mã trạng thái HTTP là phản hồi từ máy chủ để cho biết kết quả của một yêu cầu từ máy khách.

## 4xx — Lỗi phía máy khách (Client Errors)

- **400 — Bad Request**: Yêu cầu không hợp lệ hoặc sai định dạng.  
- **401 — Unauthorized**: Request thiếu hoặc sai thông tin xác thực.
- **403 — Forbidden**: Máy chủ hiểu yêu cầu nhưng từ chối truy cập.  
- **404 — File Not Found**: Không tìm thấy tài nguyên được yêu cầu.  
- **429 — Too Many Requests**: Gửi quá nhiều yêu cầu trong thời gian ngắn.

## 5xx — Lỗi phía máy chủ (Server Errors)

- **500 — Internal Server Error**: Lỗi chung từ phía máy chủ khi xử lý yêu cầu.  
- **502 — Bad Gateway**: Máy chủ gateway/proxy nhận phản hồi không hợp lệ từ máy chủ khác.  
- **503 — Service Unavailable**: Máy chủ tạm thời không thể xử lý yêu cầu (quá tải hoặc bảo trì).  
- **504 — Gateway Timeout**: Gateway/proxy không nhận được phản hồi kịp thời từ máy chủ khác.