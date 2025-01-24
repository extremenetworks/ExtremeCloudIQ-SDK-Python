# extremecloudiq.model.xiq_device_monitor_refresh_status_response.XiqDeviceMonitorRefreshStatusResponse

The request for on demand refresh information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request for on demand refresh information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**percentage** | decimal.Decimal, int,  | decimal.Decimal,  | The device monitor refresh percentage | value must be a 32 bit integer
**task_key** | str,  | str,  | The device monitor refresh task key | 
**status** | str,  | str,  | The device monitor refresh status | must be one of ["INVALID", "FINISHED", "UNFINISHED", "TASK_NOT_EXIST", "UNKNOWN", "UNRECOGNIZED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

