# XiqSetSsidModePskRequest

The request for setting the SSID to be PSK mode.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_management** | [**XiqSsidPskKeyManagement**](XiqSsidPskKeyManagement.md) |  | 
**encryption_method** | [**XiqSsidPskEncryptionMethod**](XiqSsidPskEncryptionMethod.md) |  | 
**anti_logging_threshold** | **int** | The anti logging threshold | [optional] 
**key_type** | [**XiqSsidKeyType**](XiqSsidKeyType.md) |  | 
**key_value** | **str** | The PSK key value, minimum 8 characters long | 
**sae_group** | [**XiqSsidSaeGroup**](XiqSsidSaeGroup.md) |  | [optional] 
**transition_mode** | **bool** | Indicates the transition mode if key management is WPA3 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


