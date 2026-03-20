# Simple Books API - Deployment with Vercel

Dự án này là một API quản lý sách đơn giản được viết bằng Python (Flask) và thiết kế theo chuẩn OpenAPI 3.0.

## 🚀 Hướng dẫn Deployment lên Vercel

### 1. Yêu cầu hệ thống

- Đã cài đặt [Node.js](https://nodejs.org/) (để dùng npm).
- Tài khoản [Vercel](https://vercel.com/).

### 2. Cấu trúc file cần thiết để deploy

Đảm bảo thư mục của bạn có các file sau:

- `app.py`: Code chính của Flask app.
- `requirements.txt`: Danh sách thư viện (`Flask`, `flask-cors`).
- `vercel.json`: Cấu hình để Vercel hiểu đây là một Python app.
- `openapi.yaml`: File đặc tả API.

### 3. Các bước thực hiện

#### Bước 1: Cài đặt Vercel CLI

Nếu bạn chưa cài đặt Vercel trên máy, hãy chạy lệnh:

```powershell
npm install -g vercel
```

#### Bước 2: Đăng nhập

```powershell
vercel login
```

_Làm theo hướng dẫn trên trình duyệt để xác thực._

#### Bước 3: Deploy dự án

Tại thư mục gốc (`Week4/Code_demo`), chạy lệnh:

```powershell
vercel
```

- Khi được hỏi `Set up and deploy?`, chọn **Y**.
- Các câu hỏi khác bạn có thể nhấn **Enter** để chọn mặc định.

#### Bước 4: Deploy môi trường Production (Nếu cần)

Để cập nhật thay đổi chính thức lên link production:

```powershell
vercel --prod
```

### 4. Kiểm tra kết quả

Sau khi deploy thành công, Vercel sẽ cung cấp một đường link (Vercel URL). Bạn có thể truy cập:

- `https://bookswagger.vercel.app/docs`: Để xem tài liệu Swagger UI.


