# extremecloudiq.model.xiq_viq_task_progress.XiqViqTaskProgress

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**task_name** | str,  | str,  | Current task name | [optional] 
**finish_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Current task finish percentage | [optional] value must be a 64 bit integer
**detail** | str,  | str,  | Detail of current task | [optional] 
**status** | str,  | str,  | Status of current task | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

