#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, urllib, os
from gi.repository import GObject, Nautilus

class Search(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def search_tool(self, window, files):
        if len(files) != 1:
            return

        cmd = 'search {}'.format(str(urllib.unquote(files[0].get_uri()[7:])))
        subprocess.Popen(cmd, shell=True)
        return

    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        if not os.path.isdir(urllib.unquote(files[0].get_uri()[7:])):
            return

        item = Nautilus.MenuItem(
            name="Search::Tool",
            label="File Search",
            tip="Search Tool"
        )

        item.connect('activate', self.search_tool, files)
        return [item] 
