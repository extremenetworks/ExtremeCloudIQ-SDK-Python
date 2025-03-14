# extremecloudiq.model.xiq_client_health_grid_response.XiqClientHealthGridResponse

The client health grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The client health grid | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_hostname** | str,  | str,  | The hostname of the client | [optional] 
**client_ip** | str,  | str,  | The IP address of the client | [optional] 
**site** | str,  | str,  | The site where the client is located | [optional] 
**building** | str,  | str,  | The building where the client is located | [optional] 
**floor** | str,  | str,  | The floor where the client is located | [optional] 
**has_association_issues** | bool,  | BoolClass,  | The indicator of association issues | [optional] 
**has_authentication_issues** | bool,  | BoolClass,  | The indicator of authentication issues | [optional] 
**has_ip_address_issues** | bool,  | BoolClass,  | The indicator of IP address issues | [optional] 
**snr** | decimal.Decimal, int,  | decimal.Decimal,  | Signal-to-noise ratio of the client&#x27;s connection | [optional] value must be a 32 bit integer
**rssi** | decimal.Decimal, int,  | decimal.Decimal,  | Received signal strength indicator of the client&#x27;s connection | [optional] value must be a 32 bit integer
**air_time** | decimal.Decimal, int,  | decimal.Decimal,  | The percentage of air time used by the client | [optional] value must be a 32 bit integer
**frequency** | str,  | str,  | The frequency band used by the client (e.g., 2.4 GHz, 5 GHz, 6 GHz) | [optional] 
**has_roaming_issues** | bool,  | BoolClass,  | The indicator of roaming issues experienced by the client | [optional] 
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
**slowness** | decimal.Decimal, int,  | decimal.Decimal,  | The slowness value of the IP Address | [optional] value must be a 64 bit integer
**client_device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The client device ID | [optional] value must be a 64 bit integer
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID | [optional] value must be a 64 bit integer
**roaming_time** | decimal.Decimal, int,  | decimal.Decimal,  | The roaming time | [optional] value must be a 64 bit integer
**association_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The association duration | [optional] value must be a 64 bit integer
**dhcp_ip_assignation_time** | decimal.Decimal, int,  | decimal.Decimal,  | The DHCP IP assignation time | [optional] value must be a 64 bit integer
**authentication_response_time** | decimal.Decimal, int,  | decimal.Decimal,  | The authentication response time | [optional] value must be a 64 bit integer
**rx_client_retries** | decimal.Decimal, int, float,  | decimal.Decimal,  | The RX client retries | [optional] value must be a 32 bit float
**tx_client_retries** | decimal.Decimal, int, float,  | decimal.Decimal,  | The TX client retries | [optional] value must be a 32 bit float
**ipv4_warning** | bool,  | BoolClass,  | The number of association issues | [optional] 
**air_time_warning** | bool,  | BoolClass,  | The number of association issues | [optional] 
**association_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The number of association issues | [optional] value must be a 32 bit integer
**authentication_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The number of authentication issues | [optional] value must be a 32 bit integer
**ip_address_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The number of IP address issues | [optional] value must be a 32 bit integer
**roaming_issues** | decimal.Decimal, int,  | decimal.Decimal,  | The number of roaming issues experienced by the client | [optional] value must be a 32 bit integer
**connectionStatus** | [**XiqClientConnectionStatus**](XiqClientConnectionStatus.md) | [**XiqClientConnectionStatus**](XiqClientConnectionStatus.md) |  | [optional] 
**last_session_start_time** | decimal.Decimal, int,  | decimal.Decimal,  | The start time of the last session | [optional] value must be a 64 bit integer
**operating_system** | str,  | str,  | The operating system of the client device | [optional] 
**client_mac** | str,  | str,  | The MAC address of the client device | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

