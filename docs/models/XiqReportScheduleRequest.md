# extremecloudiq.model.xiq_report_schedule_request.XiqReportScheduleRequest

List of schedules (e.g., daily, weekly, etc.).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of schedules (e.g., daily, weekly, etc.). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[schedule_days](#schedule_days)** | list, tuple,  | tuple,  | Days on which the report is scheduled (e.g., [0] for Sunday). | 
**frequency_type** | [**XiqScheduleFrequency**](XiqScheduleFrequency.md) | [**XiqScheduleFrequency**](XiqScheduleFrequency.md) |  | 
**schedule_time** | str,  | str,  | The scheduled time in HH:MM format (e.g., 08:00). | [optional] if omitted the server will use the default value of "1439"
**schedule_timezone** | str,  | str,  | The timezone of the scheduled report. | [optional] if omitted the server will use the default value of "UTC"
**enable_schedule** | bool,  | BoolClass,  | Whether the schedule is enabled or not. | [optional] if omitted the server will use the default value of True
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

