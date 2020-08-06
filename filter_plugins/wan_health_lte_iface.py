class FilterModule(object):

    def filters(self):
        return {
            'wan_health_lte_cleanup': self.wan_health_lte_cleanup,
        }

    def wan_health_lte_cleanup(self, value):
        interface_report = {}

        interface_report['name'] = value['name'][0]['data']
        interface_report['status'] = value['admin-status'][0]['data']
        interface_report['oper_status'] = value['oper-status'][0]['data']
        interface_report['description'] = value['description'][0]['data']
        interface_report['mtu'] = value['mtu'][0]['data']
        interface_report['speed'] = value['speed'][0]['data']
        interface_report['mac_address'] = value['current-physical-address'][0]['data']
        interface_report['last_flap'] = value['interface-flapped'][0]['data']
        # traffic stats
        interface_report['traffic_stats'] = {}
        interface_report['traffic_stats']['input_bps'] = value['traffic-statistics'][0]['input-bps'][0]['data']
        interface_report['traffic_stats']['input_pps'] = value['traffic-statistics'][0]['input-pps'][0]['data']
        interface_report['traffic_stats']['output_bps'] = value['traffic-statistics'][0]['output-bps'][0]['data']
        interface_report['traffic_stats']['output_pps'] = value['traffic-statistics'][0]['output-pps'][0]['data']
        # logical interface
        interface_report['logical_interface'] = {}
        interface_report['logical_interface']['name'] = value['logical-interface'][0]['name'][0]['data']
        interface_report['logical_interface']['encapsulation'] = value['logical-interface'][0]['encapsulation'][0]['data']
        interface_report['logical_interface']['dialer_information'] = {}
        interface_report['logical_interface']['dialer_information']['state'] = value['logical-interface'][0]['dialer-information'][0]['dialer-interface-information'][0]['dialer-interface'][0]['dialer-interface-state'][0]['data']
        interface_report['logical_interface']['dialer_information']['pool_id'] = value['logical-interface'][0]['dialer-information'][0]['dialer-interface-information'][0]['dialer-interface'][0]['pool-id'][0]['data']
        interface_report['logical_interface']['dialer_information']['dial_string'] = value['logical-interface'][0]['dialer-information'][0]['dialer-interface-information'][0]['dialer-interface'][0]['dial-string-list'][0]['dial-string'][0]['data']
        interface_report['logical_interface']['dialer_information']['sub_interface'] = value['logical-interface'][0]['dialer-information'][0]['dialer-interface-information'][0]['dialer-interface'][0]['sub-interface-list'][0]['sub-interface-name'][0]['data']

        return interface_report