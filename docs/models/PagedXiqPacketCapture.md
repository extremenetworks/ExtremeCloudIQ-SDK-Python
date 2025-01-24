# extremecloudiq.model.paged_xiq_packet_capture.PagedXiqPacketCapture

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_count** | decimal.Decimal, int,  | decimal.Decimal,  | The total element count | value must be a 64 bit integer
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The element count of the current page | value must be a 32 bit integer
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The current page number | value must be a 32 bit integer
**total_pages** | decimal.Decimal, int,  | decimal.Decimal,  | The total page number based on request page size | value must be a 32 bit integer
**[data](#data)** | list, tuple,  | tuple,  | The data in the current page | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

The data in the current page

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The data in the current page | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqPacketCapture**](XiqPacketCapture.md) | [**XiqPacketCapture**](XiqPacketCapture.md) | [**XiqPacketCapture**](XiqPacketCapture.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

