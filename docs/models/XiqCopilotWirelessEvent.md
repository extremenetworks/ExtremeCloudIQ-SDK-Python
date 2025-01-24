# extremecloudiq.model.xiq_copilot_wireless_event.XiqCopilotWirelessEvent

ExtremeCloud IQ Connectivity Experience Client Details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Connectivity Experience Client Details | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_id** | str,  | str,  | The unique identifier for clients | 
**mac** | str,  | str,  | The mac address | 
**average_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | The average duration to associate/authenticate | [optional] value must be a 64 bit float
**maximum_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum duration to associate/authenticate | [optional] value must be a 64 bit float
**os_type** | str,  | str,  | The os type | [optional] 
**threshold** | decimal.Decimal, int, float,  | decimal.Decimal,  | The threshold for association/authentication | [optional] value must be a 64 bit float
**hostname** | str,  | str,  | The hostname | [optional] 
**ssid** | str,  | str,  | The SSID | [optional] 
**retries_data** | [**XiqWirelessEventRetriesEntity**](XiqWirelessEventRetriesEntity.md) | [**XiqWirelessEventRetriesEntity**](XiqWirelessEventRetriesEntity.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

