# extremecloudiq.model.xiq_viq_export_import_status_response.XiqViqExportImportStatusResponse

ExtremeCloud IQ Viq Export Import Status 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Viq Export Import Status  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_name** | str,  | str,  | Name of the user | [optional] 
**vhm_id** | str,  | str,  | VHM ID of the user | [optional] 
**operation** | str,  | str,  | Type of operation | [optional] 
**status** | str,  | str,  | Current status of operation | [optional] 
**total_finish_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Total finish percentage | [optional] value must be a 64 bit integer
**[viq_task_progresses](#viq_task_progresses)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# viq_task_progresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqViqTaskProgress**](XiqViqTaskProgress.md) | [**XiqViqTaskProgress**](XiqViqTaskProgress.md) | [**XiqViqTaskProgress**](XiqViqTaskProgress.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

