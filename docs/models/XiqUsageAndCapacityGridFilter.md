# extremecloudiq.model.xiq_usage_and_capacity_grid_filter.XiqUsageAndCapacityGridFilter

Request body for Usage and Capacity Filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request body for Usage and Capacity Filter | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | List of site ids | [optional] 
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | List of device ids | [optional] 
**[building_ids](#building_ids)** | list, tuple,  | tuple,  | List of building ids | [optional] 
**[buildings](#buildings)** | list, tuple,  | tuple,  | List of buildings | [optional] 
**[floors](#floors)** | list, tuple,  | tuple,  | List of floors | [optional] 
**has_usage_capacity_issues** | bool,  | BoolClass,  | Flag to filter usage capacity issues | [optional] 
**[number_filters](#number_filters)** | list, tuple,  | tuple,  | List of number filters | [optional] 
**has_packet_loss_issues** | bool,  | BoolClass,  | Flag to filter packet loss issues | [optional] 
**has_retries_issues** | bool,  | BoolClass,  | Flag to filter retry issues | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# site_ids

List of site ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of site ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of site ids | value must be a 64 bit integer

# device_ids

List of device ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of device ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of device ids | value must be a 64 bit integer

# building_ids

List of building ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of building ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of building ids | value must be a 64 bit integer

# buildings

List of buildings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of buildings | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of buildings | 

# floors

List of floors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of floors | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of floors | 

# number_filters

List of number filters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of number filters | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqNumberFilter**](XiqNumberFilter.md) | [**XiqNumberFilter**](XiqNumberFilter.md) | [**XiqNumberFilter**](XiqNumberFilter.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

