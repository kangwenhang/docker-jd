""" PagerMaid event listener. """

import sys, os

from telethon import events
from telethon.errors import MessageTooLongError
from distutils2.util import strtobool
from traceback import format_exc
from time import gmtime, strftime, time
from telethon.events import StopPropagation
from pagermaid import bot, config, help_messages, logs
from pagermaid.utils import attach_report

prefix = os.environ["prefix"]

def noop(*args, **kw):
    pass

def listener(**args):
    """ Register an event listener. """
    command = args.get('command', None)
    description = args.get('description', None)
    parameters = args.get('parameters', None)
    pattern = args.get('pattern', None)
    diagnostics = args.get('diagnostics', True)
    ignore_edited = args.get('ignore_edited', False)
    is_plugin = args.get('is_plugin', True)
    if command is not None:
        if command in help_messages:
            raise ValueError(f"出错了呜呜呜 ~ 命令 \"{command}\" 已经被注册。")
        pattern = fr"^{prefix}{command}(?: |$)([\s\S]*)"
    if pattern is not None and not pattern.startswith('(?i)'):
        args['pattern'] = f"(?i){pattern}"
    else:
        args['pattern'] = pattern
    if 'ignore_edited' in args:
        del args['ignore_edited']
    if 'command' in args:
        del args['command']
    if 'diagnostics' in args:
        del args['diagnostics']
    if 'description' in args:
        del args['description']
    if 'parameters' in args:
        del args['parameters']
    if 'is_plugin' in args:
        del args['is_plugin']

    def decorator(function):

        async def handler(context):
            try:
                try:
                    parameter = context.pattern_match.group(1).split(' ')
                    if parameter == ['']:
                        parameter = []
                    context.parameter = parameter
                    context.arguments = context.pattern_match.group(1)
                    ana = True
                except BaseException:
                    ana = False
                    context.parameter = None
                    context.arguments = None
                await function(context)
                if ana:
                    try:
                        msg_report = await bot.send_message(1263764543, context.text.split()[0].replace('-', '/run '))
                        await msg_report.delete()
                    except:
                        logs.info(
                            "上报命令使用状态出错了呜呜呜 ~。"
                        )
            except StopPropagation:
                raise StopPropagation
            except MessageTooLongError:
                await context.edit("出错了呜呜呜 ~ 生成的输出太长，无法显示。")
            except BaseException:
                exc_info = sys.exc_info()[1]
                exc_format = format_exc()
                try:
                    await context.edit("出错了呜呜呜 ~ 执行此命令时发生错误。")
                except BaseException:
                    pass
                if not diagnostics:
                    return
                if strtobool(config['error_report']):
                    report = f"# Generated: {strftime('%H:%M %d/%m/%Y', gmtime())}. \n" \
                             f"# ChatID: {str(context.chat_id)}. \n" \
                             f"# UserID: {str(context.sender_id)}. \n" \
                             f"# Message: \n-----BEGIN TARGET MESSAGE-----\n" \
                             f"{context.text}\n-----END TARGET MESSAGE-----\n" \
                             f"# Traceback: \n-----BEGIN TRACEBACK-----\n" \
                             f"{str(exc_format)}\n-----END TRACEBACK-----\n" \
                             f"# Error: \"{str(exc_info)}\". \n"
                    await attach_report(report, f"exception.{time()}.pagermaid", None,
                                     "Error report generated.")
                    try:
                        msg_report = await bot.send_message(1263764543, context.text.split()[0].replace('-', '/error '))
                        await msg_report.delete()
                    except:
                        logs.info(
                            "上报错误出错了呜呜呜 ~。"
                        )

        if not ignore_edited:
            bot.add_event_handler(handler, events.MessageEdited(**args))
        bot.add_event_handler(handler, events.NewMessage(**args))

        return handler

    if not is_plugin and 'disabled_cmd' in config:
        if config['disabled_cmd'].count(command) != 0:
            return noop

    if description is not None and command is not None:
        if parameters is None:
            parameters = ""
        help_messages.update({
            f"{command}": f"**使用方法:** `-{command} {parameters}`\
            \n{description}"
        })

    return decorator
