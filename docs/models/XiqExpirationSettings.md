# extremecloudiq.model.xiq_expiration_settings.XiqExpirationSettings

The password expiration settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The password expiration settings | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**expiration_type** | [**XiqExpirationType**](XiqExpirationType.md) | [**XiqExpirationType**](XiqExpirationType.md) |  | [optional] 
**valid_during_dates** | [**XiqValidDuringDateSettings**](XiqValidDuringDateSettings.md) | [**XiqValidDuringDateSettings**](XiqValidDuringDateSettings.md) |  | [optional] 
**valid_for_time_period** | [**XiqValidForTimePeriodSettings**](XiqValidForTimePeriodSettings.md) | [**XiqValidForTimePeriodSettings**](XiqValidForTimePeriodSettings.md) |  | [optional] 
**valid_daily** | [**XiqValidDailySettings**](XiqValidDailySettings.md) | [**XiqValidDailySettings**](XiqValidDailySettings.md) |  | [optional] 
**expiration_action** | [**XiqExpirationActionType**](XiqExpirationActionType.md) | [**XiqExpirationActionType**](XiqExpirationActionType.md) |  | [optional] 
**post_expiration_action** | [**XiqPostExpirationAction**](XiqPostExpirationAction.md) | [**XiqPostExpirationAction**](XiqPostExpirationAction.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

