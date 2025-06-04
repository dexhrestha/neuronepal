#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Wed Jun  4 12:26:45 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from expSetup_env
# import libraries
import random
from psychopy import event
#defining global variables

experimentExpired = False
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'TemporalReproduction'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/dexhrestha/Documents/Portfolio/neuronepal/neuronepal/psychopy/TemporalReproduction.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[-0.0000, 0.0000, 0.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='deg',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-0.0000, 0.0000, 0.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'deg'
    if expInfo is not None:
        expInfo['frameRate'] = 60
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('keyWelcome') is None:
        # initialise keyWelcome
        keyWelcome = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyWelcome',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('respKeyPress') is None:
        # initialise respKeyPress
        respKeyPress = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respKeyPress',
        )
    if deviceManager.getDevice('respKeyRelease') is None:
        # initialise respKeyRelease
        respKeyRelease = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respKeyRelease',
        )
    if deviceManager.getDevice('feedbackResp') is None:
        # initialise feedbackResp
        feedbackResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='feedbackResp',
        )
    if deviceManager.getDevice('breakResp') is None:
        # initialise breakResp
        breakResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='breakResp',
        )
    if deviceManager.getDevice('keyEnd') is None:
        # initialise keyEnd
        keyEnd = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyEnd',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcomeRoutine" ---
    welcomeText = visual.TextStim(win=win, name='welcomeText',
        text='Temporal Reproduction Task\n\nYou will see brief flashes of light in a temporal pattern. Then, you need to press the spacebar to repeat the pattern of flashes.\n\n ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.75, wrapWidth=25.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyWelcome = keyboard.Keyboard(deviceName='keyWelcome')
    
    # --- Initialize components for Routine "expSetup" ---
    # Run 'Begin Experiment' code from expSetup_env
    # Environment variables
    totalTime  = 3525/1000.
    
    startTimes = [0,325,1025,1500,2400,3500]
    #startTimes = [400,800,1200,1600,2000,2400]
    startTimes = [x/1000. for x in startTimes] 
    
    min_val = min(startTimes)
    max_val = max(startTimes)
    
    normTimes = [((x - min_val) / (max_val - min_val)) * 20 - 10 for x in startTimes]
    
    
    respTimes = [-10,-10,-10,-10,-10,-10]
    normRespTimes =[-10,-10,-10,-10,-10,-10]
    normRespTimes_orig = [-10,-10,-10,-10,-10,-10]
    
    speedOptions = [ 0.5, 0.66,1, 1.5, 2]
    #speedOptions = [1,1,1,1,1]
    
    # --- Initialize components for Routine "blockSetup" ---
    
    # --- Initialize components for Routine "trial" ---
    stimulusWhite1 = visual.ShapeStim(
        win=win, name='stimulusWhite1',
        size=(5, 5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    stimulusWhite2 = visual.ShapeStim(
        win=win, name='stimulusWhite2',
        size=(5, 5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    stimulusWhite3 = visual.ShapeStim(
        win=win, name='stimulusWhite3',
        size=(5, 5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    stimulusWhite4 = visual.ShapeStim(
        win=win, name='stimulusWhite4',
        size=(5, 5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    stimulusWhite5 = visual.ShapeStim(
        win=win, name='stimulusWhite5',
        size=(5, 5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    stimulusWhite6 = visual.ShapeStim(
        win=win, name='stimulusWhite6',
        size=(5, 5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    fixationRed = visual.ShapeStim(
        win=win, name='fixationRed',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-6.0, interpolate=True)
    statusText = visual.TextStim(win=win, name='statusText',
        text='Press spacebar and reproduce the pattern.',
        font='Arial',
        pos=(0, -0.8), draggable=False, height=0.6, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "testRoutine" ---
    respKeyPress = keyboard.Keyboard(deviceName='respKeyPress')
    respKeyRelease = keyboard.Keyboard(deviceName='respKeyRelease')
    responseGreen = visual.ShapeStim(
        win=win, name='responseGreen',
        size=(5, 5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=[-1.0000, 1.0000, -1.0000],
        opacity=0.0, depth=-3.0, interpolate=True)
    fixationRedTest = visual.ShapeStim(
        win=win, name='fixationRedTest',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-4.0, interpolate=True)
    
    # --- Initialize components for Routine "feedbackRoutine" ---
    stimBar = visual.Rect(
        win=win, name='stimBar',
        width=(20, 1)[0], height=(20, 1)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    responseBar = visual.Rect(
        win=win, name='responseBar',
        width=(stimBar.width, stimBar.height)[0], height=(stimBar.width, stimBar.height)[1],
        ori=0.0, pos=(stimBar.pos[0], stimBar.pos[1]-3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    feedbackResp = keyboard.Keyboard(deviceName='feedbackResp')
    stim1Pos = visual.Rect(
        win=win, name='stim1Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normTimes[0], stimBar.pos[1]), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=-4.0, interpolate=True)
    stim2Pos = visual.Rect(
        win=win, name='stim2Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normTimes[1], stimBar.pos[1]), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=-5.0, interpolate=True)
    stim3Pos = visual.Rect(
        win=win, name='stim3Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normTimes[2], stimBar.pos[1]), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=-6.0, interpolate=True)
    stim4Pos = visual.Rect(
        win=win, name='stim4Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normTimes[3], stimBar.pos[1]), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=-7.0, interpolate=True)
    stim5Pos = visual.Rect(
        win=win, name='stim5Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normTimes[4], stimBar.pos[1]), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=-8.0, interpolate=True)
    stim6Pos = visual.Rect(
        win=win, name='stim6Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normTimes[5], stimBar.pos[1]), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, 1.0000], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=-9.0, interpolate=True)
    resp1Pos = visual.Rect(
        win=win, name='resp1Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normRespTimes[0], stimBar.pos[1]-3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
        opacity=None, depth=-10.0, interpolate=True)
    resp2Pos = visual.Rect(
        win=win, name='resp2Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normRespTimes[1], stimBar.pos[1]-3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
        opacity=None, depth=-11.0, interpolate=True)
    resp3Pos = visual.Rect(
        win=win, name='resp3Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normRespTimes[2], stimBar.pos[1]-3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
        opacity=None, depth=-12.0, interpolate=True)
    resp4Pos = visual.Rect(
        win=win, name='resp4Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normRespTimes[3], stimBar.pos[1]-3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
        opacity=None, depth=-13.0, interpolate=True)
    resp5Pos = visual.Rect(
        win=win, name='resp5Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normRespTimes[4], stimBar.pos[1]-3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
        opacity=None, depth=-14.0, interpolate=True)
    resp6Pos = visual.Rect(
        win=win, name='resp6Pos',
        width=(0.5, stimBar.height)[0], height=(0.5, stimBar.height)[1],
        ori=0.0, pos=(normRespTimes[5], stimBar.pos[1]-3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
        opacity=None, depth=-15.0, interpolate=True)
    corrText = visual.TextStim(win=win, name='corrText',
        text='Score: ',
        font='Arial',
        pos=(10, 10), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-16.0);
    
    # --- Initialize components for Routine "breakRoutine" ---
    breakText = visual.TextStim(win=win, name='breakText',
        text='End of this block.\nTake a rest and press space whenever you are ready to proceed to the next block.',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    breakResp = keyboard.Keyboard(deviceName='breakResp')
    
    # --- Initialize components for Routine "endRoutine" ---
    completionText = visual.TextStim(win=win, name='completionText',
        text='Thank you for your time.\n\nPress space or escape key to exit.',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyEnd = keyboard.Keyboard(deviceName='keyEnd')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcomeRoutine" ---
    # create an object to store info about Routine welcomeRoutine
    welcomeRoutine = data.Routine(
        name='welcomeRoutine',
        components=[welcomeText, keyWelcome],
    )
    welcomeRoutine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyWelcome
    keyWelcome.keys = []
    keyWelcome.rt = []
    _keyWelcome_allKeys = []
    # store start times for welcomeRoutine
    welcomeRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcomeRoutine.tStart = globalClock.getTime(format='float')
    welcomeRoutine.status = STARTED
    thisExp.addData('welcomeRoutine.started', welcomeRoutine.tStart)
    welcomeRoutine.maxDuration = None
    # keep track of which components have finished
    welcomeRoutineComponents = welcomeRoutine.components
    for thisComponent in welcomeRoutine.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcomeRoutine" ---
    welcomeRoutine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcomeText* updates
        
        # if welcomeText is starting this frame...
        if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcomeText.frameNStart = frameN  # exact frame index
            welcomeText.tStart = t  # local t and not account for scr refresh
            welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcomeText.started')
            # update status
            welcomeText.status = STARTED
            welcomeText.setAutoDraw(True)
        
        # if welcomeText is active this frame...
        if welcomeText.status == STARTED:
            # update params
            pass
        
        # *keyWelcome* updates
        waitOnFlip = False
        
        # if keyWelcome is starting this frame...
        if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyWelcome.frameNStart = frameN  # exact frame index
            keyWelcome.tStart = t  # local t and not account for scr refresh
            keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyWelcome.started')
            # update status
            keyWelcome.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyWelcome.status == STARTED and not waitOnFlip:
            theseKeys = keyWelcome.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyWelcome_allKeys.extend(theseKeys)
            if len(_keyWelcome_allKeys):
                keyWelcome.keys = _keyWelcome_allKeys[-1].name  # just the last key pressed
                keyWelcome.rt = _keyWelcome_allKeys[-1].rt
                keyWelcome.duration = _keyWelcome_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcomeRoutine.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcomeRoutine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcomeRoutine" ---
    for thisComponent in welcomeRoutine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcomeRoutine
    welcomeRoutine.tStop = globalClock.getTime(format='float')
    welcomeRoutine.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcomeRoutine.stopped', welcomeRoutine.tStop)
    thisExp.nextEntry()
    # the Routine "welcomeRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "expSetup" ---
    # create an object to store info about Routine expSetup
    expSetup = data.Routine(
        name='expSetup',
        components=[],
    )
    expSetup.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from expSetup_env
    # each block within a block mode  has different speed and visual mode
    random.seed(42)
    
    
    # speedOptions = [ 1,1,1,1,1]
    
    random.shuffle(speedOptions)
    
    
    # store start times for expSetup
    expSetup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    expSetup.tStart = globalClock.getTime(format='float')
    expSetup.status = STARTED
    thisExp.addData('expSetup.started', expSetup.tStart)
    expSetup.maxDuration = None
    # keep track of which components have finished
    expSetupComponents = expSetup.components
    for thisComponent in expSetup.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "expSetup" ---
    expSetup.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            expSetup.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in expSetup.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "expSetup" ---
    for thisComponent in expSetup.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for expSetup
    expSetup.tStop = globalClock.getTime(format='float')
    expSetup.tStopRefresh = tThisFlipGlobal
    thisExp.addData('expSetup.stopped', expSetup.tStop)
    thisExp.nextEntry()
    # the Routine "expSetup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    speedBlock = data.TrialHandler2(
        name='speedBlock',
        nReps=len(speedOptions), 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(speedBlock)  # add the loop to the experiment
    thisSpeedBlock = speedBlock.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSpeedBlock.rgb)
    if thisSpeedBlock != None:
        for paramName in thisSpeedBlock:
            globals()[paramName] = thisSpeedBlock[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisSpeedBlock in speedBlock:
        currentLoop = speedBlock
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisSpeedBlock.rgb)
        if thisSpeedBlock != None:
            for paramName in thisSpeedBlock:
                globals()[paramName] = thisSpeedBlock[paramName]
        
        # --- Prepare to start Routine "blockSetup" ---
        # create an object to store info about Routine blockSetup
        blockSetup = data.Routine(
            name='blockSetup',
            components=[],
        )
        blockSetup.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from blockSetupCode
        speed = speedOptions[speedBlock.thisN]
        startTimes = [0,325,1025,1500,2400,3500]
        #startTimes = [0,400,800,1200,1600,2000]
        startTimes = [(x*speed)/1000. for x in startTimes] 
        
        # store start times for blockSetup
        blockSetup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blockSetup.tStart = globalClock.getTime(format='float')
        blockSetup.status = STARTED
        thisExp.addData('blockSetup.started', blockSetup.tStart)
        blockSetup.maxDuration = None
        # keep track of which components have finished
        blockSetupComponents = blockSetup.components
        for thisComponent in blockSetup.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blockSetup" ---
        # if trial has changed, end Routine now
        if isinstance(speedBlock, data.TrialHandler2) and thisSpeedBlock.thisN != speedBlock.thisTrial.thisN:
            continueRoutine = False
        blockSetup.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blockSetup.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockSetup.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blockSetup" ---
        for thisComponent in blockSetup.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blockSetup
        blockSetup.tStop = globalClock.getTime(format='float')
        blockSetup.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blockSetup.stopped', blockSetup.tStop)
        # the Routine "blockSetup" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trialBlock = data.TrialHandler2(
            name='trialBlock',
            nReps=4.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(trialBlock)  # add the loop to the experiment
        thisTrialBlock = trialBlock.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrialBlock.rgb)
        if thisTrialBlock != None:
            for paramName in thisTrialBlock:
                globals()[paramName] = thisTrialBlock[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrialBlock in trialBlock:
            currentLoop = trialBlock
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrialBlock.rgb)
            if thisTrialBlock != None:
                for paramName in thisTrialBlock:
                    globals()[paramName] = thisTrialBlock[paramName]
            
            # set up handler to look after randomisation of conditions etc
            trials = data.TrialHandler2(
                name='trials',
                nReps=15.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(trials)  # add the loop to the experiment
            thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            for thisTrial in trials:
                currentLoop = trials
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
                if thisTrial != None:
                    for paramName in thisTrial:
                        globals()[paramName] = thisTrial[paramName]
                
                # --- Prepare to start Routine "trial" ---
                # create an object to store info about Routine trial
                trial = data.Routine(
                    name='trial',
                    components=[stimulusWhite1, stimulusWhite2, stimulusWhite3, stimulusWhite4, stimulusWhite5, stimulusWhite6, fixationRed, statusText, key_resp],
                )
                trial.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # create starting attributes for key_resp
                key_resp.keys = []
                key_resp.rt = []
                _key_resp_allKeys = []
                # store start times for trial
                trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                trial.tStart = globalClock.getTime(format='float')
                trial.status = STARTED
                thisExp.addData('trial.started', trial.tStart)
                trial.maxDuration = None
                # keep track of which components have finished
                trialComponents = trial.components
                for thisComponent in trial.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "trial" ---
                # if trial has changed, end Routine now
                if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                    continueRoutine = False
                trial.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *stimulusWhite1* updates
                    
                    # if stimulusWhite1 is starting this frame...
                    if stimulusWhite1.status == NOT_STARTED and tThisFlip >= startTimes[0]-frameTolerance:
                        # keep track of start time/frame for later
                        stimulusWhite1.frameNStart = frameN  # exact frame index
                        stimulusWhite1.tStart = t  # local t and not account for scr refresh
                        stimulusWhite1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stimulusWhite1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulusWhite1.started')
                        # update status
                        stimulusWhite1.status = STARTED
                        stimulusWhite1.setAutoDraw(True)
                    
                    # if stimulusWhite1 is active this frame...
                    if stimulusWhite1.status == STARTED:
                        # update params
                        pass
                    
                    # if stimulusWhite1 is stopping this frame...
                    if stimulusWhite1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > stimulusWhite1.tStartRefresh + 0.025-frameTolerance:
                            # keep track of stop time/frame for later
                            stimulusWhite1.tStop = t  # not accounting for scr refresh
                            stimulusWhite1.tStopRefresh = tThisFlipGlobal  # on global time
                            stimulusWhite1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'stimulusWhite1.stopped')
                            # update status
                            stimulusWhite1.status = FINISHED
                            stimulusWhite1.setAutoDraw(False)
                    
                    # *stimulusWhite2* updates
                    
                    # if stimulusWhite2 is starting this frame...
                    if stimulusWhite2.status == NOT_STARTED and tThisFlip >= startTimes[1]-frameTolerance:
                        # keep track of start time/frame for later
                        stimulusWhite2.frameNStart = frameN  # exact frame index
                        stimulusWhite2.tStart = t  # local t and not account for scr refresh
                        stimulusWhite2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stimulusWhite2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulusWhite2.started')
                        # update status
                        stimulusWhite2.status = STARTED
                        stimulusWhite2.setAutoDraw(True)
                    
                    # if stimulusWhite2 is active this frame...
                    if stimulusWhite2.status == STARTED:
                        # update params
                        pass
                    
                    # if stimulusWhite2 is stopping this frame...
                    if stimulusWhite2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > stimulusWhite2.tStartRefresh + 0.025-frameTolerance:
                            # keep track of stop time/frame for later
                            stimulusWhite2.tStop = t  # not accounting for scr refresh
                            stimulusWhite2.tStopRefresh = tThisFlipGlobal  # on global time
                            stimulusWhite2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'stimulusWhite2.stopped')
                            # update status
                            stimulusWhite2.status = FINISHED
                            stimulusWhite2.setAutoDraw(False)
                    
                    # *stimulusWhite3* updates
                    
                    # if stimulusWhite3 is starting this frame...
                    if stimulusWhite3.status == NOT_STARTED and tThisFlip >= startTimes[2]-frameTolerance:
                        # keep track of start time/frame for later
                        stimulusWhite3.frameNStart = frameN  # exact frame index
                        stimulusWhite3.tStart = t  # local t and not account for scr refresh
                        stimulusWhite3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stimulusWhite3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulusWhite3.started')
                        # update status
                        stimulusWhite3.status = STARTED
                        stimulusWhite3.setAutoDraw(True)
                    
                    # if stimulusWhite3 is active this frame...
                    if stimulusWhite3.status == STARTED:
                        # update params
                        pass
                    
                    # if stimulusWhite3 is stopping this frame...
                    if stimulusWhite3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > stimulusWhite3.tStartRefresh + 0.025-frameTolerance:
                            # keep track of stop time/frame for later
                            stimulusWhite3.tStop = t  # not accounting for scr refresh
                            stimulusWhite3.tStopRefresh = tThisFlipGlobal  # on global time
                            stimulusWhite3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'stimulusWhite3.stopped')
                            # update status
                            stimulusWhite3.status = FINISHED
                            stimulusWhite3.setAutoDraw(False)
                    
                    # *stimulusWhite4* updates
                    
                    # if stimulusWhite4 is starting this frame...
                    if stimulusWhite4.status == NOT_STARTED and tThisFlip >= startTimes[3]-frameTolerance:
                        # keep track of start time/frame for later
                        stimulusWhite4.frameNStart = frameN  # exact frame index
                        stimulusWhite4.tStart = t  # local t and not account for scr refresh
                        stimulusWhite4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stimulusWhite4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulusWhite4.started')
                        # update status
                        stimulusWhite4.status = STARTED
                        stimulusWhite4.setAutoDraw(True)
                    
                    # if stimulusWhite4 is active this frame...
                    if stimulusWhite4.status == STARTED:
                        # update params
                        pass
                    
                    # if stimulusWhite4 is stopping this frame...
                    if stimulusWhite4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > stimulusWhite4.tStartRefresh + 0.025-frameTolerance:
                            # keep track of stop time/frame for later
                            stimulusWhite4.tStop = t  # not accounting for scr refresh
                            stimulusWhite4.tStopRefresh = tThisFlipGlobal  # on global time
                            stimulusWhite4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'stimulusWhite4.stopped')
                            # update status
                            stimulusWhite4.status = FINISHED
                            stimulusWhite4.setAutoDraw(False)
                    
                    # *stimulusWhite5* updates
                    
                    # if stimulusWhite5 is starting this frame...
                    if stimulusWhite5.status == NOT_STARTED and tThisFlip >= startTimes[4]-frameTolerance:
                        # keep track of start time/frame for later
                        stimulusWhite5.frameNStart = frameN  # exact frame index
                        stimulusWhite5.tStart = t  # local t and not account for scr refresh
                        stimulusWhite5.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stimulusWhite5, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulusWhite5.started')
                        # update status
                        stimulusWhite5.status = STARTED
                        stimulusWhite5.setAutoDraw(True)
                    
                    # if stimulusWhite5 is active this frame...
                    if stimulusWhite5.status == STARTED:
                        # update params
                        pass
                    
                    # if stimulusWhite5 is stopping this frame...
                    if stimulusWhite5.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > stimulusWhite5.tStartRefresh + 0.025-frameTolerance:
                            # keep track of stop time/frame for later
                            stimulusWhite5.tStop = t  # not accounting for scr refresh
                            stimulusWhite5.tStopRefresh = tThisFlipGlobal  # on global time
                            stimulusWhite5.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'stimulusWhite5.stopped')
                            # update status
                            stimulusWhite5.status = FINISHED
                            stimulusWhite5.setAutoDraw(False)
                    
                    # *stimulusWhite6* updates
                    
                    # if stimulusWhite6 is starting this frame...
                    if stimulusWhite6.status == NOT_STARTED and tThisFlip >= startTimes[5]-frameTolerance:
                        # keep track of start time/frame for later
                        stimulusWhite6.frameNStart = frameN  # exact frame index
                        stimulusWhite6.tStart = t  # local t and not account for scr refresh
                        stimulusWhite6.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stimulusWhite6, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulusWhite6.started')
                        # update status
                        stimulusWhite6.status = STARTED
                        stimulusWhite6.setAutoDraw(True)
                    
                    # if stimulusWhite6 is active this frame...
                    if stimulusWhite6.status == STARTED:
                        # update params
                        pass
                    
                    # if stimulusWhite6 is stopping this frame...
                    if stimulusWhite6.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > stimulusWhite6.tStartRefresh + 0.025-frameTolerance:
                            # keep track of stop time/frame for later
                            stimulusWhite6.tStop = t  # not accounting for scr refresh
                            stimulusWhite6.tStopRefresh = tThisFlipGlobal  # on global time
                            stimulusWhite6.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'stimulusWhite6.stopped')
                            # update status
                            stimulusWhite6.status = FINISHED
                            stimulusWhite6.setAutoDraw(False)
                    
                    # *fixationRed* updates
                    
                    # if fixationRed is starting this frame...
                    if fixationRed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixationRed.frameNStart = frameN  # exact frame index
                        fixationRed.tStart = t  # local t and not account for scr refresh
                        fixationRed.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixationRed, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixationRed.started')
                        # update status
                        fixationRed.status = STARTED
                        fixationRed.setAutoDraw(True)
                    
                    # if fixationRed is active this frame...
                    if fixationRed.status == STARTED:
                        # update params
                        pass
                    
                    # if fixationRed is stopping this frame...
                    if fixationRed.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixationRed.tStartRefresh + startTimes[5]-frameTolerance:
                            # keep track of stop time/frame for later
                            fixationRed.tStop = t  # not accounting for scr refresh
                            fixationRed.tStopRefresh = tThisFlipGlobal  # on global time
                            fixationRed.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixationRed.stopped')
                            # update status
                            fixationRed.status = FINISHED
                            fixationRed.setAutoDraw(False)
                    
                    # *statusText* updates
                    
                    # if statusText is starting this frame...
                    if statusText.status == NOT_STARTED and tThisFlip >= startTimes[5]+0.025-frameTolerance:
                        # keep track of start time/frame for later
                        statusText.frameNStart = frameN  # exact frame index
                        statusText.tStart = t  # local t and not account for scr refresh
                        statusText.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(statusText, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'statusText.started')
                        # update status
                        statusText.status = STARTED
                        statusText.setAutoDraw(True)
                    
                    # if statusText is active this frame...
                    if statusText.status == STARTED:
                        # update params
                        pass
                    # Run 'Each Frame' code from stimulusCode
                    try:
                        statusText.text = f"""Speed: {speed}  \n 
                    1 : {startTimes[0]*speed:.2f},{stimulusWhite1.tStart:.2f} \n 
                    2 : {startTimes[1]*speed:.2f},{stimulusWhite2.tStart:.2f} \n 
                    3 : {startTimes[2]*speed:.2f},{stimulusWhite3.tStart:.2f}\n 
                    4 : {startTimes[3]*speed:.2f},{stimulusWhite4.tStart:.2f}\n 
                    5 : {startTimes[4]*speed:.2f},{stimulusWhite5.tStart:.2f}\n 
                    6 : {startTimes[5]*speed:.2f},{stimulusWhite6.tStart:.2f}"""
                    except:
                        statusText.text = ''
                    statusText.text = 'Press spacebar and reproduce the pattern.'
                    
                    thisExp.addData('speed',speed)
                    thisExp.addData('startTimes',startTimes)
                    
                    # *key_resp* updates
                    waitOnFlip = False
                    
                    # if key_resp is starting this frame...
                    if key_resp.status == NOT_STARTED and tThisFlip >= startTimes[5]+0.025-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp.frameNStart = frameN  # exact frame index
                        key_resp.tStart = t  # local t and not account for scr refresh
                        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp.started')
                        # update status
                        key_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_allKeys.extend(theseKeys)
                        if len(_key_resp_allKeys):
                            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                            key_resp.rt = _key_resp_allKeys[-1].rt
                            key_resp.duration = _key_resp_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        trial.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trial.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "trial" ---
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for trial
                trial.tStop = globalClock.getTime(format='float')
                trial.tStopRefresh = tThisFlipGlobal
                thisExp.addData('trial.stopped', trial.tStop)
                # check responses
                if key_resp.keys in ['', [], None]:  # No response was made
                    key_resp.keys = None
                trials.addData('key_resp.keys',key_resp.keys)
                if key_resp.keys != None:  # we had a response
                    trials.addData('key_resp.rt', key_resp.rt)
                    trials.addData('key_resp.duration', key_resp.duration)
                # the Routine "trial" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "testRoutine" ---
                # create an object to store info about Routine testRoutine
                testRoutine = data.Routine(
                    name='testRoutine',
                    components=[respKeyPress, respKeyRelease, responseGreen, fixationRedTest],
                )
                testRoutine.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # create starting attributes for respKeyPress
                respKeyPress.keys = []
                respKeyPress.rt = []
                _respKeyPress_allKeys = []
                # create starting attributes for respKeyRelease
                respKeyRelease.keys = []
                respKeyRelease.rt = []
                _respKeyRelease_allKeys = []
                # store start times for testRoutine
                testRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                testRoutine.tStart = globalClock.getTime(format='float')
                testRoutine.status = STARTED
                thisExp.addData('testRoutine.started', testRoutine.tStart)
                testRoutine.maxDuration = None
                # keep track of which components have finished
                testRoutineComponents = testRoutine.components
                for thisComponent in testRoutine.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "testRoutine" ---
                # if trial has changed, end Routine now
                if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                    continueRoutine = False
                testRoutine.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *respKeyPress* updates
                    waitOnFlip = False
                    
                    # if respKeyPress is starting this frame...
                    if respKeyPress.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        respKeyPress.frameNStart = frameN  # exact frame index
                        respKeyPress.tStart = t  # local t and not account for scr refresh
                        respKeyPress.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(respKeyPress, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'respKeyPress.started')
                        # update status
                        respKeyPress.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(respKeyPress.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(respKeyPress.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if respKeyPress is stopping this frame...
                    if respKeyPress.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > respKeyPress.tStartRefresh + startTimes[5]+0.025+2-frameTolerance:
                            # keep track of stop time/frame for later
                            respKeyPress.tStop = t  # not accounting for scr refresh
                            respKeyPress.tStopRefresh = tThisFlipGlobal  # on global time
                            respKeyPress.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'respKeyPress.stopped')
                            # update status
                            respKeyPress.status = FINISHED
                            respKeyPress.status = FINISHED
                    if respKeyPress.status == STARTED and not waitOnFlip:
                        theseKeys = respKeyPress.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _respKeyPress_allKeys.extend(theseKeys)
                        if len(_respKeyPress_allKeys):
                            respKeyPress.keys = [key.name for key in _respKeyPress_allKeys]  # storing all keys
                            respKeyPress.rt = [key.rt for key in _respKeyPress_allKeys]
                            respKeyPress.duration = [key.duration for key in _respKeyPress_allKeys]
                    
                    # *respKeyRelease* updates
                    waitOnFlip = False
                    
                    # if respKeyRelease is starting this frame...
                    if respKeyRelease.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        respKeyRelease.frameNStart = frameN  # exact frame index
                        respKeyRelease.tStart = t  # local t and not account for scr refresh
                        respKeyRelease.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(respKeyRelease, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'respKeyRelease.started')
                        # update status
                        respKeyRelease.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(respKeyRelease.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(respKeyRelease.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if respKeyRelease is stopping this frame...
                    if respKeyRelease.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > respKeyRelease.tStartRefresh + startTimes[5]+0.025+2-frameTolerance:
                            # keep track of stop time/frame for later
                            respKeyRelease.tStop = t  # not accounting for scr refresh
                            respKeyRelease.tStopRefresh = tThisFlipGlobal  # on global time
                            respKeyRelease.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'respKeyRelease.stopped')
                            # update status
                            respKeyRelease.status = FINISHED
                            respKeyRelease.status = FINISHED
                    if respKeyRelease.status == STARTED and not waitOnFlip:
                        theseKeys = respKeyRelease.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=True)
                        _respKeyRelease_allKeys.extend(theseKeys)
                        if len(_respKeyRelease_allKeys):
                            respKeyRelease.keys = [key.name for key in _respKeyRelease_allKeys]  # storing all keys
                            respKeyRelease.rt = [key.rt for key in _respKeyRelease_allKeys]
                            respKeyRelease.duration = [key.duration for key in _respKeyRelease_allKeys]
                    # Run 'Each Frame' code from testCode
                    if len(respKeyRelease.keys)>len(respKeyPress.keys):
                        responseGreen.opacity = 0
                        win.flip()
                    else:
                        responseGreen.opacity = 1
                        win.flip()
                        
                    if len(respKeyPress.keys) == 5:
                        continueRoutine = False
                    
                    
                    # *responseGreen* updates
                    
                    # if responseGreen is starting this frame...
                    if responseGreen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        responseGreen.frameNStart = frameN  # exact frame index
                        responseGreen.tStart = t  # local t and not account for scr refresh
                        responseGreen.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(responseGreen, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'responseGreen.started')
                        # update status
                        responseGreen.status = STARTED
                        responseGreen.setAutoDraw(True)
                    
                    # if responseGreen is active this frame...
                    if responseGreen.status == STARTED:
                        # update params
                        pass
                    
                    # if responseGreen is stopping this frame...
                    if responseGreen.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > responseGreen.tStartRefresh + startTimes[5]+0.025+2-frameTolerance:
                            # keep track of stop time/frame for later
                            responseGreen.tStop = t  # not accounting for scr refresh
                            responseGreen.tStopRefresh = tThisFlipGlobal  # on global time
                            responseGreen.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'responseGreen.stopped')
                            # update status
                            responseGreen.status = FINISHED
                            responseGreen.setAutoDraw(False)
                    
                    # *fixationRedTest* updates
                    
                    # if fixationRedTest is starting this frame...
                    if fixationRedTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixationRedTest.frameNStart = frameN  # exact frame index
                        fixationRedTest.tStart = t  # local t and not account for scr refresh
                        fixationRedTest.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixationRedTest, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixationRedTest.started')
                        # update status
                        fixationRedTest.status = STARTED
                        fixationRedTest.setAutoDraw(True)
                    
                    # if fixationRedTest is active this frame...
                    if fixationRedTest.status == STARTED:
                        # update params
                        pass
                    
                    # if fixationRedTest is stopping this frame...
                    if fixationRedTest.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixationRedTest.tStartRefresh + startTimes[5]+0.025+2-frameTolerance:
                            # keep track of stop time/frame for later
                            fixationRedTest.tStop = t  # not accounting for scr refresh
                            fixationRedTest.tStopRefresh = tThisFlipGlobal  # on global time
                            fixationRedTest.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixationRedTest.stopped')
                            # update status
                            fixationRedTest.status = FINISHED
                            fixationRedTest.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        testRoutine.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in testRoutine.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "testRoutine" ---
                for thisComponent in testRoutine.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for testRoutine
                testRoutine.tStop = globalClock.getTime(format='float')
                testRoutine.tStopRefresh = tThisFlipGlobal
                thisExp.addData('testRoutine.stopped', testRoutine.tStop)
                # check responses
                if respKeyPress.keys in ['', [], None]:  # No response was made
                    respKeyPress.keys = None
                trials.addData('respKeyPress.keys',respKeyPress.keys)
                if respKeyPress.keys != None:  # we had a response
                    trials.addData('respKeyPress.rt', respKeyPress.rt)
                    trials.addData('respKeyPress.duration', respKeyPress.duration)
                # check responses
                if respKeyRelease.keys in ['', [], None]:  # No response was made
                    respKeyRelease.keys = None
                trials.addData('respKeyRelease.keys',respKeyRelease.keys)
                if respKeyRelease.keys != None:  # we had a response
                    trials.addData('respKeyRelease.rt', respKeyRelease.rt)
                    trials.addData('respKeyRelease.duration', respKeyRelease.duration)
                # the Routine "testRoutine" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "feedbackRoutine" ---
                # create an object to store info about Routine feedbackRoutine
                feedbackRoutine = data.Routine(
                    name='feedbackRoutine',
                    components=[stimBar, responseBar, feedbackResp, stim1Pos, stim2Pos, stim3Pos, stim4Pos, stim5Pos, stim6Pos, resp1Pos, resp2Pos, resp3Pos, resp4Pos, resp5Pos, resp6Pos, corrText],
                )
                feedbackRoutine.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from feedBackCode
                min_val = min(startTimes)
                max_val = max(startTimes)
                
                normTimes = [((x - min_val) / (max_val - min_val)) * 20 - 10 for x in startTimes]
                
                
                respTimes = [-10,-10,-10,-10,-10,-10]
                respTimes_orig = [-10,-10,-10,-10,-10,-10]
                normRespTimes =[-10,-10,-10,-10,-10,-10]
                normRespTimes_orig = [-10,-10,-10,-10,-10,-10]
                
                if respKeyPress.rt:
                    respTimes = respKeyPress.rt[:5]
                
                    min_val = min(startTimes)
                    max_val = max(startTimes)
                
                    normRespTimes = [((x - min_val) / (max_val - min_val)) * 20 - 10 for x in respTimes]
                    
                    respTimes
                
                for i in  range(len(normRespTimes[:5])):
                    normRespTimes_orig[i+1] = normRespTimes[i]
                    respTimes_orig[i+1] = respTimes[i]
                   
                corr = np.corrcoef(respTimes_orig, startTimes)[0, 1]
                corrText.text = f'Score : {corr:.2f}'
                
                 
                 
                # create starting attributes for feedbackResp
                feedbackResp.keys = []
                feedbackResp.rt = []
                _feedbackResp_allKeys = []
                # store start times for feedbackRoutine
                feedbackRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                feedbackRoutine.tStart = globalClock.getTime(format='float')
                feedbackRoutine.status = STARTED
                thisExp.addData('feedbackRoutine.started', feedbackRoutine.tStart)
                feedbackRoutine.maxDuration = None
                # keep track of which components have finished
                feedbackRoutineComponents = feedbackRoutine.components
                for thisComponent in feedbackRoutine.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "feedbackRoutine" ---
                # if trial has changed, end Routine now
                if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                    continueRoutine = False
                feedbackRoutine.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from feedBackCode
                    resp1Pos.pos = (normRespTimes_orig[0],stimBar.pos[1]-3)
                    resp2Pos.pos = (normRespTimes_orig[1],stimBar.pos[1]-3)
                    resp3Pos.pos = (normRespTimes_orig[2],stimBar.pos[1]-3)
                    resp4Pos.pos = (normRespTimes_orig[3],stimBar.pos[1]-3)
                    resp5Pos.pos = (normRespTimes_orig[4],stimBar.pos[1]-3)
                    resp6Pos.pos = (normRespTimes_orig[5],stimBar.pos[1]-3)
                    
                    
                    stim1Pos.pos = (normTimes[0],stimBar.pos[1])
                    stim2Pos.pos = (normTimes[1],stimBar.pos[1])
                    stim3Pos.pos = (normTimes[2],stimBar.pos[1])
                    stim4Pos.pos = (normTimes[3],stimBar.pos[1])
                    stim5Pos.pos = (normTimes[4],stimBar.pos[1])
                    stim6Pos.pos = (normTimes[5],stimBar.pos[1])
                     
                    
                    # *stimBar* updates
                    
                    # if stimBar is starting this frame...
                    if stimBar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stimBar.frameNStart = frameN  # exact frame index
                        stimBar.tStart = t  # local t and not account for scr refresh
                        stimBar.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stimBar, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimBar.started')
                        # update status
                        stimBar.status = STARTED
                        stimBar.setAutoDraw(True)
                    
                    # if stimBar is active this frame...
                    if stimBar.status == STARTED:
                        # update params
                        pass
                    
                    # *responseBar* updates
                    
                    # if responseBar is starting this frame...
                    if responseBar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        responseBar.frameNStart = frameN  # exact frame index
                        responseBar.tStart = t  # local t and not account for scr refresh
                        responseBar.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(responseBar, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'responseBar.started')
                        # update status
                        responseBar.status = STARTED
                        responseBar.setAutoDraw(True)
                    
                    # if responseBar is active this frame...
                    if responseBar.status == STARTED:
                        # update params
                        pass
                    
                    # *feedbackResp* updates
                    waitOnFlip = False
                    
                    # if feedbackResp is starting this frame...
                    if feedbackResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        feedbackResp.frameNStart = frameN  # exact frame index
                        feedbackResp.tStart = t  # local t and not account for scr refresh
                        feedbackResp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(feedbackResp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedbackResp.started')
                        # update status
                        feedbackResp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(feedbackResp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(feedbackResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if feedbackResp.status == STARTED and not waitOnFlip:
                        theseKeys = feedbackResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                        _feedbackResp_allKeys.extend(theseKeys)
                        if len(_feedbackResp_allKeys):
                            feedbackResp.keys = _feedbackResp_allKeys[-1].name  # just the last key pressed
                            feedbackResp.rt = _feedbackResp_allKeys[-1].rt
                            feedbackResp.duration = _feedbackResp_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # *stim1Pos* updates
                    
                    # if stim1Pos is starting this frame...
                    if stim1Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stim1Pos.frameNStart = frameN  # exact frame index
                        stim1Pos.tStart = t  # local t and not account for scr refresh
                        stim1Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim1Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim1Pos.started')
                        # update status
                        stim1Pos.status = STARTED
                        stim1Pos.setAutoDraw(True)
                    
                    # if stim1Pos is active this frame...
                    if stim1Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *stim2Pos* updates
                    
                    # if stim2Pos is starting this frame...
                    if stim2Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stim2Pos.frameNStart = frameN  # exact frame index
                        stim2Pos.tStart = t  # local t and not account for scr refresh
                        stim2Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim2Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim2Pos.started')
                        # update status
                        stim2Pos.status = STARTED
                        stim2Pos.setAutoDraw(True)
                    
                    # if stim2Pos is active this frame...
                    if stim2Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *stim3Pos* updates
                    
                    # if stim3Pos is starting this frame...
                    if stim3Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stim3Pos.frameNStart = frameN  # exact frame index
                        stim3Pos.tStart = t  # local t and not account for scr refresh
                        stim3Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim3Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim3Pos.started')
                        # update status
                        stim3Pos.status = STARTED
                        stim3Pos.setAutoDraw(True)
                    
                    # if stim3Pos is active this frame...
                    if stim3Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *stim4Pos* updates
                    
                    # if stim4Pos is starting this frame...
                    if stim4Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stim4Pos.frameNStart = frameN  # exact frame index
                        stim4Pos.tStart = t  # local t and not account for scr refresh
                        stim4Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim4Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim4Pos.started')
                        # update status
                        stim4Pos.status = STARTED
                        stim4Pos.setAutoDraw(True)
                    
                    # if stim4Pos is active this frame...
                    if stim4Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *stim5Pos* updates
                    
                    # if stim5Pos is starting this frame...
                    if stim5Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stim5Pos.frameNStart = frameN  # exact frame index
                        stim5Pos.tStart = t  # local t and not account for scr refresh
                        stim5Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim5Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim5Pos.started')
                        # update status
                        stim5Pos.status = STARTED
                        stim5Pos.setAutoDraw(True)
                    
                    # if stim5Pos is active this frame...
                    if stim5Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *stim6Pos* updates
                    
                    # if stim6Pos is starting this frame...
                    if stim6Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        stim6Pos.frameNStart = frameN  # exact frame index
                        stim6Pos.tStart = t  # local t and not account for scr refresh
                        stim6Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim6Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim6Pos.started')
                        # update status
                        stim6Pos.status = STARTED
                        stim6Pos.setAutoDraw(True)
                    
                    # if stim6Pos is active this frame...
                    if stim6Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *resp1Pos* updates
                    
                    # if resp1Pos is starting this frame...
                    if resp1Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        resp1Pos.frameNStart = frameN  # exact frame index
                        resp1Pos.tStart = t  # local t and not account for scr refresh
                        resp1Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(resp1Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp1Pos.started')
                        # update status
                        resp1Pos.status = STARTED
                        resp1Pos.setAutoDraw(True)
                    
                    # if resp1Pos is active this frame...
                    if resp1Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *resp2Pos* updates
                    
                    # if resp2Pos is starting this frame...
                    if resp2Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        resp2Pos.frameNStart = frameN  # exact frame index
                        resp2Pos.tStart = t  # local t and not account for scr refresh
                        resp2Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(resp2Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp2Pos.started')
                        # update status
                        resp2Pos.status = STARTED
                        resp2Pos.setAutoDraw(True)
                    
                    # if resp2Pos is active this frame...
                    if resp2Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *resp3Pos* updates
                    
                    # if resp3Pos is starting this frame...
                    if resp3Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        resp3Pos.frameNStart = frameN  # exact frame index
                        resp3Pos.tStart = t  # local t and not account for scr refresh
                        resp3Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(resp3Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp3Pos.started')
                        # update status
                        resp3Pos.status = STARTED
                        resp3Pos.setAutoDraw(True)
                    
                    # if resp3Pos is active this frame...
                    if resp3Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *resp4Pos* updates
                    
                    # if resp4Pos is starting this frame...
                    if resp4Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        resp4Pos.frameNStart = frameN  # exact frame index
                        resp4Pos.tStart = t  # local t and not account for scr refresh
                        resp4Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(resp4Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp4Pos.started')
                        # update status
                        resp4Pos.status = STARTED
                        resp4Pos.setAutoDraw(True)
                    
                    # if resp4Pos is active this frame...
                    if resp4Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *resp5Pos* updates
                    
                    # if resp5Pos is starting this frame...
                    if resp5Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        resp5Pos.frameNStart = frameN  # exact frame index
                        resp5Pos.tStart = t  # local t and not account for scr refresh
                        resp5Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(resp5Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp5Pos.started')
                        # update status
                        resp5Pos.status = STARTED
                        resp5Pos.setAutoDraw(True)
                    
                    # if resp5Pos is active this frame...
                    if resp5Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *resp6Pos* updates
                    
                    # if resp6Pos is starting this frame...
                    if resp6Pos.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        resp6Pos.frameNStart = frameN  # exact frame index
                        resp6Pos.tStart = t  # local t and not account for scr refresh
                        resp6Pos.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(resp6Pos, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp6Pos.started')
                        # update status
                        resp6Pos.status = STARTED
                        resp6Pos.setAutoDraw(True)
                    
                    # if resp6Pos is active this frame...
                    if resp6Pos.status == STARTED:
                        # update params
                        pass
                    
                    # *corrText* updates
                    
                    # if corrText is starting this frame...
                    if corrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        corrText.frameNStart = frameN  # exact frame index
                        corrText.tStart = t  # local t and not account for scr refresh
                        corrText.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(corrText, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'corrText.started')
                        # update status
                        corrText.status = STARTED
                        corrText.setAutoDraw(True)
                    
                    # if corrText is active this frame...
                    if corrText.status == STARTED:
                        # update params
                        pass
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        feedbackRoutine.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in feedbackRoutine.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "feedbackRoutine" ---
                for thisComponent in feedbackRoutine.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for feedbackRoutine
                feedbackRoutine.tStop = globalClock.getTime(format='float')
                feedbackRoutine.tStopRefresh = tThisFlipGlobal
                thisExp.addData('feedbackRoutine.stopped', feedbackRoutine.tStop)
                # check responses
                if feedbackResp.keys in ['', [], None]:  # No response was made
                    feedbackResp.keys = None
                trials.addData('feedbackResp.keys',feedbackResp.keys)
                if feedbackResp.keys != None:  # we had a response
                    trials.addData('feedbackResp.rt', feedbackResp.rt)
                    trials.addData('feedbackResp.duration', feedbackResp.duration)
                # the Routine "feedbackRoutine" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed 15.0 repeats of 'trials'
            
            
            # --- Prepare to start Routine "breakRoutine" ---
            # create an object to store info about Routine breakRoutine
            breakRoutine = data.Routine(
                name='breakRoutine',
                components=[breakText, breakResp],
            )
            breakRoutine.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for breakResp
            breakResp.keys = []
            breakResp.rt = []
            _breakResp_allKeys = []
            # store start times for breakRoutine
            breakRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            breakRoutine.tStart = globalClock.getTime(format='float')
            breakRoutine.status = STARTED
            thisExp.addData('breakRoutine.started', breakRoutine.tStart)
            breakRoutine.maxDuration = None
            # keep track of which components have finished
            breakRoutineComponents = breakRoutine.components
            for thisComponent in breakRoutine.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "breakRoutine" ---
            # if trial has changed, end Routine now
            if isinstance(trialBlock, data.TrialHandler2) and thisTrialBlock.thisN != trialBlock.thisTrial.thisN:
                continueRoutine = False
            breakRoutine.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *breakText* updates
                
                # if breakText is starting this frame...
                if breakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    breakText.frameNStart = frameN  # exact frame index
                    breakText.tStart = t  # local t and not account for scr refresh
                    breakText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(breakText, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'breakText.started')
                    # update status
                    breakText.status = STARTED
                    breakText.setAutoDraw(True)
                
                # if breakText is active this frame...
                if breakText.status == STARTED:
                    # update params
                    pass
                
                # *breakResp* updates
                waitOnFlip = False
                
                # if breakResp is starting this frame...
                if breakResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    breakResp.frameNStart = frameN  # exact frame index
                    breakResp.tStart = t  # local t and not account for scr refresh
                    breakResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(breakResp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'breakResp.started')
                    # update status
                    breakResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(breakResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(breakResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if breakResp.status == STARTED and not waitOnFlip:
                    theseKeys = breakResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _breakResp_allKeys.extend(theseKeys)
                    if len(_breakResp_allKeys):
                        breakResp.keys = _breakResp_allKeys[-1].name  # just the last key pressed
                        breakResp.rt = _breakResp_allKeys[-1].rt
                        breakResp.duration = _breakResp_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    breakRoutine.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in breakRoutine.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "breakRoutine" ---
            for thisComponent in breakRoutine.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for breakRoutine
            breakRoutine.tStop = globalClock.getTime(format='float')
            breakRoutine.tStopRefresh = tThisFlipGlobal
            thisExp.addData('breakRoutine.stopped', breakRoutine.tStop)
            # check responses
            if breakResp.keys in ['', [], None]:  # No response was made
                breakResp.keys = None
            trialBlock.addData('breakResp.keys',breakResp.keys)
            if breakResp.keys != None:  # we had a response
                trialBlock.addData('breakResp.rt', breakResp.rt)
                trialBlock.addData('breakResp.duration', breakResp.duration)
            # the Routine "breakRoutine" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 4.0 repeats of 'trialBlock'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        thisExp.nextEntry()
        
    # completed len(speedOptions) repeats of 'speedBlock'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "endRoutine" ---
    # create an object to store info about Routine endRoutine
    endRoutine = data.Routine(
        name='endRoutine',
        components=[completionText, keyEnd],
    )
    endRoutine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyEnd
    keyEnd.keys = []
    keyEnd.rt = []
    _keyEnd_allKeys = []
    # store start times for endRoutine
    endRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    endRoutine.tStart = globalClock.getTime(format='float')
    endRoutine.status = STARTED
    thisExp.addData('endRoutine.started', endRoutine.tStart)
    endRoutine.maxDuration = None
    # keep track of which components have finished
    endRoutineComponents = endRoutine.components
    for thisComponent in endRoutine.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "endRoutine" ---
    endRoutine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *completionText* updates
        
        # if completionText is starting this frame...
        if completionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            completionText.frameNStart = frameN  # exact frame index
            completionText.tStart = t  # local t and not account for scr refresh
            completionText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(completionText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'completionText.started')
            # update status
            completionText.status = STARTED
            completionText.setAutoDraw(True)
        
        # if completionText is active this frame...
        if completionText.status == STARTED:
            # update params
            pass
        
        # *keyEnd* updates
        waitOnFlip = False
        
        # if keyEnd is starting this frame...
        if keyEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyEnd.frameNStart = frameN  # exact frame index
            keyEnd.tStart = t  # local t and not account for scr refresh
            keyEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyEnd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyEnd.started')
            # update status
            keyEnd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyEnd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyEnd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyEnd.status == STARTED and not waitOnFlip:
            theseKeys = keyEnd.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyEnd_allKeys.extend(theseKeys)
            if len(_keyEnd_allKeys):
                keyEnd.keys = _keyEnd_allKeys[-1].name  # just the last key pressed
                keyEnd.rt = _keyEnd_allKeys[-1].rt
                keyEnd.duration = _keyEnd_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            endRoutine.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endRoutine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "endRoutine" ---
    for thisComponent in endRoutine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for endRoutine
    endRoutine.tStop = globalClock.getTime(format='float')
    endRoutine.tStopRefresh = tThisFlipGlobal
    thisExp.addData('endRoutine.stopped', endRoutine.tStop)
    # check responses
    if keyEnd.keys in ['', [], None]:  # No response was made
        keyEnd.keys = None
    thisExp.addData('keyEnd.keys',keyEnd.keys)
    if keyEnd.keys != None:  # we had a response
        thisExp.addData('keyEnd.rt', keyEnd.rt)
        thisExp.addData('keyEnd.duration', keyEnd.duration)
    thisExp.nextEntry()
    # the Routine "endRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
