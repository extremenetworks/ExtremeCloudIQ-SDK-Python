# extremecloudiq.model.xiq_alert.XiqAlert

The Alert Model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Alert Model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The unique identifier | 
**[tags](#tags)** | list, tuple,  | tuple,  | Additional information for the alert | 
**timestamp** | str, datetime,  | str,  | The alert create time | value must conform to RFC-3339 date-time
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The owner ID | [optional] value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**message_metadata_id** | decimal.Decimal, int,  | decimal.Decimal,  | The message metadata id | [optional] value must be a 64 bit integer
**message_metadata_type** | str,  | str,  | The message metadata type | [optional] 
**message_metadata_name** | str,  | str,  | The message metadata name | [optional] 
**summary** | str,  | str,  | A high-level, text summary message of the event. Will be used to construct an alert&#x27;s description. | [optional] 
**severity_name** | str,  | str,  | The severity name of the alert | [optional] 
**category_name** | str,  | str,  | The alert category name | [optional] 
**severity_id** | decimal.Decimal, int,  | decimal.Decimal,  | The severity Id of the alert | [optional] value must be a 64 bit integer
**category_id** | decimal.Decimal, int,  | decimal.Decimal,  | The alert category Id | [optional] value must be a 64 bit integer
**source** | [**XiqAlertSource**](XiqAlertSource.md) | [**XiqAlertSource**](XiqAlertSource.md) |  | [optional] 
**acknowledged** | bool,  | BoolClass,  | The acknowledged status of alert | [optional] 
**site_id** | decimal.Decimal, int,  | decimal.Decimal,  | The site id of alert | [optional] value must be a 64 bit integer
**site_name** | str,  | str,  | The site name of alert | [optional] 
**alert_policy_id** | decimal.Decimal, int,  | decimal.Decimal,  | The policy id of alert | [optional] value must be a 64 bit integer
**alert_policy_name** | str,  | str,  | The policy name of alert | [optional] 
**alert_rule_id** | decimal.Decimal, int,  | decimal.Decimal,  | The rule id of alert | [optional] value must be a 64 bit integer
**acknowledged_username** | str,  | str,  | The user&#x27;s email who acknowledged | [optional] 
**floor_id** | decimal.Decimal, int,  | decimal.Decimal,  | The floor id of alert | [optional] value must be a 64 bit integer
**floor_name** | str,  | str,  | The floor name of alert | [optional] 
**building_id** | decimal.Decimal, int,  | decimal.Decimal,  | The buiding id of alert | [optional] value must be a 64 bit integer
**building_name** | str,  | str,  | The building name of alert | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Additional information for the alert

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional information for the alert | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAlertTag**](XiqAlertTag.md) | [**XiqAlertTag**](XiqAlertTag.md) | [**XiqAlertTag**](XiqAlertTag.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

