# extremecloudiq.model.xiq_hotspot_online_signup.XiqHotspotOnlineSignup

The Hotspot profile Online Signup settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Hotspot profile Online Signup settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**network_auth_type** | [**XiqHotspotOsuNetworkAuthType**](XiqHotspotOsuNetworkAuthType.md) | [**XiqHotspotOsuNetworkAuthType**](XiqHotspotOsuNetworkAuthType.md) |  | 
**redirection_url** | str,  | str,  | The redirection URL, when the Network Authentication type is CWP. | [optional] 
**ssid_id** | decimal.Decimal, int,  | decimal.Decimal,  | OSU SSID ID, when the Network Authentication type is ONLINE_SIGN_UP. The authentication mode must be open or OSEN. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

