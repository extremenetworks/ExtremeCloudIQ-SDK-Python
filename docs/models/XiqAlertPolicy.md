# extremecloudiq.model.xiq_alert_policy.XiqAlertPolicy

The Alert Policy Model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Alert Policy Model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The owner ID | [optional] value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The name of the alert policy | [optional] 
**[sites](#sites)** | list, tuple,  | tuple,  | The message metadata type | [optional] 
**[event_rules_overview](#event_rules_overview)** | list, tuple,  | tuple,  | A list of overviews of the event-based alert rules, grouped by category. | [optional] 
**[metric_rules_overview](#metric_rules_overview)** | list, tuple,  | tuple,  | A list of overviews of the metric-based alert rules, grouped by metricset. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sites

The message metadata type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The message metadata type | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAlertSite**](XiqAlertSite.md) | [**XiqAlertSite**](XiqAlertSite.md) | [**XiqAlertSite**](XiqAlertSite.md) |  | 

# event_rules_overview

A list of overviews of the event-based alert rules, grouped by category.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of overviews of the event-based alert rules, grouped by category. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAlertEventRulesByCategory**](XiqAlertEventRulesByCategory.md) | [**XiqAlertEventRulesByCategory**](XiqAlertEventRulesByCategory.md) | [**XiqAlertEventRulesByCategory**](XiqAlertEventRulesByCategory.md) |  | 

# metric_rules_overview

A list of overviews of the metric-based alert rules, grouped by metricset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of overviews of the metric-based alert rules, grouped by metricset. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAlertMetricRulesByMetricset**](XiqAlertMetricRulesByMetricset.md) | [**XiqAlertMetricRulesByMetricset**](XiqAlertMetricRulesByMetricset.md) | [**XiqAlertMetricRulesByMetricset**](XiqAlertMetricRulesByMetricset.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

