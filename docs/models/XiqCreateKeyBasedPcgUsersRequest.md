# extremecloudiq.model.xiq_create_key_based_pcg_users_request.XiqCreateKeyBasedPcgUsersRequest

The payload of add Key-based Private Client Group users request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of add Key-based Private Client Group users request | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[users](#users)** | list, tuple,  | tuple,  | The key based PCG users | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# users

The key based PCG users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The key based PCG users | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqKeyBasedPcgUserBaseInfo**](XiqKeyBasedPcgUserBaseInfo.md) | [**XiqKeyBasedPcgUserBaseInfo**](XiqKeyBasedPcgUserBaseInfo.md) | [**XiqKeyBasedPcgUserBaseInfo**](XiqKeyBasedPcgUserBaseInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

