# extremecloudiq.model.xiq_tunnel_concentrator_request.XiqTunnelConcentratorRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**primary_bridging_interface** | decimal.Decimal, int,  | decimal.Decimal,  | Primary Bridging Interface ID. | value must be a 32 bit integer
**primary_vlan** | decimal.Decimal, int,  | decimal.Decimal,  | The VLAN ID for the primary listening interface | value must be a 32 bit integer
**tunnel_address** | str,  | str,  | IP address/CIDR of listening interface. | 
**name** | str,  | str,  |  The Tunnel Concentrator Service name | 
**description** | str,  | str,  |  The Tunnel Concentrator Service description | 
**native_vlan** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies which VLAN ID is transmitted untagged on the bridged interface. | value must be a 32 bit integer
**primary_listening_interface** | decimal.Decimal, int,  | decimal.Decimal,  | Primary Listening Interface ID. | value must be a 32 bit integer
**primary_tagged** | bool,  | BoolClass,  | Indicates if primary VLAN is tagged. | 
**primary_tc** | decimal.Decimal, int,  | decimal.Decimal,  |  The Primary Tunnel Concentrator device ID | value must be a 64 bit integer
**redundant** | bool,  | BoolClass,  | Indicates if redundant Tunnel Concentrators (primary and backup) are configured  | [optional] 
**backup_tc** | decimal.Decimal, int,  | decimal.Decimal,  | The Backup Tunnel Concentrator device ID | [optional] value must be a 64 bit integer
**backup_listening_interface** | decimal.Decimal, int,  | decimal.Decimal,  | Backup Listening Interface ID. | [optional] value must be a 32 bit integer
**backup_bridging_interface** | decimal.Decimal, int,  | decimal.Decimal,  | Backup Bridging Interface ID. | [optional] value must be a 32 bit integer
**primary_ip** | str,  | str,  | The primary IP address of network interface for accepting connections from APs (listening interface). | [optional] 
**backup_ip** | str,  | str,  | The backup IP address of network interface for accepting connections from APs (listening interface) | [optional] 
**backup_vlan** | decimal.Decimal, int,  | decimal.Decimal,  | The VLAN ID for the backup listening interface | [optional] value must be a 32 bit integer
**backup_tagged** | bool,  | BoolClass,  | Indicates if backup VLAN is tagged | [optional] 
**router_id** | decimal.Decimal, int,  | decimal.Decimal,  | Virtual Router group ID | [optional] value must be a 32 bit integer
**gateway** | str,  | str,  | The TunnelConcentrator optional gateway ip address | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

