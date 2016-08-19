# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.config.types import (
    StaticSection, ValidatedAttribute, FilenameAttribute
)
import sopel.module


class CTFSection(StaticSection):
    """Config section for CTF information"""

    uname = ValidatedAttribute('uname', default='b01lers')
    """The username for logging into CTFs"""

    email = ValidatedAttribute('email', default='ctf@b01lers.net')
    """Email used to login for CTFs"""

    passwd = ValidatedAttribute('passwd')
    """Password used to login for CTFS"""

    teamid = ValidatedAttribute('teamid')
    """The Team ID code for joining team"""



def configure(config):
    config.define_section('ctf', CTFSection)
    config.ctf.configure_setting('uname', 'Enter the username for ctf', default='b01lers')
    config.ctf.configure_setting('email', 'Enter the email for ctf', default='ctf@b01lers.net')
    config.ctf.configure_setting('passwd', 'Enter the passwd for ctf')
    config.ctf.configure_setting('teamid', 'Enter the team id for ctf')



def setup(bot):
    bot.config.define_section('ctf', CTFSection)
