# XiqVlanProfile

The payload of common object - VLAN profile
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**name** | **str** | The VLAN profile name | 
**default_vlan_id** | **int** | The default VLAN ID | 
**enable_classification** | **bool** | If apply VLANs to devices using classification | 
**classified_entries** | [**list[XiqVlanObjectClassifiedEntry]**](XiqVlanObjectClassifiedEntry.md) | The VLAN object classified entries | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


