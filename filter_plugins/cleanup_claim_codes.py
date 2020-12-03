class FilterModule(object):

    def filters(self):
        return {
            'cleanup_claim_codes': self.cleanup_claim_codes,
        }

    def cleanup_claim_code(self, value):
        return (value.strip(",").replace(" ", "").split(","))
