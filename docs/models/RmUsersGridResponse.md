# extremecloudiq.model.rm_users_grid_response.RmUsersGridResponse

The User Grid Response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The User Grid Response | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status** | bool,  | BoolClass,  | The connection status of user | [optional] 
**site** | str,  | str,  | The site where the user is located | [optional] 
**building** | str,  | str,  | The building where the user is located | [optional] 
**floor** | str,  | str,  | The floor where the user is located | [optional] 
**user_name** | str,  | str,  | The Name of the user | [optional] 
**email** | str,  | str,  | The Email address of the user | [optional] 
**group** | str,  | str,  | Group to which the user belongs | [optional] 
**wireless_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The number of wireless clients | [optional] value must be a 32 bit integer
**wired_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The number of wired clients | [optional] value must be a 32 bit integer
**data_usage** | decimal.Decimal, int,  | decimal.Decimal,  | Total data usage in bytes | [optional] value must be a 64 bit integer
**source** | str,  | str,  | &#x27;Source of the session (e.g., RADIUS, SAML)&#x27; | [optional] 
**session_duration** | decimal.Decimal, int,  | decimal.Decimal,  | Duration of the session in seconds | [optional] value must be a 64 bit integer
**expiration** | decimal.Decimal, int,  | decimal.Decimal,  | Time in seconds until the session expires | [optional] value must be a 64 bit integer
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The location ID | [optional] value must be a 64 bit integer
**user_id** | decimal.Decimal, int,  | decimal.Decimal,  | The User ID | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

