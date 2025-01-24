# extremecloudiq.model.xiq_device_level_ssid.XiqDeviceLevelSsid

The ssid/passphrase for device level ssid to override

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The ssid/passphrase for device level ssid to override | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ssid_id** | decimal.Decimal, int,  | decimal.Decimal,  | The SSID ID to override, cannot be null. | value must be a 64 bit integer
**ssid** | str,  | str,  | The broadcast ssid name to override. Can only override if the SSID profile is OPEN or PSK mode. | [optional] 
**passphrase** | str,  | str,  | The ssid passphrase to override. Can only override if the SSID profile is in PSK mode. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

