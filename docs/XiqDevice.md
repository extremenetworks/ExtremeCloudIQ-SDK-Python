# XiqDevice

Generic ExtremeCloud IQ Device model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**serial_number** | **str** | The device serial number, valid for all non-HAC devices | [optional] 
**service_tag** | **str** | The device service tag, valid for all HAC devices | [optional] 
**mac_address** | **str** | The device MAC address | [optional] 
**device_function** | [**XiqDeviceFunction**](XiqDeviceFunction.md) |  | [optional] 
**product_type** | **str** | The product type, such as: AP_230, BR_100, NX9600, etc. | [optional] 
**hostname** | **str** | The device hostname | [optional] 
**ip_address** | **str** | The device IPv4 address | [optional] 
**software_version** | **str** | The device OS software version | [optional] 
**device_admin_state** | [**XiqDeviceAdminState**](XiqDeviceAdminState.md) |  | [optional] 
**connected** | **bool** | The device connection status | [optional] 
**last_connect_time** | **datetime** | The device last connect time | [optional] 
**network_policy_name** | **str** | The network policy name for the device | [optional] 
**network_policy_id** | **int** | The network policy ID for the device | [optional] 
**primary_ntp_server_address** | **str** | The primary NTP server address for the device | [optional] 
**primary_dns_server_address** | **str** | The primary DNS server address for the device | [optional] 
**subnet_mask** | **str** | The subnet mask for the device | [optional] 
**default_gateway** | **str** | The default gateway for the device | [optional] 
**ipv6_address** | **str** | The ipv6 address for the device | [optional] 
**ipv6_netmask** | **int** | The ipv6 netmask for the device | [optional] 
**simulated** | **bool** | The device is simulated or not | [optional] 
**display_version** | **str** | The display version for the device | [optional] 
**active_clients** | **int** | The active client count for the device | [optional] 
**location_id** | **int** | The location ID for the device | [optional] 
**locations** | [**list[XiqLocationLegend]**](XiqLocationLegend.md) | The detailed location | [optional] 
**country_code** | **int** | The assigned country code on the device | [optional] 
**description** | **str** | The device description | [optional] 
**lldp_cdp_infos** | [**list[XiqDeviceLldpCdpInfo]**](XiqDeviceLldpCdpInfo.md) | The device LLDP/CDP information | [optional] 
**system_up_time** | **int** | The device uptime | [optional] 
**config_mismatch** | **bool** | Config audit status(MATCHED or UNMATCHED) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


