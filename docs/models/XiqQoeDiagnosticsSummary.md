# extremecloudiq.model.xiq_qoe_diagnostics_summary.XiqQoeDiagnosticsSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metrics** | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) | [**XiqQoeDiagnosticsMetrics**](XiqQoeDiagnosticsMetrics.md) |  | [optional] 
**description** | str,  | str,  | Description for the metrics | [optional] 
**[filters_supported](#filters_supported)** | list, tuple,  | tuple,  | Filters applicable for the metrics | [optional] 
**metrics_group** | str,  | str,  | Metrics Grouping | [optional] must be one of ["GROUP_DEVICES", "GROUP_CLIENTS", "GROUP_APPLICATIONS_USAGE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# filters_supported

Filters applicable for the metrics

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Filters applicable for the metrics | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Filters applicable for the metrics | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

