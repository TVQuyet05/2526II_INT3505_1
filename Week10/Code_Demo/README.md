# Flask Observability & Rate Limiting Demo

Đây là một project demo nhỏ sử dụng Python Flask kết hợp với Docker để minh họa các khái niệm về:

- **Observability**: Ghi log dưới dạng JSON chuẩn (Audit logs) và thu thập Metrics bằng Prometheus.
- **Rate Limiting**: Giới hạn số lượng request tới API bằng `Flask-Limiter`.

## Cấu trúc

- `app.py`: Source code API Flask.
- `requirements.txt`: Các thư viện Python cần thiết.
- `prometheus.yml`: File cấu hình cho Prometheus để tự động scrape dữ liệu từ ứng dụng Flask.
- `docker-compose.yml`: Chạy Prometheus và Grafana qua Docker.

## Yêu cầu hệ thống

- Python 3.8+ (nên sử dụng môi trường ảo như venv hoặc conda)
- Docker Desktop đang chạy (do sử dụng host.docker.internal trong cấu hình).

## Hướng dẫn chạy

### 1. Khởi chạy Flask API

Mở terminal, kích hoạt môi trường ảo (nếu có) và chạy các lệnh sau:

```bash
pip install -r requirements.txt
python app.py
```

> API sẽ chạy tại `http://localhost:8000`

### 2. Khởi chạy Prometheus & Grafana

Mở một terminal khác, chạy:

```bash
docker compose up -d
```

## Các cổng & Dịch vụ

- **Flask API**: `http://localhost:8000`
  - `/health`: Kiểm tra trạng thái máy chủ (không bị giới hạn Rate Limit)
  - `/metrics`: Endpoint cho Prometheus cào dữ liệu metrics
  - `/v1/echo?msg=hi`: GET request, rate limit 10/phút.
  - `/v1/items`: POST request (truyền raw JSON `{"name": "test"}`), rate limit 5/phút.

- **Prometheus**: `http://localhost:9090`
  - Vào `Status` -> `Targets` để xác nhận `flask_api` đang ở trạng thái UP.
  - Chạy thử query: `http_requests_total`

- **Grafana**: `http://localhost:3000`
  - Đăng nhập với Username/Password mặc định: `admin` / `admin`
  - Bạn có thể tạo Data Source kết nối đến Prometheus (`http://prometheus:9090`) và xây dựng Dashboard quan sát Metrics.
