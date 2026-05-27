# extremecloudiq.model.xiq_locked_client.XiqLockedClient

The data in the current page

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The data in the current page | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_name** | str,  | str,  | The client name | [optional] 
**client_mac** | str,  | str,  | The client mac address | [optional] 
**ssid** | str,  | str,  | The ssid | [optional] 
**user_name** | str,  | str,  | The user name | [optional] 
**[hm_id_names](#hm_id_names)** | list, tuple,  | tuple,  | The HM ID and name list | [optional] 
**locked_at** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp when the client was locked | [optional] value must be a 64 bit integer
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID of the client | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# hm_id_names

The HM ID and name list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The HM ID and name list | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHmIdName**](XiqHmIdName.md) | [**XiqHmIdName**](XiqHmIdName.md) | [**XiqHmIdName**](XiqHmIdName.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

