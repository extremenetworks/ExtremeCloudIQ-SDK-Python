# XiqWebhookSubscription

The webhook subscription data model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**application** | **str** | The external application name. | 
**url** | **str** | The webhook endpoint URL. | 
**secret** | **str** | The basic auth secret for the webhook endpoint. | 
**data_type** | [**XiqSubscriptionDataType**](XiqSubscriptionDataType.md) |  | 
**message_type** | [**XiqSubscriptionMessageType**](XiqSubscriptionMessageType.md) |  | 
**status** | [**XiqSubscriptionStatus**](XiqSubscriptionStatus.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


