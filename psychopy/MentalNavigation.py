#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Mon May 26 12:39:23 2025
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware, iohub
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

# Run 'Before Experiment' code from initializationCode
import random
from psychopy import event

totalLandmarks  = 7
landmarkWidth = 0.5
landmarkHeight = 0.5 
interlmdistance = 0.5
tolerance=0.25
seed = random.randint(0,9999)

random.seed(42)

# Step 1: Build distance-to-pairs dictionary
all_distance_to_pairs = {
    k: [(i, j) for i in range(totalLandmarks) for j in range(totalLandmarks)
        if abs(i - j) == k]
    for k in range(1, totalLandmarks)
}

# Step 2: Select half of the pairs for training
training_pairs = {}

for k, pairs in all_distance_to_pairs.items():
    shuffled = pairs.copy()
    random.shuffle(shuffled)
    half_n = len(shuffled) // 2
    training_pairs[k] = shuffled[:half_n]

# Run 'Before Experiment' code from initializationCode
import random
from psychopy import event

totalLandmarks  = 7
landmarkWidth = 0.5
landmarkHeight = 0.5 
interlmdistance = 0.5
tolerance=0.25
seed = random.randint(0,9999)

random.seed(42)

# Step 1: Build distance-to-pairs dictionary
all_distance_to_pairs = {
    k: [(i, j) for i in range(totalLandmarks) for j in range(totalLandmarks)
        if abs(i - j) == k]
    for k in range(1, totalLandmarks)
}

# Step 2: Select half of the pairs for training
training_pairs = {}

