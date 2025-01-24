# extremecloudiq.model.xiq_hotspot_service_provider_profile_request.XiqHotspotServiceProviderProfileRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The Hotspot Service Provider profile name. | 
**description** | str,  | str,  | The Hotspot Service Provider profile description. | [optional] 
**[friendly_names](#friendly_names)** | list, tuple,  | tuple,  | List of friendly names. | [optional] 
**[descriptions](#descriptions)** | list, tuple,  | tuple,  | List of Hotspot profile descriptions | [optional] 
**[icon_files](#icon_files)** | list, tuple,  | tuple,  | The list of localized icon files for the service provider. | [optional] 
**[nai_realms](#nai_realms)** | list, tuple,  | tuple,  | List of Network Access Identification (NAI) realms. A NAI realm is a FQDN of a service provider. | [optional] 
**[roaming_consortiums](#roaming_consortiums)** | list, tuple,  | tuple,  | List of Roaming Consortium identifiers. | [optional] 
**[cellular_networks](#cellular_networks)** | list, tuple,  | tuple,  | List of 3rd Generation Partnership Project (3GPP) cellular networks. | [optional] 
**osu_uri** | str,  | str,  | The online signup (OSU) server URI. | [optional] 
**[osu_methods](#osu_methods)** | list, tuple,  | tuple,  | Encoded OSU methods and their priorities. Priority is given by the index/position in the array. | [optional] 
**osu_nai** | str,  | str,  | Network Access Identifier (NAI) used as client identity during EAP authentication. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# friendly_names

List of friendly names.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of friendly names. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) | [**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) | [**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) |  | 

# descriptions

List of Hotspot profile descriptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Hotspot profile descriptions | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) | [**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) | [**XiqHotspotLocalizedName**](XiqHotspotLocalizedName.md) |  | 

# icon_files

The list of localized icon files for the service provider.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of localized icon files for the service provider. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotServiceProviderIconFile**](XiqHotspotServiceProviderIconFile.md) | [**XiqHotspotServiceProviderIconFile**](XiqHotspotServiceProviderIconFile.md) | [**XiqHotspotServiceProviderIconFile**](XiqHotspotServiceProviderIconFile.md) |  | 

# nai_realms

List of Network Access Identification (NAI) realms. A NAI realm is a FQDN of a service provider.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Network Access Identification (NAI) realms. A NAI realm is a FQDN of a service provider. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotNaiRealm**](XiqHotspotNaiRealm.md) | [**XiqHotspotNaiRealm**](XiqHotspotNaiRealm.md) | [**XiqHotspotNaiRealm**](XiqHotspotNaiRealm.md) |  | 

# roaming_consortiums

List of Roaming Consortium identifiers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Roaming Consortium identifiers. | 

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

# osu_methods

Encoded OSU methods and their priorities. Priority is given by the index/position in the array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Encoded OSU methods and their priorities. Priority is given by the index/position in the array. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotServiceProviderOsuMethod**](XiqHotspotServiceProviderOsuMethod.md) | [**XiqHotspotServiceProviderOsuMethod**](XiqHotspotServiceProviderOsuMethod.md) | [**XiqHotspotServiceProviderOsuMethod**](XiqHotspotServiceProviderOsuMethod.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

