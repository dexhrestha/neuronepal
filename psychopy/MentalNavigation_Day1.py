#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Wed Jun  4 18:41:28 2025
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
expName = 'MentalNavigation_Day1'  # from the Builder filename that created this script
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
_winSize = [1920, 1080]
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
        originPath='/Users/dexhrestha/Documents/Portfolio/neuronepal/neuronepal/psychopy/MentalNavigation_Day1.py',
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
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='deg',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'deg'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
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
    if deviceManager.getDevice('keyWelcome_2') is None:
        # initialise keyWelcome_2
        keyWelcome_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyWelcome_2',
        )
    if deviceManager.getDevice('keyWelcome_3') is None:
        # initialise keyWelcome_3
        keyWelcome_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyWelcome_3',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('keyPress') is None:
        # initialise keyPress
        keyPress = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyPress',
        )
    if deviceManager.getDevice('keyRelease') is None:
        # initialise keyRelease
        keyRelease = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyRelease',
        )
    if deviceManager.getDevice('stopKey') is None:
        # initialise stopKey
        stopKey = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='stopKey',
        )
    if deviceManager.getDevice('stopResp') is None:
        # initialise stopResp
        stopResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='stopResp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
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
    
    # --- Initialize components for Routine "welcome" ---
    welcomeText = visual.TextStim(win=win, name='welcomeText',
        text='Mental Navigation Task  \n\nYour goal is to reach the target image by continuously traversing through a sequence of images using the left/right arrow keys IN ONE SINGLE BUTTON PRESS.  You must fixate your eyes on the fixation point in the center of the screen.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.75, wrapWidth=25.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyWelcome = keyboard.Keyboard(deviceName='keyWelcome')
    
    # --- Initialize components for Routine "welcome2" ---
    welcomeText_2 = visual.TextStim(win=win, name='welcomeText_2',
        text='Mental Navigation Task  \n\nThe center image shows your current position and the bottom image your target position.\n\n\nPress and hold a key (left/right key) to drift left or right and try to land exactly on the target image.\n\nYou may retry if you miss, but the goal is to succeed in one SINGLE press.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.75, wrapWidth=25.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyWelcome_2 = keyboard.Keyboard(deviceName='keyWelcome_2')
    
    # --- Initialize components for Routine "welcome3" ---
    welcomeText_3 = visual.TextStim(win=win, name='welcomeText_3',
        text='Mental Navigation Task\n\nThere are two modes in this experiment.\n\nVisual Mode: Images are visible as you move.\n\nMental Mode: Images are hidden—you must mentally track your position.\n\nThe sequence shifts at multiple speeds, indicated by the background dot movement.\n\n\nEach session lasts 60 minutes.\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.75, wrapWidth=25.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyWelcome_3 = keyboard.Keyboard(deviceName='keyWelcome_3')
    
    # --- Initialize components for Routine "expSetup" ---
    # Run 'Begin Experiment' code from expSetup_env
    
    
    ## Environment variables start
    imageset=1 # Image set
    landmarkWidth = 5 #Landmark width in degrees
    landmarkHeight = 5 #Landmark height in degrees
    startLandmarkY = 4# Y position of start Landmark in degrees
    targetLandmarkY =  -4# Y position of target Landmark in degrees
    interLandmarkDistance = 5# Distance between two neighboring landmarks in degrees
    trainingStepSizes = [1,1.5]#speed of landmarks during training in terms of degrees per frame
    testingStepSizes = [0.5,0.66,1,1.25,1.5,2]#speed of landmarks during testing in terms of degrees per frame
    numLandmarks = 7 # Total number of Landmarks
    tolerance = 0.25# Amount of permissible error while matching target and start Landmark
    initialTrials = 100# Number of trails as visual for day 2
    stopKey = "s" # A key to stop the experiment at anypoint and then save the data
    nDots = 100 # Number of white dots in background at any one frame
    fixationSize = (0.5,0.5) # Size of fixation dot in degree
    nIter = 10 # number of iteration of second part of the exp  
    #dotRadius = # Size of white dots in background
    dotLife = 60 # Number of frames a particular dot will be shown
    blockSize = 15 #15 # Block is collection of Trials. Number of trials in a block
    #screenHeight = # Height of screen in cm
    #objectDistance = # Distance from the eye to the screen in cm
    edgeLandmarkDistance = 12.5 # maximum distance of edge landmarks from the center
    totalTime = 5*60 # total time before the experiment ends automatically 
    score = 0
    currentTrialDD = 0  
    devMode = False
    ## Environment variables end
    
    dt = 0.167 # distance between lms is 10deg; this step size is for 10 deg/sec at 60 fps
    #defining global variables
    targetReached = False
    experimentExpired = False
    isTrain = True 
    loopName = "blockTrials"
    seed = random.randint(0,9999)
    
    random.seed(42)
    
    #Build distance-to-pairs dictionary
    all_distance_to_pairs = {
        k: [(i, j) for i in range(numLandmarks) for j in range(numLandmarks)
            if abs(i - j) == k]
        for k in range(1, numLandmarks)
    }
    
    #Select half of the pairs for training
    training_pairs = {}
    
    for k, pairs in all_distance_to_pairs.items():
        shuffled = pairs.copy()
        random.shuffle(shuffled)
        half_n = len(shuffled) // 2
        training_pairs[k] = shuffled[:half_n]
    
    
    # --- Initialize components for Routine "eyeSetup" ---
    text = visual.TextStim(win=win, name='text',
        text='Setting up the experiment.\n\nPress space to proceed.',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=25.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "blockSetup" ---
    
    # --- Initialize components for Routine "setup" ---
    fixationRed = visual.ShapeStim(
        win=win, name='fixationRed',units='deg', 
        size=fixationSize, vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "trial" ---
    dots = visual.DotStim(
        win=win, name='dots',units='deg', 
        nDots=300, dotSize=3.0,
        speed=0.0, dir=0.0, coherence=1.0,
        fieldPos=(0.0, 0.0), fieldSize=50.0, fieldAnchor='center', fieldShape='circle',
        signalDots='same', noiseDots='direction',dotLife=0.0,
        color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
        depth=0.0)
    targetLandmark = visual.ImageStim(
        win=win,
        name='targetLandmark', units='deg', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, targetLandmarkY), draggable=False, size=(landmarkWidth, landmarkHeight),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    fixationRedTrial = visual.ShapeStim(
        win=win, name='fixationRedTrial',units='deg', 
        size=fixationSize, vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    keyPress = keyboard.Keyboard(deviceName='keyPress')
    keyRelease = keyboard.Keyboard(deviceName='keyRelease')
    timeText = visual.TextStim(win=win, name='timeText',
        text='Time: ',
        font='Arial',
        units='deg', pos=(6,-5), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    stopKey = keyboard.Keyboard(deviceName='stopKey')
    
    # --- Initialize components for Routine "reset" ---
    targetLandmark2 = visual.ImageStim(
        win=win,
        name='targetLandmark2', units='deg', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, targetLandmarkY), draggable=False, size=(landmarkWidth, landmarkHeight),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    fixationRedReset = visual.ShapeStim(
        win=win, name='fixationRedReset',units='deg', 
        size=fixationSize, vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "stopEye" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Stop Eye Tracking.\n\nPress space to proceed.',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    stopResp = keyboard.Keyboard(deviceName='stopResp')
    
    # --- Initialize components for Routine "breakRoutine" ---
    breakText = visual.TextStim(win=win, name='breakText',
        text="This concludes this part of the experiment.\n\nPlease take a short break and press the space key when you're ready to proceed to the next part",
        font='Arial',
        units='deg', pos=(0,0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=25.0, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "blockSetup2" ---
    
    # --- Initialize components for Routine "setup" ---
    fixationRed = visual.ShapeStim(
        win=win, name='fixationRed',units='deg', 
        size=fixationSize, vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "trial" ---
    dots = visual.DotStim(
        win=win, name='dots',units='deg', 
        nDots=300, dotSize=3.0,
        speed=0.0, dir=0.0, coherence=1.0,
        fieldPos=(0.0, 0.0), fieldSize=50.0, fieldAnchor='center', fieldShape='circle',
        signalDots='same', noiseDots='direction',dotLife=0.0,
        color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
        depth=0.0)
    targetLandmark = visual.ImageStim(
        win=win,
        name='targetLandmark', units='deg', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, targetLandmarkY), draggable=False, size=(landmarkWidth, landmarkHeight),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    fixationRedTrial = visual.ShapeStim(
        win=win, name='fixationRedTrial',units='deg', 
        size=fixationSize, vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    keyPress = keyboard.Keyboard(deviceName='keyPress')
    keyRelease = keyboard.Keyboard(deviceName='keyRelease')
    timeText = visual.TextStim(win=win, name='timeText',
        text='Time: ',
        font='Arial',
        units='deg', pos=(6,-5), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color=[1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    stopKey = keyboard.Keyboard(deviceName='stopKey')
    
    # --- Initialize components for Routine "reset" ---
    targetLandmark2 = visual.ImageStim(
        win=win,
        name='targetLandmark2', units='deg', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, targetLandmarkY), draggable=False, size=(landmarkWidth, landmarkHeight),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    fixationRedReset = visual.ShapeStim(
        win=win, name='fixationRedReset',units='deg', 
        size=fixationSize, vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "stopEye" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Stop Eye Tracking.\n\nPress space to proceed.',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    stopResp = keyboard.Keyboard(deviceName='stopResp')
    
    # --- Initialize components for Routine "complete" ---
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
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[welcomeText, keyWelcome],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyWelcome
    keyWelcome.keys = []
    keyWelcome.rt = []
    _keyWelcome_allKeys = []
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    thisExp.addData('welcome.started', welcome.tStart)
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
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
    
    # --- Run Routine "welcome" ---
    welcome.forceEnded = routineForceEnded = not continueRoutine
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
            welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome.stopped', welcome.tStop)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "welcome2" ---
    # create an object to store info about Routine welcome2
    welcome2 = data.Routine(
        name='welcome2',
        components=[welcomeText_2, keyWelcome_2],
    )
    welcome2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyWelcome_2
    keyWelcome_2.keys = []
    keyWelcome_2.rt = []
    _keyWelcome_2_allKeys = []
    # store start times for welcome2
    welcome2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome2.tStart = globalClock.getTime(format='float')
    welcome2.status = STARTED
    thisExp.addData('welcome2.started', welcome2.tStart)
    welcome2.maxDuration = None
    # keep track of which components have finished
    welcome2Components = welcome2.components
    for thisComponent in welcome2.components:
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
    
    # --- Run Routine "welcome2" ---
    welcome2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcomeText_2* updates
        
        # if welcomeText_2 is starting this frame...
        if welcomeText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcomeText_2.frameNStart = frameN  # exact frame index
            welcomeText_2.tStart = t  # local t and not account for scr refresh
            welcomeText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcomeText_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcomeText_2.started')
            # update status
            welcomeText_2.status = STARTED
            welcomeText_2.setAutoDraw(True)
        
        # if welcomeText_2 is active this frame...
        if welcomeText_2.status == STARTED:
            # update params
            pass
        
        # *keyWelcome_2* updates
        waitOnFlip = False
        
        # if keyWelcome_2 is starting this frame...
        if keyWelcome_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyWelcome_2.frameNStart = frameN  # exact frame index
            keyWelcome_2.tStart = t  # local t and not account for scr refresh
            keyWelcome_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyWelcome_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyWelcome_2.started')
            # update status
            keyWelcome_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyWelcome_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyWelcome_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyWelcome_2.status == STARTED and not waitOnFlip:
            theseKeys = keyWelcome_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyWelcome_2_allKeys.extend(theseKeys)
            if len(_keyWelcome_2_allKeys):
                keyWelcome_2.keys = _keyWelcome_2_allKeys[-1].name  # just the last key pressed
                keyWelcome_2.rt = _keyWelcome_2_allKeys[-1].rt
                keyWelcome_2.duration = _keyWelcome_2_allKeys[-1].duration
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
            welcome2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome2" ---
    for thisComponent in welcome2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome2
    welcome2.tStop = globalClock.getTime(format='float')
    welcome2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome2.stopped', welcome2.tStop)
    thisExp.nextEntry()
    # the Routine "welcome2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "welcome3" ---
    # create an object to store info about Routine welcome3
    welcome3 = data.Routine(
        name='welcome3',
        components=[welcomeText_3, keyWelcome_3],
    )
    welcome3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyWelcome_3
    keyWelcome_3.keys = []
    keyWelcome_3.rt = []
    _keyWelcome_3_allKeys = []
    # store start times for welcome3
    welcome3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome3.tStart = globalClock.getTime(format='float')
    welcome3.status = STARTED
    thisExp.addData('welcome3.started', welcome3.tStart)
    welcome3.maxDuration = None
    # keep track of which components have finished
    welcome3Components = welcome3.components
    for thisComponent in welcome3.components:
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
    
    # --- Run Routine "welcome3" ---
    welcome3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcomeText_3* updates
        
        # if welcomeText_3 is starting this frame...
        if welcomeText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcomeText_3.frameNStart = frameN  # exact frame index
            welcomeText_3.tStart = t  # local t and not account for scr refresh
            welcomeText_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcomeText_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcomeText_3.started')
            # update status
            welcomeText_3.status = STARTED
            welcomeText_3.setAutoDraw(True)
        
        # if welcomeText_3 is active this frame...
        if welcomeText_3.status == STARTED:
            # update params
            pass
        
        # *keyWelcome_3* updates
        waitOnFlip = False
        
        # if keyWelcome_3 is starting this frame...
        if keyWelcome_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyWelcome_3.frameNStart = frameN  # exact frame index
            keyWelcome_3.tStart = t  # local t and not account for scr refresh
            keyWelcome_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyWelcome_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyWelcome_3.started')
            # update status
            keyWelcome_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyWelcome_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyWelcome_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyWelcome_3.status == STARTED and not waitOnFlip:
            theseKeys = keyWelcome_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keyWelcome_3_allKeys.extend(theseKeys)
            if len(_keyWelcome_3_allKeys):
                keyWelcome_3.keys = _keyWelcome_3_allKeys[-1].name  # just the last key pressed
                keyWelcome_3.rt = _keyWelcome_3_allKeys[-1].rt
                keyWelcome_3.duration = _keyWelcome_3_allKeys[-1].duration
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
            welcome3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome3" ---
    for thisComponent in welcome3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome3
    welcome3.tStop = globalClock.getTime(format='float')
    welcome3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome3.stopped', welcome3.tStop)
    thisExp.nextEntry()
    # the Routine "welcome3" was not non-slip safe, so reset the non-slip timer
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
    speedOptions = [1,1.5,1.5,1.5,1,1]
    #speedOptions = [0.5,0.66,1,1.25,1.5,2]
    visualModeOptions = [True,True,False,True,True,False]
    
    # generarte a list of distances
    allDistances = list(range(1,numLandmarks))
    # two list of distances for two block modes
    distances1 = [random.choice(allDistances) for _ in range(blockSize*len(speedOptions))]
    distances2 =  [random.choice(allDistances) for  _ in range(len(speedOptions)*nIter*blockSize)]
    # sampling from distance for two block modes
    pairs1 = [random.choice(training_pairs[distance]) for distance in distances1]
    pairs2 = [random.choice(training_pairs[distance]) for distance in distances2]
    # merge the pairs
    allPairs = pairs1+pairs2
    print("Length of trials",len(pairs1),len(pairs2))
    # randomizing pairs 
    random.seed(None)
    random.shuffle(allPairs)
    
    random.seed(42)
    trainingSpeeds = [s for _ in range(nIter) for s in trainingStepSizes]
    print("ts",trainingSpeeds)
    random.shuffle(trainingSpeeds)
    
    
    
    
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
    
    # --- Prepare to start Routine "eyeSetup" ---
    # create an object to store info about Routine eyeSetup
    eyeSetup = data.Routine(
        name='eyeSetup',
        components=[text, key_resp],
    )
    eyeSetup.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # Run 'Begin Routine' code from setupLMs
    expClock = core.Clock()
    
    landmarks = []
    dotsArray = []
    
    dots.depth = 0.5
    loopName = "blockTrials"
    for i in range(numLandmarks):
        # Create image
        lm = visual.ImageStim(
            win=win,
            name=str(i), units='deg', 
            image=f'public/landmarks/images/imageset1/{i}.jpg', mask=None, anchor='center',
            ori=0.0, pos=[0, 0], draggable=False, size=(landmarkWidth, landmarkHeight),
            color=[1,1,1], colorSpace='rgb', opacity=1,
            flipHoriz=False, flipVert=False,
            texRes=128.0, interpolate=True, depth=0.0  # higher depth: behind
        )
        lm.idx = i
        # Create and position dot in front
        dot = visual.Circle(
            win=win,
            radius=0.1,
            fillColor='red',
            lineColor='red',
            units='deg',
            pos=lm.pos,
            opacity=lm.opacity,
            depth=-1.0  # lower depth: in front of image
        )
        
        landmarks.append(lm)
        dotsArray.append(dot)
    # store start times for eyeSetup
    eyeSetup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    eyeSetup.tStart = globalClock.getTime(format='float')
    eyeSetup.status = STARTED
    thisExp.addData('eyeSetup.started', eyeSetup.tStart)
    eyeSetup.maxDuration = None
    # keep track of which components have finished
    eyeSetupComponents = eyeSetup.components
    for thisComponent in eyeSetup.components:
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
    
    # --- Run Routine "eyeSetup" ---
    eyeSetup.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            eyeSetup.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eyeSetup.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "eyeSetup" ---
    for thisComponent in eyeSetup.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for eyeSetup
    eyeSetup.tStop = globalClock.getTime(format='float')
    eyeSetup.tStopRefresh = tThisFlipGlobal
    thisExp.addData('eyeSetup.stopped', eyeSetup.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "eyeSetup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    lastLoop = data.TrialHandler2(
        name='lastLoop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(lastLoop)  # add the loop to the experiment
    thisLastLoop = lastLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLastLoop.rgb)
    if thisLastLoop != None:
        for paramName in thisLastLoop:
            globals()[paramName] = thisLastLoop[paramName]
    
    for thisLastLoop in lastLoop:
        currentLoop = lastLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisLastLoop.rgb)
        if thisLastLoop != None:
            for paramName in thisLastLoop:
                globals()[paramName] = thisLastLoop[paramName]
        
        # set up handler to look after randomisation of conditions etc
        blockTrials = data.TrialHandler2(
            name='blockTrials',
            nReps=len(speedOptions), 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(blockTrials)  # add the loop to the experiment
        thisBlockTrial = blockTrials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisBlockTrial.rgb)
        if thisBlockTrial != None:
            for paramName in thisBlockTrial:
                globals()[paramName] = thisBlockTrial[paramName]
        
        for thisBlockTrial in blockTrials:
            currentLoop = blockTrials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisBlockTrial.rgb)
            if thisBlockTrial != None:
                for paramName in thisBlockTrial:
                    globals()[paramName] = thisBlockTrial[paramName]
            
            # --- Prepare to start Routine "blockSetup" ---
            # create an object to store info about Routine blockSetup
            blockSetup = data.Routine(
                name='blockSetup',
                components=[],
            )
            blockSetup.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from blockSetup_2
            visualMode= visualModeOptions[blockTrials.thisN]
            speed = speedOptions[blockTrials.thisN]
            
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
            if isinstance(blockTrials, data.TrialHandler2) and thisBlockTrial.thisN != blockTrials.thisTrial.thisN:
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
            trials = data.TrialHandler2(
                name='trials',
                nReps=blockSize, 
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
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisTrial in trials:
                currentLoop = trials
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
                if thisTrial != None:
                    for paramName in thisTrial:
                        globals()[paramName] = thisTrial[paramName]
                
                # --- Prepare to start Routine "setup" ---
                # create an object to store info about Routine setup
                setup = data.Routine(
                    name='setup',
                    components=[fixationRed],
                )
                setup.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from initializationCode
                dots.speed = 0
                dots.dotLife = -1
                turn = 1
                random.seed(None)
                 
                startId = allPairs[currentTrialDD][0]
                targetId = allPairs[currentTrialDD][1]
                
                targetReached = False
                
                for  lm in  landmarks:
                    # Position it
                    lm.pos = ((lm.idx - startId) * (landmarkWidth + interLandmarkDistance), startLandmarkY)
                    dotsArray[lm.idx].pos = lm.pos
                    
                    if not visualMode:
                        if lm.idx not in [startId-1, startId, startId+1]:
                            lm.opacity = 0
                             
                        else:
                            lm.opacity = 1
                    else:
                        lm.opacity = 1
                        
                    dotsArray[lm.idx].opacity = lm.opacity
                    
                    dotsArray[lm.idx].setAutoDraw(True)
                    lm.setAutoDraw(True)
                    
                currentTrialDD+=1 
                # store start times for setup
                setup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                setup.tStart = globalClock.getTime(format='float')
                setup.status = STARTED
                thisExp.addData('setup.started', setup.tStart)
                setup.maxDuration = None
                # keep track of which components have finished
                setupComponents = setup.components
                for thisComponent in setup.components:
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
                
                # --- Run Routine "setup" ---
                # if trial has changed, end Routine now
                if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                    continueRoutine = False
                setup.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
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
                        if tThisFlipGlobal > fixationRed.tStartRefresh + random.uniform(0,0.5)-frameTolerance:
                            # keep track of stop time/frame for later
                            fixationRed.tStop = t  # not accounting for scr refresh
                            fixationRed.tStopRefresh = tThisFlipGlobal  # on global time
                            fixationRed.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixationRed.stopped')
                            # update status
                            fixationRed.status = FINISHED
                            fixationRed.setAutoDraw(False)
                    
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
                        setup.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in setup.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "setup" ---
                for thisComponent in setup.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for setup
                setup.tStop = globalClock.getTime(format='float')
                setup.tStopRefresh = tThisFlipGlobal
                thisExp.addData('setup.stopped', setup.tStop)
                # the Routine "setup" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                responseBlock = data.TrialHandler2(
                    name='responseBlock',
                    nReps=2.0, 
                    method='sequential', 
                    extraInfo=expInfo, 
                    originPath=-1, 
                    trialList=[None], 
                    seed=None, 
                )
                thisExp.addLoop(responseBlock)  # add the loop to the experiment
                thisResponseBlock = responseBlock.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisResponseBlock.rgb)
                if thisResponseBlock != None:
                    for paramName in thisResponseBlock:
                        globals()[paramName] = thisResponseBlock[paramName]
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                
                for thisResponseBlock in responseBlock:
                    currentLoop = responseBlock
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                    # abbreviate parameter names if possible (e.g. rgb = thisResponseBlock.rgb)
                    if thisResponseBlock != None:
                        for paramName in thisResponseBlock:
                            globals()[paramName] = thisResponseBlock[paramName]
                    
                    # --- Prepare to start Routine "trial" ---
                    # create an object to store info about Routine trial
                    trial = data.Routine(
                        name='trial',
                        components=[dots, targetLandmark, fixationRedTrial, keyPress, keyRelease, timeText, stopKey],
                    )
                    trial.status = NOT_STARTED
                    continueRoutine = True
                    # update component parameters for each repeat
                    dots.refreshDots()
                    targetLandmark.setImage('public/landmarks/images/imageset1/1.jpg')
                    # create starting attributes for keyPress
                    keyPress.keys = []
                    keyPress.rt = []
                    _keyPress_allKeys = []
                    # create starting attributes for keyRelease
                    keyRelease.keys = []
                    keyRelease.rt = []
                    _keyRelease_allKeys = []
                    # Run 'Begin Routine' code from move_images
                    ## add logic to  add all images on a line
                    dots.speed = 0
                    dots.dotLife = -1
                    closestLMs = sorted(landmarks,key=lambda x:abs(x.pos[0]),reverse=False)
                    
                    if visualMode:
                        for index,lm  in  enumerate(closestLMs):
                            lm.opacity = 1  
                    else:
                        closestLMs[0].opacity = 1
                        closestIdx = closestLMs[0].idx
                        leftLM = landmarks[closestIdx-1] if closestIdx>0 else landmarks[closestIdx]
                        leftLM.opacity = 1
                        rightLM = landmarks[closestIdx+1] if closestIdx<6 else landmarks[closestIdx]
                        rightLM.opacity = 1
                        
                        
                    targetLandmark.opacity = 1
                            
                    targetLandmark.image = f'public/landmarks/images/imageset1/{targetId}.jpg'
                    
                        
                    if targetReached:
                        score += 1
                        continueRoutine = False
                        
                    # create starting attributes for stopKey
                    stopKey.keys = []
                    stopKey.rt = []
                    _stopKey_allKeys = []
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
                    if isinstance(responseBlock, data.TrialHandler2) and thisResponseBlock.thisN != responseBlock.thisTrial.thisN:
                        continueRoutine = False
                    trial.forceEnded = routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *dots* updates
                        
                        # if dots is starting this frame...
                        if dots.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            dots.frameNStart = frameN  # exact frame index
                            dots.tStart = t  # local t and not account for scr refresh
                            dots.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(dots, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'dots.started')
                            # update status
                            dots.status = STARTED
                            dots.setAutoDraw(True)
                        
                        # if dots is active this frame...
                        if dots.status == STARTED:
                            # update params
                            pass
                        
                        # *targetLandmark* updates
                        
                        # if targetLandmark is starting this frame...
                        if targetLandmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            targetLandmark.frameNStart = frameN  # exact frame index
                            targetLandmark.tStart = t  # local t and not account for scr refresh
                            targetLandmark.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(targetLandmark, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'targetLandmark.started')
                            # update status
                            targetLandmark.status = STARTED
                            targetLandmark.setAutoDraw(True)
                        
                        # if targetLandmark is active this frame...
                        if targetLandmark.status == STARTED:
                            # update params
                            pass
                        
                        # *fixationRedTrial* updates
                        
                        # if fixationRedTrial is starting this frame...
                        if fixationRedTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            fixationRedTrial.frameNStart = frameN  # exact frame index
                            fixationRedTrial.tStart = t  # local t and not account for scr refresh
                            fixationRedTrial.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(fixationRedTrial, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixationRedTrial.started')
                            # update status
                            fixationRedTrial.status = STARTED
                            fixationRedTrial.setAutoDraw(True)
                        
                        # if fixationRedTrial is active this frame...
                        if fixationRedTrial.status == STARTED:
                            # update params
                            pass
                        
                        # *keyPress* updates
                        waitOnFlip = False
                        
                        # if keyPress is starting this frame...
                        if keyPress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            keyPress.frameNStart = frameN  # exact frame index
                            keyPress.tStart = t  # local t and not account for scr refresh
                            keyPress.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(keyPress, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'keyPress.started')
                            # update status
                            keyPress.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(keyPress.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(keyPress.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if keyPress.status == STARTED and not waitOnFlip:
                            theseKeys = keyPress.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                            _keyPress_allKeys.extend(theseKeys)
                            if len(_keyPress_allKeys):
                                keyPress.keys = _keyPress_allKeys[-1].name  # just the last key pressed
                                keyPress.rt = _keyPress_allKeys[-1].rt
                                keyPress.duration = _keyPress_allKeys[-1].duration
                        
                        # *keyRelease* updates
                        waitOnFlip = False
                        
                        # if keyRelease is starting this frame...
                        if keyRelease.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            keyRelease.frameNStart = frameN  # exact frame index
                            keyRelease.tStart = t  # local t and not account for scr refresh
                            keyRelease.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(keyRelease, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'keyRelease.started')
                            # update status
                            keyRelease.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(keyRelease.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(keyRelease.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if keyRelease.status == STARTED and not waitOnFlip:
                            theseKeys = keyRelease.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=True)
                            _keyRelease_allKeys.extend(theseKeys)
                            if len(_keyRelease_allKeys):
                                keyRelease.keys = _keyRelease_allKeys[-1].name  # just the last key pressed
                                keyRelease.rt = _keyRelease_allKeys[-1].rt
                                keyRelease.duration = _keyRelease_allKeys[-1].duration
                                # a response ends the routine
                                continueRoutine = False
                        # Run 'Each Frame' code from move_images
                        ## add logic to  move the image for each frame    
                        if loopName == "blockTrials":
                            completedTrials  = blockTrials.thisN
                        elif loopName == "breakLoop":
                            completedTrials = breakLoop.thisN
                        
                        if devMode:    
                            statusText = f"Current Time : {str(int(expClock.getTime()))} \n Completed Trials:{completedTrials}/{currentTrialDD} \n Score: {score} \n Speed: {speed} \n Step Size : {dt} \n Visual : {visualMode} " 
                        else:
                            statusText = ''
                            
                        timeText.setText(statusText)
                            
                        if  keyRelease.keys == 'left' or keyRelease.keys == 'right':
                            targetReached = abs(landmarks[targetId].pos[0])   <= tolerance * landmarkWidth
                            dots.dir =  0
                            dots.dotLife = -1
                            dots.speed = 0
                            
                        if keyPress.keys == 'left' or keyPress.keys  == 'right':
                            if not visualMode:
                                for lm in  landmarks:
                                    lm.opacity = 0
                                    dotsArray[lm.idx].opacity = 0
                                targetLandmark.opacity = 0
                                
                        if  keyPress.keys == 'left':
                            dots.dir =  180
                            for lm in landmarks:
                                if  landmarks[-1].pos[0]<-1*edgeLandmarkDistance:
                                    break
                                lm.pos -= (speed*dt,0)
                                dotsArray[lm.idx].pos -= (speed*dt,0)
                        
                            if  landmarks[-1].pos[0]<-1*edgeLandmarkDistance:
                                dots.speed = 0
                                dots.dotLife = -1
                            else:
                                dots.speed =  speed*dt
                                dots.dotLife = dotLife
                            
                        elif  keyPress.keys == 'right':
                            dots.dir = 0
                            for lm in landmarks:
                                if  landmarks[0].pos[0]>edgeLandmarkDistance:
                                    break
                                lm.pos += (speed*dt,0)
                                dotsArray[lm.idx].pos += (speed*dt,0)
                            if  landmarks[0].pos[0]>edgeLandmarkDistance:
                                dots.speed = 0
                                dots.dotLife = -1
                            else:
                                dots.speed =  speed*dt
                                dots.dotLife = dotLife
                        
                        
                        
                        for lm in landmarks:
                            dotsArray[lm.idx].opacity = lm.opacity
                        
                        
                         
                        
                        # *timeText* updates
                        
                        # if timeText is starting this frame...
                        if timeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            timeText.frameNStart = frameN  # exact frame index
                            timeText.tStart = t  # local t and not account for scr refresh
                            timeText.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(timeText, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'timeText.started')
                            # update status
                            timeText.status = STARTED
                            timeText.setAutoDraw(True)
                        
                        # if timeText is active this frame...
                        if timeText.status == STARTED:
                            # update params
                            pass
                        
                        # *stopKey* updates
                        waitOnFlip = False
                        
                        # if stopKey is starting this frame...
                        if stopKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            stopKey.frameNStart = frameN  # exact frame index
                            stopKey.tStart = t  # local t and not account for scr refresh
                            stopKey.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(stopKey, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'stopKey.started')
                            # update status
                            stopKey.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(stopKey.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(stopKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        if stopKey.status == STARTED and not waitOnFlip:
                            theseKeys = stopKey.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
                            _stopKey_allKeys.extend(theseKeys)
                            if len(_stopKey_allKeys):
                                stopKey.keys = _stopKey_allKeys[-1].name  # just the last key pressed
                                stopKey.rt = _stopKey_allKeys[-1].rt
                                stopKey.duration = _stopKey_allKeys[-1].duration
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
                    if keyPress.keys in ['', [], None]:  # No response was made
                        keyPress.keys = None
                    responseBlock.addData('keyPress.keys',keyPress.keys)
                    if keyPress.keys != None:  # we had a response
                        responseBlock.addData('keyPress.rt', keyPress.rt)
                        responseBlock.addData('keyPress.duration', keyPress.duration)
                    # check responses
                    if keyRelease.keys in ['', [], None]:  # No response was made
                        keyRelease.keys = None
                    responseBlock.addData('keyRelease.keys',keyRelease.keys)
                    if keyRelease.keys != None:  # we had a response
                        responseBlock.addData('keyRelease.rt', keyRelease.rt)
                        responseBlock.addData('keyRelease.duration', keyRelease.duration)
                    # Run 'End Routine' code from move_images
                    ## check if start and target is same
                    if stopKey.keys == 's':
                    #    print("Stopping experiment sending bye signal.")
                        continueRoutine = False
                        experimentExpired = True
                        if loopName == 'blockTrials':
                            responseBlock.finished = True
                        elif loopName == 'breakLoop':
                            responseBlock2.finished = True
                    
                    # check responses
                    if stopKey.keys in ['', [], None]:  # No response was made
                        stopKey.keys = None
                    responseBlock.addData('stopKey.keys',stopKey.keys)
                    if stopKey.keys != None:  # we had a response
                        responseBlock.addData('stopKey.rt', stopKey.rt)
                        responseBlock.addData('stopKey.duration', stopKey.duration)
                    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                # completed 2.0 repeats of 'responseBlock'
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                
                # --- Prepare to start Routine "reset" ---
                # create an object to store info about Routine reset
                reset = data.Routine(
                    name='reset',
                    components=[targetLandmark2, fixationRedReset],
                )
                reset.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from resetCode
                 
                if stopKey.keys == 's':
                #    print("Stopping experiment sending bye signal.")
                    continueRoutine = False
                    experimentExpired = True
                    
                if expClock.getTime()>=totalTime:
                #    print("Time limit reached. Ending experiment")
                    continueRoutine = False
                    experimentExpired = True
                targetLandmark2.setImage('public/landmarks/images/imageset1/1.jpg')
                # store start times for reset
                reset.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                reset.tStart = globalClock.getTime(format='float')
                reset.status = STARTED
                thisExp.addData('reset.started', reset.tStart)
                reset.maxDuration = None
                # keep track of which components have finished
                resetComponents = reset.components
                for thisComponent in reset.components:
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
                
                # --- Run Routine "reset" ---
                # if trial has changed, end Routine now
                if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                    continueRoutine = False
                reset.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.5:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from resetCode
                    
                    for index,lm in enumerate(landmarks):
                        lm.opacity = 1
                        dotsArray[index].opacity = 1
                    
                    targetLandmark2.image = targetLandmark.image
                    targetLandmark2.opacity = 1
                    
                    # *targetLandmark2* updates
                    
                    # if targetLandmark2 is starting this frame...
                    if targetLandmark2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        targetLandmark2.frameNStart = frameN  # exact frame index
                        targetLandmark2.tStart = t  # local t and not account for scr refresh
                        targetLandmark2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(targetLandmark2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'targetLandmark2.started')
                        # update status
                        targetLandmark2.status = STARTED
                        targetLandmark2.setAutoDraw(True)
                    
                    # if targetLandmark2 is active this frame...
                    if targetLandmark2.status == STARTED:
                        # update params
                        pass
                    
                    # if targetLandmark2 is stopping this frame...
                    if targetLandmark2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > targetLandmark2.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            targetLandmark2.tStop = t  # not accounting for scr refresh
                            targetLandmark2.tStopRefresh = tThisFlipGlobal  # on global time
                            targetLandmark2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'targetLandmark2.stopped')
                            # update status
                            targetLandmark2.status = FINISHED
                            targetLandmark2.setAutoDraw(False)
                    
                    # *fixationRedReset* updates
                    
                    # if fixationRedReset is starting this frame...
                    if fixationRedReset.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixationRedReset.frameNStart = frameN  # exact frame index
                        fixationRedReset.tStart = t  # local t and not account for scr refresh
                        fixationRedReset.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixationRedReset, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixationRedReset.started')
                        # update status
                        fixationRedReset.status = STARTED
                        fixationRedReset.setAutoDraw(True)
                    
                    # if fixationRedReset is active this frame...
                    if fixationRedReset.status == STARTED:
                        # update params
                        pass
                    
                    # if fixationRedReset is stopping this frame...
                    if fixationRedReset.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixationRedReset.tStartRefresh + 0.5-frameTolerance:
                            # keep track of stop time/frame for later
                            fixationRedReset.tStop = t  # not accounting for scr refresh
                            fixationRedReset.tStopRefresh = tThisFlipGlobal  # on global time
                            fixationRedReset.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixationRedReset.stopped')
                            # update status
                            fixationRedReset.status = FINISHED
                            fixationRedReset.setAutoDraw(False)
                    
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
                        reset.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in reset.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "reset" ---
                for thisComponent in reset.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for reset
                reset.tStop = globalClock.getTime(format='float')
                reset.tStopRefresh = tThisFlipGlobal
                thisExp.addData('reset.stopped', reset.tStop)
                # Run 'End Routine' code from resetCode
                
                for index,lm in enumerate(landmarks):
                    lm.opacity = 0
                    dotsArray[index].opacity = 0
                
                if 'experimentExpired' in globals() and experimentExpired:
                    print("Received experiment expired signal. Bye")
                
                    # Try to end the outer loop, whatever it's named
                    if loopName == "blockTrials":
                        continueRoutine =  False
                        trials.finished = True
                        blockTrials.finished = True
                        loopName='breakLoop'
                        
                    elif loopName == "breakLoop":
                        continueRoutine =  False
                        responseBlock2.finished=True
                        trials2.finished=True
                        blockTrials2.finished=True
                        breakLoop.finished = True
                    
                    lastLoop.finished = True
                
                thisExp.addData('speed',speed)
                thisExp.addData('stepSize',dt)
                thisExp.addData('speed',speed)
                thisExp.addData('startId',startId)
                thisExp.addData('targetId',targetId)
                thisExp.addData('startLandmarkPos',landmarks[startId].pos)
                thisExp.addData('experimentExpired',experimentExpired)
                thisExp.addData('visualMode',visualMode)
                thisExp.addData('devMode',devMode)
                thisExp.addData(f'{loopName}_duration',expClock.getTime())
                thisExp.addData('turn',turn)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if reset.maxDurationReached:
                    routineTimer.addTime(-reset.maxDuration)
                elif reset.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.500000)
                thisExp.nextEntry()
                
            # completed blockSize repeats of 'trials'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed len(speedOptions) repeats of 'blockTrials'
        
        
        # --- Prepare to start Routine "stopEye" ---
        # create an object to store info about Routine stopEye
        stopEye = data.Routine(
            name='stopEye',
            components=[text_3, stopResp],
        )
        stopEye.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for stopResp
        stopResp.keys = []
        stopResp.rt = []
        _stopResp_allKeys = []
        # store start times for stopEye
        stopEye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        stopEye.tStart = globalClock.getTime(format='float')
        stopEye.status = STARTED
        stopEye.maxDuration = None
        # keep track of which components have finished
        stopEyeComponents = stopEye.components
        for thisComponent in stopEye.components:
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
        
        # --- Run Routine "stopEye" ---
        # if trial has changed, end Routine now
        if isinstance(lastLoop, data.TrialHandler2) and thisLastLoop.thisN != lastLoop.thisTrial.thisN:
            continueRoutine = False
        stopEye.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # *stopResp* updates
            waitOnFlip = False
            
            # if stopResp is starting this frame...
            if stopResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stopResp.frameNStart = frameN  # exact frame index
                stopResp.tStart = t  # local t and not account for scr refresh
                stopResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stopResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stopResp.started')
                # update status
                stopResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(stopResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(stopResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if stopResp.status == STARTED and not waitOnFlip:
                theseKeys = stopResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _stopResp_allKeys.extend(theseKeys)
                if len(_stopResp_allKeys):
                    stopResp.keys = _stopResp_allKeys[-1].name  # just the last key pressed
                    stopResp.rt = _stopResp_allKeys[-1].rt
                    stopResp.duration = _stopResp_allKeys[-1].duration
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
                stopEye.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stopEye.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stopEye" ---
        for thisComponent in stopEye.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for stopEye
        stopEye.tStop = globalClock.getTime(format='float')
        stopEye.tStopRefresh = tThisFlipGlobal
        # check responses
        if stopResp.keys in ['', [], None]:  # No response was made
            stopResp.keys = None
        lastLoop.addData('stopResp.keys',stopResp.keys)
        if stopResp.keys != None:  # we had a response
            lastLoop.addData('stopResp.rt', stopResp.rt)
            lastLoop.addData('stopResp.duration', stopResp.duration)
        # the Routine "stopEye" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        breakLoop = data.TrialHandler2(
            name='breakLoop',
            nReps=6.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(breakLoop)  # add the loop to the experiment
        thisBreakLoop = breakLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisBreakLoop.rgb)
        if thisBreakLoop != None:
            for paramName in thisBreakLoop:
                globals()[paramName] = thisBreakLoop[paramName]
        
        for thisBreakLoop in breakLoop:
            currentLoop = breakLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisBreakLoop.rgb)
            if thisBreakLoop != None:
                for paramName in thisBreakLoop:
                    globals()[paramName] = thisBreakLoop[paramName]
            
            # --- Prepare to start Routine "breakRoutine" ---
            # create an object to store info about Routine breakRoutine
            breakRoutine = data.Routine(
                name='breakRoutine',
                components=[breakText, key_resp_2],
            )
            breakRoutine.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from blockSetup_3
            visualMode =True
            loopName =  "breakLoop"
            
            if 'experimentExpired' in globals() and experimentExpired:
                print('dont run breakloop')
                continueRoutine = False    
                breakLoop.finished = True
                break
            # create starting attributes for key_resp_2
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
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
            if isinstance(breakLoop, data.TrialHandler2) and thisBreakLoop.thisN != breakLoop.thisTrial.thisN:
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
                
                # *key_resp_2* updates
                waitOnFlip = False
                
                # if key_resp_2 is starting this frame...
                if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.started')
                    # update status
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                        key_resp_2.duration = _key_resp_2_allKeys[-1].duration
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
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys = None
            breakLoop.addData('key_resp_2.keys',key_resp_2.keys)
            if key_resp_2.keys != None:  # we had a response
                breakLoop.addData('key_resp_2.rt', key_resp_2.rt)
                breakLoop.addData('key_resp_2.duration', key_resp_2.duration)
            # the Routine "breakRoutine" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            blockTrials2 = data.TrialHandler2(
                name='blockTrials2',
                nReps=12.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=[None], 
                seed=None, 
            )
            thisExp.addLoop(blockTrials2)  # add the loop to the experiment
            thisBlockTrials2 = blockTrials2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisBlockTrials2.rgb)
            if thisBlockTrials2 != None:
                for paramName in thisBlockTrials2:
                    globals()[paramName] = thisBlockTrials2[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisBlockTrials2 in blockTrials2:
                currentLoop = blockTrials2
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisBlockTrials2.rgb)
                if thisBlockTrials2 != None:
                    for paramName in thisBlockTrials2:
                        globals()[paramName] = thisBlockTrials2[paramName]
                
                # --- Prepare to start Routine "blockSetup2" ---
                # create an object to store info about Routine blockSetup2
                blockSetup2 = data.Routine(
                    name='blockSetup2',
                    components=[],
                )
                blockSetup2.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from block2SetupCode
                speed = trainingSpeeds[blockTrials2.thisN]
                # store start times for blockSetup2
                blockSetup2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                blockSetup2.tStart = globalClock.getTime(format='float')
                blockSetup2.status = STARTED
                thisExp.addData('blockSetup2.started', blockSetup2.tStart)
                blockSetup2.maxDuration = None
                # keep track of which components have finished
                blockSetup2Components = blockSetup2.components
                for thisComponent in blockSetup2.components:
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
                
                # --- Run Routine "blockSetup2" ---
                # if trial has changed, end Routine now
                if isinstance(blockTrials2, data.TrialHandler2) and thisBlockTrials2.thisN != blockTrials2.thisTrial.thisN:
                    continueRoutine = False
                blockSetup2.forceEnded = routineForceEnded = not continueRoutine
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
                        blockSetup2.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blockSetup2.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blockSetup2" ---
                for thisComponent in blockSetup2.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for blockSetup2
                blockSetup2.tStop = globalClock.getTime(format='float')
                blockSetup2.tStopRefresh = tThisFlipGlobal
                thisExp.addData('blockSetup2.stopped', blockSetup2.tStop)
                # the Routine "blockSetup2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials2 = data.TrialHandler2(
                    name='trials2',
                    nReps=15.0, 
                    method='random', 
                    extraInfo=expInfo, 
                    originPath=-1, 
                    trialList=[None], 
                    seed=None, 
                )
                thisExp.addLoop(trials2)  # add the loop to the experiment
                thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
                if thisTrials2 != None:
                    for paramName in thisTrials2:
                        globals()[paramName] = thisTrials2[paramName]
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                
                for thisTrials2 in trials2:
                    currentLoop = trials2
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
                    if thisTrials2 != None:
                        for paramName in thisTrials2:
                            globals()[paramName] = thisTrials2[paramName]
                    
                    # --- Prepare to start Routine "setup" ---
                    # create an object to store info about Routine setup
                    setup = data.Routine(
                        name='setup',
                        components=[fixationRed],
                    )
                    setup.status = NOT_STARTED
                    continueRoutine = True
                    # update component parameters for each repeat
                    # Run 'Begin Routine' code from initializationCode
                    dots.speed = 0
                    dots.dotLife = -1
                    turn = 1
                    random.seed(None)
                     
                    startId = allPairs[currentTrialDD][0]
                    targetId = allPairs[currentTrialDD][1]
                    
                    targetReached = False
                    
                    for  lm in  landmarks:
                        # Position it
                        lm.pos = ((lm.idx - startId) * (landmarkWidth + interLandmarkDistance), startLandmarkY)
                        dotsArray[lm.idx].pos = lm.pos
                        
                        if not visualMode:
                            if lm.idx not in [startId-1, startId, startId+1]:
                                lm.opacity = 0
                                 
                            else:
                                lm.opacity = 1
                        else:
                            lm.opacity = 1
                            
                        dotsArray[lm.idx].opacity = lm.opacity
                        
                        dotsArray[lm.idx].setAutoDraw(True)
                        lm.setAutoDraw(True)
                        
                    currentTrialDD+=1 
                    # store start times for setup
                    setup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                    setup.tStart = globalClock.getTime(format='float')
                    setup.status = STARTED
                    thisExp.addData('setup.started', setup.tStart)
                    setup.maxDuration = None
                    # keep track of which components have finished
                    setupComponents = setup.components
                    for thisComponent in setup.components:
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
                    
                    # --- Run Routine "setup" ---
                    # if trial has changed, end Routine now
                    if isinstance(trials2, data.TrialHandler2) and thisTrials2.thisN != trials2.thisTrial.thisN:
                        continueRoutine = False
                    setup.forceEnded = routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
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
                            if tThisFlipGlobal > fixationRed.tStartRefresh + random.uniform(0,0.5)-frameTolerance:
                                # keep track of stop time/frame for later
                                fixationRed.tStop = t  # not accounting for scr refresh
                                fixationRed.tStopRefresh = tThisFlipGlobal  # on global time
                                fixationRed.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'fixationRed.stopped')
                                # update status
                                fixationRed.status = FINISHED
                                fixationRed.setAutoDraw(False)
                        
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
                            setup.forceEnded = routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in setup.components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "setup" ---
                    for thisComponent in setup.components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store stop times for setup
                    setup.tStop = globalClock.getTime(format='float')
                    setup.tStopRefresh = tThisFlipGlobal
                    thisExp.addData('setup.stopped', setup.tStop)
                    # the Routine "setup" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    
                    # set up handler to look after randomisation of conditions etc
                    responseBlock2 = data.TrialHandler2(
                        name='responseBlock2',
                        nReps=2.0, 
                        method='random', 
                        extraInfo=expInfo, 
                        originPath=-1, 
                        trialList=[None], 
                        seed=None, 
                    )
                    thisExp.addLoop(responseBlock2)  # add the loop to the experiment
                    thisResponseBlock2 = responseBlock2.trialList[0]  # so we can initialise stimuli with some values
                    # abbreviate parameter names if possible (e.g. rgb = thisResponseBlock2.rgb)
                    if thisResponseBlock2 != None:
                        for paramName in thisResponseBlock2:
                            globals()[paramName] = thisResponseBlock2[paramName]
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                    
                    for thisResponseBlock2 in responseBlock2:
                        currentLoop = responseBlock2
                        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                        if thisSession is not None:
                            # if running in a Session with a Liaison client, send data up to now
                            thisSession.sendExperimentData()
                        # abbreviate parameter names if possible (e.g. rgb = thisResponseBlock2.rgb)
                        if thisResponseBlock2 != None:
                            for paramName in thisResponseBlock2:
                                globals()[paramName] = thisResponseBlock2[paramName]
                        
                        # --- Prepare to start Routine "trial" ---
                        # create an object to store info about Routine trial
                        trial = data.Routine(
                            name='trial',
                            components=[dots, targetLandmark, fixationRedTrial, keyPress, keyRelease, timeText, stopKey],
                        )
                        trial.status = NOT_STARTED
                        continueRoutine = True
                        # update component parameters for each repeat
                        dots.refreshDots()
                        targetLandmark.setImage('public/landmarks/images/imageset1/1.jpg')
                        # create starting attributes for keyPress
                        keyPress.keys = []
                        keyPress.rt = []
                        _keyPress_allKeys = []
                        # create starting attributes for keyRelease
                        keyRelease.keys = []
                        keyRelease.rt = []
                        _keyRelease_allKeys = []
                        # Run 'Begin Routine' code from move_images
                        ## add logic to  add all images on a line
                        dots.speed = 0
                        dots.dotLife = -1
                        closestLMs = sorted(landmarks,key=lambda x:abs(x.pos[0]),reverse=False)
                        
                        if visualMode:
                            for index,lm  in  enumerate(closestLMs):
                                lm.opacity = 1  
                        else:
                            closestLMs[0].opacity = 1
                            closestIdx = closestLMs[0].idx
                            leftLM = landmarks[closestIdx-1] if closestIdx>0 else landmarks[closestIdx]
                            leftLM.opacity = 1
                            rightLM = landmarks[closestIdx+1] if closestIdx<6 else landmarks[closestIdx]
                            rightLM.opacity = 1
                            
                            
                        targetLandmark.opacity = 1
                                
                        targetLandmark.image = f'public/landmarks/images/imageset1/{targetId}.jpg'
                        
                            
                        if targetReached:
                            score += 1
                            continueRoutine = False
                            
                        # create starting attributes for stopKey
                        stopKey.keys = []
                        stopKey.rt = []
                        _stopKey_allKeys = []
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
                        if isinstance(responseBlock2, data.TrialHandler2) and thisResponseBlock2.thisN != responseBlock2.thisTrial.thisN:
                            continueRoutine = False
                        trial.forceEnded = routineForceEnded = not continueRoutine
                        while continueRoutine:
                            # get current time
                            t = routineTimer.getTime()
                            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                            # update/draw components on each frame
                            
                            # *dots* updates
                            
                            # if dots is starting this frame...
                            if dots.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                                # keep track of start time/frame for later
                                dots.frameNStart = frameN  # exact frame index
                                dots.tStart = t  # local t and not account for scr refresh
                                dots.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(dots, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'dots.started')
                                # update status
                                dots.status = STARTED
                                dots.setAutoDraw(True)
                            
                            # if dots is active this frame...
                            if dots.status == STARTED:
                                # update params
                                pass
                            
                            # *targetLandmark* updates
                            
                            # if targetLandmark is starting this frame...
                            if targetLandmark.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                                # keep track of start time/frame for later
                                targetLandmark.frameNStart = frameN  # exact frame index
                                targetLandmark.tStart = t  # local t and not account for scr refresh
                                targetLandmark.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(targetLandmark, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'targetLandmark.started')
                                # update status
                                targetLandmark.status = STARTED
                                targetLandmark.setAutoDraw(True)
                            
                            # if targetLandmark is active this frame...
                            if targetLandmark.status == STARTED:
                                # update params
                                pass
                            
                            # *fixationRedTrial* updates
                            
                            # if fixationRedTrial is starting this frame...
                            if fixationRedTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                                # keep track of start time/frame for later
                                fixationRedTrial.frameNStart = frameN  # exact frame index
                                fixationRedTrial.tStart = t  # local t and not account for scr refresh
                                fixationRedTrial.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(fixationRedTrial, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'fixationRedTrial.started')
                                # update status
                                fixationRedTrial.status = STARTED
                                fixationRedTrial.setAutoDraw(True)
                            
                            # if fixationRedTrial is active this frame...
                            if fixationRedTrial.status == STARTED:
                                # update params
                                pass
                            
                            # *keyPress* updates
                            waitOnFlip = False
                            
                            # if keyPress is starting this frame...
                            if keyPress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                                # keep track of start time/frame for later
                                keyPress.frameNStart = frameN  # exact frame index
                                keyPress.tStart = t  # local t and not account for scr refresh
                                keyPress.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(keyPress, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'keyPress.started')
                                # update status
                                keyPress.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(keyPress.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(keyPress.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            if keyPress.status == STARTED and not waitOnFlip:
                                theseKeys = keyPress.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                                _keyPress_allKeys.extend(theseKeys)
                                if len(_keyPress_allKeys):
                                    keyPress.keys = _keyPress_allKeys[-1].name  # just the last key pressed
                                    keyPress.rt = _keyPress_allKeys[-1].rt
                                    keyPress.duration = _keyPress_allKeys[-1].duration
                            
                            # *keyRelease* updates
                            waitOnFlip = False
                            
                            # if keyRelease is starting this frame...
                            if keyRelease.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                                # keep track of start time/frame for later
                                keyRelease.frameNStart = frameN  # exact frame index
                                keyRelease.tStart = t  # local t and not account for scr refresh
                                keyRelease.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(keyRelease, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'keyRelease.started')
                                # update status
                                keyRelease.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(keyRelease.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(keyRelease.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            if keyRelease.status == STARTED and not waitOnFlip:
                                theseKeys = keyRelease.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=True)
                                _keyRelease_allKeys.extend(theseKeys)
                                if len(_keyRelease_allKeys):
                                    keyRelease.keys = _keyRelease_allKeys[-1].name  # just the last key pressed
                                    keyRelease.rt = _keyRelease_allKeys[-1].rt
                                    keyRelease.duration = _keyRelease_allKeys[-1].duration
                                    # a response ends the routine
                                    continueRoutine = False
                            # Run 'Each Frame' code from move_images
                            ## add logic to  move the image for each frame    
                            if loopName == "blockTrials":
                                completedTrials  = blockTrials.thisN
                            elif loopName == "breakLoop":
                                completedTrials = breakLoop.thisN
                            
                            if devMode:    
                                statusText = f"Current Time : {str(int(expClock.getTime()))} \n Completed Trials:{completedTrials}/{currentTrialDD} \n Score: {score} \n Speed: {speed} \n Step Size : {dt} \n Visual : {visualMode} " 
                            else:
                                statusText = ''
                                
                            timeText.setText(statusText)
                                
                            if  keyRelease.keys == 'left' or keyRelease.keys == 'right':
                                targetReached = abs(landmarks[targetId].pos[0])   <= tolerance * landmarkWidth
                                dots.dir =  0
                                dots.dotLife = -1
                                dots.speed = 0
                                
                            if keyPress.keys == 'left' or keyPress.keys  == 'right':
                                if not visualMode:
                                    for lm in  landmarks:
                                        lm.opacity = 0
                                        dotsArray[lm.idx].opacity = 0
                                    targetLandmark.opacity = 0
                                    
                            if  keyPress.keys == 'left':
                                dots.dir =  180
                                for lm in landmarks:
                                    if  landmarks[-1].pos[0]<-1*edgeLandmarkDistance:
                                        break
                                    lm.pos -= (speed*dt,0)
                                    dotsArray[lm.idx].pos -= (speed*dt,0)
                            
                                if  landmarks[-1].pos[0]<-1*edgeLandmarkDistance:
                                    dots.speed = 0
                                    dots.dotLife = -1
                                else:
                                    dots.speed =  speed*dt
                                    dots.dotLife = dotLife
                                
                            elif  keyPress.keys == 'right':
                                dots.dir = 0
                                for lm in landmarks:
                                    if  landmarks[0].pos[0]>edgeLandmarkDistance:
                                        break
                                    lm.pos += (speed*dt,0)
                                    dotsArray[lm.idx].pos += (speed*dt,0)
                                if  landmarks[0].pos[0]>edgeLandmarkDistance:
                                    dots.speed = 0
                                    dots.dotLife = -1
                                else:
                                    dots.speed =  speed*dt
                                    dots.dotLife = dotLife
                            
                            
                            
                            for lm in landmarks:
                                dotsArray[lm.idx].opacity = lm.opacity
                            
                            
                             
                            
                            # *timeText* updates
                            
                            # if timeText is starting this frame...
                            if timeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                                # keep track of start time/frame for later
                                timeText.frameNStart = frameN  # exact frame index
                                timeText.tStart = t  # local t and not account for scr refresh
                                timeText.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(timeText, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'timeText.started')
                                # update status
                                timeText.status = STARTED
                                timeText.setAutoDraw(True)
                            
                            # if timeText is active this frame...
                            if timeText.status == STARTED:
                                # update params
                                pass
                            
                            # *stopKey* updates
                            waitOnFlip = False
                            
                            # if stopKey is starting this frame...
                            if stopKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                                # keep track of start time/frame for later
                                stopKey.frameNStart = frameN  # exact frame index
                                stopKey.tStart = t  # local t and not account for scr refresh
                                stopKey.tStartRefresh = tThisFlipGlobal  # on global time
                                win.timeOnFlip(stopKey, 'tStartRefresh')  # time at next scr refresh
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'stopKey.started')
                                # update status
                                stopKey.status = STARTED
                                # keyboard checking is just starting
                                waitOnFlip = True
                                win.callOnFlip(stopKey.clock.reset)  # t=0 on next screen flip
                                win.callOnFlip(stopKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                            if stopKey.status == STARTED and not waitOnFlip:
                                theseKeys = stopKey.getKeys(keyList=['s'], ignoreKeys=["escape"], waitRelease=False)
                                _stopKey_allKeys.extend(theseKeys)
                                if len(_stopKey_allKeys):
                                    stopKey.keys = _stopKey_allKeys[-1].name  # just the last key pressed
                                    stopKey.rt = _stopKey_allKeys[-1].rt
                                    stopKey.duration = _stopKey_allKeys[-1].duration
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
                        if keyPress.keys in ['', [], None]:  # No response was made
                            keyPress.keys = None
                        responseBlock2.addData('keyPress.keys',keyPress.keys)
                        if keyPress.keys != None:  # we had a response
                            responseBlock2.addData('keyPress.rt', keyPress.rt)
                            responseBlock2.addData('keyPress.duration', keyPress.duration)
                        # check responses
                        if keyRelease.keys in ['', [], None]:  # No response was made
                            keyRelease.keys = None
                        responseBlock2.addData('keyRelease.keys',keyRelease.keys)
                        if keyRelease.keys != None:  # we had a response
                            responseBlock2.addData('keyRelease.rt', keyRelease.rt)
                            responseBlock2.addData('keyRelease.duration', keyRelease.duration)
                        # Run 'End Routine' code from move_images
                        ## check if start and target is same
                        if stopKey.keys == 's':
                        #    print("Stopping experiment sending bye signal.")
                            continueRoutine = False
                            experimentExpired = True
                            if loopName == 'blockTrials':
                                responseBlock.finished = True
                            elif loopName == 'breakLoop':
                                responseBlock2.finished = True
                        
                        # check responses
                        if stopKey.keys in ['', [], None]:  # No response was made
                            stopKey.keys = None
                        responseBlock2.addData('stopKey.keys',stopKey.keys)
                        if stopKey.keys != None:  # we had a response
                            responseBlock2.addData('stopKey.rt', stopKey.rt)
                            responseBlock2.addData('stopKey.duration', stopKey.duration)
                        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset()
                        thisExp.nextEntry()
                        
                    # completed 2.0 repeats of 'responseBlock2'
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                    
                    # --- Prepare to start Routine "reset" ---
                    # create an object to store info about Routine reset
                    reset = data.Routine(
                        name='reset',
                        components=[targetLandmark2, fixationRedReset],
                    )
                    reset.status = NOT_STARTED
                    continueRoutine = True
                    # update component parameters for each repeat
                    # Run 'Begin Routine' code from resetCode
                     
                    if stopKey.keys == 's':
                    #    print("Stopping experiment sending bye signal.")
                        continueRoutine = False
                        experimentExpired = True
                        
                    if expClock.getTime()>=totalTime:
                    #    print("Time limit reached. Ending experiment")
                        continueRoutine = False
                        experimentExpired = True
                    targetLandmark2.setImage('public/landmarks/images/imageset1/1.jpg')
                    # store start times for reset
                    reset.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                    reset.tStart = globalClock.getTime(format='float')
                    reset.status = STARTED
                    thisExp.addData('reset.started', reset.tStart)
                    reset.maxDuration = None
                    # keep track of which components have finished
                    resetComponents = reset.components
                    for thisComponent in reset.components:
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
                    
                    # --- Run Routine "reset" ---
                    # if trial has changed, end Routine now
                    if isinstance(trials2, data.TrialHandler2) and thisTrials2.thisN != trials2.thisTrial.thisN:
                        continueRoutine = False
                    reset.forceEnded = routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 0.5:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        # Run 'Each Frame' code from resetCode
                        
                        for index,lm in enumerate(landmarks):
                            lm.opacity = 1
                            dotsArray[index].opacity = 1
                        
                        targetLandmark2.image = targetLandmark.image
                        targetLandmark2.opacity = 1
                        
                        # *targetLandmark2* updates
                        
                        # if targetLandmark2 is starting this frame...
                        if targetLandmark2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            targetLandmark2.frameNStart = frameN  # exact frame index
                            targetLandmark2.tStart = t  # local t and not account for scr refresh
                            targetLandmark2.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(targetLandmark2, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'targetLandmark2.started')
                            # update status
                            targetLandmark2.status = STARTED
                            targetLandmark2.setAutoDraw(True)
                        
                        # if targetLandmark2 is active this frame...
                        if targetLandmark2.status == STARTED:
                            # update params
                            pass
                        
                        # if targetLandmark2 is stopping this frame...
                        if targetLandmark2.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > targetLandmark2.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                targetLandmark2.tStop = t  # not accounting for scr refresh
                                targetLandmark2.tStopRefresh = tThisFlipGlobal  # on global time
                                targetLandmark2.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'targetLandmark2.stopped')
                                # update status
                                targetLandmark2.status = FINISHED
                                targetLandmark2.setAutoDraw(False)
                        
                        # *fixationRedReset* updates
                        
                        # if fixationRedReset is starting this frame...
                        if fixationRedReset.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            fixationRedReset.frameNStart = frameN  # exact frame index
                            fixationRedReset.tStart = t  # local t and not account for scr refresh
                            fixationRedReset.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(fixationRedReset, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixationRedReset.started')
                            # update status
                            fixationRedReset.status = STARTED
                            fixationRedReset.setAutoDraw(True)
                        
                        # if fixationRedReset is active this frame...
                        if fixationRedReset.status == STARTED:
                            # update params
                            pass
                        
                        # if fixationRedReset is stopping this frame...
                        if fixationRedReset.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > fixationRedReset.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                fixationRedReset.tStop = t  # not accounting for scr refresh
                                fixationRedReset.tStopRefresh = tThisFlipGlobal  # on global time
                                fixationRedReset.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'fixationRedReset.stopped')
                                # update status
                                fixationRedReset.status = FINISHED
                                fixationRedReset.setAutoDraw(False)
                        
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
                            reset.forceEnded = routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in reset.components:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "reset" ---
                    for thisComponent in reset.components:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    # store stop times for reset
                    reset.tStop = globalClock.getTime(format='float')
                    reset.tStopRefresh = tThisFlipGlobal
                    thisExp.addData('reset.stopped', reset.tStop)
                    # Run 'End Routine' code from resetCode
                    
                    for index,lm in enumerate(landmarks):
                        lm.opacity = 0
                        dotsArray[index].opacity = 0
                    
                    if 'experimentExpired' in globals() and experimentExpired:
                        print("Received experiment expired signal. Bye")
                    
                        # Try to end the outer loop, whatever it's named
                        if loopName == "blockTrials":
                            continueRoutine =  False
                            trials.finished = True
                            blockTrials.finished = True
                            loopName='breakLoop'
                            
                        elif loopName == "breakLoop":
                            continueRoutine =  False
                            responseBlock2.finished=True
                            trials2.finished=True
                            blockTrials2.finished=True
                            breakLoop.finished = True
                        
                        lastLoop.finished = True
                    
                    thisExp.addData('speed',speed)
                    thisExp.addData('stepSize',dt)
                    thisExp.addData('speed',speed)
                    thisExp.addData('startId',startId)
                    thisExp.addData('targetId',targetId)
                    thisExp.addData('startLandmarkPos',landmarks[startId].pos)
                    thisExp.addData('experimentExpired',experimentExpired)
                    thisExp.addData('visualMode',visualMode)
                    thisExp.addData('devMode',devMode)
                    thisExp.addData(f'{loopName}_duration',expClock.getTime())
                    thisExp.addData('turn',turn)
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if reset.maxDurationReached:
                        routineTimer.addTime(-reset.maxDuration)
                    elif reset.forceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-0.500000)
                    thisExp.nextEntry()
                    
                # completed 15.0 repeats of 'trials2'
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                thisExp.nextEntry()
                
            # completed 12.0 repeats of 'blockTrials2'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "stopEye" ---
            # create an object to store info about Routine stopEye
            stopEye = data.Routine(
                name='stopEye',
                components=[text_3, stopResp],
            )
            stopEye.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for stopResp
            stopResp.keys = []
            stopResp.rt = []
            _stopResp_allKeys = []
            # store start times for stopEye
            stopEye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            stopEye.tStart = globalClock.getTime(format='float')
            stopEye.status = STARTED
            stopEye.maxDuration = None
            # keep track of which components have finished
            stopEyeComponents = stopEye.components
            for thisComponent in stopEye.components:
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
            
            # --- Run Routine "stopEye" ---
            # if trial has changed, end Routine now
            if isinstance(breakLoop, data.TrialHandler2) and thisBreakLoop.thisN != breakLoop.thisTrial.thisN:
                continueRoutine = False
            stopEye.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_3* updates
                
                # if text_3 is starting this frame...
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.started')
                    # update status
                    text_3.status = STARTED
                    text_3.setAutoDraw(True)
                
                # if text_3 is active this frame...
                if text_3.status == STARTED:
                    # update params
                    pass
                
                # *stopResp* updates
                waitOnFlip = False
                
                # if stopResp is starting this frame...
                if stopResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stopResp.frameNStart = frameN  # exact frame index
                    stopResp.tStart = t  # local t and not account for scr refresh
                    stopResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stopResp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stopResp.started')
                    # update status
                    stopResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(stopResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(stopResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if stopResp.status == STARTED and not waitOnFlip:
                    theseKeys = stopResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _stopResp_allKeys.extend(theseKeys)
                    if len(_stopResp_allKeys):
                        stopResp.keys = _stopResp_allKeys[-1].name  # just the last key pressed
                        stopResp.rt = _stopResp_allKeys[-1].rt
                        stopResp.duration = _stopResp_allKeys[-1].duration
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
                    stopEye.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stopEye.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stopEye" ---
            for thisComponent in stopEye.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for stopEye
            stopEye.tStop = globalClock.getTime(format='float')
            stopEye.tStopRefresh = tThisFlipGlobal
            # check responses
            if stopResp.keys in ['', [], None]:  # No response was made
                stopResp.keys = None
            breakLoop.addData('stopResp.keys',stopResp.keys)
            if stopResp.keys != None:  # we had a response
                breakLoop.addData('stopResp.rt', stopResp.rt)
                breakLoop.addData('stopResp.duration', stopResp.duration)
            # the Routine "stopEye" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 6.0 repeats of 'breakLoop'
        
    # completed 1.0 repeats of 'lastLoop'
    
    
    # --- Prepare to start Routine "complete" ---
    # create an object to store info about Routine complete
    complete = data.Routine(
        name='complete',
        components=[completionText, keyEnd],
    )
    complete.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for keyEnd
    keyEnd.keys = []
    keyEnd.rt = []
    _keyEnd_allKeys = []
    # store start times for complete
    complete.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    complete.tStart = globalClock.getTime(format='float')
    complete.status = STARTED
    thisExp.addData('complete.started', complete.tStart)
    complete.maxDuration = None
    # keep track of which components have finished
    completeComponents = complete.components
    for thisComponent in complete.components:
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
    
    # --- Run Routine "complete" ---
    complete.forceEnded = routineForceEnded = not continueRoutine
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
            complete.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in complete.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "complete" ---
    for thisComponent in complete.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for complete
    complete.tStop = globalClock.getTime(format='float')
    complete.tStopRefresh = tThisFlipGlobal
    thisExp.addData('complete.stopped', complete.tStop)
    # check responses
    if keyEnd.keys in ['', [], None]:  # No response was made
        keyEnd.keys = None
    thisExp.addData('keyEnd.keys',keyEnd.keys)
    if keyEnd.keys != None:  # we had a response
        thisExp.addData('keyEnd.rt', keyEnd.rt)
        thisExp.addData('keyEnd.duration', keyEnd.duration)
    thisExp.nextEntry()
    # the Routine "complete" was not non-slip safe, so reset the non-slip timer
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
    expInfo = showExpInfoDlg(expInfo=expInfo)
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
