# Mô hình định giá và Kiếm tiền từ API (API Monetization)

Việc chọn mô hình kiếm tiền phụ thuộc vào giá trị doanh nghiệp mang lại từ API. Hai mô hình phổ biến và linh hoạt nhất hiện nay là:

## 1. Mô hình Freemium (Miễn phí kết hợp trả phí / Tiered Pricing)

- **Mô tả**: Mô hình này cung cấp một lượng giới hạn sử dụng hoặc giới hạn tính năng miễn phí (Free Tier) nhằm thu hút dev dùng thử, phát triển prototype. Khi dự án của họ lớn lên và cần thêm dung lượng truy cập, họ sẽ bắt buộc phải nâng cấp lên các gói trả phí.
- **Chiến lược bậc giá (Tiers)**:
  - **Free Tier (Hobby/Developer)**:
    - Miễn phí 1,000 request/tháng.
    - Giới hạn Rate-limit: 1-2 request/giây.
    - Chỉ cho truy cập các endpoint cơ bản. Hỗ trợ cộng đồng.
  - **Pro/Startup Tier**:
    - Trả phí cố định: $49/tháng.
    - Hạn mức: 100,000 request/tháng.
    - Rate-limit nới lỏng: 50 request/giây. Truy cập các endpoint phân tích sâu.
  - **Enterprise Tier**:
    - Giá thỏa thuận (Custom Pricing), thanh toán hằng năm.
    - Request không giới hạn, cam kết SLA (Ví dụ: Uptime 99.99%), có account manager hỗ trợ trực tiếp.
- **Ưu điểm**: Mở rộng phễu người dùng, giảm thiểu rào cản chuyển đổi. Dễ tạo uy tín với tập lập trình viên độc lập.

## 2. Mô hình Pay-Per-Call (Trả tiền theo lượng dùng / Pay-As-You-Go)

- **Mô tả**: Tính phí khách hàng hoàn toàn dựa trên khối lượng tài nguyên máy chủ mà họ đã tiêu thụ (vd: tính theo mỗi Request, Megabyte data truyền, hoặc Token AI sinh ra).
- **Cấu trúc giá**: Thường áp dụng kết hợp cơ chế giảm giá khi mua số lượng lớn (Volume Discount).
  - 10,000 API calls đầu tiên: Miễn phí.
  - Lên đến 1 triệu calls: $0.005 / cuộc gọi.
  - Trên 1 triệu calls: $0.001 / cuộc gọi (càng dùng nhiều càng rẻ).
- **Ưu điểm**: Cực kỳ hấp dẫn cho các start-up vì họ "chỉ trả tiền với những gì họ dùng", không bị mắc kẹt vào phí thuê bao hàng tháng nếu ứng dụng của họ chưa có traffic. Phù hợp cho các dịch vụ đòi hỏi khả năng điện toán nặng (như LLM, Image Processing, SMS, Email).

## 3. Khuyến nghị chiến lược chung

- **Hybrid (Freemium kết hợp Pay-As-You-Go)**: Là cơ chế phổ biến nhất ngày nay của các nền tảng lớn (ví dụ: Stripe, Twilio, OpenAI). Trong đó, DEV đăng ký sẽ có 1 lượng Credit hoặc Request miễn phí hàng tháng. Sau khi dùng hết mức miễn phí đó, hệ thống bắt đầu tính tiền pay-per-call nhỏ.
- Để tránh lạm dụng (Abuse) tài khoản Free, nên bắt buộc người dùng thêm thẻ tín dụng (Credit Card) kể cả khi đăng ký tài khoản Free Tier.
- Sử dụng API Gateway quản lý như **Kong**, **Apigee** hoặc nền tảng thanh toán của **Stripe (Stripe Billing, Stripe Metered Billing)** để tự động hóa việc đếm số request và tạo hoá đơn.
