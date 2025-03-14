# extremecloudiq.model.xiq_update_webhook_subscription_request.XiqUpdateWebhookSubscriptionRequest

The payload to update webhook subscription

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload to update webhook subscription | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**application** | str,  | str,  | The external application name. | 
**message_type** | [**XiqSubscriptionMessageType**](XiqSubscriptionMessageType.md) | [**XiqSubscriptionMessageType**](XiqSubscriptionMessageType.md) |  | 
**url** | str,  | str,  | The webhook endpoint URL. | 
**status** | [**XiqSubscriptionStatus**](XiqSubscriptionStatus.md) | [**XiqSubscriptionStatus**](XiqSubscriptionStatus.md) |  | 
**secret** | str,  | str,  | The basic auth secret for the webhook endpoint. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

