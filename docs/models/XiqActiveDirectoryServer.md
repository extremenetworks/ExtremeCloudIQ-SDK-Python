# extremecloudiq.model.xiq_active_directory_server.XiqActiveDirectoryServer

The configuration of Active Directory Server

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration of Active Directory Server | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The active directory server name | [optional] 
**description** | str,  | str,  | The description for active directory server | [optional] 
**base_dn** | str,  | str,  | The base DN of active directory server | [optional] 
**enable_tls** | bool,  | BoolClass,  | Flag to enable TLS | [optional] 
**bind_dn** | str,  | str,  | The bind DN of active directory server | [optional] 
**bind_dn_password** | str,  | str,  | The bind DN password of active directory server | [optional] 
**domain** | str,  | str,  | The domain of active directory server | [optional] 
**computer_ou** | str,  | str,  | The compute OU of active directory server | [optional] 
**domain_admin** | str,  | str,  | The domain admin of active directory server | [optional] 
**domain_admin_password** | str,  | str,  | The domain admin password of active directory server | [optional] 
**enable_save_domain_admin_credentials** | bool,  | BoolClass,  | Flag to enable save domain admin credentials | [optional] 
**short_domain** | str,  | str,  | The short domain of active directory server | [optional] 
**realm** | str,  | str,  | The realm of active directory server | [optional] 
**base_dn_fetch_mode** | [**XiqActiveDirectoryServerBaseDnFetchMode**](XiqActiveDirectoryServerBaseDnFetchMode.md) | [**XiqActiveDirectoryServerBaseDnFetchMode**](XiqActiveDirectoryServerBaseDnFetchMode.md) |  | [optional] 
**connection_setup_device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The connection setup device ID for active directory server | [optional] value must be a 64 bit integer
**l3_address_profile_id** | decimal.Decimal, int,  | decimal.Decimal,  | The associate L3 address profile ID for active directory server | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

