# extremecloudiq.model.xiq_set_ssid_mode_dot1x_request.XiqSetSsidModeDot1xRequest

The request for setting the SSID to be 802.1x mode.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request for setting the SSID to be 802.1x mode. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**key_management** | [**XiqSsidDot1xKeyManagement**](XiqSsidDot1xKeyManagement.md) | [**XiqSsidDot1xKeyManagement**](XiqSsidDot1xKeyManagement.md) |  | 
**encryption_method** | [**XiqSsidDot1xEncryptionMethod**](XiqSsidDot1xEncryptionMethod.md) | [**XiqSsidDot1xEncryptionMethod**](XiqSsidDot1xEncryptionMethod.md) |  | 
**enable_idm** | bool,  | BoolClass,  | Flag for using ExtremeCloud IQ Authentication Service or not | 
**transition_mode** | bool,  | BoolClass,  | Flag for enabling transition mode if using WPA3 as the key management type | [optional] 
**radius_server_group_id** | decimal.Decimal, int,  | decimal.Decimal,  | The RADIUS server group ID if not using ExtremeCloud IQ Authentication Service | [optional] value must be a 64 bit integer
**[user_group_ids](#user_group_ids)** | list, tuple,  | tuple,  | The user group IDs if using ExtremeCloud IQ Authentication Service | [optional] 
**enable_uztna** | bool,  | BoolClass,  | Flag for using Authentication with ExtremeCloud Universal ZTNA or not | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# user_group_ids

The user group IDs if using ExtremeCloud IQ Authentication Service

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The user group IDs if using ExtremeCloud IQ Authentication Service | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The user group IDs if using ExtremeCloud IQ Authentication Service | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

