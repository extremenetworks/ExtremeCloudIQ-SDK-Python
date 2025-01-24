# extremecloudiq.model.xiq_advanced_onboard_device_request.XiqAdvancedOnboardDeviceRequest

The payload to advanced onboard devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload to advanced onboard devices | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[extreme](#extreme)** | list, tuple,  | tuple,  | The selected target devices | [optional] 
**[exos](#exos)** | list, tuple,  | tuple,  | The selected target devices | [optional] 
**[voss](#voss)** | list, tuple,  | tuple,  | The selected target devices | [optional] 
**[wing](#wing)** | list, tuple,  | tuple,  | The selected target devices | [optional] 
**[dell](#dell)** | list, tuple,  | tuple,  | The selected target devices | [optional] 
**[dt](#dt)** | list, tuple,  | tuple,  | The selected target devices | [optional] 
**unmanaged** | bool,  | BoolClass,  | Whether to unmanage the devices | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extreme

The selected target devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The selected target devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqExtremeDevice**](XiqExtremeDevice.md) | [**XiqExtremeDevice**](XiqExtremeDevice.md) | [**XiqExtremeDevice**](XiqExtremeDevice.md) |  | 

# exos

The selected target devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The selected target devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqExosDevice**](XiqExosDevice.md) | [**XiqExosDevice**](XiqExosDevice.md) | [**XiqExosDevice**](XiqExosDevice.md) |  | 

# voss

The selected target devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The selected target devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqVossDevice**](XiqVossDevice.md) | [**XiqVossDevice**](XiqVossDevice.md) | [**XiqVossDevice**](XiqVossDevice.md) |  | 

# wing

The selected target devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The selected target devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWingDevice**](XiqWingDevice.md) | [**XiqWingDevice**](XiqWingDevice.md) | [**XiqWingDevice**](XiqWingDevice.md) |  | 

# dell

The selected target devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The selected target devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDellDevice**](XiqDellDevice.md) | [**XiqDellDevice**](XiqDellDevice.md) | [**XiqDellDevice**](XiqDellDevice.md) |  | 

# dt

The selected target devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The selected target devices | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDigitalTwinOnboardDevice**](XiqDigitalTwinOnboardDevice.md) | [**XiqDigitalTwinOnboardDevice**](XiqDigitalTwinOnboardDevice.md) | [**XiqDigitalTwinOnboardDevice**](XiqDigitalTwinOnboardDevice.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

