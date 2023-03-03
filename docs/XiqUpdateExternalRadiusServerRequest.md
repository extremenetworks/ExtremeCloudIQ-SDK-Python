# XiqUpdateExternalRadiusServerRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The external RADIUS server name | 
**shared_secret** | **str** | The shared secret for the external RADIUS server (optional) | [optional] 
**authentication_port** | **int** | The authentication port for the external RADIUS server (1 ~ 65535) | [default to 1812]
**accounting_port** | **int** | The accounting port for the external RADIUS server (1 ~ 65535) | [default to 1813]
**server_type** | [**XiqRadiusServerType**](XiqRadiusServerType.md) |  | 
**ip_addr** | **str** | The IP address or hostname of the RADIUS server | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


