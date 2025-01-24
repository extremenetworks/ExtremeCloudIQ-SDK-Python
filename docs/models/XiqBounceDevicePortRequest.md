# extremecloudiq.model.xiq_bounce_device_port_request.XiqBounceDevicePortRequest

The request for bouncing port of a single device. Includes EXOS, VOSS devices and SR switches

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request for bouncing port of a single device. Includes EXOS, VOSS devices and SR switches | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device id | [optional] value must be a 64 bit integer
**port_number** | str,  | str,  | The port number of the device (eg. 1,2, ..) | [optional] 
**bounce_port_reason** | str,  | str,  | The reason to bounce the port of the device (eg. reset the inline power on the port so that the connected AP can be restarted) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

