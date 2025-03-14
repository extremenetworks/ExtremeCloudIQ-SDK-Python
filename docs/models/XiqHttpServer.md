# extremecloudiq.model.xiq_http_server.XiqHttpServer

The BLE Scan destination HTTP server URL.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The BLE Scan destination HTTP server URL. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**url** | str,  | str,  | The HTTP server URL. | [optional] 
**interval** | decimal.Decimal, int,  | decimal.Decimal,  | The HTTP server interval, in seconds. | [optional] value must be a 32 bit integer
**enable_deduplication** | bool,  | BoolClass,  | Enable to remove BLE scan duplicates entries within the specified time interval. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

