# openapi_client.BooksApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**books_get**](BooksApi.md#books_get) | **GET** /books | List books
[**books_id_delete**](BooksApi.md#books_id_delete) | **DELETE** /books/{id} | Delete a book
[**books_id_get**](BooksApi.md#books_id_get) | **GET** /books/{id} | Get a book by ID
[**books_id_put**](BooksApi.md#books_id_put) | **PUT** /books/{id} | Update a book
[**books_post**](BooksApi.md#books_post) | **POST** /books | Create a book


# **books_get**
> List[Book] books_get()

List books

### Example


```python
import openapi_client
from openapi_client.models.book import Book
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)

    try:
        # List books
        api_response = api_instance.books_get()
        print("The response of BooksApi->books_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->books_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Book]**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of books. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **books_id_delete**
> books_id_delete(id)

Delete a book

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the book

    try:
        # Delete a book
        api_instance.books_id_delete(id)
    except Exception as e:
        print("Exception when calling BooksApi->books_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the book | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Book deleted. |  -  |
**404** | Book not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **books_id_get**
> Book books_id_get(id)

Get a book by ID

### Example


```python
import openapi_client
from openapi_client.models.book import Book
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the book

    try:
        # Get a book by ID
        api_response = api_instance.books_id_get(id)
        print("The response of BooksApi->books_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->books_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the book | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book details. |  -  |
**404** | Book not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **books_id_put**
> Book books_id_put(id, new_book)

Update a book

### Example


```python
import openapi_client
from openapi_client.models.book import Book
from openapi_client.models.new_book import NewBook
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)
    id = 'id_example' # str | The unique identifier of the book
    new_book = openapi_client.NewBook() # NewBook | 

    try:
        # Update a book
        api_response = api_instance.books_id_put(id, new_book)
        print("The response of BooksApi->books_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->books_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the book | 
 **new_book** | [**NewBook**](NewBook.md)|  | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Book updated. |  -  |
**404** | Book not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **books_post**
> Book books_post(new_book)

Create a book

### Example


```python
import openapi_client
from openapi_client.models.book import Book
from openapi_client.models.new_book import NewBook
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BooksApi(api_client)
    new_book = openapi_client.NewBook() # NewBook | 

    try:
        # Create a book
        api_response = api_instance.books_post(new_book)
        print("The response of BooksApi->books_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BooksApi->books_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_book** | [**NewBook**](NewBook.md)|  | 

### Return type

[**Book**](Book.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Book created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

