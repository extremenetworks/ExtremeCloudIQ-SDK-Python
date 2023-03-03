# XiqExternalRadiusServer

The configuration of external RADIUS server object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The external RADIUS server name | 
**shared_secret** | **str** | The shared secret for the external RADIUS server (optional) | [optional] 
**authentication_port** | **int** | The authentication port for the external RADIUS server (1 ~ 65535) | 
**accounting_port** | **int** | The accounting port for the external RADIUS server (1 ~ 65535) | 
**server_type** | [**XiqRadiusServerType**](XiqRadiusServerType.md) |  | 
**ip_address** | **str** | The ip address or hostname of the RADIUS server | 
**enable_a3** | **bool** | Indicates whether this is an Extreme A3 RADIUS server or not, cannot be updated after creation. Please set it to false if it is not an Extreme A3 RADIUS server. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


