# extremecloudiq.model.xiq_update_alert_rule_request.XiqUpdateAlertRuleRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  | This is a description for the alert rule. | [optional] 
**severity_id** | decimal.Decimal, int,  | decimal.Decimal,  | The severity identifier. The currently supported severity IDs are 1 for critical, 2 for warning, and 3 for info. | [optional] value must be a 64 bit integer
**trigger_type** | str,  | str,  | The configured trigger type of the rule. | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Has value when trigger_type is \&quot;DEFERRED\&quot;. The deferred duration, in seconds. | [optional] value must be a 32 bit integer
**time_window** | decimal.Decimal, int,  | decimal.Decimal,  | Has value when trigger_type is \&quot;REPEATED\&quot;. The time window to count the number of repeated messages, in seconds. | [optional] value must be a 32 bit integer
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Has value when trigger_type is \&quot;REPEATED\&quot;. The lower bound of the number of messages required to trigger this rule. | [optional] value must be a 32 bit integer
**threshold** | decimal.Decimal, int, float,  | decimal.Decimal,  | Has value when type is \&quot;METRIC\&quot;. The threshold for the message. | [optional] value must be a 64 bit float
**operator** | str,  | str,  | Has value when message_metadata_type is \&quot;METRIC\&quot;. The operator to compare against the threshold. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

