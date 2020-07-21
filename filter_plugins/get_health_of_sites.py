class FilterModule(object):

    def filters(self):
        return {
            'get_health_of_sites': self.get_health_of_sites,
        }

    def get_health_of_sites(self, value):
        import json
        sites = []

        for each in value['json']['tenant-sites']:
          site = {}
          for fq in each['fq_name']:
            if "OAM" in fq:
              pass
            elif "JNPR" in fq:
              pass
            else:
              site["name"] = each["fq_name"][0]
              site["uuid"] = each["uuid"]
              site["href"] = each["href"]
              site["location"] = each["location"]
              site["display_name"] = each["display_name"]
              site["state"] = each["device"][0]["state"]
              site["device_serial_number"] = each["device"][0]["device_serial_number"]
              site["management_state"] = each["device"][0]["management_state"]
              site["activation_state"] = each["device"][0]["activation_state"]["current_state"]
              sites.append(site)
        return sites
