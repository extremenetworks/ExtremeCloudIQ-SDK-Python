# extremecloudiq.model.xiq_wifi_efficiency_stats_response.XiqWifiEfficiencyStatsResponse

Copilot Wifi Efficiency Stats

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Wifi Efficiency Stats | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_client_sessions** | decimal.Decimal, int,  | decimal.Decimal,  | The total client sessions | [optional] value must be a 64 bit integer
**show_tx_data** | bool,  | BoolClass,  | The show tx data | [optional] 
**[sessions_data](#sessions_data)** | list, tuple,  | tuple,  | The sessions data | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sessions_data

The sessions data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The sessions data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqSessionsDataEntity**](XiqSessionsDataEntity.md) | [**XiqSessionsDataEntity**](XiqSessionsDataEntity.md) | [**XiqSessionsDataEntity**](XiqSessionsDataEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

