# XiqVlanObject

The payload of VLAN common object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The VLAN object ID | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier | [optional] 
**owner_id** | **int** | The owner ID | 
**name** | **str** | The VLAN object name | 
**default_vlan_id** | **int** | The default VLAN ID | 
**enable_classification** | **bool** | If apply VLANs to devices using classification | [optional] 
**classified_entries** | [**list[XiqVlanObjectClassifiedEntry]**](XiqVlanObjectClassifiedEntry.md) | The VLAN object classified entries | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


