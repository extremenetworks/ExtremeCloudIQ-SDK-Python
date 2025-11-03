# extremecloudiq.model.event_count.EventCount

Event count for a specific type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Event count for a specific type | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**event_name** | str,  | str,  | The name of the event type | [optional] must be one of ["CRITICAL", "MAJOR", "MINOR", "INFO", "ACTIVE", "CLEAR", "ALL", "WARNING", ] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of events of this type at the timestamp | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

