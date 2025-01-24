# extremecloudiq.model.xiq_create_ldap_server_request.XiqCreateLdapServerRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bind_dn** | str,  | str,  | The LDAP server bind DN name | 
**protocol_type** | [**XiqLdapProtocolType**](XiqLdapProtocolType.md) | [**XiqLdapProtocolType**](XiqLdapProtocolType.md) |  | 
**enable_tls** | bool,  | BoolClass,  | To enable TLS or not, if ture, caCertificateId, clientCertificateId and clientKeyId must be specified | 
**base_dn** | str,  | str,  | The RADIUS user base DN | 
**enable_strip_realm_name** | bool,  | BoolClass,  | enable strip realm name or not | 
**l3_address_profile_id** | decimal.Decimal, int,  | decimal.Decimal,  | The L3 address profile ID | value must be a 64 bit integer
**destination_port** | decimal.Decimal, int,  | decimal.Decimal,  | The LDAP server destination port (1 ~ 65535) | value must be a 32 bit integer
**verification_mode** | [**XiqLdapServerVerificationMode**](XiqLdapServerVerificationMode.md) | [**XiqLdapServerVerificationMode**](XiqLdapServerVerificationMode.md) |  | 
**name** | str,  | str,  | The LDAP server name | 
**bind_dn_password** | str,  | str,  | The LDAP server bind DN password | 
**description** | str,  | str,  | The LDAP server description(optional) | [optional] 
**ca_certificate_id** | decimal.Decimal, int,  | decimal.Decimal,  | The CA certificate ID, refer to XiqCertificate | [optional] value must be a 64 bit integer
**client_certificate_id** | decimal.Decimal, int,  | decimal.Decimal,  | The client certificate ID, refer to XiqCertificate | [optional] value must be a 64 bit integer
**client_key_id** | decimal.Decimal, int,  | decimal.Decimal,  | The client key ID, refer to XiqCertificate | [optional] value must be a 64 bit integer
**client_key_password** | str,  | str,  | The LDAP server client key password | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

