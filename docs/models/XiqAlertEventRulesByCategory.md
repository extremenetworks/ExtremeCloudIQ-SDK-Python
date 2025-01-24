# extremecloudiq.model.xiq_alert_event_rules_by_category.XiqAlertEventRulesByCategory

The Alert Event Rule Model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Alert Event Rule Model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**category_name** | str,  | str,  | The category name of category | 
**category_id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier of category ID. | value must be a 64 bit integer
**[rules](#rules)** | list, tuple,  | tuple,  | A list of overviews of the event-based alert rules, grouped by event. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rules

A list of overviews of the event-based alert rules, grouped by event.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of overviews of the event-based alert rules, grouped by event. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAlertRuleOverview**](XiqAlertRuleOverview.md) | [**XiqAlertRuleOverview**](XiqAlertRuleOverview.md) | [**XiqAlertRuleOverview**](XiqAlertRuleOverview.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

