# extremecloudiq.model.xiq_ssid_access_security.XiqSsidAccessSecurity

The SSID access security.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The SSID access security. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**key_type** | [**XiqSsidKeyType**](XiqSsidKeyType.md) | [**XiqSsidKeyType**](XiqSsidKeyType.md) |  | [optional] 
**key_value** | str,  | str,  | The schedule type name. | [optional] 
**sae_group** | [**XiqSsidSaeGroup**](XiqSsidSaeGroup.md) | [**XiqSsidSaeGroup**](XiqSsidSaeGroup.md) |  | [optional] 
**anti_logging_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | The anti logging threshold value. | [optional] value must be a 64 bit integer
**transition_mode** | bool,  | BoolClass,  | The flag for enabling transition mode. | [optional] 
**security_type** | str,  | str,  | The security type. | [optional] 
**key_management** | [**XiqSsidKeyManagement**](XiqSsidKeyManagement.md) | [**XiqSsidKeyManagement**](XiqSsidKeyManagement.md) |  | [optional] 
**encryption_method** | [**XiqSsidEncryptionMethod**](XiqSsidEncryptionMethod.md) | [**XiqSsidEncryptionMethod**](XiqSsidEncryptionMethod.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

