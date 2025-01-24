# extremecloudiq.model.xiq_hotspot_nai_realm.XiqHotspotNaiRealm

List of Network Access Identification (NAI) realms. A NAI realm is a FQDN of a service provider.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of Network Access Identification (NAI) realms. A NAI realm is a FQDN of a service provider. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The Network Access Identifier (NAI) Realm name | 
**description** | str,  | str,  | The NAI Realm description. | [optional] 
**[eap_methods](#eap_methods)** | list, tuple,  | tuple,  | The list of Extensible Authentication Protocol (EAP) methods. | [optional] 
**encoding_type** | [**XiqHotspotNaiEncodingType**](XiqHotspotNaiEncodingType.md) | [**XiqHotspotNaiEncodingType**](XiqHotspotNaiEncodingType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# eap_methods

The list of Extensible Authentication Protocol (EAP) methods.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of Extensible Authentication Protocol (EAP) methods. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqHotspotEapMethod**](XiqHotspotEapMethod.md) | [**XiqHotspotEapMethod**](XiqHotspotEapMethod.md) | [**XiqHotspotEapMethod**](XiqHotspotEapMethod.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

