# XiqRadioProfile

The payload of Radio Profile
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**name** | **str** | The radio profile name | [optional] 
**predefined** | **bool** | Whether the radio profile is predefined or user-customized. | [optional] 
**description** | **str** | The radio profile description. | [optional] 
**transmission_power** | **int** | The transmission power floor from 1 up to 20 dBm or null for Auto. | [optional] 
**max_transmit_power** | **int** | The maximum transmit power from 10 up to 20 dBm. | [optional] 
**transmission_power_floor** | **int** | The transmission power floor from 2 up to 20 dBm. | [optional] 
**transmission_power_max_drop** | **int** | The transmission power max drop from 0 up to 18 dB. | [optional] 
**max_clients** | **int** | The maximum number of clients from 1 up to 255. | [optional] 
**enable_client_transmission_power** | **bool** | Whether or not client transmission power control (802.11h) is enabled. | [optional] 
**client_transmission_power** | **int** | The client transmission power from 1 up to 20 dBm if it is enabled. | [optional] 
**enable_ofdma** | **bool** | Whether to enable Orthogonal Frequency Division Multiple Access (802.11ax) for multiple-user access by subdividing a channel. | [optional] 
**radio_mode** | [**XiqRadioMode**](XiqRadioMode.md) |  | [optional] 
**neighborhood_analysis_id** | **int** | The neighborhood analysis Id. | [optional] 
**channel_selection_id** | **int** | The channel selection Id. | [optional] 
**radio_usage_optimization_id** | **int** | The radio usage optimization Id. | [optional] 
**miscellaneous_settings_id** | **int** | The miscellaneous settings Id | [optional] 
**presence_server_settings_id** | **int** | The presence server settings Id. | [optional] 
**sensor_scan_settings_id** | **int** | The sensor scan settings Id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


