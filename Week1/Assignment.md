# Phân tích 3 API công khai phổ biến

---

## 1. GitHub REST API
Hệ thống API mạnh mẽ nhất dành cho việc quản lý mã nguồn và tương tác với hệ sinh thái Git.

* **Chức năng chính:** Truy cập thông tin người dùng, danh sách repository, quản lý issue và pull request.
* **Giao thức:** RESTful (định dạng dữ liệu JSON).
* **Xác thực:** Không bắt buộc với dữ liệu công khai; yêu cầu **Personal Access Token (PAT)** cho dữ liệu riêng tư hoặc giới hạn request cao hơn.
* **Endpoint ví dụ:** `https://api.github.com/users/{username}`

## 2. OpenWeatherMap API
Dịch vụ cung cấp dữ liệu khí tượng toàn cầu, rất phổ biến cho các ứng dụng dự báo thời tiết.

* **Chức năng chính:** Cung cấp dữ liệu thời tiết hiện tại, dự báo ngắn hạn/dài hạn và lịch sử thời tiết.
* **Giao thức:** RESTful (hỗ trợ JSON, XML).
* **Xác thực:** **Bắt buộc** sử dụng API Key (cấp qua email sau khi đăng ký).
* **Endpoint ví dụ:** `https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}`

## 3. PokeAPI
Một API miễn phí, không yêu cầu xác thực, cực kỳ phù hợp cho việc thực hành lập trình và demo.

* **Chức năng chính:** Cung cấp dữ liệu chi tiết về Pokémon (chỉ số, kỹ năng, hình ảnh, tiến hóa).
* **Giao thức:** RESTful (định dạng dữ liệu JSON).
* **Xác thực:** **Không yêu cầu** (Open Access).
* **Endpoint ví dụ:** `https://pokeapi.co/api/v2/pokemon/{name_or_id}`

---

## Bảng so sánh tóm tắt

| Tiêu chí | GitHub API | OpenWeather API | PokeAPI |
| :--- | :--- | :--- | :--- |
| **Độ phức tạp** | Cao | Trung bình | Thấp |
| **Xác thực** | Token (Tùy chọn) | API Key (Bắt buộc) | Không cần |
| **Định dạng** | JSON | JSON, XML | JSON |
| **Mục đích** | Quản lý dự án | Dữ liệu thời tiết | Học tập / Giải trí |