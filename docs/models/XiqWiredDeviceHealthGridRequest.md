# extremecloudiq.model.xiq_wired_device_health_grid_request.XiqWiredDeviceHealthGridRequest

Request body for the Wired Device Health grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request body for the Wired Device Health grid | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | List of site IDs to filter the Wired Device Health grid | [optional] 
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | List of device IDs to filter the Wired Device Health grid | [optional] 
**[filter_field](#filter_field)** | list, tuple,  | tuple,  | The filters available for the Wired Device Health grid | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# site_ids

List of site IDs to filter the Wired Device Health grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of site IDs to filter the Wired Device Health grid | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of site IDs to filter the Wired Device Health grid | value must be a 64 bit integer

# device_ids

List of device IDs to filter the Wired Device Health grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of device IDs to filter the Wired Device Health grid | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of device IDs to filter the Wired Device Health grid | value must be a 64 bit integer

# filter_field

The filters available for the Wired Device Health grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The filters available for the Wired Device Health grid | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWiredDeviceHealthFilterField**](XiqWiredDeviceHealthFilterField.md) | [**XiqWiredDeviceHealthFilterField**](XiqWiredDeviceHealthFilterField.md) | [**XiqWiredDeviceHealthFilterField**](XiqWiredDeviceHealthFilterField.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

