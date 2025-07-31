# extremecloudiq.model.xiq_afc_mobileapp_anchor_candidate.XiqAfcMobileappAnchorCandidate

List of AP candidates that may be used as anchors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of AP candidates that may be used as anchors | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID | [optional] value must be a 64 bit integer
**serial_number** | str,  | str,  | The serial number | [optional] 
**name** | str,  | str,  | The device name | [optional] 
**mac_address** | str,  | str,  | The device MAC address | [optional] 
**make** | str,  | str,  | The product make, such as: WiNG, Aerohive, Extreme etc | [optional] 
**product_type** | str,  | str,  | The product type, such as: AP_5050U, AP5050D, AP5020 etc. | [optional] 
**location** | str,  | str,  | The location of the device, including floor name | [optional] 
**bssid** | str,  | str,  | The base radio BSSID | [optional] 
**gps_anchor** | bool,  | BoolClass,  | The AP used as GPS anchor to derive geo-coordinates of other APs on the floor | [optional] 
**coordinates** | [**XiqAfcMobileappCoordinates**](XiqAfcMobileappCoordinates.md) | [**XiqAfcMobileappCoordinates**](XiqAfcMobileappCoordinates.md) |  | [optional] 
**neighbors** | decimal.Decimal, int,  | decimal.Decimal,  | The number of neighboring APs | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

