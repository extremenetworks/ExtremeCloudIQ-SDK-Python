# extremecloudiq.model.xiq_thread_network_interface.XiqThreadNetworkInterface

The thread veth0 network interface

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The thread veth0 network interface | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**interface_name** | str,  | str,  |  | [optional] 
**is_active** | bool,  | BoolClass,  |  | [optional] 
**is_broadcast** | bool,  | BoolClass,  |  | [optional] 
**is_loopback** | bool,  | BoolClass,  |  | [optional] 
**is_point_to_point** | bool,  | BoolClass,  |  | [optional] 
**is_running** | bool,  | BoolClass,  |  | [optional] 
**is_arp** | bool,  | BoolClass,  |  | [optional] 
**is_promisc** | bool,  | BoolClass,  |  | [optional] 
**is_all_multi** | bool,  | BoolClass,  |  | [optional] 
**is_multicast** | bool,  | BoolClass,  |  | [optional] 
**is_dynamic** | bool,  | BoolClass,  |  | [optional] 
**mtu** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**hw_mac_address** | str,  | str,  |  | [optional] 
**ipv4** | str,  | str,  |  | [optional] 
**ipv4_mask** | str,  | str,  |  | [optional] 
**ipv4_broadcast** | str,  | str,  |  | [optional] 
**[ipv6_settings](#ipv6_settings)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ipv6_settings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqThreadIpv6Setting**](XiqThreadIpv6Setting.md) | [**XiqThreadIpv6Setting**](XiqThreadIpv6Setting.md) | [**XiqThreadIpv6Setting**](XiqThreadIpv6Setting.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

