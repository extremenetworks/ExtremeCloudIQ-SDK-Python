# extremecloudiq.model.xiq_grant_external_user_request.XiqGrantExternalUserRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_role** | [**XiqUserRole**](XiqUserRole.md) | [**XiqUserRole**](XiqUserRole.md) |  | 
**login_name** | str,  | str,  | Login name, i.e. username or login Email | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The HIQ organization ID if it is HIQ user, otherwise leave it as empty | [optional] value must be a 64 bit integer
**[location_ids](#location_ids)** | list, tuple,  | tuple,  | The location IDs to assign. Null or empty list will assign Admin default locations. | [optional] 
**access_scope** | decimal.Decimal, int,  | decimal.Decimal,  | The user has access on all sites / the authorized sites. 0: VIQ_SCOPE, 1: SITE_SCOPE. | [optional] value must be a 32 bit integer
**viq_access_control** | decimal.Decimal, int,  | decimal.Decimal,  | The permissions for Site Scope user on Global Scope resources. 0: READ_WRITE, 1: READ_ONLY. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# location_ids

The location IDs to assign. Null or empty list will assign Admin default locations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The location IDs to assign. Null or empty list will assign Admin default locations. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The location IDs to assign. Null or empty list will assign Admin default locations. | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

