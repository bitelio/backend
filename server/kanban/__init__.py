#!/usr/bin/python
# vim:fileencoding=utf-8

from . import kanban


def load(board_id):
    return kanban.Board(board_id)
