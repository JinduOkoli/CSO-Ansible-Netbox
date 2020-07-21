class FilterModule(object):

    def filters(self):
        return {
            'get_health_of_sites': self.get_health_of_sites,
        }

    def get_health_of_sites(self, value):
        import json
        sites = []

        for each in value['results']:
          site = {}
          for fq in each['json']['tenant-sites']['fq_name']:
            if "OAM" in fq:
              pass
            elif "JNPR" in fq:
              pass
            else:
              site["name"] = each['json']['tenant-sites']["fq_name"][0]
              site["uuid"] = each['json']['tenant-sites']["uuid"]
              site["href"] = each['json']['tenant-sites']["href"]
              site["location"] = each['json']['tenant-sites']["location"]
              site["display_name"] = each['json']['tenant-sites']["display_name"]
              site["state"] = each['json']['tenant-sites']["device"][0]["state"]
              site["device_serial_number"] = each['json']['tenant-sites']["device"][0]["device_serial_number"]
              site["management_state"] = each['json']['tenant-sites']["device"][0]["management_state"]
              site["activation_state"] = each['json']['tenant-sites']["device"][0]["activation_state"]["current_state"]
              sites.append(site)
        return sites
