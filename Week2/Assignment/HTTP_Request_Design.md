# Thiết kế HTTP Request cho 5 tình huống

Dưới đây là thiết kế các HTTP request cho tài nguyên Người dùng (User). Giả sử Base URL là `https://api.example.com`.

## 1. Lấy danh sách người dùng (Get User List)

Dùng để lấy danh sách người dùng, có phân trang.

- **Request:**
  - **Method:** `GET`
  - **URL:** `/api/v1/users`
  - **Query Parameters:**
    - `page`: 1 (Trang hiện tại)
    - `limit`: 10 (Số lượng bản ghi mỗi trang)
- **Response (200 OK):**
  ```json
  {
    "data": [
      { "id": 1, "name": "Nguyen Van A", "email": "a@example.com" },
      { "id": 2, "name": "Tran Thi B", "email": "b@example.com" }
    ],
    "meta": {
      "total": 100,
      "page": 1,
      "limit": 10
    }
  }
  ```

## 2. Lấy thông tin chi tiết người dùng (Get User Details)

Dùng để xem thông tin cụ thể của một người dùng dựa vào ID.

- **Request:**
  - **Method:** `GET`
  - **URL:** `/api/v1/users/{user_id}`
  - **Headers:**
    - `Authorization`: `Bearer <token>`
- **Response (200 OK):**
  ```json
  {
    "id": 1,
    "name": "Nguyen Van A",
    "email": "a@example.com",
    "created_at": "2023-10-01T10:00:00Z"
  }
  ```

## 3. Tạo người dùng mới (Create New User)

Dùng để tạo một tài khoản người dùng mới.

- **Request:**
  - **Method:** `POST`
  - **URL:** `/api/v1/users`
  - **Headers:**
    - `Content-Type`: `application/json`
  - **Body:**
    ```json
    {
      "name": "Le Van C",
      "email": "c@example.com",
      "password": "SecurePassword123!"
    }
    ```
- **Response (201 Created):**
  ```json
  {
    "id": 3,
    "name": "Le Van C",
    "email": "c@example.com",
    "message": "User created successfully"
  }
  ```

## 4. Cập nhật email người dùng (Update User Email)

Dùng để cập nhật địa chỉ email cho một người dùng cụ thể. Sử dụng PATCH để cập nhật một phần.

- **Request:**
  - **Method:** `PATCH`
  - **URL:** `/api/v1/users/{user_id}`
  - **Headers:**
    - `Content-Type`: `application/json`
    - `Authorization`: `Bearer <token>`
  - **Body:**
    ```json
    {
      "email": "new_email@example.com"
    }
    ```
- **Response (200 OK):**
  ```json
  {
    "id": 1,
    "email": "new_email@example.com",
    "message": "Email updated successfully"
  }
  ```

## 5. Xóa người dùng (Delete User)

Dùng để xóa vĩnh viễn một người dùng khỏi hệ thống.

- **Request:**
  - **Method:** `DELETE`
  - **URL:** `/api/v1/users/{user_id}`
  - **Headers:**
    - `Authorization`: `Bearer <token>`
- **Response (204 No Content):**
  - _(Không có nội dung body)_
