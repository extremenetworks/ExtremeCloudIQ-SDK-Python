# extremecloudiq.model.xiq_schedule.XiqSchedule

The OS object.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The OS object. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  | Schedule description. | [optional] 
**schedule_type** | [**XiqScheduleType**](XiqScheduleType.md) | [**XiqScheduleType**](XiqScheduleType.md) |  | [optional] 
**start_date** | str, date,  | str,  | The start date of the schedule. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**end_date** | str, date,  | str,  | The end date of the schedule. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**start_time** | str,  | str,  | The start time of the schedule. | [optional] 
**end_time** | str,  | str,  | The end time of the schedule. | [optional] 
**recurrence_type** | [**XiqRecurrenceType**](XiqRecurrenceType.md) | [**XiqRecurrenceType**](XiqRecurrenceType.md) |  | [optional] 
**weekday_from** | [**XiqWeekday**](XiqWeekday.md) | [**XiqWeekday**](XiqWeekday.md) |  | [optional] 
**weekday_to** | [**XiqWeekday**](XiqWeekday.md) | [**XiqWeekday**](XiqWeekday.md) |  | [optional] 
**start_time2** | str,  | str,  | The start time of the schedule. | [optional] 
**end_time2** | str,  | str,  | The end time of the schedule. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

