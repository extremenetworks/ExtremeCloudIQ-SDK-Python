# extremecloudiq.model.xiq_qoe_diagnostics_channel_metadata_filter.XiqQoeDiagnosticsChannelMetadataFilter

Request body for Alert Diagnostics Filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Request body for Alert Diagnostics Filter | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[site_ids](#site_ids)** | list, tuple,  | tuple,  | List of site ids | [optional] 
**[building_ids](#building_ids)** | list, tuple,  | tuple,  | List of building ids | [optional] 
**[floor_ids](#floor_ids)** | list, tuple,  | tuple,  | List of floor ids | [optional] 
**[ssids](#ssids)** | list, tuple,  | tuple,  | List of ssids | [optional] 
**[bands](#bands)** | list, tuple,  | tuple,  | List of band | [optional] 
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

# floor_ids

List of floor ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of floor ids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | List of floor ids | value must be a 64 bit integer

# ssids

List of ssids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of ssids | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of ssids | 

# bands

List of band

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of band | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) | [**XiqDiagnosticsBands**](XiqDiagnosticsBands.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

