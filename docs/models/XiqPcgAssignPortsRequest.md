# extremecloudiq.model.xiq_pcg_assign_ports_request.XiqPcgAssignPortsRequest

The payload to assign ports for AP150W or AP302W)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload to assign ports for AP150W or AP302W) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[port_assignments](#port_assignments)** | list, tuple,  | tuple,  | The port assignment list | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# port_assignments

The port assignment list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The port assignment list | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqPcgPortAssignment**](XiqPcgPortAssignment.md) | [**XiqPcgPortAssignment**](XiqPcgPortAssignment.md) | [**XiqPcgPortAssignment**](XiqPcgPortAssignment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

