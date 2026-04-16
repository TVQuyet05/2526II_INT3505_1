import http from "k6/http";
import { check, sleep } from "k6";

// Cấu hình kịch bản test (Load Test)
export const options = {
  // Giả lập 10 người dùng ảo (virtual users) hoạt động đồng thời
  vus: 10,
  // Chạy trong vòng 10 giây
  duration: "10s",
};

// Vòng lặp chính của mỗi Virtual User (VU)
export default function () {
  // 1. Gửi request GET tới endpoint lấy danh sách sách
  const res = http.get("http://127.0.0.1:5000/books");

  // 2. Kiểm tra xem response trả về có status code là 200 không
  check(res, {
    "status is 200": (r) => r.status === 200,
    "transaction time < 500ms": (r) => r.timings.duration < 500,
  });

  sleep(1);
}
