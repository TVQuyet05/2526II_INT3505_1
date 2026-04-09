# NewBook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**author** | **str** |  | 
**published_year** | **int** |  | 
**genre** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.new_book import NewBook

# TODO update the JSON string below
json = "{}"
# create an instance of NewBook from a JSON string
new_book_instance = NewBook.from_json(json)
# print the JSON string representation of the object
print(NewBook.to_json())

# convert the object into a dict
new_book_dict = new_book_instance.to_dict()
# create an instance of NewBook from a dict
new_book_from_dict = NewBook.from_dict(new_book_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


