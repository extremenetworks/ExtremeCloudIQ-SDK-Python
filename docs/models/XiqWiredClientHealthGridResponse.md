# extremecloudiq.model.xiq_wired_client_health_grid_response.XiqWiredClientHealthGridResponse

Response for Wired Client Grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response for Wired Client Grid | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**connection_status** | [**XiqClientConnectionStatus**](XiqClientConnectionStatus.md) | [**XiqClientConnectionStatus**](XiqClientConnectionStatus.md) |  | [optional] 
**client_hostname** | str,  | str,  | The hostname of the client | [optional] 
**client_ip** | str,  | str,  | The IP address of the client | [optional] 
**site** | str,  | str,  | The site where the client is located | [optional] 
**building** | str,  | str,  | The building where the client is located | [optional] 
**floor** | str,  | str,  | The floor where the client is located | [optional] 
**ipv4** | str,  | str,  | The IPv4 address assigned to the client | [optional] 
**ipv6** | str,  | str,  | The IPv6 address assigned to the client | [optional] 
**port_number** | str,  | str,  | The port number on which the device is connected | [optional] 
**switch_name** | str,  | str,  | The switch name of the connected device | [optional] 
**vlan** | decimal.Decimal, int,  | decimal.Decimal,  | The VLAN | [optional] value must be a 32 bit integer
**operating_system** | str,  | str,  | The operating system of the client device | [optional] 
**mac** | str,  | str,  | The MAC address of the client device | [optional] 
**username** | str,  | str,  | The username of the client | [optional] 
**instant_port_profile** | str,  | str,  | The Instant Port Profile type assignment to client | [optional] 
**total_congestion_packets** | decimal.Decimal, int,  | decimal.Decimal,  | The total congestion packets | [optional] value must be a 64 bit integer
**total_unicast_packets_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | The total unicast packets percentage | [optional] value must be a 32 bit integer
**total_multicast_packets_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | The total multicast packets percentage | [optional] value must be a 32 bit integer
**total_broadcast_packets_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | The total broadcast packets percentage | [optional] value must be a 32 bit integer
**total_port_errors** | decimal.Decimal, int,  | decimal.Decimal,  | The total port errors | [optional] value must be a 64 bit integer
**has_ip_address_issues** | bool,  | BoolClass,  | Indicates if there are IP address issues (related to UI tooltip) | [optional] 
**has_port_congestions** | bool,  | BoolClass,  | Indicates if there are port congestions (related to UI tooltip) | [optional] 
**has_traffic_anomalies** | bool,  | BoolClass,  | Indicates if there are traffic anomalies (related to UI tooltip) | [optional] 
**has_port_errors** | bool,  | BoolClass,  | Indicates if there are port errors (related to UI tooltip) | [optional] 
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device to which client is connected | [optional] value must be a 64 bit integer
**client_id** | decimal.Decimal, int,  | decimal.Decimal,  | The client ID | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

