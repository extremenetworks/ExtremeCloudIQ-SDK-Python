# extremecloudiq.model.xiq_valid_daily_settings.XiqValidDailySettings

The settings for Valid Daily option or null for other settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The settings for Valid Daily option or null for other settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**daily_start_minute** | decimal.Decimal, int,  | decimal.Decimal,  | The minute of the hour | value must be a 32 bit integer
**daily_end_minute** | decimal.Decimal, int,  | decimal.Decimal,  | The minute of the hour | value must be a 32 bit integer
**daily_end_hour** | decimal.Decimal, int,  | decimal.Decimal,  | The 24-hour format end hour of day the end | value must be a 32 bit integer
**daily_start_hour** | decimal.Decimal, int,  | decimal.Decimal,  | The 24-hour format start hour of the day | value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

