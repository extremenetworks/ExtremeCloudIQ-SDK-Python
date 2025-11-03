# extremecloudiq.model.xiq_ssh_active_sessions_response.XiqSshActiveSessionsResponse

Response model for active SSH sessions on a device.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Response model for active SSH sessions on a device. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID. | [optional] value must be a 64 bit integer
**host_name** | str,  | str,  | The device name. | [optional] 
**serial_number** | str,  | str,  | The device serial number. | [optional] 
**site_name** | str,  | str,  | The site name of device. | [optional] 
**start_time** | decimal.Decimal, int,  | decimal.Decimal,  | The start time of ssh session. | [optional] value must be a 64 bit integer
**time_out** | decimal.Decimal, int,  | decimal.Decimal,  | The time out for ssh session. | [optional] value must be a 64 bit integer
**percentage_progress** | decimal.Decimal, int,  | decimal.Decimal,  | The percentage ssh session timeout in mins. | [optional] value must be a 32 bit integer
**session_id** | str,  | str,  | The session ID for the active ssh access of device | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

