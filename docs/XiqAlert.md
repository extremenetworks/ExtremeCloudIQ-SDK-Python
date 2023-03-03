# XiqAlert

The Alert Model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier | 
**owner_id** | **int** | The owner ID | [optional] 
**timestamp** | **datetime** | The alert create time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**type** | **str** | The alert type | [optional] 
**summary** | **str** | A high-level, text summary message of the event. Will be used to construct an alert&#39;s description. | [optional] 
**severity** | [**XiqAlertSeverity**](XiqAlertSeverity.md) |  | [optional] 
**category** | [**XiqAlertCategory**](XiqAlertCategory.md) |  | [optional] 
**source** | [**XiqAlertSource**](XiqAlertSource.md) |  | [optional] 
**tags** | **dict(str, str)** | Additional information for the alert | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


