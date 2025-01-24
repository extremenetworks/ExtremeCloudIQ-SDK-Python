# extremecloudiq.model.xiq_key_based_pcg_user.XiqKeyBasedPcgUser

The key based PCG user detailed info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The key based PCG user detailed info | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The create timestamp | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create timestamp | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The user name of key based PCG, which could not share with other exist key based PCG | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The user ID | value must be a 64 bit integer
**user_group_name** | str,  | str,  | The user group name | 
**email** | str,  | str,  | The email for deliver key based PCG user password | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization ID | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

