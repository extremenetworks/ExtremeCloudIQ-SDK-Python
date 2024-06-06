# XiqDeviceConfigureIpv4Interface

IPv4 Interface model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnetwork** | [**XiqDeviceSubnetworkIpv4**](XiqDeviceSubnetworkIpv4.md) |  | [optional] 
**vlan_attribute** | [**XiqDeviceVlanAttributes**](XiqDeviceVlanAttributes.md) |  | 
**ip_address** | **str** | The IPv4 address set on the interface | 
**ip_address_to_int** | **int** | The IPv4 address set on the interface to numeric format | [optional] 
**routing_instance** | **str** | The Routing Instance | 
**enable_forwarding** | **bool** | Indicates whether or not IPv4 is forwarding on the VLAN | 
**enable_vlan_loopback** | **bool** | Indicates whether or not Vlan Loopback is enabled on the interface | 
**use_ip_addr_as_ospf_router_id** | **bool** | Indicates whether or not to use ip address as ospf router id on the interface | 
**override_dhcp_relay** | **bool** | Indicates whether or not to override DHCP relay on the interface | 
**enable_dhcp** | **bool** | Indicates whether or not to enable DHCP relay on the interface if override DHCP relay is enabled | 
**primary_dhcp_server** | **str** | Primary DHCP Server can be set if DHCP is enabled | 
**secondary_dhcp_server** | **str** | Secondary DHCP Server can be set if DHCP is enabled | 
**predefined** | **bool** | The value is predefined and can not be change | 
**ipv4_interface_id** | **int** | The IPv4 Interface ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


