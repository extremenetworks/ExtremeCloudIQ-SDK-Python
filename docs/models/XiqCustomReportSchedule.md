# extremecloudiq.model.xiq_custom_report_schedule.XiqCustomReportSchedule

Generic ExtremeCloud IQ Scheduled Custom Report model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Generic ExtremeCloud IQ Scheduled Custom Report model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**report_schedule_id** | decimal.Decimal, int,  | decimal.Decimal,  | Unique ID of the scheduled report | [optional] value must be a 64 bit integer
**report_id** | decimal.Decimal, int,  | decimal.Decimal,  | Unique ID of the report | [optional] value must be a 64 bit integer
**report_name** | str,  | str,  | Name of the actual report | [optional] 
**report_description** | str,  | str,  | Short description of the report | [optional] 
**recipients_count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of recipients for the report | [optional] value must be a 32 bit integer
**frequency** | [**XiqScheduleFrequency**](XiqScheduleFrequency.md) | [**XiqScheduleFrequency**](XiqScheduleFrequency.md) |  | [optional] 
**enable_schedule** | bool,  | BoolClass,  | Whether the schedule is enabled or not | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

