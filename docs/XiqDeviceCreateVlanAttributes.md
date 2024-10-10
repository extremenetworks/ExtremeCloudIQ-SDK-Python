# XiqDeviceCreateVlanAttributes

Vlan Attribute model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the vlan | [optional] 
**dhcp_snooping_enabled** | **bool** | Whether dhcp snooping is enabled on this vlan | [optional] 
**dhcp_snooping_action** | [**XiqDeviceVlanAttributesDhcpSnoopingAction**](XiqDeviceVlanAttributesDhcpSnoopingAction.md) |  | [optional] 
**igmp_snooping_enabled** | **bool** | Whether igmp snooping is enabled on this vlan | [optional] 
**immediate_leave** | **bool** | When enabled, the multicast host is removed immediately if it leaves the group | [optional] 
**always_create** | **bool** | Should the vlan be created irrespective of port bindings | [optional] 
**vlan_obj** | [**XiqVlanObject**](XiqVlanObject.md) |  | [optional] 
**vlan_id** | **int** | Id of the vlan | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


