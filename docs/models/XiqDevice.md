# extremecloudiq.model.xiq_device.XiqDevice

Generic ExtremeCloud IQ Device model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Generic ExtremeCloud IQ Device model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**serial_number** | str,  | str,  | The device serial number, valid for all non-HAC devices | [optional] 
**service_tag** | str,  | str,  | The device service tag, valid for all HAC devices | [optional] 
**mac_address** | str,  | str,  | The device MAC address | [optional] 
**device_function** | [**XiqDeviceFunction**](XiqDeviceFunction.md) | [**XiqDeviceFunction**](XiqDeviceFunction.md) |  | [optional] 
**product_type** | str,  | str,  | The product type, such as: AP_230, BR_100, NX9600, etc. | [optional] 
**hostname** | str,  | str,  | The device hostname | [optional] 
**ip_address** | str,  | str,  | The device IPv4 address | [optional] 
**software_version** | str,  | str,  | The device OS software version | [optional] 
**device_admin_state** | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) |  | [optional] 
**connected** | bool,  | BoolClass,  | The device connection status | [optional] 
**last_connect_time** | str, datetime,  | str,  | The device last connect time | [optional] value must conform to RFC-3339 date-time
**network_policy_name** | str,  | str,  | The network policy name for the device | [optional] 
**network_policy_id** | decimal.Decimal, int,  | decimal.Decimal,  | The network policy ID for the device | [optional] value must be a 64 bit integer
**primary_ntp_server_address** | str,  | str,  | The primary NTP server address for the device | [optional] 
**primary_dns_server_address** | str,  | str,  | The primary DNS server address for the device | [optional] 
**subnet_mask** | str,  | str,  | The subnet mask for the device | [optional] 
**default_gateway** | str,  | str,  | The default gateway for the device | [optional] 
**ipv6_address** | str,  | str,  | The ipv6 address for the device | [optional] 
**ipv6_netmask** | decimal.Decimal, int,  | decimal.Decimal,  | The ipv6 netmask for the device | [optional] value must be a 32 bit integer
**simulated** | bool,  | BoolClass,  | The device is simulated or not | [optional] 
**display_version** | str,  | str,  | The display version for the device | [optional] 
**active_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The active client count for the device | [optional] value must be a 32 bit integer
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The location ID for the device | [optional] value must be a 64 bit integer
**[locations](#locations)** | list, tuple,  | tuple,  | The detailed location | [optional] 
**country_code** | decimal.Decimal, int,  | decimal.Decimal,  | The assigned country code on the device | [optional] value must be a 32 bit integer
**description** | str,  | str,  | The device description | [optional] 
**[lldp_cdp_infos](#lldp_cdp_infos)** | list, tuple,  | tuple,  | The device LLDP/CDP information | [optional] 
**system_up_time** | decimal.Decimal, int,  | decimal.Decimal,  | The device uptime | [optional] value must be a 64 bit integer
**config_mismatch** | bool,  | BoolClass,  | Config audit status(MATCHED or UNMATCHED) | [optional] 
**managed_by** | str,  | str,  | The managed application for the device | [optional] 
**thread0_eui64** | str,  | str,  | Thread router EUI64 | [optional] 
**thread0_ext_mac** | str,  | str,  | Thread router extended MAC address | [optional] 
**mgt_vlan** | decimal.Decimal, int,  | decimal.Decimal,  | Management VLAN | [optional] value must be a 32 bit integer
**[images_names](#images_names)** | list, tuple,  | tuple,  | List of images assigned to this device | [optional] 
**visible** | bool,  | BoolClass,  | The visible status of a device in a floor. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# locations

The detailed location

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The detailed location | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqLocationLegend**](XiqLocationLegend.md) | [**XiqLocationLegend**](XiqLocationLegend.md) | [**XiqLocationLegend**](XiqLocationLegend.md) |  | 

# lldp_cdp_infos

The device LLDP/CDP information

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The device LLDP/CDP information | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDeviceLldpCdpInfo**](XiqDeviceLldpCdpInfo.md) | [**XiqDeviceLldpCdpInfo**](XiqDeviceLldpCdpInfo.md) | [**XiqDeviceLldpCdpInfo**](XiqDeviceLldpCdpInfo.md) |  | 

# images_names

List of images assigned to this device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of images assigned to this device | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of images assigned to this device | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

