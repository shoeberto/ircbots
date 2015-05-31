# coding=utf8
"""
highlight_all.py - Willie @all Highlighter
Use WillieBot to highlight all users in a channel for a message using @all syntax.

Non-admins are limited to 1 @all per 20 seconds.
"""
from __future__ import unicode_literals

import re
import sys
from willie import web, tools
from willie.module import commands, rule, example, rate


@rule('(?u)^\@all.*')
@rate(20)
def title_auto(bot, trigger):
    users = bot.privileges[trigger.sender].keys()

    # Remove the sender and bot from the nick list.
    if bot.nick in users: users.remove(bot.nick)
    if trigger.nick in users: users.remove(trigger.nick)

    if not users: return None

    separator = ' '
    nicks = separator.join(users)

    msg = trigger.args[1]

    # Strip out the @all and start/end whitespace on the sender's message
    msg = msg.replace('@all', '', 1)
    msg = msg.strip()

    msg = msg + ' (@all from: ' + trigger.nick + ' to ' + nicks + ')'
    bot.say(msg)


if __name__ == "__main__":
    from willie.test_tools import run_example_tests
    run_example_tests(__file__)
