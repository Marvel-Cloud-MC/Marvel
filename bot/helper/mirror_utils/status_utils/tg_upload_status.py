#!/usr/bin/env python3
from pkg_resources import get_distribution

from bot.helper.ext_utils.bot_utils import (MirrorStatus,
                                            get_readable_file_size,
                                            get_readable_time)

engine_ = f"Pyrogram"

class TgUploadStatus:
    def __init__(self, obj, size, gid, message, extra_details):
        self.__obj = obj
        self.__size = size
        self.__gid = gid
        self.message = message
        self.startTime = extra_details['startTime']
        self.mode = extra_details['mode']
        self.source = extra_details['source']
        self.engine = engine_

    def processed_bytes(self):
        return get_readable_file_size(self.__obj.uploaded_bytes)

    def size(self):
        return get_readable_file_size(self.__size)

    def status(self):
        return MirrorStatus.STATUS_UPLOADING

    def name(self):
        return self.__obj.name

    def progress_raw(self):
        try:
            return self.__obj.uploaded_bytes / self.__size * 100
        except ZeroDivisionError:
            return 0

    def progress(self):
        return f'{round(self.progress_raw(), 2)}%'

    def speed(self):
        return f'{get_readable_file_size(self.__obj.speed)}/s'

    def eta(self):
        try:
            seconds = (self.__size - self.__obj.uploaded_bytes) / self.__obj.speed
            return f'{get_readable_time(seconds)}'
        except ZeroDivisionError:
            return '-'

    def gid(self) -> str:
        return self.__gid

    def download(self):
        return self.__obj
