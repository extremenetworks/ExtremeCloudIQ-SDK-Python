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
**device_model** | str,  | str,  | The model of the device | [optional] 
**function** | [**XiqDeviceFunction**](XiqDeviceFunction.md) | [**XiqDeviceFunction**](XiqDeviceFunction.md) |  | [optional] 
**device_template** | str,  | str,  | The configuration template applied to the device | [optional] 
**configuration_type** | str,  | str,  | The device configuration type. Possible values: DEFAULT (factory default), TEMPLATE (applied from a template), CUSTOM (user-configured). | [optional] must be one of ["DEFAULT", "TEMPLATE", "CUSTOM", ] 
**serial_number** | str,  | str,  | The serial number of the device | [optional] 
**iq_engine** | str,  | str,  | The IQ engine version or type used by the device | [optional] 
**device_status** | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) |  | [optional] 
**mgt0_ipv4_address** | str,  | str,  | Management IPv4 address | [optional] 
**mgt0_ipv6_address** | str,  | str,  | Management IPv6 address | [optional] 
**ipv4_subnet_mask** | str,  | str,  | The IPv4 subnet mask in dotted-decimal notation. | [optional] 
**ipv6_subnet_mask** | str,  | str,  | The IPv6 subnet mask or prefix length. Accepted formats: numeric prefix length (e.g., \&quot;64\&quot;) or CIDR notation with an IPv6 network (e.g., \&quot;2001:db8::/64\&quot;). | [optional] 
**ipv4_default_gateway** | str,  | str,  | The IPv4 default gateway address | [optional] 
**ipv6_default_gateway** | str,  | str,  | The IPv6 default gateway address | [optional] 
**mgt0_macaddress** | str,  | str,  | The MAC address of the management interface in six hex byte pairs (colon or hyphen separated). | [optional] 
**dns** | str,  | str,  | The DNS server address(es). Either a single IPv4 or IPv6 address, or a comma-separated list of addresses. Spaces around commas are allowed. | [optional] 
**ntp** | str,  | str,  | The NTP server address(es). Either a single hostname or IP (IPv4/IPv6), or a comma-separated list of addresses. Spaces around commas are allowed. | [optional] 
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

