# extremecloudiq.model.xiq_client_connection_trail_response.XiqClientConnectionTrailResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[links](#links)** | list, tuple,  | tuple,  |  | [optional] 
**[nodes](#nodes)** | list, tuple,  | tuple,  |  | [optional] 
**baseline** | bool,  | BoolClass,  |  | [optional] 
**user_initiated** | bool,  | BoolClass,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**zoom** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**pan** | [**XiqPosition**](XiqPosition.md) | [**XiqPosition**](XiqPosition.md) |  | [optional] 
**[neighbors](#neighbors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# links

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqTopologyViewLink**](XiqTopologyViewLink.md) | [**XiqTopologyViewLink**](XiqTopologyViewLink.md) | [**XiqTopologyViewLink**](XiqTopologyViewLink.md) |  | 

# nodes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqTopologyViewNode**](XiqTopologyViewNode.md) | [**XiqTopologyViewNode**](XiqTopologyViewNode.md) | [**XiqTopologyViewNode**](XiqTopologyViewNode.md) |  | 

# neighbors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqNeighborAp**](XiqNeighborAp.md) | [**XiqNeighborAp**](XiqNeighborAp.md) | [**XiqNeighborAp**](XiqNeighborAp.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

