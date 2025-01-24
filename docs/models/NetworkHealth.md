# extremecloudiq.model.network_health.NetworkHealth

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**overall_score** | decimal.Decimal, int,  | decimal.Decimal,  | The overall health score | [optional] value must be a 32 bit integer
**internet_availability_score** | decimal.Decimal, int,  | decimal.Decimal,  | The overall internet availability score | [optional] value must be a 64 bit integer
**internet_performance** | decimal.Decimal, int,  | decimal.Decimal,  | The internet performance value in milli-seconds | [optional] value must be a 64 bit integer
**network_usage** | decimal.Decimal, int,  | decimal.Decimal,  | The network usage value in MB | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

