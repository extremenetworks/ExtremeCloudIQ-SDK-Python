# extremecloudiq.model.xiq_webhook_subscription.XiqWebhookSubscription

The webhook subscription data model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The webhook subscription data model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**application** | str,  | str,  | The external application name. | 
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**data_type** | [**XiqSubscriptionDataType**](XiqSubscriptionDataType.md) | [**XiqSubscriptionDataType**](XiqSubscriptionDataType.md) |  | 
**message_type** | [**XiqSubscriptionMessageType**](XiqSubscriptionMessageType.md) | [**XiqSubscriptionMessageType**](XiqSubscriptionMessageType.md) |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**secret** | str,  | str,  | The basic auth secret for the webhook endpoint. | 
**url** | str,  | str,  | The webhook endpoint URL. | 
**status** | [**XiqSubscriptionStatus**](XiqSubscriptionStatus.md) | [**XiqSubscriptionStatus**](XiqSubscriptionStatus.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

