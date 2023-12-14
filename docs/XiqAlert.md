# XiqAlert

The Alert Model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier | 
**owner_id** | **int** | The owner ID | [optional] 
**timestamp** | **datetime** | The alert create time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**message_metadata_id** | **int** | The message metadata id | [optional] 
**message_metadata_type** | **str** | The message metadata type | [optional] 
**summary** | **str** | A high-level, text summary message of the event. Will be used to construct an alert&#39;s description. | [optional] 
**severity_name** | **str** | The severity name of the alert | [optional] 
**category_name** | **str** | The alert category name | [optional] 
**severity_id** | **int** | The severity Id of the alert | [optional] 
**category_id** | **int** | The alert category Id | [optional] 
**source** | [**XiqAlertSource**](XiqAlertSource.md) |  | [optional] 
**tags** | [**list[XiqAlertTag]**](XiqAlertTag.md) | Additional information for the alert | 
**acknowledged** | **bool** | The acknowledged status of alert | [optional] 
**site_id** | **int** | The site id of alert | [optional] 
**site_name** | **str** | The site name of alert | [optional] 
**alert_policy_id** | **int** | The policy id of alert | [optional] 
**alert_policy_name** | **str** | The policy name of alert | [optional] 
**alert_rule_id** | **int** | The rule id of alert | [optional] 
**acknowledged_username** | **str** | The user&#39;s email who acknowledged | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


