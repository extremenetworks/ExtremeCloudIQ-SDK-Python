# XiqSmsTemplate

The password or PPSK notification template for user groups.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The SMS template name | 
**description** | **str** | The SMS template description | [optional] 
**predefined** | **bool** | Wheter or not it is a system prefined template | 
**content** | **str** | The SMS template content | [optional] 
**password_type** | [**XiqPasswordType**](XiqPasswordType.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


