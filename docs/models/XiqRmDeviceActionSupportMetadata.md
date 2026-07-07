# extremecloudiq.model.xiq_rm_device_action_support_metadata.XiqRmDeviceActionSupportMetadata

The metadata for device action support

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The metadata for device action support | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_action** | [**XiqRmDeviceAction**](XiqRmDeviceAction.md) | [**XiqRmDeviceAction**](XiqRmDeviceAction.md) |  | [optional] 
**[supported_wireless_product_types](#supported_wireless_product_types)** | list, tuple,  | tuple,  | The wireless device models supported | [optional] 
**[supported_wired_product_types](#supported_wired_product_types)** | list, tuple,  | tuple,  | The wired device models supported | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# supported_wireless_product_types

The wireless device models supported

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The wireless device models supported | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The wireless device models supported | 

# supported_wired_product_types

The wired device models supported

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The wired device models supported | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The wired device models supported | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

