# extremecloudiq.model.xiq_patch_alert_service_now_subscription_request.XiqPatchAlertServiceNowSubscriptionRequest

The payload of ServiceNow subscription.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of ServiceNow subscription. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**servicenow_account_email** | str,  | str,  | The servicenow email address. | [optional] 
**is_enabled** | bool,  | BoolClass,  | Enable/disable servicenow notification. | [optional] 
**is_subscribe_all** | bool,  | BoolClass,  | The all alert policy selected flag. | [optional] 
**[alert_policy_ids](#alert_policy_ids)** | list, tuple,  | tuple,  | The selected alert policy list. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# alert_policy_ids

The selected alert policy list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The selected alert policy list. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The selected alert policy list. | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

