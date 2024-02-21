# XiqDeviceMonitorVlanAttributesInfo

The VLAN attributes info that are monitored per VLAN on the device
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | The VLAN ID | 
**vlan_name** | **str** | The VLAN Name | [optional] 
**active_ports** | **list[str]** | The active ports in the VLAN | [optional] 
**stp_instance** | **str** | The STP instance name for the VLAN | [optional] 
**stp_enabled** | **bool** | Indicates whether or not STP is enabled or disabled on the VLAN | [optional] 
**igmp_snooping_enabled** | **bool** | Indicates whether or not IGMP Snooping is enabled or disabled on the VLAN | [optional] 
**dhcp_snooping_enabled** | **bool** | Indicates whether or not DCHP Snooping is enabled or disabled on the VLAN | [optional] 
**vrf_name** | **str** | The name of the VRF for the VLAN | [optional] 
**dynamic_enabled** | **bool** | Indicates whether or not this is a Dynamic VLAN | [optional] 
**member_ports** | **list[str]** | The member ports in the VLAN | [optional] 
**tagged_ports** | **list[str]** | The tagged ports in the VLAN | [optional] 
**untagged_ports** | **list[str]** | The untagged ports in the VLAN | [optional] 
**dynamic_ports** | **list[str]** | The dynamic ports in the VLAN | [optional] 
**non_forwarding_vlan_enabled** | **bool** | Indicates whether or not this is a Non Forwarding VLAN (learning VLAN) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