for k, pairs in all_distance_to_pairs.items():
    shuffled = pairs.copy()
    random.shuffle(shuffled)
    half_n = len(shuffled) // 2
    training_pairs[k] = shuffled[:half_n]

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'MentalNavigation'  # from the Builder filename that created this script
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
        originPath='/Users/dexhrestha/Documents/Portfolio/neuronepal/neuronepal/psychopy/MentalNavigation.py',
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
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
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
    
    # Setup eyetracking
    ioConfig['eyetracker.hw.mouse.EyeTracker'] = {
        'name': 'tracker',
        'controls': {
            'move': [],
            'blink':('LEFT_BUTTON',),
            'saccade_threshold': 0.5,
        }
    }
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    deviceManager.devices['eyetracker'] = ioServer.getDevice('tracker')
    
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
        text='Welcome to the experiment.\n\nFix your eyes on the screen.\n\nPress left or right keys to reach the target landmark.\n\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyWelcome = keyboard.Keyboard(deviceName='keyWelcome')
    
    # --- Initialize components for Routine "blockSetup" ---
    
    # --- Initialize components for Routine "setup" ---
    fixationRed = visual.ShapeStim(
        win=win, name='fixationRed',units='norm', 
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "trial" ---
    dots = visual.DotStim(
        win=win, name='dots',units='norm', 
        nDots=200, dotSize=5.0,
        speed=0.0, dir=0.0, coherence=1.0,
        fieldPos=(0.0, 0.0), fieldSize=3.0, fieldAnchor='center', fieldShape='circle',
        signalDots='same', noiseDots='direction',dotLife=0.0,
        color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
        depth=0.0)
    targetLandmark = visual.ImageStim(
        win=win,
        name='targetLandmark', units='norm', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.4), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    fixationGreen = visual.ShapeStim(
        win=win, name='fixationGreen',units='norm', 
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    keyPress = keyboard.Keyboard(deviceName='keyPress')
    keyRelease = keyboard.Keyboard(deviceName='keyRelease')
    
    # --- Initialize components for Routine "reset" ---
    
    # --- Initialize components for Routine "setup" ---
    fixationRed = visual.ShapeStim(
        win=win, name='fixationRed',units='norm', 
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, -1.0000, -1.0000], fillColor=[1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "trial" ---
    dots = visual.DotStim(
        win=win, name='dots',units='norm', 
        nDots=200, dotSize=5.0,
        speed=0.0, dir=0.0, coherence=1.0,
        fieldPos=(0.0, 0.0), fieldSize=3.0, fieldAnchor='center', fieldShape='circle',
        signalDots='same', noiseDots='direction',dotLife=0.0,
        color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
        depth=0.0)
    targetLandmark = visual.ImageStim(
        win=win,
        name='targetLandmark', units='norm', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.4), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    fixationGreen = visual.ShapeStim(
        win=win, name='fixationGreen',units='norm', 
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    keyPress = keyboard.Keyboard(deviceName='keyPress')
    keyRelease = keyboard.Keyboard(deviceName='keyRelease')
    
    # --- Initialize components for Routine "reset" ---
    
    # --- Initialize components for Routine "complete" ---
    completionText = visual.TextStim(win=win, name='completionText',
        text='Thank you for your time',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
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
    
    # set up handler to look after randomisation of conditions etc
    blockTrials = data.TrialHandler2(
        name='blockTrials',
        nReps=6.0, 
        method='random', 
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
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisBlockTrial in blockTrials:
        currentLoop = blockTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
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
        speedOptions = [1,1.5,1.5,1.5,1,1]
        visualModeOptions = [True,True,False,True,True,False]
        
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
            dt = 0.01
            dots.speed = 0
            dots.dotLife = -1
            
            targetReached = False
            isTrain = True
            
            random.seed(None)
            
            distance_to_pairs = training_pairs if isTrain else all_distance_to_pairs
            distance  = random.randint(1,totalLandmarks-1)
            pairList = distance_to_pairs[distance].copy()
            random.shuffle(pairList)
            currentPair = random.choice(pairList)
            
            startId = currentPair[0]
            targetId =  currentPair[1]
            
            landmarks = [visual.ImageStim(
                win=win,
                name=str(i), units='norm', 
                image=f'public/landmarks/images/imageset1/{i}.jpg', mask=None, anchor='center',
                ori=0.0, pos=[0,0], draggable=False, size=(landmarkWidth, landmarkHeight),
                color=[1,1,1], colorSpace='rgb', opacity=None,
                flipHoriz=False, flipVert=False,
                texRes=128.0, interpolate=True, depth=-1.0) 
                for i in range(totalLandmarks)
                ]
            
            for index,lm in enumerate(landmarks):
                lm.pos = ((index - startId) * (landmarkWidth + interlmdistance),0.4)
                lm.setAutoDraw(True)
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
                    if tThisFlipGlobal > fixationRed.tStartRefresh + random.uniform(0,1)-frameTolerance:
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
            
            for thisResponseBlock in responseBlock:
                currentLoop = responseBlock
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # abbreviate parameter names if possible (e.g. rgb = thisResponseBlock.rgb)
                if thisResponseBlock != None:
                    for paramName in thisResponseBlock:
                        globals()[paramName] = thisResponseBlock[paramName]
                
                # --- Prepare to start Routine "trial" ---
                # create an object to store info about Routine trial
                trial = data.Routine(
                    name='trial',
                    components=[dots, targetLandmark, fixationGreen, keyPress, keyRelease],
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
                
                for lm  in  landmarks:
                    lm.opacity = 1
                targetLandmark.opacity = 1
                        
                targetLandmark.image = f'public/landmarks/images/imageset1/{targetId}.jpg'
                
                win.flip()
                
                
                if targetReached:
                    continueRoutine = False
                    
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
                    
                    # *fixationGreen* updates
                    
                    # if fixationGreen is starting this frame...
                    if fixationGreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixationGreen.frameNStart = frameN  # exact frame index
                        fixationGreen.tStart = t  # local t and not account for scr refresh
                        fixationGreen.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixationGreen, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixationGreen.started')
                        # update status
                        fixationGreen.status = STARTED
                        fixationGreen.setAutoDraw(True)
                    
                    # if fixationGreen is active this frame...
                    if fixationGreen.status == STARTED:
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
                    if  keyRelease.keys == 'left' or keyRelease.keys == 'right':
                        targetReached = abs(abs(targetLandmark.pos[0] - landmarks[startId].pos[0]) -  abs(targetId-startId)) <= tolerance * landmarkWidth
                    if keyPress.keys == 'left' or keyPress.keys  == 'right':
                        if not visualMode:
                            for lm  in  landmarks:
                                lm.opacity = 0
                            targetLandmark.opacity = 0
                            
                    if  keyPress.keys == 'left':
                        for lm in landmarks:
                            if  landmarks[-1].pos[0]<-1:
                                break
                            lm.pos -= (speed*dt,0)
                        dots.dir =  180
                    #    dots.speed = dt
                        dots.dotLife = 60
                        
                    elif  keyPress.keys == 'right':
                        for lm in landmarks:
                            if  landmarks[0].pos[0]>1:
                                break
                            lm.pos += (speed*dt,0)
                        dots.dir = 0
                    #    dots.speed =  dt
                        dots.dotLife = 60
                    
                     
                    
                    
                    
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
                # the Routine "trial" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
            # completed 2.0 repeats of 'responseBlock'
            
            
            # --- Prepare to start Routine "reset" ---
            # create an object to store info about Routine reset
            reset = data.Routine(
                name='reset',
                components=[],
            )
            reset.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
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
            for lm in landmarks:
                lm.opacity = 0
                del lm
            del landmarks
            core.wait(0.2)
            eyeRecord = False
            # the Routine "reset" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 15.0 repeats of 'trials'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        thisExp.nextEntry()
        
    # completed 6.0 repeats of 'blockTrials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler2(
        name='trials_3',
        nReps=5.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            globals()[paramName] = thisTrial_3[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
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
        dt = 0.01
        dots.speed = 0
        dots.dotLife = -1
        
        targetReached = False
        isTrain = True
        
        random.seed(None)
        
        distance_to_pairs = training_pairs if isTrain else all_distance_to_pairs
        distance  = random.randint(1,totalLandmarks-1)
        pairList = distance_to_pairs[distance].copy()
        random.shuffle(pairList)
        currentPair = random.choice(pairList)
        
        startId = currentPair[0]
        targetId =  currentPair[1]
        
        landmarks = [visual.ImageStim(
            win=win,
            name=str(i), units='norm', 
            image=f'public/landmarks/images/imageset1/{i}.jpg', mask=None, anchor='center',
            ori=0.0, pos=[0,0], draggable=False, size=(landmarkWidth, landmarkHeight),
            color=[1,1,1], colorSpace='rgb', opacity=None,
            flipHoriz=False, flipVert=False,
            texRes=128.0, interpolate=True, depth=-1.0) 
            for i in range(totalLandmarks)
            ]
        
        for index,lm in enumerate(landmarks):
            lm.pos = ((index - startId) * (landmarkWidth + interlmdistance),0.4)
            lm.setAutoDraw(True)
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
        if isinstance(trials_3, data.TrialHandler2) and thisTrial_3.thisN != trials_3.thisTrial.thisN:
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
                if tThisFlipGlobal > fixationRed.tStartRefresh + random.uniform(0,1)-frameTolerance:
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
        trials_2 = data.TrialHandler2(
            name='trials_2',
            nReps=2.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[dots, targetLandmark, fixationGreen, keyPress, keyRelease],
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
            
            for lm  in  landmarks:
                lm.opacity = 1
            targetLandmark.opacity = 1
                    
            targetLandmark.image = f'public/landmarks/images/imageset1/{targetId}.jpg'
            
            win.flip()
            
            
            if targetReached:
                continueRoutine = False
                
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
            if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
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
                
                # *fixationGreen* updates
                
                # if fixationGreen is starting this frame...
                if fixationGreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixationGreen.frameNStart = frameN  # exact frame index
                    fixationGreen.tStart = t  # local t and not account for scr refresh
                    fixationGreen.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixationGreen, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationGreen.started')
                    # update status
                    fixationGreen.status = STARTED
                    fixationGreen.setAutoDraw(True)
                
                # if fixationGreen is active this frame...
                if fixationGreen.status == STARTED:
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
                if  keyRelease.keys == 'left' or keyRelease.keys == 'right':
                    targetReached = abs(abs(targetLandmark.pos[0] - landmarks[startId].pos[0]) -  abs(targetId-startId)) <= tolerance * landmarkWidth
                if keyPress.keys == 'left' or keyPress.keys  == 'right':
                    if not visualMode:
                        for lm  in  landmarks:
                            lm.opacity = 0
                        targetLandmark.opacity = 0
                        
                if  keyPress.keys == 'left':
                    for lm in landmarks:
                        if  landmarks[-1].pos[0]<-1:
                            break
                        lm.pos -= (speed*dt,0)
                    dots.dir =  180
                #    dots.speed = dt
                    dots.dotLife = 60
                    
                elif  keyPress.keys == 'right':
                    for lm in landmarks:
                        if  landmarks[0].pos[0]>1:
                            break
                        lm.pos += (speed*dt,0)
                    dots.dir = 0
                #    dots.speed =  dt
                    dots.dotLife = 60
                
                 
                
                
                
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
            trials_2.addData('keyPress.keys',keyPress.keys)
            if keyPress.keys != None:  # we had a response
                trials_2.addData('keyPress.rt', keyPress.rt)
                trials_2.addData('keyPress.duration', keyPress.duration)
            # check responses
            if keyRelease.keys in ['', [], None]:  # No response was made
                keyRelease.keys = None
            trials_2.addData('keyRelease.keys',keyRelease.keys)
            if keyRelease.keys != None:  # we had a response
                trials_2.addData('keyRelease.rt', keyRelease.rt)
                trials_2.addData('keyRelease.duration', keyRelease.duration)
            # Run 'End Routine' code from move_images
            ## check if start and target is same
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 2.0 repeats of 'trials_2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "reset" ---
        # create an object to store info about Routine reset
        reset = data.Routine(
            name='reset',
            components=[],
        )
        reset.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
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
        if isinstance(trials_3, data.TrialHandler2) and thisTrial_3.thisN != trials_3.thisTrial.thisN:
            continueRoutine = False
        reset.forceEnded = routineForceEnded = not continueRoutine
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
        for lm in landmarks:
            lm.opacity = 0
            del lm
        del landmarks
        core.wait(0.2)
        eyeRecord = False
        # the Routine "reset" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'trials_3'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
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
