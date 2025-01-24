# extremecloudiq.model.xiq_alert_rule_overview.XiqAlertRuleOverview

The Alert Rule Overview Model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Alert Rule Overview Model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The human-readable name of this rule. Corresponds to the message_metadata_name from the get alert rule details API. | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier of rule. | value must be a 64 bit integer
**enabled** | bool,  | BoolClass,  | Indicates whether this rule is in effect. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

