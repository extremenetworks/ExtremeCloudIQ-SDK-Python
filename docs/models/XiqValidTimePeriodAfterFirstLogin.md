# extremecloudiq.model.xiq_valid_time_period_after_first_login.XiqValidTimePeriodAfterFirstLogin

The settings for the valid time period after First Login option or null for the other option

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The settings for the valid time period after First Login option or null for the other option | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**valid_time_period** | decimal.Decimal, int,  | decimal.Decimal,  | The valid time period after the first login | value must be a 32 bit integer
**valid_time_period_unit** | [**XiqDateTimeUnitType**](XiqDateTimeUnitType.md) | [**XiqDateTimeUnitType**](XiqDateTimeUnitType.md) |  | 
**first_login_within_unit** | [**XiqDateTimeUnitType**](XiqDateTimeUnitType.md) | [**XiqDateTimeUnitType**](XiqDateTimeUnitType.md) |  | 
**first_login_within** | decimal.Decimal, int,  | decimal.Decimal,  | The first time the access key must be used | value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

