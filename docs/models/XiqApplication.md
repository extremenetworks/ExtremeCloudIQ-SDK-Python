# extremecloudiq.model.xiq_application.XiqApplication

The Application Model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Application Model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The application name | [optional] 
**description** | str,  | str,  | The application description | [optional] 
**predefined** | bool,  | BoolClass,  | Flag to describle whether the application is predefined or customized | [optional] 
**category_id** | decimal.Decimal, int,  | decimal.Decimal,  | The category ID of application | [optional] value must be a 64 bit integer
**category_name** | str,  | str,  | The category name of application | [optional] 
**[detection_rules](#detection_rules)** | list, tuple,  | tuple,  | The application detection rules | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# detection_rules

The application detection rules

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The application detection rules | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqApplicationDetectionRule**](XiqApplicationDetectionRule.md) | [**XiqApplicationDetectionRule**](XiqApplicationDetectionRule.md) | [**XiqApplicationDetectionRule**](XiqApplicationDetectionRule.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

