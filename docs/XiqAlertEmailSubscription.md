# XiqAlertEmailSubscription

The alert email subscription data model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**email** | **str** | The email address. | 
**is_enabled** | **bool** | Enable/disable alert notifications for an email. | 
**is_email_verified** | **bool** | The email address verified flag. | 
**is_subscribe_all** | **bool** | The all alert policy selected flag. | 
**alert_policy_ids** | **list[int]** | The selected alert policy list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


