# XiqSetSsidModeWepRequest

The request for setting the SSID to be WEP mode.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_management** | [**XiqSsidWepKeyManagement**](XiqSsidWepKeyManagement.md) |  | 
**encryption_method** | [**XiqSsidWepEncryptionMethod**](XiqSsidWepEncryptionMethod.md) |  | 
**authentication_method** | [**XiqSsidWepAuthenticationMethod**](XiqSsidWepAuthenticationMethod.md) |  | [optional] 
**default_key** | [**XiqSsidWepDefaultKey**](XiqSsidWepDefaultKey.md) |  | [optional] 
**key_type** | [**XiqSsidKeyType**](XiqSsidKeyType.md) |  | [optional] 
**key_value** | **str** | The first key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key | [optional] 
**key_value2** | **str** | The second key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key | [optional] 
**key_value3** | **str** | The third key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key | [optional] 
**key_value4** | **str** | The fourth key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key | [optional] 
**radius_server_group_id** | **int** | The RADIUS server group ID if using WEP_8021x as the key management | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


