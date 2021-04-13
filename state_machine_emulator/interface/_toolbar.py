from tkinter import *

"""
    build the toolbar with associated call back functions
"""


def quit_callback(self):
    self.__del__()


def step_callback(self):
    # print('do one step')
    if self.current_clock < self.max_clock-1:
        self.current_clock += 1
    else:
        print("step_callback: already at max")
    self.update_display()


def restart_callback(self):
    # print('restart')
    self.current_clock = 0
    self.update_display()


def step_back_callback(self):
    # print('do one step back')
    if self.current_clock > 0:
        self.current_clock -= 1
    else:
        print("step_back_callback: already at clock 0")
    self.update_display()


def step_10_callback(self):
    # print('do 10 steps')
    if self.current_clock < self.max_clock-10:
        self.current_clock += 10
    else:
        self.current_clock = self.max_clock-1
    self.update_display()


def step_10_back_callback(self):
    # print('do 10 steps back')
    if self.current_clock >= 10:
        self.current_clock -= 10
    else:
        self.current_clock = 0
    self.update_display()


def step_50_callback(self):
    # print('do 50 steps')
    if self.current_clock < self.max_clock-50:
        self.current_clock += 50
    else:
        self.current_clock = self.max_clock-1
    self.update_display()


def step_50_back_callback(self):
    # print('do 50 steps back')
    if self.current_clock >= 50:
        self.current_clock -= 50
    else:
        self.current_clock = 0
    self.update_display()


def build_toolbar(self):
    """ build the toolbar """
    self.toolbar = Frame(self.root, borderwidth=2, relief='raised')
    self.toolbar.grid(row=0, columnspan=4, padx=10, pady=2, sticky="EW")

    self.restart_button = Button(
        self.toolbar, text="Restart", command=lambda: self.restart_callback())
    self.restart_button.pack(side=LEFT, fill=NONE)
    self.step_50_back_button = Button(
        self.toolbar, text="Back50", command=lambda: self.step_50_back_callback())
    self.step_50_back_button.pack(side=LEFT, fill=NONE)
    self.step_10_back_button = Button(
        self.toolbar, text="Back10", command=lambda: self.step_10_back_callback())
    self.step_10_back_button.pack(side=LEFT, fill=NONE)
    self.step_back_button = Button(
        self.toolbar, text="Back", command=lambda: self.step_back_callback())
    self.step_back_button.pack(side=LEFT, fill=NONE)
    self.step_button = Button(
        self.toolbar, text="Step", command=lambda: self.step_callback())
    self.step_button.pack(side=LEFT, fill=NONE)
    self.step_10_button = Button(
        self.toolbar, text="Step10", command=lambda: self.step_10_callback())
    self.step_10_button.pack(side=LEFT, fill=NONE)
    self.step_50_button = Button(
        self.toolbar, text="Step50", command=lambda: self.step_50_callback())
    self.step_50_button.pack(side=LEFT, fill=NONE)

    self.quit_button = Button(
        self.toolbar, text="Quit", command=lambda: self.quit_callback())
    self.quit_button.pack(side=RIGHT, fill=NONE)