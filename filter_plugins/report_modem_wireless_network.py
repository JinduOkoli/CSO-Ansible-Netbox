class FilterModule(object):

    def filters(self):
        return {
            'report_modem_wireless_network': self.report_modem_wireless_network,
        }

    def report_modem_wireless_network(self, value):
        report_modem = {}

        # connection time
        report_modem['connected_time'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['lte-network-generic'][0]['connected-time'][0]['data']
        # network information
        report_modem['lte_network_ipv4'] = {}
        report_modem['lte_network_ipv4']['dns'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['lte-network-ipv4'][0]['dns'][0]['data']
        report_modem['lte_network_ipv4']['gateway'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['lte-network-ipv4'][0]['gateway'][0]['data']
        report_modem['lte_network_ipv4']['ip_addr'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['lte-network-ipv4'][0]['ip-addr'][0]['data']
        # GSM interface 
        report_modem['gsm_network'] = {}
        report_modem['gsm_network']['apn'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['apn'][0]['data']
        report_modem['gsm_network']['cell_id'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['cell-id'][0]['data']
        report_modem['gsm_network']['gsm_band'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['gsm-band'][0]['data']
        report_modem['gsm_network']['modem_status'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['modem-status'][0]['data']
        report_modem['gsm_network']['network'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['network'][0]['data']
        report_modem['gsm_network']['rsrp'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['rsrp'][0]['data']
        report_modem['gsm_network']['rsrq'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['rsrq'][0]['data']
        report_modem['gsm_network']['service_mode'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['service-mode'][0]['data']
        report_modem['gsm_network']['sinr'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['sinr'][0]['data']
        report_modem['gsm_network']['snr'] = value['parsed_output']['wwand-modem-wireless-lte-network'][0]['wwand-modem-wireless-gsm-interface-network'][0]['snr'][0]['data']

        return report_modem
