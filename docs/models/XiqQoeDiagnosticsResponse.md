# extremecloudiq.model.xiq_qoe_diagnostics_response.XiqQoeDiagnosticsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple,  | tuple,  |  | 
**time_range** | [**XiqDiagnosticsTimeRange**](XiqDiagnosticsTimeRange.md) | [**XiqDiagnosticsTimeRange**](XiqDiagnosticsTimeRange.md) |  | 
**metrics_group** | str,  | str,  | Metrics Group | must be one of ["GROUP_DEVICES", "GROUP_CLIENTS", "GROUP_APPLICATIONS_USAGE", ] 
**name** | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) |  | 
**[os_row_data](#os_row_data)** | list, tuple,  | tuple,  |  | [optional] 
**[session_row_data](#session_row_data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# os_row_data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqQoeDiagnosticsOsRowData**](XiqQoeDiagnosticsOsRowData.md) | [**XiqQoeDiagnosticsOsRowData**](XiqQoeDiagnosticsOsRowData.md) | [**XiqQoeDiagnosticsOsRowData**](XiqQoeDiagnosticsOsRowData.md) |  | 

# session_row_data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqQoeDiagnosticsSessionRowData**](XiqQoeDiagnosticsSessionRowData.md) | [**XiqQoeDiagnosticsSessionRowData**](XiqQoeDiagnosticsSessionRowData.md) | [**XiqQoeDiagnosticsSessionRowData**](XiqQoeDiagnosticsSessionRowData.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

