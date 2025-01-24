# extremecloudiq.model.xiq_set_ssid_mode_psk_request.XiqSetSsidModePskRequest

The request for setting the SSID to be PSK mode.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request for setting the SSID to be PSK mode. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**key_management** | [**XiqSsidPskKeyManagement**](XiqSsidPskKeyManagement.md) | [**XiqSsidPskKeyManagement**](XiqSsidPskKeyManagement.md) |  | 
**encryption_method** | [**XiqSsidPskEncryptionMethod**](XiqSsidPskEncryptionMethod.md) | [**XiqSsidPskEncryptionMethod**](XiqSsidPskEncryptionMethod.md) |  | 
**key_type** | [**XiqSsidKeyType**](XiqSsidKeyType.md) | [**XiqSsidKeyType**](XiqSsidKeyType.md) |  | 
**key_value** | str,  | str,  | The PSK key value, minimum 8 characters long | 
**anti_logging_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | The anti logging threshold | [optional] value must be a 32 bit integer
**sae_group** | [**XiqSsidSaeGroup**](XiqSsidSaeGroup.md) | [**XiqSsidSaeGroup**](XiqSsidSaeGroup.md) |  | [optional] 
**transition_mode** | bool,  | BoolClass,  | Indicates the transition mode if key management is WPA3 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

