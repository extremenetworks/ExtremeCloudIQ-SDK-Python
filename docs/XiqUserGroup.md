# XiqUserGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The user group name | 
**description** | **str** | The user group description | [optional] 
**predefined** | **bool** | Whether it is predefined | 
**password_db_location** | [**XiqPasswordDbLocation**](XiqPasswordDbLocation.md) |  | 
**password_type** | [**XiqPasswordType**](XiqPasswordType.md) |  | 
**pcg_use_only** | **bool** |  Whether it&#39;s for PCG use only | [optional] 
**pcg_type** | [**XiqPcgType**](XiqPcgType.md) |  | [optional] 
**ppsk_use_only** | **bool** | Whether it&#39;s for PPSK use only | [optional] 
**enable_cwp_reg** | **bool** | Whether to enable CWP registration setting | [optional] 
**password_settings** | [**XiqPasswordSettings**](XiqPasswordSettings.md) |  | 
**expiration_settings** | [**XiqExpirationSettings**](XiqExpirationSettings.md) |  | 
**delivery_settings** | [**XiqDeliverySettings**](XiqDeliverySettings.md) |  | 
**user_count** | **int** | The user count | 
**ssids** | **list[str]** | The ssids | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


