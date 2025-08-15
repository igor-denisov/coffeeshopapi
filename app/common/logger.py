"""
This module contains the minimal logger configuration.
"""

from sys import stdout

from loguru import logger, Record


def log_formatter(record: Record):
    log = (
        "{level.icon}<g>[{time:YYYY-MM-DD at HH:mm:ss}]</> | "
        "<b><e>{level}</></> | "
        "<m>{name}<lw>:</>{function}<lw>:</>{line}</> - "
        "<c><b>{message}</></>\n"
    )
    if record["extra"]:
        log += "{extra}\n"
    return log


logger.remove()
logger.add(
    sink=stdout,
    format=log_formatter,
    colorize=True,
)
