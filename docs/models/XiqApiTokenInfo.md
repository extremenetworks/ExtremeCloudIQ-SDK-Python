# extremecloudiq.model.xiq_api_token_info.XiqApiTokenInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**role** | str,  | str,  | The role of login user | 
**user_id** | decimal.Decimal, int,  | decimal.Decimal,  | The login user ID | value must be a 64 bit integer
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The home ownerId of login user | value must be a 64 bit integer
**user_name** | str,  | str,  | The login username | 
**data_center** | str,  | str,  | The home data center of login user | 
**[scopes](#scopes)** | list, tuple,  | tuple,  | The login user permissions | 
**issued_at** | str, datetime,  | str,  | The time at which the JWT was issued | value must conform to RFC-3339 date-time
**expiration_time** | str, datetime,  | str,  | The expiration time on or after which the JWT MUST NOT be accepted for processing | [optional] value must conform to RFC-3339 date-time
**expires_in** | decimal.Decimal, int,  | decimal.Decimal,  | The expires in seconds | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scopes

The login user permissions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The login user permissions | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The login user permissions | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

