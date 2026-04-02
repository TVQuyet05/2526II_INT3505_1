const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json()); // Để Express có thể đọc được JSON body

// Khoá bí mật dùng để ký và giải mã JWT (trong thực tế KHÔNG ĐƯỢC để hardcode thế này, 
// mà phải lưu trong biến môi trường .env)
const SECRET_KEY = "bgiagodmmmvupanrckcrpihjhbwldf";

// ==========================================
// 1. API: Đăng nhập và Sinh (Sign) Token
// ==========================================
app.post('/api/login', (req, res) => {
    const { username, password } = req.body;
    
    // Giả lập bước xác thực DB (Ví dụ user 'admin', pass '123456')
    if (username === 'admin' && password === '123456') {
        
        // Payload: Nội dung được lưu trữ trong token, không nên chứa dữ liệu nhạy cảm như password
        const payload = {
            id: 1,
            username: username,
            role: 'admin'
        };
        
        // Tạo JWT: jwt.sign(payload, secret_key, options)
        // Thiết lập thời gian hết hạn của token là 1 giờ ('1h')
        const token = jwt.sign(payload, SECRET_KEY, { expiresIn: '1h' });
        
        return res.json({
            message: "Đăng nhập thành công!",
            token: token
        });
    }
    
    return res.status(401).json({ error: "Sai tên đăng nhập hoặc mật khẩu" });
});

// ==========================================
// 2. Middleware: Xác thực (Verify) Token
// ==========================================
const authenticateJWT = (req, res, next) => {
    // Lấy header 'Authorization' từ Request
    const authHeader = req.headers.authorization;
    
    // Header phải có dạng: 'Bearer <TOKEN>'
    if (authHeader && authHeader.startsWith('Bearer ')) {
        const token = authHeader.split(' ')[1]; // Tách lấy chuỗi mã thật sự
        
        // Giải mã token bằng secret key
        jwt.verify(token, SECRET_KEY, (err, decodedUser) => {
            if (err) {
                // Token bị thay đổi, giả mạo, hoặc đã hết hạn
                return res.status(403).json({ error: "Token không hợp lệ hoặc đã hết hạn" });
            }
            
            // Nếu thành công -> token chuẩn xác
            // Lưu thông tin người dùng được giải mã từ token vào Request 
            // để các endpoint phía sau có thể tái sử dụng
            req.user = decodedUser;
            next(); // Cho phép đi tiếp vào endpoint
        });
    } else {
        res.status(401).json({ error: "Thiếu Bearer Token trong header Authorization" });
    }
};

// ==========================================
// 3. API: Truy cập tài nguyên bảo mật (Yêu cầu JWT)
// ==========================================
app.get('/api/protected/profile', authenticateJWT, (req, res) => {
    // Chỉ những Request vượt qua middleware `authenticateJWT` mới tiếp cận được block lệnh này.
    
    res.json({
        message: "Bạn đã vào được private route!",
        user_info_from_token: req.user // Lấy ra từ token đã được giải mã
    });
});

// Khởi chạy Server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server đang chạy tại http://localhost:${PORT}`);
    console.log('Các bước test:');
    console.log('1. POST /api/login với body { "username": "admin", "password": "123456" } để lấy token');
    console.log('2. GET /api/protected/profile và thêm Header Authorization: Bearer <TOKEN_VUA_LAY>');
});
