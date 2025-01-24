# extremecloudiq.model.xiq_pcg_assign_ports_response.XiqPcgAssignPortsResponse

The response of assign ports for AP150W or AP302W

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The response of assign ports for AP150W or AP302W | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[pcg_port_assignment_entries](#pcg_port_assignment_entries)** | list, tuple,  | tuple,  | The port assignment entry list | 
**policy_id** | decimal.Decimal, int,  | decimal.Decimal,  | The network policy ID | value must be a 64 bit integer
**policy_name** | str,  | str,  | The network policy name | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pcg_port_assignment_entries

The port assignment entry list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The port assignment entry list | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqPcgPortAssignmentEntry**](XiqPcgPortAssignmentEntry.md) | [**XiqPcgPortAssignmentEntry**](XiqPcgPortAssignmentEntry.md) | [**XiqPcgPortAssignmentEntry**](XiqPcgPortAssignmentEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

