# extremecloudiq.model.xiq_device_system_information.XiqDeviceSystemInformation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**host_name** | str,  | str,  | The name of the host | [optional] 
**network_policy** | str,  | str,  | The network policy applied to the device | [optional] 
**[ssids](#ssids)** | list, tuple,  | tuple,  | The SSID of the network | [optional] 
**device_model** | str,  | str,  |  | [optional] 
**function** | [**XiqDeviceFunction**](XiqDeviceFunction.md) | [**XiqDeviceFunction**](XiqDeviceFunction.md) |  | [optional] 
**device_template** | str,  | str,  |  | [optional] 
**configuration_type** | str,  | str,  |  | [optional] 
**serial_number** | str,  | str,  |  | [optional] 
**iq_engine** | str,  | str,  |  | [optional] 
**device_status** | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) |  | [optional] 
**mgt0_ipv4_address** | str,  | str,  |  | [optional] 
**mgt0_ipv6_address** | str,  | str,  |  | [optional] 
**ipv4_subnet_mask** | str,  | str,  |  | [optional] 
**ipv6_subnet_mask** | str,  | str,  |  | [optional] 
**ipv4_default_gateway** | str,  | str,  |  | [optional] 
**ipv6_default_gateway** | str,  | str,  |  | [optional] 
**mgt0_macaddress** | str,  | str,  |  | [optional] 
**dns** | str,  | str,  |  | [optional] 
**ntp** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssids

The SSID of the network

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The SSID of the network | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | The SSID of the network | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

