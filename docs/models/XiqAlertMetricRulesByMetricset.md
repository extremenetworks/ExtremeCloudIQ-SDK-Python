# extremecloudiq.model.xiq_alert_metric_rules_by_metricset.XiqAlertMetricRulesByMetricset

The Alert Metric Rule Model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Alert Metric Rule Model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metricset_name** | str,  | str,  | The human-readable name of the metricset. | 
**[rules](#rules)** | list, tuple,  | tuple,  | A list of overviews of the metric-based alert rules, grouped by metricset. | 
**metricset_id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier of the metricset. | value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rules

A list of overviews of the metric-based alert rules, grouped by metricset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of overviews of the metric-based alert rules, grouped by metricset. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAlertRuleOverview**](XiqAlertRuleOverview.md) | [**XiqAlertRuleOverview**](XiqAlertRuleOverview.md) | [**XiqAlertRuleOverview**](XiqAlertRuleOverview.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

