# XiqWildcardHostNameAddressProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**predefined** | **bool** | Flag to describe whether the application is predefined or customised | [optional] 
**name** | **str** | Address profile name | 
**description** | **str** | Address profile description | [optional] 
**value** | **str** | Address profile value | [optional] 
**enable_classification** | **bool** | The flag to enable classification on L3 address profile | [optional] 
**address_type** | [**XiqL3AddressType**](XiqL3AddressType.md) |  | 
**classified_entries** | [**list[XiqAddressProfileClassifiedEntry]**](XiqAddressProfileClassifiedEntry.md) | The address profile classified entries | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


