# extremecloudiq.model.xiq_device_alarm.XiqDeviceAlarm

The device alarm view

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The device alarm view | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**entity_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID | [optional] value must be a 64 bit integer
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp for alarm created | [optional] value must be a 64 bit integer
**severity** | str,  | str,  | The severity of the alarm | [optional] 
**category** | str,  | str,  | The category of the alarm | [optional] 
**device_mac** | str,  | str,  | The device MAC of the alarm | [optional] 
**client_mac** | str,  | str,  | The client MAC of the alarm | [optional] 
**description** | str,  | str,  | The alarm description | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

