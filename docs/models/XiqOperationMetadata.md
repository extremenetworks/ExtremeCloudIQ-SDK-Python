# extremecloudiq.model.xiq_operation_metadata.XiqOperationMetadata

The metadata of Long Running Operation (LRO)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The metadata of Long Running Operation (LRO) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The operation&#x27;s last update time | value must conform to RFC-3339 date-time
**cancelable** | bool,  | BoolClass,  | Indicates if the operation can be canceled in the current status | 
**create_time** | str, datetime,  | str,  | The operation&#x27;s create time, which is the time when the operation is in PENDING status | value must conform to RFC-3339 date-time
**expires_in** | decimal.Decimal, int,  | decimal.Decimal,  | The number of seconds remaining until the operation expires and is to be deleted. | value must be a 64 bit integer
**status** | [**XiqOperationStatus**](XiqOperationStatus.md) | [**XiqOperationStatus**](XiqOperationStatus.md) |  | 
**percentage** | decimal.Decimal, int,  | decimal.Decimal,  | The progress in percentage ranges from 0 to 100 (it&#x27;s not guaranteed to be accurate) | [optional] value must be a 32 bit integer
**step** | str,  | str,  | The optional step name for multiple steps operations when the operation is running | [optional] 
**start_time** | str, datetime,  | str,  | The operation&#x27;s start time, which is the time when the operation is in RUNNING status | [optional] value must conform to RFC-3339 date-time
**end_time** | str, datetime,  | str,  | The operation&#x27;s end time, which is the time when the operation is done | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

