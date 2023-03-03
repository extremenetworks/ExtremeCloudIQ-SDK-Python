# XiqCreateRadioProfileRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The radio profile name | 
**description** | **str** | The radio profile description. | [optional] 
**transmission_power** | **int** | The transmission power floor in the range of 1-20 dBm or null for Auto. | [optional] 
**max_transmit_power** | **int** | The maximum transmit power in the range of 10-20 dBm. | [optional] 
**transmission_power_floor** | **int** | The transmission power floor in the range of 2-20 dBm. | [optional] 
**transmission_power_max_drop** | **int** | The transmission power max drop in the range of 0-18 dB. | [optional] 
**max_clients** | **int** | The maximum number of clients in the range of 1-255. | [optional] 
**enable_client_transmission_power** | **bool** | Whether or not client transmission power control (802.11h) is enabled. | [optional] 
**client_transmission_power** | **int** | The client transmission power (in the range of 1-20 dBm) if it is enabled. | [optional] 
**radio_mode** | [**XiqRadioMode**](XiqRadioMode.md) |  | [optional] 
**enable_ofdma** | **bool** | Whether to enable Orthogonal Frequency Division Multiple Access (802.11ax) for multiple-user access by subdividing a channel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


