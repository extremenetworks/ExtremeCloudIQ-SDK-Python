# extremecloudiq.model.xiq_device_firmware_metadata.XiqDeviceFirmwareMetadata

The device compatible firmware metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The device compatible firmware metadata | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**firmware_id** | decimal.Decimal, int,  | decimal.Decimal,  | The firmware metadata ID | value must be a 64 bit integer
**firmware_name** | str,  | str,  | The firmware name | [optional] 
**firmware_type** | str,  | str,  | The firmware type | [optional] 
**scope** | str,  | str,  | The firmware availability scope | [optional] 
**version** | str,  | str,  | The firmware version | [optional] 
**date** | str,  | str,  | The firmware release date | [optional] 
**firmware_size** | str,  | str,  | The firmware size | [optional] 
**display_version** | str,  | str,  | The firmware display version | [optional] 
**supported_platforms** | str,  | str,  | The platforms supported by the firmware | [optional] 
**md5** | str,  | str,  | The firmware md5 hash | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

