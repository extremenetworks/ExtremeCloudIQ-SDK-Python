# XiqClient

The Client associate to ExtremeCloud IQ device
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**location_id** | **int** | The location ID | [optional] 
**device_id** | **int** | The device ID | [optional] 
**hostname** | **str** | The hostname of the client | [optional] 
**mac_address** | **str** | The MAC address of the client | [optional] 
**ip_address** | **str** | The IP address of the client | [optional] 
**ipv6_address** | **str** | The IPv6 address of the client | [optional] 
**os_type** | **str** | The OS type of the client | [optional] 
**username** | **str** | The username of the client. | [optional] 
**user_profile_name** | **str** | The user profile name of the client | [optional] 
**connected** | **bool** | Client is connected or not | [optional] 
**online_time** | **datetime** | The online time for the client | [optional] 
**offline_time** | **datetime** | The offline time for the client | [optional] 
**vlan** | **int** | The associate VLAN | [optional] 
**connection_type** | **int** | The connection type | [optional] 
**ssid** | **str** | The SSID | [optional] 
**port** | **str** | The associate device port | [optional] 
**org_name** | **str** | The organization name | [optional] 
**device_function** | **int** | The associated device function | [optional] 
**device_mac_address** | **str** | The associated device mac address | [optional] 
**device_name** | **str** | The associated device name | [optional] 
**auth** | **int** | The authentication type | [optional] 
**channel** | **int** | The channel value | [optional] 
**client_health** | **int** | The health score of client | [optional] 
**application_health** | **int** | The health score of application | [optional] 
**radio_health** | **int** | The health score of radio | [optional] 
**network_health** | **int** | The health score of network | [optional] 
**radio_type** | **int** | The radio type | [optional] 
**encryption_method** | **int** | The encryption method | [optional] 
**interface_name** | **str** | The interface name | [optional] 
**bssid** | **str** | The bssid | [optional] 
**rssi** | **int** | The RSSI | [optional] 
**snr** | **int** | The SNR | [optional] 
**description** | **str** | The description of client | [optional] 
**category** | **str** | The category of client | [optional] 
**mobility** | **str** | The client mobility | [optional] 
**port_type_name** | **str** | The client port type name | [optional] 
**wing_ap** | **bool** | Wing ap flag | [optional] 
**vendor** | **str** | The vendor of client | [optional] 
**locations** | [**list[XiqLocationLegend]**](XiqLocationLegend.md) | The detailed location | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


