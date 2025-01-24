# extremecloudiq.model.xiq_set_ssid_mode_ppsk_request.XiqSetSsidModePpskRequest

The request for setting the SSID to be PPSK mode.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request for setting the SSID to be PPSK mode. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**key_management** | [**XiqSsidPpskKeyManagement**](XiqSsidPpskKeyManagement.md) | [**XiqSsidPpskKeyManagement**](XiqSsidPpskKeyManagement.md) |  | 
**encryption_method** | [**XiqSsidPskEncryptionMethod**](XiqSsidPskEncryptionMethod.md) | [**XiqSsidPskEncryptionMethod**](XiqSsidPskEncryptionMethod.md) |  | 
**enable_mac_bind** | bool,  | BoolClass,  | Flag for enabling mac binding or not. This setting is only supported with local PPSK. | 
**[user_group_ids](#user_group_ids)** | list, tuple,  | tuple,  | The user group IDs to be attached to the SSID, cannot be empty | 
**enable_max_clients_per_ppsk** | bool,  | BoolClass,  | Flag for enabling the max clients per PPSK | 
**max_clients_per_ppsk** | decimal.Decimal, int,  | decimal.Decimal,  | The max clients (0-15) per PPSK if enabled enable_max_clients_per_ppsk flag, 0 means unlimited | [optional] value must be a 32 bit integer
**max_macs_per_ppsk** | decimal.Decimal, int,  | decimal.Decimal,  | Set the max MAC binding numbers per private PSK, Min:1, Max:5 | [optional] value must be a 32 bit integer
**ppsk_server_id** | decimal.Decimal, int,  | decimal.Decimal,  | The PPSK server device ID | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user_group_ids

The user group IDs to be attached to the SSID, cannot be empty

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The user group IDs to be attached to the SSID, cannot be empty | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The user group IDs to be attached to the SSID, cannot be empty | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

