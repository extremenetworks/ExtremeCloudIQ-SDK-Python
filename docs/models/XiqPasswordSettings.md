# extremecloudiq.model.xiq_password_settings.XiqPasswordSettings

The password settings ID

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The password settings ID | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**psk_generation_method** | [**XiqPskGenerationMethod**](XiqPskGenerationMethod.md) | [**XiqPskGenerationMethod**](XiqPskGenerationMethod.md) |  | 
**password_character_types** | [**XiqPasswordCharacterType**](XiqPasswordCharacterType.md) | [**XiqPasswordCharacterType**](XiqPasswordCharacterType.md) |  | 
**password_length** | decimal.Decimal, int,  | decimal.Decimal,  | The maximun password string length | value must be a 32 bit integer
**enable_letters** | bool,  | BoolClass,  | Enable use of letters | [optional] 
**enable_numbers** | bool,  | BoolClass,  | Enable use of numbers | [optional] 
**enable_special_characters** | bool,  | BoolClass,  | Enable use of special characters | [optional] 
**password_concat_string** | str,  | str,  | The password concatenated string | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

