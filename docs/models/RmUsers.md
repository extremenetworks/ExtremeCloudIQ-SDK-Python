# extremecloudiq.model.rm_users.RmUsers

Data usage per user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data usage per user. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_name** | str,  | str,  | Name or identifier of the user | [optional] 
**data_usage_gb** | decimal.Decimal, int, float,  | decimal.Decimal,  | Data usage in bytes | [optional] value must be a 32 bit float
**user_id** | decimal.Decimal, int,  | decimal.Decimal,  | The User ID | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

