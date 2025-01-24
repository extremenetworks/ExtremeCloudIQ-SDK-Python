# extremecloudiq.model.xiq_create_radio_profile_request.XiqCreateRadioProfileRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The radio profile name | 
**description** | str,  | str,  | The radio profile description. | [optional] 
**transmission_power** | decimal.Decimal, int,  | decimal.Decimal,  | The transmission power floor in the range of 1-20 dBm or null for Auto. | [optional] value must be a 32 bit integer
**max_transmit_power** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum transmit power in the range of 10-20 dBm. | [optional] value must be a 32 bit integer
**transmission_power_floor** | decimal.Decimal, int,  | decimal.Decimal,  | The transmission power floor in the range of 2-20 dBm. | [optional] value must be a 32 bit integer
**transmission_power_max_drop** | decimal.Decimal, int,  | decimal.Decimal,  | The transmission power max drop in the range of 0-18 dB. | [optional] value must be a 32 bit integer
**max_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of clients in the range of 1-255. | [optional] value must be a 32 bit integer
**enable_client_transmission_power** | bool,  | BoolClass,  | Whether or not client transmission power control (802.11h) is enabled. | [optional] 
**client_transmission_power** | decimal.Decimal, int,  | decimal.Decimal,  | The client transmission power (in the range of 1-20 dBm) if it is enabled. | [optional] value must be a 32 bit integer
**radio_mode** | [**XiqRadioMode**](XiqRadioMode.md) | [**XiqRadioMode**](XiqRadioMode.md) |  | [optional] 
**enable_ofdma** | bool,  | BoolClass,  | Whether to enable Orthogonal Frequency Division Multiple Access (802.11ax) for multiple-user access by subdividing a channel. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

