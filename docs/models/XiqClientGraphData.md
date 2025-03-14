# extremecloudiq.model.xiq_client_graph_data.XiqClientGraphData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The client graph timestamp | [optional] value must be a 64 bit integer
**unique_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The client graph value for unique clients | [optional] value must be a 64 bit integer
**connected_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The client graph value for connected clients | [optional] value must be a 64 bit integer
**poor_health_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The client graph value for poor clients | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

