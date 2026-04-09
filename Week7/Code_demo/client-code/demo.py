import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Khởi tạo cấu hình (nếu server chạy cổng khác, có thể override ở đây)
configuration = openapi_client.Configuration(
    host = "http://localhost:8080"
)

# Sử dụng Client
with openapi_client.ApiClient(configuration) as api_client:
    # Gọi tới Books api
    api_instance = openapi_client.BooksApi(api_client)

    try:
        # Lấy danh sách Book
        api_response = api_instance.books_get()
        pprint(api_response)
    except ApiException as e:
        print("Lỗi khi gọi API: %s\n" % e)