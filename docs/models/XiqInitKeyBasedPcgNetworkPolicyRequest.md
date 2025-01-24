# extremecloudiq.model.xiq_init_key_based_pcg_network_policy_request.XiqInitKeyBasedPcgNetworkPolicyRequest

The request to create Key-based Private Client Group

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The request to create Key-based Private Client Group | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**policy_name** | str,  | str,  | The network policy name | 
**ssid_name** | str,  | str,  | The SSID name | 
**[users](#users)** | list, tuple,  | tuple,  | The Key-based PCG users | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# users

The Key-based PCG users

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Key-based PCG users | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqKeyBasedPcgUserBaseInfo**](XiqKeyBasedPcgUserBaseInfo.md) | [**XiqKeyBasedPcgUserBaseInfo**](XiqKeyBasedPcgUserBaseInfo.md) | [**XiqKeyBasedPcgUserBaseInfo**](XiqKeyBasedPcgUserBaseInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

