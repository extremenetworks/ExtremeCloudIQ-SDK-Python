# extremecloudiq.model.xiq_set_ssid_mode_wep_request.XiqSetSsidModeWepRequest

The request for setting the SSID to be WEP mode.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request for setting the SSID to be WEP mode. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**key_management** | [**XiqSsidWepKeyManagement**](XiqSsidWepKeyManagement.md) | [**XiqSsidWepKeyManagement**](XiqSsidWepKeyManagement.md) |  | 
**encryption_method** | [**XiqSsidWepEncryptionMethod**](XiqSsidWepEncryptionMethod.md) | [**XiqSsidWepEncryptionMethod**](XiqSsidWepEncryptionMethod.md) |  | 
**authentication_method** | [**XiqSsidWepAuthenticationMethod**](XiqSsidWepAuthenticationMethod.md) | [**XiqSsidWepAuthenticationMethod**](XiqSsidWepAuthenticationMethod.md) |  | [optional] 
**default_key** | [**XiqSsidWepDefaultKey**](XiqSsidWepDefaultKey.md) | [**XiqSsidWepDefaultKey**](XiqSsidWepDefaultKey.md) |  | [optional] 
**key_type** | [**XiqSsidKeyType**](XiqSsidKeyType.md) | [**XiqSsidKeyType**](XiqSsidKeyType.md) |  | [optional] 
**key_value** | str,  | str,  | The first key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key | [optional] 
**key_value2** | str,  | str,  | The second key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key | [optional] 
**key_value3** | str,  | str,  | The third key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key | [optional] 
**key_value4** | str,  | str,  | The fourth key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key | [optional] 
**radius_server_group_id** | decimal.Decimal, int,  | decimal.Decimal,  | The RADIUS server group ID if using WEP_8021x as the key management | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

