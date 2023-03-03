# XiqExternalUserDirectory

The setting for external user directory, AD or LDAP
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldap_retry_interval** | **int** | Retry the previously unresponsive primary server after the specified seconds | [default to 600]
**local_check_interval** | **int** | Time to user local cache if none of the external servers are reachable in seconds | [default to 300]
**remote_check_interval** | **int** | Try the next backup server after specified seconds | [default to 30]
**enable_radius_server_credential_caching** | **bool** | Caching credentials allows for better performance and higher availability by reducing the dependence on RADIUS servers across high-latency WAN links. | 
**cache_lifetime** | **int** | Retain Cache for | [default to 86400]
**user_group_attribute** | **str** | The user group attribute, use string such as: &#39;memberOf&#39; | [default to 'memberOf']
**external_user_directory_type** | [**XiqExternalUserDirectoryType**](XiqExternalUserDirectoryType.md) |  | 
**entries** | [**list[XiqExternalUserDirectoryEntry]**](XiqExternalUserDirectoryEntry.md) | The external user directory server entries | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


