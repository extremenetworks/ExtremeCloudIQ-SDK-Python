# extremecloudiq.model.xiq_wired_client_health_port_errors_response.XiqWiredClientHealthPortErrorsResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The total number of clients | [optional] value must be a 64 bit integer
**port_errors** | decimal.Decimal, int,  | decimal.Decimal,  | The number of clients with port errors | [optional] value must be a 64 bit integer
**healthy** | decimal.Decimal, int,  | decimal.Decimal,  | The number of healthy client that do not have port errors | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

