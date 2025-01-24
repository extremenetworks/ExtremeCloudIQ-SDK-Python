# extremecloudiq.model.xiq_device_interface_radio_mode.XiqDeviceInterfaceRadioMode

Wirelss Interfaces.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Wirelss Interfaces. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | [**XiqWirelessIfName**](XiqWirelessIfName.md) | [**XiqWirelessIfName**](XiqWirelessIfName.md) |  | [optional] 
**band** | str,  | str,  | The default radio band | [optional] must be one of ["BAND24", "BAND5", "BAND5LOW", "BAND5HIGH", "BAND6", "BAND6LOW", "BAND6HIGH", "BANDNONE", ] 
**default_radio_mode** | [**XiqRadioMode**](XiqRadioMode.md) | [**XiqRadioMode**](XiqRadioMode.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

