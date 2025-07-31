# extremecloudiq.model.xiq_radio_profile.XiqRadioProfile

The payload of Radio Profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of Radio Profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**name** | str,  | str,  | The radio profile name | [optional] 
**predefined** | bool,  | BoolClass,  | Whether the radio profile is predefined or user-customized. | [optional] 
**description** | str,  | str,  | The radio profile description. | [optional] 
**transmission_power** | decimal.Decimal, int,  | decimal.Decimal,  | The transmission power floor from 1 up to 20 dBm or null for Auto. | [optional] value must be a 32 bit integer
**max_transmit_power** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum transmit power from 10 up to 20 dBm. | [optional] value must be a 32 bit integer
**transmission_power_floor** | decimal.Decimal, int,  | decimal.Decimal,  | The transmission power floor from 2 up to 20 dBm. | [optional] value must be a 32 bit integer
**transmission_power_max_drop** | decimal.Decimal, int,  | decimal.Decimal,  | The transmission power max drop from 0 up to 18 dB. | [optional] value must be a 32 bit integer
**max_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of clients from 1 up to 255. | [optional] value must be a 32 bit integer
**enable_client_transmission_power** | bool,  | BoolClass,  | Whether or not client transmission power control (802.11h) is enabled. | [optional] 
**client_transmission_power** | decimal.Decimal, int,  | decimal.Decimal,  | The client transmission power from 1 up to 20 dBm if it is enabled. | [optional] value must be a 32 bit integer
**enable_ofdma** | bool,  | BoolClass,  | Whether to enable Orthogonal Frequency Division Multiple Access (802.11ax) for multiple-user access by subdividing a channel. | [optional] 
**radio_mode** | [**XiqRadioMode**](XiqRadioMode.md) | [**XiqRadioMode**](XiqRadioMode.md) |  | [optional] 
**neighborhood_analysis_id** | decimal.Decimal, int,  | decimal.Decimal,  | The neighborhood analysis Id. | [optional] value must be a 64 bit integer
**channel_selection_id** | decimal.Decimal, int,  | decimal.Decimal,  | The channel selection Id. | [optional] value must be a 64 bit integer
**radio_usage_optimization_id** | decimal.Decimal, int,  | decimal.Decimal,  | The radio usage optimization Id. | [optional] value must be a 64 bit integer
**miscellaneous_settings_id** | decimal.Decimal, int,  | decimal.Decimal,  | The miscellaneous settings Id | [optional] value must be a 64 bit integer
**presence_server_settings_id** | decimal.Decimal, int,  | decimal.Decimal,  | The presence server settings Id. | [optional] value must be a 64 bit integer
**sensor_scan_settings_id** | decimal.Decimal, int,  | decimal.Decimal,  | The sensor scan settings Id. | [optional] value must be a 64 bit integer
**afc_power_mode** | str,  | str,  | The power mode for 6 GHZ radio profiles for supporting APs | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

