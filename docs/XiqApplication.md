# XiqApplication

The Application Model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The application name | [optional] 
**description** | **str** | The application description | [optional] 
**predefined** | **bool** | Flag to describle whether the application is predefined or customized | [optional] 
**category_id** | **int** | The category ID of application | [optional] 
**category_name** | **str** | The category name of application | [optional] 
**detection_rules** | [**list[XiqApplicationDetectionRule]**](XiqApplicationDetectionRule.md) | The application detection rules | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


