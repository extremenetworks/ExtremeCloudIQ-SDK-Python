# extremecloudiq.model.xiq_thread_stop_commissioner_by_buildings_response.XiqThreadStopCommissionerByBuildingsResponse

The response for stopping the thread commissioner on devices under buildings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The response for stopping the thread commissioner on devices under buildings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[success_devices](#success_devices)** | list, tuple,  | tuple,  | The devices where the commissioner stopped successfully. | [optional] 
**[failure_devices](#failure_devices)** | list, tuple,  | tuple,  | The devices where the commissioner failed to stop. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# success_devices

The devices where the commissioner stopped successfully.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The devices where the commissioner stopped successfully. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqSuccessCommissionerDevice**](XiqSuccessCommissionerDevice.md) | [**XiqSuccessCommissionerDevice**](XiqSuccessCommissionerDevice.md) | [**XiqSuccessCommissionerDevice**](XiqSuccessCommissionerDevice.md) |  | 

# failure_devices

The devices where the commissioner failed to stop.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The devices where the commissioner failed to stop. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqFailureCommissionerDevice**](XiqFailureCommissionerDevice.md) | [**XiqFailureCommissionerDevice**](XiqFailureCommissionerDevice.md) | [**XiqFailureCommissionerDevice**](XiqFailureCommissionerDevice.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

