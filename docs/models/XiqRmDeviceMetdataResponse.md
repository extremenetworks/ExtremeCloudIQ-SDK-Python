# extremecloudiq.model.xiq_rm_device_metdata_response.XiqRmDeviceMetdataResponse

RM Metadata Response Class

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | RM Metadata Response Class | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[default_gateway](#default_gateway)** | list, tuple,  | tuple,  | The device default gateway | [optional] 
**[software_version](#software_version)** | list, tuple,  | tuple,  | The device OS software version | [optional] 
**[product_type](#product_type)** | list, tuple,  | tuple,  | The product type, such as AP_230, BR_100, NX9600, etc. | [optional] 
**[device_admin_state](#device_admin_state)** | list, tuple,  | tuple,  | The device admin state | [optional] 
**[country_code](#country_code)** | list, tuple,  | tuple,  | The assigned country code on the device | [optional] 
**[managed_by](#managed_by)** | list, tuple,  | tuple,  | The managed application for the device | [optional] 
**[sim_type](#sim_type)** | list, tuple,  | tuple,  | The device type - REAL or SIMULATED | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# default_gateway

The device default gateway

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device default gateway | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The device default gateway | 

# software_version

The device OS software version

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device OS software version | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The device OS software version | 

# product_type

The product type, such as AP_230, BR_100, NX9600, etc.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The product type, such as AP_230, BR_100, NX9600, etc. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The product type, such as AP_230, BR_100, NX9600, etc. | 

# device_admin_state

The device admin state

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device admin state | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDeviceAdminState**](XiqDeviceAdminState.md) | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) |  | 

# country_code

The assigned country code on the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The assigned country code on the device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The assigned country code on the device | value must be a 32 bit integer

# managed_by

The managed application for the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The managed application for the device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The managed application for the device | 

# sim_type

The device type - REAL or SIMULATED

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device type - REAL or SIMULATED | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDeviceType**](XiqDeviceType.md) | [**XiqDeviceType**](XiqDeviceType.md) | [**XiqDeviceType**](XiqDeviceType.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

