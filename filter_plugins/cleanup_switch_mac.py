class FilterModule(object):

    def filters(self):
        return {
            'cleanup_switch_mac': self.cleanup_switch_mac,
        }

    def cleanup_switch_mac(self, value):
        macs = []
        for each in value:
            macs.append(each["mac"])
        return macs
