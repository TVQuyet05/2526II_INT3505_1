const express = require("express");
const app = express();
const cors = require("cors"); // Để client có thể gọi nếu khác port (option)

// Cho phép CORS để client dễ dàng gọi
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  next();
});

// 1. Data endpoint: Danh sách điểm thi
app.get("/api/scores", (req, res) => {
  res.json([45, 80, 32, 90, 65]);
});

// 2. Logic endpoint: Hàm kiểm tra Đậu/Rớt
// Nếu muốn đổi logic thành >= 60 mới đậu, chỉ cần sửa ở đây mà không cần update Client
app.get("/api/logic", (req, res) => {
  res.type("application/javascript");
  res.send(`function classify(score) { return score >= 50 ? "ĐẬU" : "RỚT"; }`);
});

app.listen(3000, () => console.log("Server: http://localhost:3000"));
