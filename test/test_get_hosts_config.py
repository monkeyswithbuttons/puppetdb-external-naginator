from naginator import get_config
from mock import *


def mock_get_nagios_data(__):
    return [
        {
            "certname": "aaaa.ofi.lan",
            "title": "aaaa.ofi.lan",
            "parameters": {
                "address": "172.20.4.20",
                "alias": "aaaa.ofi",
                "contact_groups": "nobody",
                "host_name": "aaaa.ofi.lan",
                "use": "generic-host",
            },
        },
        {
            "certname": "bbbb.ofi.lan",
            "title": "bbbb.ofi.lan",
            "parameters": {
                "address": "172.20.4.30",
                "alias": "bbbb.ofi",
                "contact_groups": "nobody",
                "host_name": "bbbb.ofi.lan",
                "use": "generic-host",
            },
        },
    ]


@patch('naginator.get_nagios_data', mock_get_nagios_data)
def test_get_hosts_config():
    assert get_config('host') == """
define host {
        address                        172.20.4.20
        alias                          aaaa.ofi
        contact_groups                 nobody
        host_name                      aaaa.ofi.lan
        use                            generic-host
}

define host {
        address                        172.20.4.30
        alias                          bbbb.ofi
        contact_groups                 nobody
        host_name                      bbbb.ofi.lan
        use                            generic-host
}

"""

