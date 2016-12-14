# -*- coding: utf-8 -*-
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# vim:sw=4:ts=4:et


class Storage:

    @property
    def storage_device_info(self):
        ret = self.command(
            'storageDevice.cgi?action=getDeviceAllInfo'
        )
        return ret.content.decode('utf-8')

    @property
    def storage_device_names(self):
        ret = self.command(
            'storageDevice.cgi?action=factory.getCollect'
        )
        return ret.content.decode('utf-8')

    @property
    def storage_used_bytes(self, dev='/dev/mmc0', unit='GB'):
        ret = self.storage_device_info
        #TODO
        #Use regex to enhance the filter
        status = [s for s in ret.split() if '.UsedBytes=' in s][0]
        return self.to_unit(status.split('=')[-1])

    @property
    def storage_total_bytes(self, dev='/dev/mmc0', unit='GB'):
        ret = self.storage_device_info
        #TODO
        #Use regex to enhance the filter
        status = [s for s in ret.split() if '.TotalBytes=' in s][0]
        return self.to_unit(status.split('=')[-1])
