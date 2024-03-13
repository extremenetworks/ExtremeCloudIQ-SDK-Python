# XiqDeviceSubnetworkIpv4

The IPv4 Subnetwork Interface that is configured on the device.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The IPv4 Subnetwork ID | 
**name** | **str** | Subnetwork name | 
**description** | **str** | Subnetwork description | [optional] 
**ip_addr_space** | **str** | Subnetwork Ipv4 address | 
**gateway_ip_type** | [**XiqGatewayIpType**](XiqGatewayIpType.md) |  | 
**vlan_profile** | **str** | The VLAN ID | 
**enable_dhcp** | **bool** | Enable DHCP relay server | 
**dhcp_relay** | [**XiqDeviceDhcpRelay**](XiqDeviceDhcpRelay.md) |  | [optional] 
**clients_number** | **int** | Number of clients available for subnetwork | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


