# XiqDeviceMonitorVlanIpv4InterfacesDetails

The VLAN IPv4 Interfaces info that are monitored per VLAN on the device
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | The VLAN ID | 
**vlan_name** | **str** | The VLAN Name | [optional] 
**ipv4_forwarding_enabled** | **bool** | Indication of IPv4 Forwarding status on the VLAN | [optional] 
**routing_instance** | **str** | The Routing instance name where the IPv4 Interface is configured for this VLAN | [optional] 
**ipv4_address** | **str** | The IPv4 Address of the interface | [optional] 
**ipv4_subnet** | **str** | The IPv4 Subnet of the interface | [optional] 
**member_ports** | **list[str]** | The member ports in the VLAN | [optional] 
**tagged_ports** | **list[str]** | The tagged ports in the VLAN | [optional] 
**untagged_ports** | **list[str]** | The untagged ports in the VLAN | [optional] 
**non_forwarding_vlan_enabled** | **bool** | Indicates whether or not this is a Non Forwarding VLAN (learning VLAN) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


