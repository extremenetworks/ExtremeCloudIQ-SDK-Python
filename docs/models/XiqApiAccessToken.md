# extremecloudiq.model.xiq_api_access_token.XiqApiAccessToken

 The API Access Token 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  The API Access Token  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**application** | str,  | str,  | The application name | [optional] 
**access_token** | str,  | str,  | The Access Token | [optional] 
**grantor** | str,  | str,  | The Grantor of the token | [optional] 
**generated_on** | str, datetime,  | str,  | The create time | [optional] value must conform to RFC-3339 date-time
**expiration** | decimal.Decimal, int,  | decimal.Decimal,  | The expiration time | [optional] value must be a 64 bit integer
**refresh_token** | str,  | str,  | The refresh token | [optional] 
**client_id** | str,  | str,  | The client ID | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

