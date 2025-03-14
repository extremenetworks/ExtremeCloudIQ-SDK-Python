# extremecloudiq.model.xiq_client_detail.XiqClientDetail

The Client Details Info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Client Details Info | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_connected** | bool,  | BoolClass,  | The device connected value | [optional] 
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID | [optional] value must be a 64 bit integer
**os_type** | str,  | str,  | The client Os Type | [optional] 
**ip_address** | str,  | str,  | The client Ip Address | [optional] 
**mac_address** | str,  | str,  | The client mac Address | [optional] 
**device_location_names** | str,  | str,  | The location hierarchical tree | [optional] 
**device_location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The location ID | [optional] value must be a 64 bit integer
**alias** | str,  | str,  | The client alias name | [optional] 
**user** | str,  | str,  | The user name | [optional] 
**connection_to** | str,  | str,  | The Ap hostname | [optional] 
**connection_time** | decimal.Decimal, int,  | decimal.Decimal,  | The connection Time | [optional] value must be a 64 bit integer
**vlan** | decimal.Decimal, int,  | decimal.Decimal,  | The vlan | [optional] value must be a 32 bit integer
**cwp_used** | decimal.Decimal, int,  | decimal.Decimal,  | The Captive Web Portal used | [optional] value must be a 32 bit integer
**user_profile** | str,  | str,  | The user profile name | [optional] 
**ssid** | str,  | str,  | The SSID | [optional] 
**radio** | str,  | str,  | The Radio Info (2G,5G,6G) | [optional] 
**wifi_protocol** | str,  | str,  | The wifi Protocol | [optional] 
**channel** | decimal.Decimal, int,  | decimal.Decimal,  | The channel value | [optional] value must be a 32 bit integer
**client_hostname** | str,  | str,  | The Client hostName | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

