# extremecloudiq.model.xiq_external_user_directory_entry.XiqExternalUserDirectoryEntry

The payload of common object - External User Directory Entry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of common object - External User Directory Entry | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**default_server_id** | decimal.Decimal, int,  | decimal.Decimal,  | The default external user directory server id, could be active directory server id(get the id list from endpoint: &#x27;/ad-servers&#x27;) or LDAP server id(get the id list from endpoint: &#x27;/ldap-servers&#x27;) depends on the &#x27;external_user_directory_type&#x27;  | value must be a 64 bit integer
**server_role** | [**XiqServerRole**](XiqServerRole.md) | [**XiqServerRole**](XiqServerRole.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

