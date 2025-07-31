# extremecloudiq.model.xiq_topology_view_node.XiqTopologyViewNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**hostname** | str,  | str,  |  | [optional] 
**mac_address** | str,  | str,  |  | [optional] 
**ip_address** | str,  | str,  |  | [optional] 
**port_number** | str,  | str,  |  | [optional] 
**radio_info** | str,  | str,  |  | [optional] 
**health_score** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**client_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**last_node** | bool,  | BoolClass,  |  | [optional] 
**topology_start_node** | bool,  | BoolClass,  |  | [optional] 
**connected** | bool,  | BoolClass,  |  | [optional] 
**vlan_info** | [**XiqTopologyViewNodeVlanInfo**](XiqTopologyViewNodeVlanInfo.md) | [**XiqTopologyViewNodeVlanInfo**](XiqTopologyViewNodeVlanInfo.md) |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["WIRELESS_CLIENT", "WIRED_CLIENT", "UNKNOWN", "AP", "MESHAP", "PORTALAP", "SWITCH", "ROUTER", "VAASL2VG", "VAASL3VG", "GATEWAY", "STACK", "APASROUTER", "XMCSERVER", ] 
**critical_alarms** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**not_current_location_node** | bool,  | BoolClass,  |  | [optional] 
**unknown_device** | [**XiqTopologyUnknownDevice**](XiqTopologyUnknownDevice.md) | [**XiqTopologyUnknownDevice**](XiqTopologyUnknownDevice.md) |  | [optional] 
**wired_interface_name** | str,  | str,  |  | [optional] 
**connected_port** | str,  | str,  |  | [optional] 
**[stack_member_info](#stack_member_info)** | list, tuple,  | tuple,  |  | [optional] 
**make** | str,  | str,  |  | [optional] 
**position** | [**XiqPosition**](XiqPosition.md) | [**XiqPosition**](XiqPosition.md) |  | [optional] 
**poe_info** | [**XiqTopologyViewNodePoeInfo**](XiqTopologyViewNodePoeInfo.md) | [**XiqTopologyViewNodePoeInfo**](XiqTopologyViewNodePoeInfo.md) |  | [optional] 
**product_type** | str,  | str,  |  | [optional] 
**is_locally_managed** | bool,  | BoolClass,  |  | [optional] 
**sim_type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# stack_member_info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqTopologyStackMemberInfo**](XiqTopologyStackMemberInfo.md) | [**XiqTopologyStackMemberInfo**](XiqTopologyStackMemberInfo.md) | [**XiqTopologyStackMemberInfo**](XiqTopologyStackMemberInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

