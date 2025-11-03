# extremecloudiq.model.timestamped_events.TimestampedEvents

Event metrics for a specific timestamp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Event metrics for a specific timestamp | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp of the event metric (Unix epoch in ms) | [optional] value must be a 64 bit integer
**[events](#events)** | list, tuple,  | tuple,  | List of event types and their counts | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# events

List of event types and their counts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of event types and their counts | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EventCount**](EventCount.md) | [**EventCount**](EventCount.md) | [**EventCount**](EventCount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

