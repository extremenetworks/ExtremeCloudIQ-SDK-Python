# extremecloudiq.model.xiq_radio.XiqRadio

ExtremeCloud IQ Radio Information associated to a device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Radio Information associated to a device | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mode** | str,  | str,  | The radio mode indicating the WiFi standard and frequency band. | must be one of ["_11bg", "_11a", "_11an", "_11ng", "_11ac", "_11ax_2g", "_11ax_5g", "_11ax_6g", "_11be_2g", "_11be_5g", "_11be_6g", ] 
**name** | str,  | str,  | the radio name | 
**channel_width** | str,  | str,  | The channel width. | must be one of ["MHZ_20", "MHZ_40", "MHZ_80", "MHZ_160", "MHZ_320", ] 
**channel_number** | decimal.Decimal, int,  | decimal.Decimal,  | the channel number | [optional] value must be a 32 bit integer
**mac_address** | str,  | str,  | The radio MAC address in format XXXXXXXXXXXX | [optional] 
**power** | decimal.Decimal, int,  | decimal.Decimal,  | The radio transmission power in dBm. | [optional] value must be a 32 bit integer
**frequency** | str,  | str,  | WiFi frequency band | [optional] must be one of ["2.4GHz", "5GHz", "6GHz", ] 
**[clients](#clients)** | list, tuple,  | tuple,  | the clients and SSID details | [optional] 
**[wlans](#wlans)** | list, tuple,  | tuple,  | the radios WLAN details | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# clients

the clients and SSID details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the clients and SSID details | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWirelessClient**](XiqWirelessClient.md) | [**XiqWirelessClient**](XiqWirelessClient.md) | [**XiqWirelessClient**](XiqWirelessClient.md) |  | 

# wlans

the radios WLAN details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the radios WLAN details | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqWirelessWlan**](XiqWirelessWlan.md) | [**XiqWirelessWlan**](XiqWirelessWlan.md) | [**XiqWirelessWlan**](XiqWirelessWlan.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

