# XiqTunnelConcentrator

The payload of Tunnel Concentrator
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**name** | **str** |  The Tunnel Concentrator Service name | 
**description** | **str** |  The Tunnel Concentrator Service description | 
**redundant** | **bool** | Indicates if redundant Tunnel Concentrators (primary and backup) are configured  | [optional] 
**primary_tc** | **int** |  The Primary Tunnel Concentrator device ID | 
**backup_tc** | **int** | The Backup Tunnel Concentrator device ID | [optional] 
**primary_listening_interface** | **int** | Primary Listening Interface ID. | 
**backup_listening_interface** | **int** | Backup Listening Interface ID. | [optional] 
**primary_bridging_interface** | **int** | Primary Bridging Interface ID. | 
**backup_bridging_interface** | **int** | Backup Bridging Interface ID. | [optional] 
**primary_ip** | **str** | The primary IP address of network interface for accepting connections from APs (listening interface). | [optional] 
**backup_ip** | **str** | The backup IP address of network interface for accepting connections from APs (listening interface) | [optional] 
**primary_vlan** | **int** | The VLAN ID for the primary listening interface | 
**backup_vlan** | **int** | The VLAN ID for the backup listening interface | [optional] 
**primary_tagged** | **bool** | Indicates if primary VLAN is tagged. | 
**backup_tagged** | **bool** | Indicates if backup VLAN is tagged | [optional] 
**tunnel_address** | **str** | IP address/CIDR of listening interface. | 
**router_id** | **int** | Virtual Router group ID | [optional] 
**gateway** | **str** | The TunnelConcentrator optional gateway ip address | [optional] 
**native_vlan** | **int** | Specifies which VLAN ID is transmitted untagged on the bridged interface. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


