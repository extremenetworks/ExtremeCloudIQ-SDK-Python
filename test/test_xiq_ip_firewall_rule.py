# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_ip_firewall_rule import XiqIpFirewallRule  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqIpFirewallRule(unittest.TestCase):
    """XiqIpFirewallRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqIpFirewallRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_ip_firewall_rule.XiqIpFirewallRule()  # noqa: E501
        if include_optional :
            return XiqIpFirewallRule(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                action = 'PERMIT', 
                network_service = extremecloudiq.models.xiq_network_service.XiqNetworkService(
                    id = 56, 
                    create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    org_id = 56, 
                    name = '0', 
                    description = '0', 
                    ip_protocol = 'TCP', 
                    protocol_number = 56, 
                    port_number = 56, 
                    alg_type = 'NONE', 
                    service_type = 'NETWORK', ), 
                application_service = extremecloudiq.models.xiq_application_service.XiqApplicationService(
                    application = extremecloudiq.models.xiq_application.XiqApplication(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        name = '0', 
                        description = '0', 
                        predefined = True, 
                        category_id = 56, 
                        category_name = '0', 
                        detection_rules = [
                            extremecloudiq.models.xiq_application_detection_rule.XiqApplicationDetectionRule(
                                value = '0', 
                                protocol = 'HTTP', 
                                type = 'HOST_NAME', )
                            ], ), 
                    service_type = 'NETWORK', ), 
                source_ip = extremecloudiq.models.xiq_l3_address_profile.XiqL3AddressProfile(
                    id = 56, 
                    create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    org_id = 56, 
                    predefined = True, 
                    name = '0', 
                    description = '0', 
                    value = '0', 
                    enable_classification = True, 
                    address_type = 'IP_ADDRESS', 
                    classified_entries = [
                        extremecloudiq.models.xiq_address_profile_classified_entry.XiqAddressProfileClassifiedEntry(
                            class_asgn_id = 56, 
                            value = '0', 
                            description = '0', 
                            netmask = '0', 
                            ip_address_end = '0', 
                            wildcard_mask = '0', )
                        ], ), 
                destination_ip = extremecloudiq.models.xiq_l3_address_profile.XiqL3AddressProfile(
                    id = 56, 
                    create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    org_id = 56, 
                    predefined = True, 
                    name = '0', 
                    description = '0', 
                    value = '0', 
                    enable_classification = True, 
                    address_type = 'IP_ADDRESS', 
                    classified_entries = [
                        extremecloudiq.models.xiq_address_profile_classified_entry.XiqAddressProfileClassifiedEntry(
                            class_asgn_id = 56, 
                            value = '0', 
                            description = '0', 
                            netmask = '0', 
                            ip_address_end = '0', 
                            wildcard_mask = '0', )
                        ], ), 
                logging_type = 'OFF'
            )
        else :
            return XiqIpFirewallRule(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testXiqIpFirewallRule(self):
        """Test XiqIpFirewallRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
