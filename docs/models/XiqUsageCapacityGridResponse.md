# extremecloudiq.model.xiq_usage_capacity_grid_response.XiqUsageCapacityGridResponse

The usage & capacity grid of wireless devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The usage &amp; capacity grid of wireless devices | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hostname** | str,  | str,  | Hostname of the device | [optional] 
**device_ip** | str,  | str,  | The IP address of the device | [optional] 
**site** | str,  | str,  | The site where the device is located | [optional] 
**building** | str,  | str,  | The building where the device is located | [optional] 
**floor** | str,  | str,  | The floor where the device is located | [optional] 
**mac_address** | str,  | str,  | MAC address of the device | [optional] 
**wifi0_retry_score** | decimal.Decimal, int,  | decimal.Decimal,  | Retry score for wifi0 | [optional] value must be a 64 bit integer
**wifi1_retry_score** | decimal.Decimal, int,  | decimal.Decimal,  | Retry score for wifi1 | [optional] value must be a 64 bit integer
**wifi2_retry_score** | decimal.Decimal, int,  | decimal.Decimal,  | Retry score for wifi2 | [optional] value must be a 64 bit integer
**wifi0_packet_loss** | decimal.Decimal, int,  | decimal.Decimal,  | Packet loss score in APs | [optional] value must be a 64 bit integer
**wifi1_packet_loss** | decimal.Decimal, int,  | decimal.Decimal,  | Packet loss score in APs | [optional] value must be a 64 bit integer
**wifi2_packet_loss** | decimal.Decimal, int,  | decimal.Decimal,  | Packet loss score in APs | [optional] value must be a 64 bit integer
**eth0_unicast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Unicast score for Eth0 interface | [optional] value must be a 64 bit integer
**eth0_broadcast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Broadcast score for Eth0 interface | [optional] value must be a 64 bit integer
**eth0_multicast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Multicast score for Eth0 interface | [optional] value must be a 64 bit integer
**eth1_unicast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Unicast score for Eth1 interface | [optional] value must be a 64 bit integer
**eth1_broadcast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Broadcast score for Eth1 interface | [optional] value must be a 64 bit integer
**eth1_multicast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Multicast score for Eth1 interface | [optional] value must be a 64 bit integer
**wifi0_interference_score** | decimal.Decimal, int,  | decimal.Decimal,  | Interference score for wifi0 | [optional] value must be a 64 bit integer
**wifi1_interference_score** | decimal.Decimal, int,  | decimal.Decimal,  | Interference score for wifi1 | [optional] value must be a 64 bit integer
**wifi2_interference_score** | decimal.Decimal, int,  | decimal.Decimal,  | Interference score for wifi2 | [optional] value must be a 64 bit integer
**wifi0_noise** | decimal.Decimal, int,  | decimal.Decimal,  | Noise score for wifi0 | [optional] value must be a 64 bit integer
**wifi1_noise** | decimal.Decimal, int,  | decimal.Decimal,  | Noise score for wifi1 | [optional] value must be a 64 bit integer
**wifi2_noise** | decimal.Decimal, int,  | decimal.Decimal,  | Noise score for wifi2 | [optional] value must be a 64 bit integer
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device id | [optional] value must be a 64 bit integer
**packet_loss** | decimal.Decimal, int,  | decimal.Decimal,  | The device id | [optional] value must be a 64 bit integer
**link_error2_dot4_g** | decimal.Decimal, int,  | decimal.Decimal,  | Link Error for wifi0 | [optional] value must be a 64 bit integer
**link_error5g** | decimal.Decimal, int,  | decimal.Decimal,  | Link Error for wifi1 | [optional] value must be a 64 bit integer
**link_error6g** | decimal.Decimal, int,  | decimal.Decimal,  | Link Error for wifi2 | [optional] value must be a 64 bit integer
**healthy_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The associated active client count for the device | [optional] value must be a 32 bit integer
**unhealthy_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The associated inactive client count for the device | [optional] value must be a 32 bit integer
**has_usage_capacity_issue** | bool,  | BoolClass,  | Flag to indicate if device has usage capacity issue | [optional] 
**radio_2dot4g_utilization_score** | decimal.Decimal, int,  | decimal.Decimal,  | Channel Utilization score for 2.4 GHz radio | [optional] value must be a 64 bit integer
**radio_5g_utilization_score** | decimal.Decimal, int,  | decimal.Decimal,  | Channel Utilization score for 5 GHz radio | [optional] value must be a 64 bit integer
**radio_6g_utilization_score** | decimal.Decimal, int,  | decimal.Decimal,  | Channel Utilization score for 6 GHz radio | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

