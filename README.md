Yaib Logger Plugin
=================

A logging plugin for [yaib](https://github.com/collingreen/yaib) that simply
connects all the standard chat callbacks to the persistence layer.


## Setup:
The only thing required is a properly configured persistence module (Yaib comes
configured with a working local sqlite database out of the box - change the
`persistence.connection` string in config.json to change database connections.
Consult the Yaib and SQLAlchemy docs for more info.


## Tables:
This plugin creates two tables in the database, `Log` and `Activity`. Chat
messages, actions, private messages, and commands are all put into the `Log`
table, while general server activity like joining and leaving channels,
kicking/being kicked, and quitting the server are recorded in the `Activity`
table.

Rows in the `Log` table can have any of the following values in the `log_type`
column.
- `message` - regular messages from a user or yaib
- `pm` - a private message from a user to yaib
- `action` - an action by a user (eg, /me does an thing)
- `command` - a command run by a user
- `admin_command` - an admin level command run by a user

Rows in the `Activity` table can have any of the following values in the
`activity_type` column:
- `user_joined` - a user joins a channel
- `user_left` - a user leaves a channel
- `user_quit` - a user leaves the server
- `user_kick` - a user is kicked (the user and nick columns are the kicker, info1
        is the kickee, info2 is the kick message)
- `user_renamed` - a user changes nick
- `joined` - yaib joins a channel
- `left` - yaib leaves a channel
- `kick` - yaib is kicked from a channel (the user and nick columns are the
        kicker)
- `nick_change` - yaib changes nicks
