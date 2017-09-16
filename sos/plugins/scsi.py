# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from sos.plugins import Plugin, RedHatPlugin, UbuntuPlugin, DebianPlugin


class Scsi(Plugin, RedHatPlugin, UbuntuPlugin, DebianPlugin):
    """SCSI devices
    """

    plugin_name = 'scsi'
    profiles = ('storage', 'hardware')

    def setup(self):
        self.add_copy_spec([
            "/proc/scsi",
            "/etc/stinit.def"
        ])
        self.add_sysfs_path('/sys/class/scsi_host')
        self.add_sysfs_path('/sys/class/scsi_disk')
        self.add_sysfs_path('/sys/class/scsi_device')
        self.add_sysfs_path('/sys/class/scsi_generic')
        self.add_sysfs_path('/sys/bus/scsi')

        self.add_cmd_output([
            "lsscsi",
            "sg_map"
        ])

# vim: set et ts=4 sw=4 :
