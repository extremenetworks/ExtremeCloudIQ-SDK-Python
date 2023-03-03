# XiqSetSsidModeDot1xRequest

The request for setting the SSID to be 802.1x mode.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_management** | [**XiqSsidDot1xKeyManagement**](XiqSsidDot1xKeyManagement.md) |  | 
**encryption_method** | [**XiqSsidDot1xEncryptionMethod**](XiqSsidDot1xEncryptionMethod.md) |  | 
**enable_idm** | **bool** | Flag for using ExtremeCloud IQ Authentication Service or not | 
**transition_mode** | **bool** | Flag for enabling transition mode if using WPA3 as the key management type | [optional] 
**radius_server_group_id** | **int** | The RADIUS server group ID if not using ExtremeCloud IQ Authentication Service | [optional] 
**user_group_ids** | **list[int]** | The user group IDs if using ExtremeCloud IQ Authentication Service | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


