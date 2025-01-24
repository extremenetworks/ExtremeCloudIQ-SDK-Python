# extremecloudiq.model.xiq_generate_api_token_response.XiqGenerateApiTokenResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | The API access token | 
**create_time** | str, datetime,  | str,  | The create timestamp | value must conform to RFC-3339 date-time
**[permissions](#permissions)** | list, tuple,  | tuple,  | The permissions for the API token | 
**creator_id** | decimal.Decimal, int,  | decimal.Decimal,  | The user ID who created the API token | value must be a 64 bit integer
**customer_id** | decimal.Decimal, int,  | decimal.Decimal,  | The customer ID who owns the API token | value must be a 64 bit integer
**expire_time** | str, datetime,  | str,  | The expire timestamp, if null means no expiration | [optional] value must conform to RFC-3339 date-time
**description** | str,  | str,  | The description for the API token | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# permissions

The permissions for the API token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The permissions for the API token | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The permissions for the API token | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

