# extremecloudiq.model.xiq_external_user_directory.XiqExternalUserDirectory

The setting for external user directory, AD or LDAP

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The setting for external user directory, AD or LDAP | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_group_attribute** | str,  | str,  | The user group attribute, use string such as: &#x27;memberOf&#x27; | if omitted the server will use the default value of "memberOf"
**enable_radius_server_credential_caching** | bool,  | BoolClass,  | Caching credentials allows for better performance and higher availability by reducing the dependence on RADIUS servers across high-latency WAN links. | 
**[entries](#entries)** | list, tuple,  | tuple,  | The external user directory server entries | 
**local_check_interval** | decimal.Decimal, int,  | decimal.Decimal,  | Time to user local cache if none of the external servers are reachable in seconds | if omitted the server will use the default value of 300value must be a 32 bit integer
**cache_lifetime** | decimal.Decimal, int,  | decimal.Decimal,  | Retain Cache for | if omitted the server will use the default value of 86400value must be a 32 bit integer
**remote_check_interval** | decimal.Decimal, int,  | decimal.Decimal,  | Try the next backup server after specified seconds | if omitted the server will use the default value of 30value must be a 32 bit integer
**external_user_directory_type** | [**XiqExternalUserDirectoryType**](XiqExternalUserDirectoryType.md) | [**XiqExternalUserDirectoryType**](XiqExternalUserDirectoryType.md) |  | 
**ldap_retry_interval** | decimal.Decimal, int,  | decimal.Decimal,  | Retry the previously unresponsive primary server after the specified seconds | if omitted the server will use the default value of 600value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# entries

The external user directory server entries

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The external user directory server entries | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqExternalUserDirectoryEntry**](XiqExternalUserDirectoryEntry.md) | [**XiqExternalUserDirectoryEntry**](XiqExternalUserDirectoryEntry.md) | [**XiqExternalUserDirectoryEntry**](XiqExternalUserDirectoryEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

