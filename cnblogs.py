#coding=utf-8
import os
import threading
from xmlrpclib import ServerProxy, Error
import HTMLParser
from itertools import groupby
from operator import itemgetter
import xmlrpclib
#import urllib.request, urllib.parse, urllib.error

import sublime
import sublime_plugin


def status(msg, thread=False):
    if not thread:
        sublime.status_message(msg)
    else:
        sublime.set_timeout(lambda: status(msg), 0)


def handle_thread(thread, msg=None, cb=None, i=0, direction=1, width=8):
    if thread.is_alive():
        next = i + direction
        if next > width:
            direction = -1
        elif next < 0:
            direction = 1
        bar = [' '] * (width + 1)
        bar[i] = '='
        i += direction
        status('%s [%s]' % (msg, ''.join(bar)))
        sublime.set_timeout(lambda: handle_thread(thread, msg, cb, i,
                            direction, width), 100)
    else:
        cb()

def get_login_name():
    settings = sublime.load_settings('meetrice.sublime-settings')
    login_name = settings.get('login_name')

    if not login_name:
        sublime.error_message("No Login name found in settings")

    return login_name

def get_login_password():
    settings = sublime.load_settings('meetrice.sublime-settings')
    login_password = settings.get('login_password')

    if not login_password:
        sublime.error_message("No login_password found in settings")

    return login_password

def get_xml_rpc_url():
    settings = sublime.load_settings('meetrice.sublime-settings')
    xml_rpc_url = settings.get('xml_rpc_url')

    if not xml_rpc_url:
        sublime.error_message("No login_password found in settings")

    return xml_rpc_url

class NewPostCommand(sublime_plugin.TextCommand):
    """Search for snippet and insert it into document at cursor position."""

    def run(self, edit):

        self.login_name = get_login_name()
        print(self.login_name);
        self.login_password = get_login_password()
        self.url = get_xml_rpc_url()

        regions = self.view.sel()
        if not (len(regions) > 0) or (regions[0].empty()):
            status("Error: not text selected")
            return

        self.server = ServerProxy(self.url)

        self.post = {'title':'sublime默认标题',
                'description':self.view.substr(regions[0]),
                'link':'',
                'author':'meetrice@gmail.com',
                'mt_keywords':'测试标签',
                'category':''
            }

        self.title_prompt()

    def title_prompt(self):
        self.view.window().show_input_panel("title", "", 
                                            self.title_cb, None, None)

    def title_cb(self, title):
        self.post['title'] = title
        self.tags_prompt()

    def tags_prompt(self):
        self.view.window().show_input_panel("tag(use ',' to splite", "",
                                            self.tags_cb, None, None)   
    def tags_cb(self, tags):
        self.post['mt_keywords'] = tags    
        t = threading.Thread(target=self.new_post)
        t.start()
        handle_thread(t, 'Publishing ...')        


    def new_post(self):
        print("new_post")
        try:
            result = self.server.metaWeblog.newPost("", self.login_name,self.login_password, self.post,True)

            if len(result) > 0:
                status('Successful', True)
            else:
                status('Error', True)
        except Error as e:
            print 'new post error is: %s' % e
            status('Error', True)                                     
      