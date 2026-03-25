# extremecloudiq.model.xiq_update_report_schedule_request.XiqUpdateReportScheduleRequest

List of schedules (e.g., daily, weekly, etc.).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of schedules (e.g., daily, weekly, etc.). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**report_schedule_id** | decimal.Decimal, int,  | decimal.Decimal,  | Unique ID of the schedule | [optional] value must be a 64 bit integer
**frequency_type** | [**XiqScheduleFrequency**](XiqScheduleFrequency.md) | [**XiqScheduleFrequency**](XiqScheduleFrequency.md) |  | [optional] 
**schedule_time** | str,  | str,  | The scheduled time in HH:MM:SS format (e.g., 08:00:00). | [optional] 
**schedule_timezone** | str,  | str,  | The timezone of the scheduled report. | [optional] 
**[schedule_days](#schedule_days)** | list, tuple,  | tuple,  | Days on which the report is scheduled (e.g., [0] for Sunday). | [optional] 
**enable_schedule** | bool,  | BoolClass,  | Whether the schedule is enabled or not. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# schedule_days

Days on which the report is scheduled (e.g., [0] for Sunday).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Days on which the report is scheduled (e.g., [0] for Sunday). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | Days on which the report is scheduled (e.g., [0] for Sunday). | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

