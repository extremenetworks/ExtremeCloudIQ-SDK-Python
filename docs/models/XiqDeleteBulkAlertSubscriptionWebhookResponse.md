# extremecloudiq.model.xiq_delete_bulk_alert_subscription_webhook_response.XiqDeleteBulkAlertSubscriptionWebhookResponse

The result of bulk detele webhook susbscriptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The result of bulk detele webhook susbscriptions | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**result** | [**XiqBulkOperationResult**](XiqBulkOperationResult.md) | [**XiqBulkOperationResult**](XiqBulkOperationResult.md) |  | [optional] 
**reason** | str,  | str,  |  | [optional] 
**[unresolved_deletions](#unresolved_deletions)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# unresolved_deletions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqBulkDeleteWebhookSubscriptionResult**](XiqBulkDeleteWebhookSubscriptionResult.md) | [**XiqBulkDeleteWebhookSubscriptionResult**](XiqBulkDeleteWebhookSubscriptionResult.md) | [**XiqBulkDeleteWebhookSubscriptionResult**](XiqBulkDeleteWebhookSubscriptionResult.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

