#!/usr/bin/env python3

import socket, time
import logging
import threading


log = logging.getLogger('vlcsign')

class Player():
    # Initial code and awareness of the telnet interface from:
    # https://stackoverflow.com/questions/56103533/how-can-i-control-vlc-media-player-through-a-python-scripte
    def __init__(self):
        self.is_initiated = False
        self.SEEK_TIME = 20
        self.MAX_VOL = 512
        self.MIN_VOL = 0
        self.DEFAULT_VOL = 256
        self.VOL_STEP = 13
        self.current_vol = self.DEFAULT_VOL

    def toggle_play(self):
        if not self.is_initiated:
            self.is_initiated = True
            self.thrededreq("loop on")
            self.thrededreq("random on")
            self.thrededreq("add /home/pi/git/vlcsigner/content")#adding the music folder
            print("Init Playing")
            return
        self.thrededreq("pause")
        print("Toggle play")

    def fullscreenon(self):
        self.thrededreq('fullscreen on')
    def fullscreenoff(self):
        self.thrededreq('fullscreen off')

    def next(self):
        if not self.is_initiated:
            self.toggle_play()
            return
        self.thrededreq("next")
        print("Next")
        pass

    def pause(self):
        # if not self.is_initiated:
        #     self.toggle_play()
        #     return
        self.thrededreq("pause")
        print("pause")
        pass

    def prev(self):
        if not self.is_initiated:
            self.toggle_play()
            return
        self.thrededreq("prev")
        print("Previous")
        pass

    def volup(self):
        self.current_vol = self.current_vol + self.VOL_STEP
        self.thrededreq("volume " + str(self.current_vol))
        print("Volume up")
        pass

    def voldown(self):
        self.current_vol = self.current_vol - self.VOL_STEP
        self.thrededreq("volume " + str(self.current_vol))
        print("Volume Down")
        pass

    def seek(self, forward: bool):
        length = self._timeinfo("get_length")
        print(length)
        cur = self._timeinfo("get_time")
        print(cur)
        if (forward):
            seekable = cur + self.SEEK_TIME
        else:
            seekable = cur - self.SEEK_TIME
        if seekable > length:
            seekable = length - 5
        if seekable < 0:
            seekable = 0
        self.thrededreq("seek " + str(seekable))
        print("Seek: ",seekable," Cur: ",cur,"Len: ",length)
        pass

    def _timeinfo(self, msg):
        length = self.req(msg, True).split("\r\n")
        if (len(length) < 2):
            return None
        length = length[1].split(" ")
        if (len(length) < 2):
            return None
        try:
            num = int(length[1])
            return num
        except:
            return None

    def req(self, msg: str, full=False):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Connect to server and send data
                sock.settimeout(0.7)
                sock.connect(('127.0.0.1', 44500))
                response = ""
                received = ""
                sock.sendall(bytes(msg + '\n', "utf-8"))
                # if True:
                try:
                    while (True):
                        received = (sock.recv(1024)).decode()
                        response = response + received
                        if full:
                            b = response.count("\r\n")
                            if response.count("\r\n") > 1:
                                sock.close()
                                break
                        else:
                            if response.count("\r\n") > 0:
                                sock.close()
                                break
                except:
                    response = response + received
                    pass
                sock.close()
                return response
        except:
            return None
            pass

    def thrededreq(self, msg):
        threading.Thread(target=self.req, args=(msg,)).start()

    def fullblack(self):
        seq = '''
        clear
        add /opt/vlcsigner/gray.png
        fullscreen on
        '''
        self.thrededreq(seq)
        # self.threadreq("")
        # self.threadreq("")
    def _delete_(self):
        self.thrededreq('quit')
        
#'vlc --intf rc --rc-host 127.0.0.1:44500' you need to run the vlc player from command line to allo controlling it via TCP
player=Player()
player.toggle_play()
#player.next()
#player.prev()
# player.pause()
# player.fullscreenon()
# player.fullscreenoff()
# player.fullblack()