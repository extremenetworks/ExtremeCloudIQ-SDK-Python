# extremecloudiq.model.xiq_thread_network_topology.XiqThreadNetworkTopology

The thread network topology

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The thread network topology | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[neighbors](#neighbors)** | list, tuple,  | tuple,  |  | [optional] 
**[routers](#routers)** | list, tuple,  | tuple,  |  | [optional] 
**[clients](#clients)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# neighbors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqThreadRouterNeighbor**](XiqThreadRouterNeighbor.md) | [**XiqThreadRouterNeighbor**](XiqThreadRouterNeighbor.md) | [**XiqThreadRouterNeighbor**](XiqThreadRouterNeighbor.md) |  | 

# routers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqThreadRouter**](XiqThreadRouter.md) | [**XiqThreadRouter**](XiqThreadRouter.md) | [**XiqThreadRouter**](XiqThreadRouter.md) |  | 

# clients

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqClient**](XiqClient.md) | [**XiqClient**](XiqClient.md) | [**XiqClient**](XiqClient.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

