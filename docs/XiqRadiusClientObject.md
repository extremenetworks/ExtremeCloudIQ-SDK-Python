# XiqRadiusClientObject

The RADIUS client object configuration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**name** | **str** | The RADIUS client object name. | 
**description** | **str** | The RADIUS client object description. | [optional] 
**enable_inject_operator_name_attribute** | **bool** | The flag for enable inject operator name attribute. | 
**enable_message_authenticator_attribute** | **bool** | The flag for enable message authenticator attribute | 
**enable_permit_dynamic_authorization_message_change** | **bool** | The flag for enable permit dynamic authorization message change | 
**retry_interval** | **int** | The retry interval, 60 - 100000000 seconds | 
**accounting_interim_update_interval** | **int** | The accounting interim update interval, 60 - 100000000 seconds | 
**entries** | [**list[XiqRadiusClientObjectEntry]**](XiqRadiusClientObjectEntry.md) | The list of RADIUS client object entries | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


