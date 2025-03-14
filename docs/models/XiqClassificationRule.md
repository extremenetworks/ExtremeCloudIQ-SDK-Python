# extremecloudiq.model.xiq_classification_rule.XiqClassificationRule

The payload of common object - classification assignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of common object - classification assignment | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The classification assignment name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The classification assignment description | [optional] 
**[classifications](#classifications)** | list, tuple,  | tuple,  | The details of rule assignments | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# classifications

The details of rule assignments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The details of rule assignments | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqClassification**](XiqClassification.md) | [**XiqClassification**](XiqClassification.md) | [**XiqClassification**](XiqClassification.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

