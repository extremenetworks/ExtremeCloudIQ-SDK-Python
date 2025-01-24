# extremecloudiq.model.xiq_dell_device.XiqDellDevice

Dell device to onboard

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Dell device to onboard | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**service_tag** | str,  | str,  | The service tag | 
**location** | [**XiqDeviceLocationAssignment**](XiqDeviceLocationAssignment.md) | [**XiqDeviceLocationAssignment**](XiqDeviceLocationAssignment.md) |  | 
**serial_number** | str,  | str,  | The serial number | 
**network_policy_id** | decimal.Decimal, int,  | decimal.Decimal,  | The assigned network policy | [optional] value must be a 64 bit integer
**hostname** | str,  | str,  | The device hostname | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

