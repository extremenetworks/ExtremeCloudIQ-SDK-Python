# extremecloudiq.model.xiq_device_wifi_interface.XiqDeviceWifiInterface

Get the device WiFi interface stats

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Get the device WiFi interface stats | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**frequency** | str,  | str,  | The WiFi frequency. | [optional] 
**ssid_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of SSID assigned on this wireless interface. | [optional] value must be a 32 bit integer
**client_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of clients associated to this wireless interface. | [optional] value must be a 64 bit integer
**neighbor_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The number of neighboring clients. | [optional] value must be a 64 bit integer
**channel_util** | decimal.Decimal, int,  | decimal.Decimal,  | The channel utilization. | [optional] value must be a 32 bit integer
**channel** | decimal.Decimal, int,  | decimal.Decimal,  | The channel associated. | [optional] value must be a 32 bit integer
**channel_width** | decimal.Decimal, int,  | decimal.Decimal,  | The channel width. | [optional] value must be a 32 bit integer
**tx_utilization** | decimal.Decimal, int,  | decimal.Decimal,  | The total tx utilization. | [optional] value must be a 64 bit integer
**rx_utilization** | decimal.Decimal, int,  | decimal.Decimal,  | The total rx utilization. | [optional] value must be a 64 bit integer
**tx_byte_count** | decimal.Decimal, int,  | decimal.Decimal,  | The total tx byte count. | [optional] value must be a 64 bit integer
**rx_byte_count** | decimal.Decimal, int,  | decimal.Decimal,  | The total rx byte count. | [optional] value must be a 64 bit integer
**noise_floor** | decimal.Decimal, int,  | decimal.Decimal,  | The noise floor. | [optional] value must be a 64 bit integer
**crc_error_frame** | decimal.Decimal, int,  | decimal.Decimal,  | The crc error frame count. | [optional] value must be a 64 bit integer
**tx_retry_frame** | decimal.Decimal, int,  | decimal.Decimal,  | The tx retry frame | [optional] value must be a 64 bit integer
**rx_retry_frame** | decimal.Decimal, int,  | decimal.Decimal,  | The rx retry fram. | [optional] value must be a 64 bit integer
**unicast_tx_packet_count** | decimal.Decimal, int,  | decimal.Decimal,  | The unicast tx packet count. | [optional] value must be a 64 bit integer
**unicast_rx_packet_count** | decimal.Decimal, int,  | decimal.Decimal,  | The unicast rx packet count. | [optional] value must be a 64 bit integer
**broadcast_tx_packet_count** | decimal.Decimal, int,  | decimal.Decimal,  | The broadcast tx packet count. | [optional] value must be a 64 bit integer
**broadcast_rx_packet_count** | decimal.Decimal, int,  | decimal.Decimal,  | The broadcast rx packet count. | [optional] value must be a 64 bit integer
**tx_air_time** | decimal.Decimal, int,  | decimal.Decimal,  | The tx air time. | [optional] value must be a 64 bit integer
**rx_air_time** | decimal.Decimal, int,  | decimal.Decimal,  | The rx air time. | [optional] value must be a 64 bit integer
**total_utilization** | decimal.Decimal, int,  | decimal.Decimal,  | The total utilization. | [optional] value must be a 64 bit integer
**scan_avg_interference** | decimal.Decimal, int,  | decimal.Decimal,  | The average interference. | [optional] value must be a 32 bit integer
**mac_address** | str,  | str,  | The bssid. | [optional] 
**power** | decimal.Decimal, int,  | decimal.Decimal,  | The radio power. | [optional] value must be a 32 bit integer
**rx_errors** | decimal.Decimal, int,  | decimal.Decimal,  | The rx errors. | [optional] value must be a 64 bit integer
**tx_errors** | decimal.Decimal, int,  | decimal.Decimal,  | The tx errors. | [optional] value must be a 64 bit integer
**interface_name** | str,  | str,  | The interface name. | [optional] 
**radio_profile_name** | str,  | str,  | The ExtremecloudIQ radio profile name. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

