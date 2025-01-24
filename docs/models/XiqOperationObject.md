# extremecloudiq.model.xiq_operation_object.XiqOperationObject

Long Running Operation (LRO) model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Long Running Operation (LRO) model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metadata** | [**XiqOperationMetadata**](XiqOperationMetadata.md) | [**XiqOperationMetadata**](XiqOperationMetadata.md) |  | 
**id** | str,  | str,  | The unique identifier of the operation | 
**done** | bool,  | BoolClass,  | Whether the operation is done | 
**[response](#response)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The API response of the operation if the status is SUCCEEDED | [optional] 
**error** | [**XiqError**](XiqError.md) | [**XiqError**](XiqError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# response

The API response of the operation if the status is SUCCEEDED

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The API response of the operation if the status is SUCCEEDED | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

