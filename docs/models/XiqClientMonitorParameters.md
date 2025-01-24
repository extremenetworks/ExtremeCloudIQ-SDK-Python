# extremecloudiq.model.xiq_client_monitor_parameters.XiqClientMonitorParameters

This represents the client monitor parameters for a problem type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This represents the client monitor parameters for a problem type | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**trigger_times** | decimal.Decimal, int,  | decimal.Decimal,  | The trigger times, min &#x3D; 1, max &#x3D; 10 | [optional] value must be a 32 bit integer
**report_interval** | decimal.Decimal, int,  | decimal.Decimal,  | The report interval, min &#x3D; 30, max &#x3D; 3600 seconds | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

