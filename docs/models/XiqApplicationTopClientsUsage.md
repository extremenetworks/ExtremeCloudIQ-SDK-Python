# extremecloudiq.model.xiq_application_top_clients_usage.XiqApplicationTopClientsUsage

The Top N Clients Usage per Application

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Top N Clients Usage per Application | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**application_id** | decimal.Decimal, int,  | decimal.Decimal,  | The application ID | [optional] value must be a 64 bit integer
**client_id** | decimal.Decimal, int,  | decimal.Decimal,  | The TOP N client ID | [optional] value must be a 64 bit integer
**client_mac_address** | str,  | str,  | The MAC address of TOP N client | [optional] 
**client_host_name** | str,  | str,  | The host name of TOP N client | [optional] 
**usage** | decimal.Decimal, int,  | decimal.Decimal,  | The TOP N client usage | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

