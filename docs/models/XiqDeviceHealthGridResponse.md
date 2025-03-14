# extremecloudiq.model.xiq_device_health_grid_response.XiqDeviceHealthGridResponse

The device health grid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The device health grid | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hostname** | str,  | str,  | The hostname of the device | [optional] 
**device_ip** | str,  | str,  | The IP address of the device | [optional] 
**site** | str,  | str,  | The site where the device is located | [optional] 
**building** | str,  | str,  | The building where the device is located | [optional] 
**floor** | str,  | str,  | The floor where the device is located | [optional] 
**cpu_usage_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage of CPU utilisation | [optional] value must be a 64 bit integer
**memory_usage_percentage** | decimal.Decimal, int,  | decimal.Decimal,  | Percentage of memory utilisation | [optional] value must be a 64 bit integer
**poe_usage_indicator** | bool,  | BoolClass,  | Indicates whether PoE usage is within acceptable limits (device has adequate power supply) | [optional] 
**channel_change_count** | decimal.Decimal, int,  | decimal.Decimal,  | The count for channel change for the device | [optional] value must be a 64 bit integer
**wifi_reboots_count** | decimal.Decimal, int,  | decimal.Decimal,  | The count for Wi-Fi reboots for the device | [optional] value must be a 64 bit integer
**eth0_unicast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Unicast score for Eth0 interface | [optional] value must be a 64 bit integer
**eth0_broadcast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Broadcast score for Eth0 interface | [optional] value must be a 64 bit integer
**eth0_multicast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Multicast score for Eth0 interface | [optional] value must be a 64 bit integer
**eth1_unicast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Unicast score for Eth1 interface | [optional] value must be a 64 bit integer
**eth1_broadcast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Broadcast score for Eth1 interface | [optional] value must be a 64 bit integer
**eth1_multicast_score** | decimal.Decimal, int,  | decimal.Decimal,  | Multicast score for Eth1 interface | [optional] value must be a 64 bit integer
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device id | [optional] value must be a 64 bit integer
**has_device_health_issue** | bool,  | BoolClass,  | Flag to indicate if device has device health issue | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

