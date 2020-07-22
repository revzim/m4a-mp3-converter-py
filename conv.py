# ANDY ZIMMELMAN 2019
# CONVERT M4A TO MP3

import sys
import os

from pydub import AudioSegment as AS
from pydub.utils import which

class Converter:

    def __init__(self):
        self.file_name = None
        # SET CONVERTER
        self.__converter__ = "ffmpeg"
        AS.converter = which(self.__converter__)
        # SET OUTPUT FILE TYPE
        self.output_type = "mp3"
        # INIT SOUNDBYTE FILE
        self.sound_byte = None
        # INIT OUTPUT FILE
        self.output_sound_byte = None
        # INIT DESTINATION PATH
        self.destination_path = None

    def createSoundByte(self, full_file_path):
        self.sound_byte = AS.from_file(full_file_path)

    def parsePathAndName(self, full_file_path):
        self.file_path = os.path.basename(full_file_path)
        self.file_name = self.file_path.split(".")[0]

    def parseDestinationPath(self, full_file_path):
        self.destination_path = full_file_path[:full_file_path.rindex('/')]

    def exportAsMP3(self, file_path):
        self.output_sound_byte = self.sound_byte.export(file_path, format=self.output_type)


    def convertToMP3(self, full_file_path):
        # CREATES AUDIOSEGMENT FROM SOUND BYTE FILE
        self.createSoundByte(full_file_path)
        # PARSES DESTINATION PATH FOR EASIER CONVERSION FLOW
        self.parseDestinationPath(full_file_path)
        # PARSES FILE PATH AND NAME FOR CONVERSION
        self.parsePathAndName(full_file_path)
        # EXPORTS SOUND BYTE FILE AS MP3 AND STORES IN FILE PATH
        self.exportAsMP3("{0}/{1}.{2}".format(self.destination_path, self.file_name, self.output_type))

