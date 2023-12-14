# XiqAlertRule

The state for a configured alert rule
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**message_metadata_id** | **int** | The identifier for the unique message type that corresponds to this rule. | 
**message_metadata_name** | **str** | The display name for the message. | [optional] 
**message_metadata_type** | **str** | The type of the message. | [optional] 
**description** | **str** | This is a description for the alert rule. | [optional] 
**severity_id** | **int** | The severity identifier. The currently supported severity IDs are 1 for critical, 2 for warning, and 3 for info. | 
**severity_name** | **str** | The display name for the alert severity. | [optional] 
**is_enabled** | **bool** | True if this rule is active and enabled. | 
**trigger_type** | **str** | The configured trigger type of the rule. | 
**duration** | **int** | Has value when trigger_type is \&quot;DEFERRED\&quot;. The deferred duration, in seconds. | [optional] 
**time_window** | **int** | Has value when trigger_type is \&quot;REPEATED\&quot;. The time window to count the number of repeated messages, in seconds. | [optional] 
**count** | **int** | Has value when trigger_type is \&quot;REPEATED\&quot;. The lower bound of the number of messages required to trigger this rule. | [optional] 
**threshold** | **float** | Has value when type is \&quot;METRIC\&quot;. The threshold for the message. | [optional] 
**unit** | **str** | The unit of this threshold | [optional] 
**operator** | **str** | Has value when message_metadata_type is \&quot;METRIC\&quot;. The operator to compare against the threshold. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


