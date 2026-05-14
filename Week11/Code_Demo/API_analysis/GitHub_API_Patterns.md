# Phân tích API & Webhook Patterns: GitHub

## 1. Dual Approach: REST và GraphQL

**API Tương ứng chi tiết (GraphQL):**

```http
POST /graphql
Host: api.github.com
Authorization: bearer ghp_123

{
  "query": "query { viewer { login repositories(first: 3) { nodes { name } } } }"
}
```

**Phân tích:**
Bên cạnh hàng trăm endpoint REST truyền thống v3 (như `GET /users/:username`), GitHub triển khai v4 bằng GraphQL. Sự dịch chuyển này giải quyết triệt để tính trạng "Over-fetching" (Lấy rác) — client chỉ miêu tả đúng các field mình muốn lấy (`login`, `repositories` `name`) tiết kiệm băng thông tối đa và chỉ tốn đúng 1 HTTP request request kết hợp thay vì lấy hàng đống fields không cần thiết.

---

## 2. HATEOAS (Hypermedia As Engine Of Application State)

**API Tương ứng chi tiết:**

```http
GET /users/octocat
Host: api.github.com
Accept: application/vnd.github.v3+json
```

**Response chi tiết:**

```json
{
  "login": "octocat",
  "id": 1,
  "html_url": "https://github.com/octocat",
  "followers_url": "https://api.github.com/users/octocat/followers",
  "following_url": "https://api.github.com/users/octocat/following{/other_user}",
  "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}"
}
```

**Phân tích:**
Mô hình "đính kèm kèm bảng biểu chỉ đường". Gặp bất cứ mảng / object nào, API của GitHub đều cung cấp sẵn các URL tiếp theo. Developer (Client) chỉ bắt Json và sử dụng biến điều hướng thẳng (`obj.followers_url`) mà không cần nhớ hay tự gộp nối chuỗi hard-code (như `api.github.com/users/` + `id` + `/followers`) điều này nâng cao tính tương thích ngược sau này.

---

## 3. Rate Limit Headers (Kiểm soát & Minh bạch băng thông)

**API Tương ứng chi tiết:**

```http
GET /rate_limit
Host: api.github.com

# HTTP Response Headers
HTTP/2 200 OK
x-ratelimit-limit: 5000
x-ratelimit-remaining: 4998
x-ratelimit-used: 2
x-ratelimit-reset: 1614838612
```

**Phân tích:**
Mỗi phản hồi API của GitHub luôn cho biết băng thông quota tài khoản developer đang có là bao nhiêu. Nếu vượt quá (VD `remaining: 0`), server sẽ chặn trả về mã HTTP 403 Forbidden. Thuộc tính `reset` đưa ra mốc sinh hệ UNIX (timestamp) báo khi nào quota được nạp lại. Cơ chế này bảo vệ hệ thống tránh bị DDOS do BOT gọi ngu ngốc.

---

## 4. Webhook Event Định tuyến ở Header

**API Tương ứng chi tiết:**

```http
POST <Your_Webhook_URL>
Host: your-server.com
X-GitHub-Event: pull_request
X-GitHub-Delivery: 72d3162e-cc78-11e3-81ab-4c9ade678d5e
X-Hub-Signature-256: sha256=1a2b3c...

{
  "action": "opened",
  "number": 1,
  "pull_request": { ... }
}
```

**Phân tích:**
Thay vì phải phân tích (parse JSON) ở toàn bộ `Body` thì máy chủ hứng Webhook của bạn chỉ cần nhìn vào biến `X-GitHub-Event: pull_request` để quyết định chuyển thẳng luồng làm việc vào background job xử lý "Pull request", vứt bỏ Payload (drop) nếu không quan tâm để tiết kiệm tài nguyên Server. `X-GitHub-Delivery` giúp quá trình tra soát log (Traced ID) để Debug lỗi dễ dàng.

---

## 5. Tự động hóa Versioning qua Accept Header

**API Tương ứng chi tiết:**

```http
GET /repos/octocat/hello-world
Host: api.github.com
Accept: application/vnd.github.v3+json
```

**Phân tích:**
Thay vì chèn phiên bản vào URL (`/v3/repos/...`), GitHub dùng tính năng Content Negotiation thông qua `Accept` header. Việc dùng Vendor spec MIME model `application/vnd.github.v3` đảm bảo việc định tuyến hệ thống rõ ràng, chuẩn HTTP mà không làm gãy vỡ kiến trúc cây path của REST.
