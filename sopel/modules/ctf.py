# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
from sopel.module import VOICE
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

@sopel.module.require_privilege(VOICE, 'You do not have access.')
@sopel.module.require_chanmsg("This only works in channel")
@sopel.module.commands('get')
@sopel.module.example('.get passwd')
def get_ctf(bot, trigger):
    """See the CTF Login Information
    Params:
        uname
        email
        passwd
        teamid
    """
    section = 'ctf'

    # Get section and option from first argument.
    arg1 = trigger.group(3).split('.')
    if len(arg1) == 1:
        section_name, option = "ctf", arg1[0]
    else:
        bot.reply("Usage: .get option")
        return

    section = getattr(bot.config, section_name)
    static_sec = isinstance(section, StaticSection)

    if static_sec and not hasattr(section, option):
        bot.say('[{}] section has no option {}.'.format(section_name, option))
        return

    # Display current value if no value is given.
    value = trigger.group(4)
    if not value:
        if not static_sec and bot.config.parser.has_option(section, option):
            bot.reply("%s does not exist." % (option))
            return

        value = getattr(section, option)
        bot.reply(value)
        return
