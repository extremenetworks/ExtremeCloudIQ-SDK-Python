# extremecloudiq.model.xiq_hotspot_profile.XiqHotspotProfile

The payload of Hotspot profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of Hotspot profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**domain_name** | str,  | str,  | The domain name of the entity or organization operating the IEEE 802.11 access network. | 
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The Hotspot profile name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**hessid** | str,  | str,  | Homogenous Extended Service Set Identifier (HESSID) for a Hotspot 2.0 network. | [optional] 
**[operator_names](#operator_names)** | list, tuple,  | tuple,  | Localized names for the Hotspot operator. | [optional] 
**venue** | [**XiqHotspotVenue**](XiqHotspotVenue.md) | [**XiqHotspotVenue**](XiqHotspotVenue.md) |  | [optional] 
**access_network_type** | [**XiqHotspotAccessNetworkType**](XiqHotspotAccessNetworkType.md) | [**XiqHotspotAccessNetworkType**](XiqHotspotAccessNetworkType.md) |  | [optional] 
**dgaf** | bool,  | BoolClass,  | Downstream Group Address Forwarding (DGAF). Forward all downlink wireless broadcast ARP and multicast packets. | [optional] 
**ipv4_availability** | [**XiqHotspotIpv4AvailabilityType**](XiqHotspotIpv4AvailabilityType.md) | [**XiqHotspotIpv4AvailabilityType**](XiqHotspotIpv4AvailabilityType.md) |  | [optional] 
**ipv6_availability** | [**XiqHotspotIpv6AvailabilityType**](XiqHotspotIpv6AvailabilityType.md) | [**XiqHotspotIpv6AvailabilityType**](XiqHotspotIpv6AvailabilityType.md) |  | [optional] 
**wan_metrics** | [**XiqHotspotWanMetrics**](XiqHotspotWanMetrics.md) | [**XiqHotspotWanMetrics**](XiqHotspotWanMetrics.md) |  | [optional] 
**[connection_capabilities](#connection_capabilities)** | list, tuple,  | tuple,  | The connection capability informs client devices about available network services. | [optional] 
**qos_map** | [**XiqHotspotQosMap**](XiqHotspotQosMap.md) | [**XiqHotspotQosMap**](XiqHotspotQosMap.md) |  | [optional] 
**gas_comeback_delay** | decimal.Decimal, int,  | decimal.Decimal,  | Generic Advertisement Service (GAS) comeback message delay time. The unit is Time Unit (TU) 1 TU &#x3D; 1024 microseconds. When GAS delay is 0, there is no delay. | [optional] value must be a 32 bit integer
**anqp_domain_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Access Network Query protocol (ANQP) domain ID. | [optional] value must be a 32 bit integer
**online_signup** | [**XiqHotspotOnlineSignup**](XiqHotspotOnlineSignup.md) | [**XiqHotspotOnlineSignup**](XiqHotspotOnlineSignup.md) |  | [optional] 
**[nai_realms](#nai_realms)** | list, tuple,  | tuple,  | The list of Network Access Identification (NAI) realms. | [optional] 
**[roaming_consortiums](#roaming_consortiums)** | list, tuple,  | tuple,  | The list of Roaming Consortium network providers. | [optional] 
**[cellular_networks](#cellular_networks)** | list, tuple,  | tuple,  | List of 3rd Generation Partnership Project (3GPP) cellular networks. | [optional] 
**[service_providers](#service_providers)** | list, tuple,  | tuple,  | The list of supported hotspot service providers. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# operator_names

Localized names for the Hotspot operator.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Localized names for the Hotspot operator. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) | [**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) | [**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) |  | 

# connection_capabilities

The connection capability informs client devices about available network services.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The connection capability informs client devices about available network services. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotConnectionCapability**](XiqHotspotConnectionCapability.md) | [**XiqHotspotConnectionCapability**](XiqHotspotConnectionCapability.md) | [**XiqHotspotConnectionCapability**](XiqHotspotConnectionCapability.md) |  | 

# nai_realms

The list of Network Access Identification (NAI) realms.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of Network Access Identification (NAI) realms. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotNaiRealm**](XiqHotspotNaiRealm.md) | [**XiqHotspotNaiRealm**](XiqHotspotNaiRealm.md) | [**XiqHotspotNaiRealm**](XiqHotspotNaiRealm.md) |  | 

# roaming_consortiums

The list of Roaming Consortium network providers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of Roaming Consortium network providers. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotRoamingConsortium**](XiqHotspotRoamingConsortium.md) | [**XiqHotspotRoamingConsortium**](XiqHotspotRoamingConsortium.md) | [**XiqHotspotRoamingConsortium**](XiqHotspotRoamingConsortium.md) |  | 

# cellular_networks

List of 3rd Generation Partnership Project (3GPP) cellular networks.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of 3rd Generation Partnership Project (3GPP) cellular networks. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotCellularNetwork**](XiqHotspotCellularNetwork.md) | [**XiqHotspotCellularNetwork**](XiqHotspotCellularNetwork.md) | [**XiqHotspotCellularNetwork**](XiqHotspotCellularNetwork.md) |  | 

# service_providers

The list of supported hotspot service providers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of supported hotspot service providers. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotServiceProviderProfile**](XiqHotspotServiceProviderProfile.md) | [**XiqHotspotServiceProviderProfile**](XiqHotspotServiceProviderProfile.md) | [**XiqHotspotServiceProviderProfile**](XiqHotspotServiceProviderProfile.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

