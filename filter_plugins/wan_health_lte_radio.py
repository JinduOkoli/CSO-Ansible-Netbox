class FilterModule(object):

    def filters(self):
        return {
            'wan_health_lte_radio': self.wan_health_lte_radio,
        }

    def wan_health_lte_radio(self, value):
        lte_report = {}

        # LTE network
        lte_report['lte_network'] = {}
        lte_report['lte_network']['connected_time'] = value['lte-network-generic'][0]['connected-time'][0]['data']
        # ### NETWORK
        lte_report['lte_network']['network'] = {}
        lte_report['lte_network']['network']['ipv4'] = value['lte-network-ipv4'][0]['ip-addr'][0]['data']
        lte_report['lte_network']['network']['gateway'] = value['lte-network-ipv4'][0]['gateway'][0]['data']
        lte_report['lte_network']['network']['dns'] = value['lte-network-ipv4'][0]['dns'][0]['data']
        # ### LTE
        lte_report['lte_network']['lte_network_packet'] = {}
        lte_report['lte_network']['lte_network_packet']['byte_rx'] = value['lte-network-packet'][0]['byte-rx'][0]['data']
        lte_report['lte_network']['lte_network_packet']['byte_tx'] = value['lte-network-packet'][0]['byte-tx'][0]['data']
        # ### GSM
        lte_report['lte_network']['gsm'] = {}
        lte_report['lte_network']['gsm']['status_modem'] = value['wwand-modem-wireless-gsm-interface-network'][0]['modem-status'][0]['data']
        lte_report['lte_network']['gsm']['status_service'] = value['wwand-modem-wireless-gsm-interface-network'][0]['service-status'][0]['data']
        lte_report['lte_network']['gsm']['service_type'] = value['wwand-modem-wireless-gsm-interface-network'][0]['service-type'][0]['data']
        lte_report['lte_network']['gsm']['service_mode'] = value['wwand-modem-wireless-gsm-interface-network'][0]['service-mode'][0]['data']
        lte_report['lte_network']['gsm']['gsm_band'] = value['wwand-modem-wireless-gsm-interface-network'][0]['gsm-band'][0]['data']
        lte_report['lte_network']['gsm']['network'] = value['wwand-modem-wireless-gsm-interface-network'][0]['network'][0]['data']
        lte_report['lte_network']['gsm']['plmn'] = value['wwand-modem-wireless-gsm-interface-network'][0]['plmn'][0]['data']
        lte_report['lte_network']['gsm']['imsi'] = value['wwand-modem-wireless-gsm-interface-network'][0]['imsi'][0]['data']
        lte_report['lte_network']['gsm']['imei'] = value['wwand-modem-wireless-gsm-interface-network'][0]['imei'][0]['data']
        lte_report['lte_network']['gsm']['iccid'] = value['wwand-modem-wireless-gsm-interface-network'][0]['iccid'][0]['data']
        lte_report['lte_network']['gsm']['rsrp'] = value['wwand-modem-wireless-gsm-interface-network'][0]['rsrp'][0]['data']
        lte_report['lte_network']['gsm']['rsrq'] = value['wwand-modem-wireless-gsm-interface-network'][0]['rsrq'][0]['data']
        lte_report['lte_network']['gsm']['sinr'] = value['wwand-modem-wireless-gsm-interface-network'][0]['sinr'][0]['data']
        lte_report['lte_network']['gsm']['snr'] = value['wwand-modem-wireless-gsm-interface-network'][0]['snr'][0]['data']

        return lte_report