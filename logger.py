import datetime
import os

from plugins.baseplugin import BasePlugin
from plugins.logger.models import Log, Activity


class Plugin(BasePlugin):
    """Plugin for logging"""
    name = 'LoggerPlugin'

    def _log(self, log_type, user, nick, channel, message):
        with self.getDbSession() as db_session:
            db_session.add(
                Log(
                    log_type=log_type,
                    user=user,
                    nick=nick,
                    log_time=datetime.datetime.now(),
                    channel=channel,
                    message=message
                )
            )

    # log user messages
    def onMessage(self, user, nick, channel, more, highlight):
        self._log('message', user, nick, channel, more)

    def onPrivateMessage(self, user, nick, more):
        self._log('pm', user, nick, self.nick, more)

    def onUserAction(self, user, nick, channel, action):
        self._log('action', user, nick, channel, action)

    def onCommand(self, user, nick, channel, command, more):
        self._log('command', user, nick, channel, '%s %s' % (command, more))

    def onAdminCommand(self, user, nick, channel, command, more):
        self._log(
            'admin_command', user, nick, channel, '%s %s' % (command, more)
        )

    # log own messages
    def onSend(self, channel, message):
        self._log('message', self.nick, self.nick, channel, message)

    def onAction(self, channel, message):
        self._log('action', self.nick, self.nick, channel, message)


    # log user activity
    def _activity(self, activity_type, user, nick, channel, info1='', info2=''):
        with self.getDbSession() as db_session:
            db_session.add(
                Activity(
                    activity_type=activity_type,
                    user=user,
                    nick=nick,
                    activity_time=datetime.datetime.now(),
                    channel=channel,
                    info1=info1,
                    info2=info2
                )
            )

    def onUserJoined(self, user, nick, channel):
        self._activity('user_joined', user, nick, channel)

    def onUserLeft(self, user, nick, channel):
        self._activity('user_left', user, nick, channel)

    def onUserQuit(self, user, nick, quitMessage):
        self._activity('user_quit', user, nick, '', quitMessage)

    def onUserKicked(self, kickee, channel, kicker_user, kicker, message):
        self._activity(
            'user_kick', kicker_user, kicker, channel, kickee, message
        )

    def onUserRenamed(self, user, old_nick, new_nick):
        self._activity('user_renamed', user, new_nick, '', old_nick, new_nick)

    # own activity
    def onJoined(self, channel):
        self._activity('joined', self.nick, self.nick, channel)

    def onLeave(self, channel):
        self._activity('left', self.nick, self.nick, channel)

    def onKicked(self, kicker_user, kicker, channel, message):
        self._activity('kick', kicker_user, kicker, channel, self.nick, message)

    def onNickChange(self, nick, old_nick):
        self._activity('nick_change', '', self.nick, '', old_nick, nick)
