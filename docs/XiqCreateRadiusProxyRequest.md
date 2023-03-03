# XiqCreateRadiusProxyRequest

The payload to create a new RADIUS proxy
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The RADIUS proxy name | 
**description** | **str** | The RADIUS proxy description | [optional] 
**format_type** | [**XiqRadiusProxyFormatType**](XiqRadiusProxyFormatType.md) |  | 
**retry_count** | **int** | The retry count of RADIUS proxy | 
**retry_delay** | **int** | The retry delay of RADIUS proxy | 
**dead_time** | **int** | The dead time of RADIUS proxy | 
**enable_inject_operator_name_attribute** | **bool** | The flag for enable inject operator name attribute | [optional] 
**clients** | [**list[XiqCreateRadiusClient]**](XiqCreateRadiusClient.md) | The RADIUS clients of RADIUS proxy | [optional] 
**realms** | [**list[XiqCreateRadiusProxyRealm]**](XiqCreateRadiusProxyRealm.md) | The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name &#39;DEFAULT&#39; and &#39;NULL&#39; | 
**device_ids** | **list[int]** | The device IDS to assign RADIUS proxy | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


