# extremecloudiq.model.xiq_advanced_onboard_device_response.XiqAdvancedOnboardDeviceResponse

The response for advanced onboard devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The response for advanced onboard devices | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[success_devices](#success_devices)** | list, tuple,  | tuple,  | The success devices | [optional] 
**[failure_devices](#failure_devices)** | list, tuple,  | tuple,  | The failure devices | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# success_devices

The success devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The success devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqSuccessOnboardDevice**](XiqSuccessOnboardDevice.md) | [**XiqSuccessOnboardDevice**](XiqSuccessOnboardDevice.md) | [**XiqSuccessOnboardDevice**](XiqSuccessOnboardDevice.md) |  | 

# failure_devices

The failure devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The failure devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqFailureOnboardDevice**](XiqFailureOnboardDevice.md) | [**XiqFailureOnboardDevice**](XiqFailureOnboardDevice.md) | [**XiqFailureOnboardDevice**](XiqFailureOnboardDevice.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

