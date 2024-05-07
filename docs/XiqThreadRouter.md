# XiqThreadRouter

The Thread Router associate to ExtremeCloud IQ device
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**org_id** | **int** | The organization identifier, valid when enabling HIQ feature | [optional] 
**owner_id** | **int** | The owner id | [optional] 
**device_id** | **int** | The device unique identifier | [optional] 
**serial_number** | **str** | The device serial number | [optional] 
**eui64** | **str** | The Extended Unique Identifier | [optional] 
**ext_mac** | **str** | The Extended Mac Address | [optional] 
**rloc16** | **str** | The router RLOC16 | [optional] 
**global_ipv6** | **str** | The global IPv6 address | [optional] 
**tx_power** | **int** | The transmit power | [optional] 
**region** | **str** | The device region | [optional] 
**thread_platform** | **str** | The thread platform | [optional] 
**device_role** | **str** | The thread device role/state | [optional] 
**router_interface** | [**XiqThreadNetworkInterface**](XiqThreadNetworkInterface.md) |  | [optional] 
**veth0** | [**XiqThreadNetworkInterface**](XiqThreadNetworkInterface.md) |  | [optional] 
**network_data** | [**XiqThreadNetworkData**](XiqThreadNetworkData.md) |  | [optional] 
**thread_mle_link_mode** | [**XiqThreadMleLinkMode**](XiqThreadMleLinkMode.md) |  | [optional] 
**thread_version** | [**XiqThreadVersion**](XiqThreadVersion.md) |  | [optional] 
**leader_service** | [**XiqThreadLeaderService**](XiqThreadLeaderService.md) |  | [optional] 
**border_router_service** | [**XiqThreadBorderRouterService**](XiqThreadBorderRouterService.md) |  | [optional] 
**backbone_border_router_service** | [**XiqThreadBackboneBorderRouterService**](XiqThreadBackboneBorderRouterService.md) |  | [optional] 
**border_agent_service** | [**XiqThreadBorderAgentService**](XiqThreadBorderAgentService.md) |  | [optional] 
**commissioner_service** | [**XiqThreadCommissionerService**](XiqThreadCommissionerService.md) |  | [optional] 
**nat64_service** | [**XiqThreadNat64Service**](XiqThreadNat64Service.md) |  | [optional] 
**network_config** | [**XiqThreadNetworkConfig**](XiqThreadNetworkConfig.md) |  | [optional] 
**active_clients** | **int** | The count of active connected clients | [optional] 
**hostname** | **str** | The device hostname | [optional] 
**last_reported** | **datetime** | The last reported datetime | [optional] 
**thread_connected** | **bool** | Is router connected to thread network | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


