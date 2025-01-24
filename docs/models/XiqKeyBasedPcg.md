# extremecloudiq.model.xiq_key_based_pcg.XiqKeyBasedPcg

The response of key based PCG data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The response of key based PCG data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**policy_id** | decimal.Decimal, int,  | decimal.Decimal,  | The network policy ID | value must be a 64 bit integer
**policy_name** | str,  | str,  | The network policy name | 
**ssid_name** | str,  | str,  | The SSID name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**enabled** | bool,  | BoolClass,  | Enabled Key Based PCG | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**[users](#users)** | list, tuple,  | tuple,  | The XIQ key based PCG users | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# users

The XIQ key based PCG users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The XIQ key based PCG users | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqKeyBasedPcgUser**](XiqKeyBasedPcgUser.md) | [**XiqKeyBasedPcgUser**](XiqKeyBasedPcgUser.md) | [**XiqKeyBasedPcgUser**](XiqKeyBasedPcgUser.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

