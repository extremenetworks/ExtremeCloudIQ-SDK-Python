# extremecloudiq.model.xiq_thread_router.XiqThreadRouter

The Thread Router associate to ExtremeCloud IQ device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Thread Router associate to ExtremeCloud IQ device | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**owner_id** | decimal.Decimal, int,  | decimal.Decimal,  | The owner id | [optional] value must be a 64 bit integer
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device unique identifier | [optional] value must be a 64 bit integer
**serial_number** | str,  | str,  | The device serial number | [optional] 
**eui64** | str,  | str,  | The Extended Unique Identifier | [optional] 
**ext_mac** | str,  | str,  | The Extended Mac Address | [optional] 
**rloc16** | str,  | str,  | The router RLOC16 | [optional] 
**global_ipv6** | str,  | str,  | The global IPv6 address | [optional] 
**tx_power** | decimal.Decimal, int,  | decimal.Decimal,  | The transmit power | [optional] value must be a 32 bit integer
**region** | str,  | str,  | The device region | [optional] 
**thread_platform** | str,  | str,  | The thread platform | [optional] 
**device_role** | str,  | str,  | The thread device role/state | [optional] 
**router_interface** | [**XiqThreadNetworkInterface**](XiqThreadNetworkInterface.md) | [**XiqThreadNetworkInterface**](XiqThreadNetworkInterface.md) |  | [optional] 
**veth0** | [**XiqThreadNetworkInterface**](XiqThreadNetworkInterface.md) | [**XiqThreadNetworkInterface**](XiqThreadNetworkInterface.md) |  | [optional] 
**network_data** | [**XiqThreadNetworkData**](XiqThreadNetworkData.md) | [**XiqThreadNetworkData**](XiqThreadNetworkData.md) |  | [optional] 
**thread_mle_link_mode** | [**XiqThreadMleLinkMode**](XiqThreadMleLinkMode.md) | [**XiqThreadMleLinkMode**](XiqThreadMleLinkMode.md) |  | [optional] 
**thread_version** | [**XiqThreadVersion**](XiqThreadVersion.md) | [**XiqThreadVersion**](XiqThreadVersion.md) |  | [optional] 
**leader_service** | [**XiqThreadLeaderService**](XiqThreadLeaderService.md) | [**XiqThreadLeaderService**](XiqThreadLeaderService.md) |  | [optional] 
**border_router_service** | [**XiqThreadBorderRouterService**](XiqThreadBorderRouterService.md) | [**XiqThreadBorderRouterService**](XiqThreadBorderRouterService.md) |  | [optional] 
**backbone_border_router_service** | [**XiqThreadBackboneBorderRouterService**](XiqThreadBackboneBorderRouterService.md) | [**XiqThreadBackboneBorderRouterService**](XiqThreadBackboneBorderRouterService.md) |  | [optional] 
**border_agent_service** | [**XiqThreadBorderAgentService**](XiqThreadBorderAgentService.md) | [**XiqThreadBorderAgentService**](XiqThreadBorderAgentService.md) |  | [optional] 
**commissioner_service** | [**XiqThreadCommissionerService**](XiqThreadCommissionerService.md) | [**XiqThreadCommissionerService**](XiqThreadCommissionerService.md) |  | [optional] 
**nat64_service** | [**XiqThreadNat64Service**](XiqThreadNat64Service.md) | [**XiqThreadNat64Service**](XiqThreadNat64Service.md) |  | [optional] 
**network_config** | [**XiqThreadNetworkConfig**](XiqThreadNetworkConfig.md) | [**XiqThreadNetworkConfig**](XiqThreadNetworkConfig.md) |  | [optional] 
**active_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The count of active connected clients | [optional] value must be a 32 bit integer
**hostname** | str,  | str,  | The device hostname | [optional] 
**last_reported** | str, datetime,  | str,  | The last reported datetime | [optional] value must conform to RFC-3339 date-time
**thread_connected** | bool,  | BoolClass,  | Is router connected to thread network | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

