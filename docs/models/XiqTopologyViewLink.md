# extremecloudiq.model.xiq_topology_view_link.XiqTopologyViewLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**source** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**source_port_id** | str,  | str,  |  | [optional] 
**source_lag** | str,  | str,  |  | [optional] 
**destination** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**destination_port_id** | str,  | str,  |  | [optional] 
**destination_lag** | str,  | str,  |  | [optional] 
**index** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**connected** | bool,  | BoolClass,  |  | [optional] 
**connection_mode** | str,  | str,  |  | [optional] must be one of ["LLDP", "CLIENT", "UNKNOWNDEVICE", "MESH", "VGVA", "FAKEGATEWAY", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

