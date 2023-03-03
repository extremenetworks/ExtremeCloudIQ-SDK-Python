# XiqActiveDirectoryServer

The configuration of Active Directory Server
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The active directory server name | [optional] 
**description** | **str** | The description for active directory server | [optional] 
**base_dn** | **str** | The base DN of active directory server | [optional] 
**enable_tls** | **bool** | Flag to enable TLS | [optional] 
**bind_dn** | **str** | The bind DN of active directory server | [optional] 
**bind_dn_password** | **str** | The bind DN password of active directory server | [optional] 
**domain** | **str** | The domain of active directory server | [optional] 
**computer_ou** | **str** | The compute OU of active directory server | [optional] 
**domain_admin** | **str** | The domain admin of active directory server | [optional] 
**domain_admin_password** | **str** | The domain admin password of active directory server | [optional] 
**enable_save_domain_admin_credentials** | **bool** | Flag to enable save domain admin credentials | [optional] 
**short_domain** | **str** | The short domain of active directory server | [optional] 
**realm** | **str** | The realm of active directory server | [optional] 
**base_dn_fetch_mode** | [**XiqActiveDirectoryServerBaseDnFetchMode**](XiqActiveDirectoryServerBaseDnFetchMode.md) |  | [optional] 
**connection_setup_device_id** | **int** | The connection setup device ID for active directory server | [optional] 
**l3_address_profile_id** | **int** | The associate L3 address profile ID for active directory server | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


