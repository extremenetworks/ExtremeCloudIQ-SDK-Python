# XiqUpdateAlertRuleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | This is a description for the alert rule. | [optional] 
**severity_id** | **int** | The severity identifier. The currently supported severity IDs are 1 for critical, 2 for warning, and 3 for info. | [optional] 
**trigger_type** | **str** | The configured trigger type of the rule. | [optional] 
**duration** | **int** | Has value when trigger_type is \&quot;DEFERRED\&quot;. The deferred duration, in seconds. | [optional] 
**time_window** | **int** | Has value when trigger_type is \&quot;REPEATED\&quot;. The time window to count the number of repeated messages, in seconds. | [optional] 
**count** | **int** | Has value when trigger_type is \&quot;REPEATED\&quot;. The lower bound of the number of messages required to trigger this rule. | [optional] 
**threshold** | **float** | Has value when type is \&quot;METRIC\&quot;. The threshold for the message. | [optional] 
**operator** | **str** | Has value when message_metadata_type is \&quot;METRIC\&quot;. The operator to compare against the threshold. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


