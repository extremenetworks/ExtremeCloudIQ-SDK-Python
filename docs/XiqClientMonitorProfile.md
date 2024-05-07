# XiqClientMonitorProfile

The payload of client monitor profile
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The client monitor profile name | 
**description** | **str** | The client monitor profile description | [optional] 
**predefined** | **bool** | Whether the client monitor profile is predefined or user-customized. | 
**association** | [**XiqClientMonitorParameters**](XiqClientMonitorParameters.md) |  | [optional] 
**authentication** | [**XiqClientMonitorParameters**](XiqClientMonitorParameters.md) |  | [optional] 
**networking** | [**XiqClientMonitorParameters**](XiqClientMonitorParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


