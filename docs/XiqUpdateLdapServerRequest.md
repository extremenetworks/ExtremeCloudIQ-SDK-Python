# XiqUpdateLdapServerRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The LDAP server name | [optional] 
**description** | **str** | The LDAP server description | [optional] 
**enable_tls** | **bool** | enable TLS or not, if ture, caCertificateId, clientCertificateId and clientKeyId must be specified | [optional] 
**bind_dn** | **str** | The LDAP server bind DN name | [optional] 
**bind_dn_password** | **str** | The LDAP server bind DN password | [optional] 
**base_dn** | **str** | The RADIUS user base DN | [optional] 
**l3_address_profile_id** | **int** | The L3 address profile ID | [optional] 
**protocol_type** | [**XiqLdapProtocolType**](XiqLdapProtocolType.md) |  | [optional] 
**enable_strip_realm_name** | **bool** | enable strip realm name or not | [optional] 
**destination_port** | **int** | The LDAP server destination port (1 ~ 65535) | [optional] 
**verification_mode** | [**XiqLdapServerVerificationMode**](XiqLdapServerVerificationMode.md) |  | [optional] 
**ca_certificate_id** | **int** | The CA certificate ID, refer to XiqCertificate | [optional] 
**client_certificate_id** | **int** | The client certificate ID, refer to XiqCertificate | [optional] 
**client_key_id** | **int** | The client key ID, refer to XiqCertificate | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


