# extremecloudiq.model.xiq_user.XiqUser

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**login_name** | str,  | str,  | Login name, i.e. username or login Email | 
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**first_name** | str,  | str,  | The first name | [optional] 
**last_name** | str,  | str,  | The last name, i.e. family name | [optional] 
**display_name** | str,  | str,  | The name to display | [optional] 
**phone** | str,  | str,  | The Phone Number | [optional] 
**job_title** | str,  | str,  | The job title | [optional] 
**locale** | str,  | str,  | The locale | [optional] 
**user_role** | [**XiqUserRole**](XiqUserRole.md) | [**XiqUserRole**](XiqUserRole.md) |  | [optional] 
**idle_timeout** | decimal.Decimal, int,  | decimal.Decimal,  | The idle timeout in minutes, the minimum value is 5 minutes and the maximum value is 4 hours | [optional] value must be a 32 bit integer
**last_login_time** | str, datetime,  | str,  | The last login time | [optional] value must conform to RFC-3339 date-time
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The HIQ organization ID if it is HIQ user | [optional] value must be a 64 bit integer
**[location_ids](#location_ids)** | list, tuple,  | tuple,  | The assigned location IDs. | [optional] 
**access_scope** | decimal.Decimal, int,  | decimal.Decimal,  | The user has access on all sites / the authorized sites. 0: VIQ_SCOPE, 1: SITE_SCOPE. | [optional] value must be a 32 bit integer
**viq_access_control** | decimal.Decimal, int,  | decimal.Decimal,  | The permissions for Site Scope user on Global Scope resources. 0: READ_WRITE, 1: READ_ONLY. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# location_ids

The assigned location IDs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The assigned location IDs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The assigned location IDs. | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

