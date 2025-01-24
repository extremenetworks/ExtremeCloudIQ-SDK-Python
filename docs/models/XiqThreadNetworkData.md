# extremecloudiq.model.xiq_thread_network_data.XiqThreadNetworkData

The thread network data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The thread network data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**length** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**max_length** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**[net_data_on_mesh_prefixes](#net_data_on_mesh_prefixes)** | list, tuple,  | tuple,  |  | [optional] 
**[net_data_routes](#net_data_routes)** | list, tuple,  | tuple,  |  | [optional] 
**[net_data_services](#net_data_services)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# net_data_on_mesh_prefixes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqThreadNetDataPrefix**](XiqThreadNetDataPrefix.md) | [**XiqThreadNetDataPrefix**](XiqThreadNetDataPrefix.md) | [**XiqThreadNetDataPrefix**](XiqThreadNetDataPrefix.md) |  | 

# net_data_routes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqThreadNetDataRoute**](XiqThreadNetDataRoute.md) | [**XiqThreadNetDataRoute**](XiqThreadNetDataRoute.md) | [**XiqThreadNetDataRoute**](XiqThreadNetDataRoute.md) |  | 

# net_data_services

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqThreadNetDataService**](XiqThreadNetDataService.md) | [**XiqThreadNetDataService**](XiqThreadNetDataService.md) | [**XiqThreadNetDataService**](XiqThreadNetDataService.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

