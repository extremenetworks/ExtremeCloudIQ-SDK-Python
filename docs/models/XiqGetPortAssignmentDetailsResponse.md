# extremecloudiq.model.xiq_get_port_assignment_details_response.XiqGetPortAssignmentDetailsResponse

The response of port assignment details for AP150W

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The response of port assignment details for AP150W | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**policy_id** | decimal.Decimal, int,  | decimal.Decimal,  | The network policy ID | value must be a 64 bit integer
**policy_name** | str,  | str,  | The network policy name | 
**[pcg_port_assignment_entry_details](#pcg_port_assignment_entry_details)** | list, tuple,  | tuple,  | The PCG port assignment entry details | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pcg_port_assignment_entry_details

The PCG port assignment entry details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The PCG port assignment entry details | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqPcgPortAssignmentEntryDetail**](XiqPcgPortAssignmentEntryDetail.md) | [**XiqPcgPortAssignmentEntryDetail**](XiqPcgPortAssignmentEntryDetail.md) | [**XiqPcgPortAssignmentEntryDetail**](XiqPcgPortAssignmentEntryDetail.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

