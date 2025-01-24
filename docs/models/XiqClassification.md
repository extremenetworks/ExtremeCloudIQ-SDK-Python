# extremecloudiq.model.xiq_classification.XiqClassification

The payload of common object - classification

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of common object - classification | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**match** | bool,  | BoolClass,  | Contains or not contains) | 
**classification_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of location, cloud config group, IP address, IP subnet or IP range. | value must be a 64 bit integer
**classification_type** | [**XiqClassificationType**](XiqClassificationType.md) | [**XiqClassificationType**](XiqClassificationType.md) |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**value** | str,  | str,  | The value of classification | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

