# XiqSetSsidModePpskRequest

The request for setting the SSID to be PPSK mode.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_management** | [**XiqSsidPpskKeyManagement**](XiqSsidPpskKeyManagement.md) |  | 
**encryption_method** | [**XiqSsidPskEncryptionMethod**](XiqSsidPskEncryptionMethod.md) |  | 
**user_group_ids** | **list[int]** | The user group IDs to be attached to the SSID, cannot be empty | 
**enable_max_clients_per_ppsk** | **bool** | Flag for enabling the max clients per PPSK | 
**max_clients_per_ppsk** | **int** | The max clients (0-15) per PPSK if enabled enable_max_clients_per_ppsk flag, 0 means unlimited | [optional] 
**enable_mac_bind** | **bool** | Flag for enabling mac binding or not. This setting is only supported with local PPSK. | 
**max_macs_per_ppsk** | **int** | Set the max MAC binding numbers per private PSK, Min:1, Max:5 | [optional] 
**ppsk_server_id** | **int** | The PPSK server device ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


