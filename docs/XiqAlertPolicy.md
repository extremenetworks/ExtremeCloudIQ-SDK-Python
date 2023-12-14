# XiqAlertPolicy

The Alert Policy Model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**owner_id** | **int** | The owner ID | [optional] 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The name of the alert policy | [optional] 
**sites** | [**list[XiqAlertSite]**](XiqAlertSite.md) | The message metadata type | [optional] 
**event_rules_overview** | [**list[XiqAlertEventRulesByCategory]**](XiqAlertEventRulesByCategory.md) | A list of overviews of the event-based alert rules, grouped by category. | [optional] 
**metric_rules_overview** | [**list[XiqAlertMetricRulesByMetricset]**](XiqAlertMetricRulesByMetricset.md) | A list of overviews of the metric-based alert rules, grouped by metricset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


