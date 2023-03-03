# XiqRadiusProxy

The configuration of RADIUS proxy
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The RADIUS proxy name | [optional] 
**description** | **str** | The RADIUS proxy description | [optional] 
**format_type** | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) |  | [optional] 
**retry_count** | **int** | The retry count of RADIUS proxy | [optional] 
**retry_delay** | **int** | The retry delay of RADIUS proxy | [optional] 
**dead_time** | **int** | The dead time of RADIUS proxy | [optional] 
**enable_inject_operator_name_attribute** | **bool** | The flag for enable inject operator name attribute | [optional] 
**clients** | [**list[XiqRadiusClient]**](XiqRadiusClient.md) | The RADIUS clients of RADIUS proxy | [optional] 
**realms** | [**list[XiqRadiusProxyRealm]**](XiqRadiusProxyRealm.md) | The RADIUS realms of RADIUS proxy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


