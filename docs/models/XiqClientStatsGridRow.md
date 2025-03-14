# extremecloudiq.model.xiq_client_stats_grid_row.XiqClientStatsGridRow

The D360 client grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The D360 client grid | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**connection_status** | bool,  | BoolClass,  | The current connection status of the client | [optional] 
**client_hostname** | str,  | str,  | The hostname of the client | [optional] 
**client_ip** | str,  | str,  | The IP address of the client | [optional] 
**site** | str,  | str,  | The site where the client is located | [optional] 
**building** | str,  | str,  | The building where the client is located | [optional] 
**floor** | str,  | str,  | The floor where the client is located | [optional] 
**association_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The number of association issues | [optional] value must be a 64 bit integer
**authentication_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The number of authentication issues | [optional] value must be a 64 bit integer
**ip_address_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The number of IP address issues | [optional] value must be a 64 bit integer
**snr** | decimal.Decimal, int,  | decimal.Decimal,  | Signal-to-noise ratio of the client&#x27;s connection | [optional] value must be a 32 bit integer
**rssi** | decimal.Decimal, int,  | decimal.Decimal,  | Received signal strength indicator of the client&#x27;s connection | [optional] value must be a 32 bit integer
**channel_utilization_score** | decimal.Decimal, int,  | decimal.Decimal,  | The percentage of channel utilization | [optional] value must be a 32 bit integer
**frequency** | str,  | str,  | The frequency band used by the client (e.g., 2.4 GHz, 5 GHz, 6 GHz) | [optional] 
**roaming_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The number of roaming issues experienced by the client | [optional] value must be a 64 bit integer
**ipv4** | str,  | str,  | The IPv4 address assigned to the client | [optional] 
**connected_device_mac** | str,  | str,  | The MAC address of the connected device | [optional] 
**ssid** | str,  | str,  | The SSID of the network | [optional] 
**vlan** | decimal.Decimal, int,  | decimal.Decimal,  | The VLAN ID | [optional] value must be a 64 bit integer
**username** | str,  | str,  | The username of the client | [optional] 
**authentication** | str,  | str,  | The authentication method used | [optional] 
**encryption** | str,  | str,  | The encryption method used | [optional] 
**user_profile** | str,  | str,  | The user profile assigned to the client | [optional] 
**alias** | str,  | str,  | The alias of the client | [optional] 
**category_assignment** | str,  | str,  | The category assignment of the client | [optional] 
**ipv6** | str,  | str,  | The IPv6 address assigned to the client | [optional] 
**client_device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The client device ID | [optional] value must be a 64 bit integer
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID | [optional] value must be a 64 bit integer
**last_session_start_time** | decimal.Decimal, int,  | decimal.Decimal,  | The start time of the last session | [optional] value must be a 64 bit integer
**operating_system** | str,  | str,  | The operating system of the client device | [optional] 
**client_mac** | str,  | str,  | The MAC address of the client device | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

