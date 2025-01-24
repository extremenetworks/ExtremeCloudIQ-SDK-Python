# extremecloudiq.model.xiq_device_cpu_memory_usage.XiqDeviceCpuMemoryUsage

Get time series of the average device cpu and memory usage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Get time series of the average device cpu and memory usage | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**average_cpu** | decimal.Decimal, int,  | decimal.Decimal,  | The device average cpu usage | [optional] value must be a 32 bit integer
**average_memory** | decimal.Decimal, int,  | decimal.Decimal,  | The device average memory usage | [optional] value must be a 32 bit integer
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp for data aggregate | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

