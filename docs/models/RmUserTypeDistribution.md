# extremecloudiq.model.rm_user_type_distribution.RmUserTypeDistribution

The User type distribution and total connected users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The User type distribution and total connected users | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ppsk_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage of users authenticated via PPSK | [optional] value must be a 32 bit integer
**radius_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage of users authenticated via RADIUS | [optional] value must be a 32 bit integer
**others_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage of users authenticated via other methods | [optional] value must be a 32 bit integer
**total_connected_users** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of connected users | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

