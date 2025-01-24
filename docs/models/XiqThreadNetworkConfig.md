# extremecloudiq.model.xiq_thread_network_config.XiqThreadNetworkConfig

The thread network configuration and security policy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The thread network configuration and security policy | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | [optional] value must be a 64 bit integer
**channel** | decimal.Decimal, int,  | decimal.Decimal,  | The network channel | [optional] value must be a 32 bit integer
**channel_mask** | str,  | str,  | The network channel mask | [optional] 
**ext_pan_id** | str,  | str,  | The unique extended pan id | [optional] 
**mesh_local_prefix** | str,  | str,  | The mesh local prefix | [optional] 
**network_key** | str,  | str,  | The thread network key | [optional] 
**network_name** | str,  | str,  | The thread network name | [optional] 
**pan_id** | str,  | str,  | The pan id | [optional] 
**pskc** | str,  | str,  | The Pre-Shared Key for the Commissioner | [optional] 
**obtain_network_key_enabled** | bool,  | BoolClass,  |  | [optional] 
**native_commissioning_enabled** | bool,  | BoolClass,  |  | [optional] 
**routers_enabled** | bool,  | BoolClass,  |  | [optional] 
**external_commissioning_enabled** | bool,  | BoolClass,  |  | [optional] 
**beacons_enabled** | bool,  | BoolClass,  |  | [optional] 
**commercial_commissioning_enabled** | bool,  | BoolClass,  |  | [optional] 
**autonomous_enrollment_enabled** | bool,  | BoolClass,  |  | [optional] 
**network_key_provisioning_enabled** | bool,  | BoolClass,  |  | [optional] 
**non_ccm_routers_enabled** | bool,  | BoolClass,  |  | [optional] 
**active_timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

