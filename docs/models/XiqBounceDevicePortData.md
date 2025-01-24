# extremecloudiq.model.xiq_bounce_device_port_data.XiqBounceDevicePortData

The data required for bounce port response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data required for bounce port response | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status** | decimal.Decimal, int,  | decimal.Decimal,  | The status value | [optional] value must be a 32 bit integer
**request_id** | decimal.Decimal, int,  | decimal.Decimal,  | The requestId of the response | [optional] value must be a 64 bit integer
**[results](#results)** | list, tuple,  | tuple,  | The list of results | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# results

The list of results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of results | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqBounceDevicePortOperationResult**](XiqBounceDevicePortOperationResult.md) | [**XiqBounceDevicePortOperationResult**](XiqBounceDevicePortOperationResult.md) | [**XiqBounceDevicePortOperationResult**](XiqBounceDevicePortOperationResult.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

