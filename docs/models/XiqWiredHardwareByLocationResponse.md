# extremecloudiq.model.xiq_wired_hardware_by_location_response.XiqWiredHardwareByLocationResponse

Copilot Wired Hardware By Location Response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Wired Hardware By Location Response | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[quality_index_graph](#quality_index_graph)** | list, tuple,  | tuple,  | the wired hardware entities data | [optional] 
**total_affected_ports** | decimal.Decimal, int,  | decimal.Decimal,  | the total affected ports | [optional] value must be a 32 bit integer
**total_ports** | decimal.Decimal, int,  | decimal.Decimal,  | the total ports | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# quality_index_graph

the wired hardware entities data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the wired hardware entities data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWiredHardwareEntity**](XiqWiredHardwareEntity.md) | [**XiqWiredHardwareEntity**](XiqWiredHardwareEntity.md) | [**XiqWiredHardwareEntity**](XiqWiredHardwareEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

