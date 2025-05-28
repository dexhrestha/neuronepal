#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Tue May 27 16:43:15 2025
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

# Run 'Before Experiment' code from setupCode
import random

#Experiment Environment Variables Start
dotLocationX = 5 # X cord of dot stimuli in deg
dotLocationY = 0  # Y cord of dot stimuli in deg
dotDirections = list(range(0,180,45))
dotCoherence = 1 # Proporiton of dots in same direction
dotPosition = 1 #dot Position either left [-1] or right [1]
nDirections = 4
nReps = 1
#Experiment Environment Variables End


totalTrials = nDirections*2
nhalf = int(totalTrials/2)

def make_50_percent_match(arr):
    if len(arr) % 2 != 0:
        raise ValueError("Array length must be even to allow exactly 50% match.")
    
    n = len(arr)
    half = n // 2
    indices = list(range(n))
    
    # Randomly choose half of the indices to match
    match_indices = set(random.sample(indices, half))
    
    result = []
    for i in range(n):
        if i in match_indices:
            # Match the original value
            result.append(arr[i])
        else:
            # Mismatch: choose a value different from the original
            possible_values = set(arr) - {arr[i]}
            if not possible_values:
                raise ValueError("Cannot ensure mismatch due to lack of alternative values.")
            result.append(random.choice(list(possible_values)))
    
    return result
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'DelayMatchtoCategory'  # from the Builder filename that created this script
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
        originPath='/Users/dexhrestha/Documents/Portfolio/neuronepal/neuronepal/psychopy/DelayMatchtoCategory.py',
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
    if deviceManager.getDevice('welcomeResp') is None:
        # initialise welcomeResp
        welcomeResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='welcomeResp',
        )
    if deviceManager.getDevice('keyResp') is None:
        # initialise keyResp
        keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyResp',
        )
    if deviceManager.getDevice('keyRespSample') is None:
        # initialise keyRespSample
        keyRespSample = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyRespSample',
        )
    if deviceManager.getDevice('keyRespDelay') is None:
        # initialise keyRespDelay
        keyRespDelay = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyRespDelay',
        )
    if deviceManager.getDevice('keyRespTestRelease') is None:
        # initialise keyRespTestRelease
        keyRespTestRelease = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='keyRespTestRelease',
        )
    if deviceManager.getDevice('exitResp') is None:
        # initialise exitResp
        exitResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='exitResp',
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
    
    # --- Initialize components for Routine "instructionRoutine" ---
    instructionText = visual.TextStim(win=win, name='instructionText',
        text='Instrcution \n\nWhen you see a white fixation cross press the spacebar.\n\nRelease the spacebar when the test category matches the sample category.\n\nPress enter key to proceed.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.5, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    welcomeResp = keyboard.Keyboard(deviceName='welcomeResp')
    
    # --- Initialize components for Routine "expSetup" ---
    
    # --- Initialize components for Routine "fixationRoutine" ---
    fixationWhite = visual.TextStim(win=win, name='fixationWhite',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "responseRoutine" ---
    fixationGreen = visual.TextStim(win=win, name='fixationGreen',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, 1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyResp = keyboard.Keyboard(deviceName='keyResp')
    
    # --- Initialize components for Routine "sampleRoutine" ---
    fixationGreenSample = visual.TextStim(win=win, name='fixationGreenSample',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, 1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sampleDots = visual.DotStim(
        win=win, name='sampleDots',units='deg', 
        nDots=100, dotSize=3.0,
        speed=0.1, dir=0.0, coherence=1.0,
        fieldPos=(5.0, 0.0), fieldSize=5.0, fieldAnchor='center', fieldShape='circle',
        signalDots='same', noiseDots='direction',dotLife=3.0,
        color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
        depth=-1.0)
    keyRespSample = keyboard.Keyboard(deviceName='keyRespSample')
    
    # --- Initialize components for Routine "delayRoutine" ---
    fixationGreenDelay = visual.TextStim(win=win, name='fixationGreenDelay',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, 1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyRespDelay = keyboard.Keyboard(deviceName='keyRespDelay')
    
    # --- Initialize components for Routine "testRoutine" ---
    fixationGreenTest = visual.TextStim(win=win, name='fixationGreenTest',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, 1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keyRespTestRelease = keyboard.Keyboard(deviceName='keyRespTestRelease')
    testDots = visual.DotStim(
        win=win, name='testDots',units='deg', 
        nDots=100, dotSize=3.0,
        speed=0.1, dir=0.0, coherence=1.0,
        fieldPos=(5.0, 0.0), fieldSize=5.0, fieldAnchor='center', fieldShape='circle',
        signalDots='same', noiseDots='direction',dotLife=3.0,
        color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
        depth=-2.0)
    
    # --- Initialize components for Routine "feedbackRoutine" ---
    feedbackText = visual.TextStim(win=win, name='feedbackText',
        text='Feedback Text',
        font='Arial',
        pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "exitRoutine" ---
    exitText = visual.TextStim(win=win, name='exitText',
        text='Thank you for participating in the experiment.\n\nPress space key to exit the screen.',
        font='Arial',
        units='deg', pos=(0, 0), draggable=False, height=1.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    exitResp = keyboard.Keyboard(deviceName='exitResp')
    
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
    
    # --- Prepare to start Routine "instructionRoutine" ---
    # create an object to store info about Routine instructionRoutine
    instructionRoutine = data.Routine(
        name='instructionRoutine',
        components=[instructionText, welcomeResp],
    )
    instructionRoutine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for welcomeResp
    welcomeResp.keys = []
    welcomeResp.rt = []
    _welcomeResp_allKeys = []
    # store start times for instructionRoutine
    instructionRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructionRoutine.tStart = globalClock.getTime(format='float')
    instructionRoutine.status = STARTED
    thisExp.addData('instructionRoutine.started', instructionRoutine.tStart)
    instructionRoutine.maxDuration = None
    # keep track of which components have finished
    instructionRoutineComponents = instructionRoutine.components
    for thisComponent in instructionRoutine.components:
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
    
    # --- Run Routine "instructionRoutine" ---
    instructionRoutine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionText* updates
        
        # if instructionText is starting this frame...
        if instructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionText.frameNStart = frameN  # exact frame index
            instructionText.tStart = t  # local t and not account for scr refresh
            instructionText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructionText.started')
            # update status
            instructionText.status = STARTED
            instructionText.setAutoDraw(True)
        
        # if instructionText is active this frame...
        if instructionText.status == STARTED:
            # update params
            pass
        
        # *welcomeResp* updates
        waitOnFlip = False
        
        # if welcomeResp is starting this frame...
        if welcomeResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcomeResp.frameNStart = frameN  # exact frame index
            welcomeResp.tStart = t  # local t and not account for scr refresh
            welcomeResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcomeResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcomeResp.started')
            # update status
            welcomeResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcomeResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcomeResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcomeResp.status == STARTED and not waitOnFlip:
            theseKeys = welcomeResp.getKeys(keyList=['return','space'], ignoreKeys=["escape"], waitRelease=False)
            _welcomeResp_allKeys.extend(theseKeys)
            if len(_welcomeResp_allKeys):
                welcomeResp.keys = _welcomeResp_allKeys[-1].name  # just the last key pressed
                welcomeResp.rt = _welcomeResp_allKeys[-1].rt
                welcomeResp.duration = _welcomeResp_allKeys[-1].duration
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
            instructionRoutine.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionRoutine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructionRoutine" ---
    for thisComponent in instructionRoutine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructionRoutine
    instructionRoutine.tStop = globalClock.getTime(format='float')
    instructionRoutine.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructionRoutine.stopped', instructionRoutine.tStop)
    # check responses
    if welcomeResp.keys in ['', [], None]:  # No response was made
        welcomeResp.keys = None
    thisExp.addData('welcomeResp.keys',welcomeResp.keys)
    if welcomeResp.keys != None:  # we had a response
        thisExp.addData('welcomeResp.rt', welcomeResp.rt)
        thisExp.addData('welcomeResp.duration', welcomeResp.duration)
    thisExp.nextEntry()
    # the Routine "instructionRoutine" was not non-slip safe, so reset the non-slip timer
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
    # Run 'Begin Routine' code from setupCode
    assert totalTrials%nDirections == 0,"Total Number of trials should be multple of number of unique directions"
    
    dotPositions= [1 for i in range(nhalf)]+[-1 for i in range(nhalf)]
    random.shuffle(dotPositions)
    
    categoryA = [0,-45,-90]
    
    categoryB = [180,45,90]
    
    sampleDirections = categoryA+categoryB
    sampleDirections = [item for _ in range(2) for item in sampleDirections]
    
    sampleDirections = [item for _ in range(nReps) for item in sampleDirections]
    
    random.shuffle(sampleDirections)
    
    sampleCategories = ['A' if direction in categoryA else 'B' for direction in sampleDirections]
    
    testCategories = make_50_percent_match(sampleCategories)
    print("Sample",sampleCategories)
    print("Test",testCategories)
    
    testDirections = [random.choice(categoryB) if category=='B' else random.choice(categoryA)  for category in testCategories]
    print("Sample Directions",sampleDirections)
    print("Test Directions",testDirections)
    
    count = 0
    for i,_ in enumerate(testDirections):
        if  sampleCategories[i]==testCategories[i]:
            count += 1
            
    print("Proportion of match",count/len(testDirections)*100)
            
    
    
    
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
    trials = data.TrialHandler2(
        name='trials',
        nReps=nDirections*2*1, 
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
        
        # --- Prepare to start Routine "fixationRoutine" ---
        # create an object to store info about Routine fixationRoutine
        fixationRoutine = data.Routine(
            name='fixationRoutine',
            components=[fixationWhite],
        )
        fixationRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from trialSetupCode
        dotPosition = dotPositions[trials.thisN]
        dotLocation = (dotPosition*dotLocationX, dotLocationY)
        categoryMatch = False
        gazeShift = 0
        # store start times for fixationRoutine
        fixationRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixationRoutine.tStart = globalClock.getTime(format='float')
        fixationRoutine.status = STARTED
        thisExp.addData('fixationRoutine.started', fixationRoutine.tStart)
        fixationRoutine.maxDuration = None
        # keep track of which components have finished
        fixationRoutineComponents = fixationRoutine.components
        for thisComponent in fixationRoutine.components:
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
        
        # --- Run Routine "fixationRoutine" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        fixationRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationWhite* updates
            
            # if fixationWhite is starting this frame...
            if fixationWhite.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationWhite.frameNStart = frameN  # exact frame index
                fixationWhite.tStart = t  # local t and not account for scr refresh
                fixationWhite.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationWhite, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationWhite.started')
                # update status
                fixationWhite.status = STARTED
                fixationWhite.setAutoDraw(True)
            
            # if fixationWhite is active this frame...
            if fixationWhite.status == STARTED:
                # update params
                pass
            
            # if fixationWhite is stopping this frame...
            if fixationWhite.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationWhite.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationWhite.tStop = t  # not accounting for scr refresh
                    fixationWhite.tStopRefresh = tThisFlipGlobal  # on global time
                    fixationWhite.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationWhite.stopped')
                    # update status
                    fixationWhite.status = FINISHED
                    fixationWhite.setAutoDraw(False)
            
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
                fixationRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixationRoutine" ---
        for thisComponent in fixationRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixationRoutine
        fixationRoutine.tStop = globalClock.getTime(format='float')
        fixationRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixationRoutine.stopped', fixationRoutine.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixationRoutine.maxDurationReached:
            routineTimer.addTime(-fixationRoutine.maxDuration)
        elif fixationRoutine.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "responseRoutine" ---
        # create an object to store info about Routine responseRoutine
        responseRoutine = data.Routine(
            name='responseRoutine',
            components=[fixationGreen, keyResp],
        )
        responseRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for keyResp
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # store start times for responseRoutine
        responseRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        responseRoutine.tStart = globalClock.getTime(format='float')
        responseRoutine.status = STARTED
        thisExp.addData('responseRoutine.started', responseRoutine.tStart)
        responseRoutine.maxDuration = None
        # keep track of which components have finished
        responseRoutineComponents = responseRoutine.components
        for thisComponent in responseRoutine.components:
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
        
        # --- Run Routine "responseRoutine" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        responseRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
            
            # if fixationGreen is stopping this frame...
            if fixationGreen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationGreen.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationGreen.tStop = t  # not accounting for scr refresh
                    fixationGreen.tStopRefresh = tThisFlipGlobal  # on global time
                    fixationGreen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationGreen.stopped')
                    # update status
                    fixationGreen.status = FINISHED
                    fixationGreen.setAutoDraw(False)
            
            # *keyResp* updates
            waitOnFlip = False
            
            # if keyResp is starting this frame...
            if keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyResp.started')
                # update status
                keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if keyResp is stopping this frame...
            if keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyResp.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    keyResp.tStop = t  # not accounting for scr refresh
                    keyResp.tStopRefresh = tThisFlipGlobal  # on global time
                    keyResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'keyResp.stopped')
                    # update status
                    keyResp.status = FINISHED
                    keyResp.status = FINISHED
            if keyResp.status == STARTED and not waitOnFlip:
                theseKeys = keyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = _keyResp_allKeys[-1].name  # just the last key pressed
                    keyResp.rt = _keyResp_allKeys[-1].rt
                    keyResp.duration = _keyResp_allKeys[-1].duration
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
                responseRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "responseRoutine" ---
        for thisComponent in responseRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for responseRoutine
        responseRoutine.tStop = globalClock.getTime(format='float')
        responseRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('responseRoutine.stopped', responseRoutine.tStop)
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
        trials.addData('keyResp.keys',keyResp.keys)
        if keyResp.keys != None:  # we had a response
            trials.addData('keyResp.rt', keyResp.rt)
            trials.addData('keyResp.duration', keyResp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if responseRoutine.maxDurationReached:
            routineTimer.addTime(-responseRoutine.maxDuration)
        elif responseRoutine.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "sampleRoutine" ---
        # create an object to store info about Routine sampleRoutine
        sampleRoutine = data.Routine(
            name='sampleRoutine',
            components=[fixationGreenSample, sampleDots, keyRespSample],
        )
        sampleRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        sampleDots.refreshDots()
        # create starting attributes for keyRespSample
        keyRespSample.keys = []
        keyRespSample.rt = []
        _keyRespSample_allKeys = []
        # Run 'Begin Routine' code from sampleSetupCode
        sampleDots.fieldPos = dotLocation
        sampleDots.dir = sampleDirections[trials.thisN]
        # store start times for sampleRoutine
        sampleRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        sampleRoutine.tStart = globalClock.getTime(format='float')
        sampleRoutine.status = STARTED
        thisExp.addData('sampleRoutine.started', sampleRoutine.tStart)
        sampleRoutine.maxDuration = None
        # keep track of which components have finished
        sampleRoutineComponents = sampleRoutine.components
        for thisComponent in sampleRoutine.components:
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
        
        # --- Run Routine "sampleRoutine" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        sampleRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.15:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationGreenSample* updates
            
            # if fixationGreenSample is starting this frame...
            if fixationGreenSample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationGreenSample.frameNStart = frameN  # exact frame index
                fixationGreenSample.tStart = t  # local t and not account for scr refresh
                fixationGreenSample.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationGreenSample, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationGreenSample.started')
                # update status
                fixationGreenSample.status = STARTED
                fixationGreenSample.setAutoDraw(True)
            
            # if fixationGreenSample is active this frame...
            if fixationGreenSample.status == STARTED:
                # update params
                pass
            
            # if fixationGreenSample is stopping this frame...
            if fixationGreenSample.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationGreenSample.tStartRefresh + 1.15-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationGreenSample.tStop = t  # not accounting for scr refresh
                    fixationGreenSample.tStopRefresh = tThisFlipGlobal  # on global time
                    fixationGreenSample.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationGreenSample.stopped')
                    # update status
                    fixationGreenSample.status = FINISHED
                    fixationGreenSample.setAutoDraw(False)
            
            # *sampleDots* updates
            
            # if sampleDots is starting this frame...
            if sampleDots.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sampleDots.frameNStart = frameN  # exact frame index
                sampleDots.tStart = t  # local t and not account for scr refresh
                sampleDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sampleDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sampleDots.started')
                # update status
                sampleDots.status = STARTED
                sampleDots.setAutoDraw(True)
            
            # if sampleDots is active this frame...
            if sampleDots.status == STARTED:
                # update params
                pass
            
            # if sampleDots is stopping this frame...
            if sampleDots.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sampleDots.tStartRefresh + 0.65-frameTolerance:
                    # keep track of stop time/frame for later
                    sampleDots.tStop = t  # not accounting for scr refresh
                    sampleDots.tStopRefresh = tThisFlipGlobal  # on global time
                    sampleDots.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sampleDots.stopped')
                    # update status
                    sampleDots.status = FINISHED
                    sampleDots.setAutoDraw(False)
            
            # *keyRespSample* updates
            waitOnFlip = False
            
            # if keyRespSample is starting this frame...
            if keyRespSample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyRespSample.frameNStart = frameN  # exact frame index
                keyRespSample.tStart = t  # local t and not account for scr refresh
                keyRespSample.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyRespSample, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyRespSample.started')
                # update status
                keyRespSample.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyRespSample.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyRespSample.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if keyRespSample is stopping this frame...
            if keyRespSample.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyRespSample.tStartRefresh + 1.15-frameTolerance:
                    # keep track of stop time/frame for later
                    keyRespSample.tStop = t  # not accounting for scr refresh
                    keyRespSample.tStopRefresh = tThisFlipGlobal  # on global time
                    keyRespSample.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'keyRespSample.stopped')
                    # update status
                    keyRespSample.status = FINISHED
                    keyRespSample.status = FINISHED
            if keyRespSample.status == STARTED and not waitOnFlip:
                theseKeys = keyRespSample.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _keyRespSample_allKeys.extend(theseKeys)
                if len(_keyRespSample_allKeys):
                    keyRespSample.keys = _keyRespSample_allKeys[-1].name  # just the last key pressed
                    keyRespSample.rt = _keyRespSample_allKeys[-1].rt
                    keyRespSample.duration = _keyRespSample_allKeys[-1].duration
            
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
                sampleRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sampleRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "sampleRoutine" ---
        for thisComponent in sampleRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for sampleRoutine
        sampleRoutine.tStop = globalClock.getTime(format='float')
        sampleRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('sampleRoutine.stopped', sampleRoutine.tStop)
        # check responses
        if keyRespSample.keys in ['', [], None]:  # No response was made
            keyRespSample.keys = None
        trials.addData('keyRespSample.keys',keyRespSample.keys)
        if keyRespSample.keys != None:  # we had a response
            trials.addData('keyRespSample.rt', keyRespSample.rt)
            trials.addData('keyRespSample.duration', keyRespSample.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if sampleRoutine.maxDurationReached:
            routineTimer.addTime(-sampleRoutine.maxDuration)
        elif sampleRoutine.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.150000)
        
        # --- Prepare to start Routine "delayRoutine" ---
        # create an object to store info about Routine delayRoutine
        delayRoutine = data.Routine(
            name='delayRoutine',
            components=[fixationGreenDelay, keyRespDelay],
        )
        delayRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for keyRespDelay
        keyRespDelay.keys = []
        keyRespDelay.rt = []
        _keyRespDelay_allKeys = []
        # store start times for delayRoutine
        delayRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        delayRoutine.tStart = globalClock.getTime(format='float')
        delayRoutine.status = STARTED
        thisExp.addData('delayRoutine.started', delayRoutine.tStart)
        delayRoutine.maxDuration = None
        # keep track of which components have finished
        delayRoutineComponents = delayRoutine.components
        for thisComponent in delayRoutine.components:
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
        
        # --- Run Routine "delayRoutine" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        delayRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationGreenDelay* updates
            
            # if fixationGreenDelay is starting this frame...
            if fixationGreenDelay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationGreenDelay.frameNStart = frameN  # exact frame index
                fixationGreenDelay.tStart = t  # local t and not account for scr refresh
                fixationGreenDelay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationGreenDelay, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationGreenDelay.started')
                # update status
                fixationGreenDelay.status = STARTED
                fixationGreenDelay.setAutoDraw(True)
            
            # if fixationGreenDelay is active this frame...
            if fixationGreenDelay.status == STARTED:
                # update params
                pass
            
            # if fixationGreenDelay is stopping this frame...
            if fixationGreenDelay.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationGreenDelay.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationGreenDelay.tStop = t  # not accounting for scr refresh
                    fixationGreenDelay.tStopRefresh = tThisFlipGlobal  # on global time
                    fixationGreenDelay.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationGreenDelay.stopped')
                    # update status
                    fixationGreenDelay.status = FINISHED
                    fixationGreenDelay.setAutoDraw(False)
            
            # *keyRespDelay* updates
            waitOnFlip = False
            
            # if keyRespDelay is starting this frame...
            if keyRespDelay.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyRespDelay.frameNStart = frameN  # exact frame index
                keyRespDelay.tStart = t  # local t and not account for scr refresh
                keyRespDelay.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyRespDelay, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyRespDelay.started')
                # update status
                keyRespDelay.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyRespDelay.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyRespDelay.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if keyRespDelay is stopping this frame...
            if keyRespDelay.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyRespDelay.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    keyRespDelay.tStop = t  # not accounting for scr refresh
                    keyRespDelay.tStopRefresh = tThisFlipGlobal  # on global time
                    keyRespDelay.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'keyRespDelay.stopped')
                    # update status
                    keyRespDelay.status = FINISHED
                    keyRespDelay.status = FINISHED
            if keyRespDelay.status == STARTED and not waitOnFlip:
                theseKeys = keyRespDelay.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _keyRespDelay_allKeys.extend(theseKeys)
                if len(_keyRespDelay_allKeys):
                    keyRespDelay.keys = _keyRespDelay_allKeys[-1].name  # just the last key pressed
                    keyRespDelay.rt = _keyRespDelay_allKeys[-1].rt
                    keyRespDelay.duration = _keyRespDelay_allKeys[-1].duration
            
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
                delayRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in delayRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "delayRoutine" ---
        for thisComponent in delayRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for delayRoutine
        delayRoutine.tStop = globalClock.getTime(format='float')
        delayRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('delayRoutine.stopped', delayRoutine.tStop)
        # check responses
        if keyRespDelay.keys in ['', [], None]:  # No response was made
            keyRespDelay.keys = None
        trials.addData('keyRespDelay.keys',keyRespDelay.keys)
        if keyRespDelay.keys != None:  # we had a response
            trials.addData('keyRespDelay.rt', keyRespDelay.rt)
            trials.addData('keyRespDelay.duration', keyRespDelay.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if delayRoutine.maxDurationReached:
            routineTimer.addTime(-delayRoutine.maxDuration)
        elif delayRoutine.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "testRoutine" ---
        # create an object to store info about Routine testRoutine
        testRoutine = data.Routine(
            name='testRoutine',
            components=[fixationGreenTest, keyRespTestRelease, testDots],
        )
        testRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for keyRespTestRelease
        keyRespTestRelease.keys = []
        keyRespTestRelease.rt = []
        _keyRespTestRelease_allKeys = []
        testDots.refreshDots()
        # Run 'Begin Routine' code from testSetupCode
        testDots.fieldPos = dotLocation
        testDots.dir = testDirections[trials.thisN]
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
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixationGreenTest* updates
            
            # if fixationGreenTest is starting this frame...
            if fixationGreenTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationGreenTest.frameNStart = frameN  # exact frame index
                fixationGreenTest.tStart = t  # local t and not account for scr refresh
                fixationGreenTest.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationGreenTest, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationGreenTest.started')
                # update status
                fixationGreenTest.status = STARTED
                fixationGreenTest.setAutoDraw(True)
            
            # if fixationGreenTest is active this frame...
            if fixationGreenTest.status == STARTED:
                # update params
                pass
            
            # if fixationGreenTest is stopping this frame...
            if fixationGreenTest.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationGreenTest.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationGreenTest.tStop = t  # not accounting for scr refresh
                    fixationGreenTest.tStopRefresh = tThisFlipGlobal  # on global time
                    fixationGreenTest.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixationGreenTest.stopped')
                    # update status
                    fixationGreenTest.status = FINISHED
                    fixationGreenTest.setAutoDraw(False)
            
            # *keyRespTestRelease* updates
            waitOnFlip = False
            
            # if keyRespTestRelease is starting this frame...
            if keyRespTestRelease.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyRespTestRelease.frameNStart = frameN  # exact frame index
                keyRespTestRelease.tStart = t  # local t and not account for scr refresh
                keyRespTestRelease.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyRespTestRelease, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyRespTestRelease.started')
                # update status
                keyRespTestRelease.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyRespTestRelease.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyRespTestRelease.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if keyRespTestRelease is stopping this frame...
            if keyRespTestRelease.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyRespTestRelease.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    keyRespTestRelease.tStop = t  # not accounting for scr refresh
                    keyRespTestRelease.tStopRefresh = tThisFlipGlobal  # on global time
                    keyRespTestRelease.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'keyRespTestRelease.stopped')
                    # update status
                    keyRespTestRelease.status = FINISHED
                    keyRespTestRelease.status = FINISHED
            if keyRespTestRelease.status == STARTED and not waitOnFlip:
                theseKeys = keyRespTestRelease.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=True)
                _keyRespTestRelease_allKeys.extend(theseKeys)
                if len(_keyRespTestRelease_allKeys):
                    keyRespTestRelease.keys = _keyRespTestRelease_allKeys[0].name  # just the first key pressed
                    keyRespTestRelease.rt = _keyRespTestRelease_allKeys[0].rt
                    keyRespTestRelease.duration = _keyRespTestRelease_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *testDots* updates
            
            # if testDots is starting this frame...
            if testDots.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                testDots.frameNStart = frameN  # exact frame index
                testDots.tStart = t  # local t and not account for scr refresh
                testDots.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(testDots, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'testDots.started')
                # update status
                testDots.status = STARTED
                testDots.setAutoDraw(True)
            
            # if testDots is active this frame...
            if testDots.status == STARTED:
                # update params
                pass
            
            # if testDots is stopping this frame...
            if testDots.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > testDots.tStartRefresh + 0.65-frameTolerance:
                    # keep track of stop time/frame for later
                    testDots.tStop = t  # not accounting for scr refresh
                    testDots.tStopRefresh = tThisFlipGlobal  # on global time
                    testDots.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'testDots.stopped')
                    # update status
                    testDots.status = FINISHED
                    testDots.setAutoDraw(False)
            
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
        if keyRespTestRelease.keys in ['', [], None]:  # No response was made
            keyRespTestRelease.keys = None
        trials.addData('keyRespTestRelease.keys',keyRespTestRelease.keys)
        if keyRespTestRelease.keys != None:  # we had a response
            trials.addData('keyRespTestRelease.rt', keyRespTestRelease.rt)
            trials.addData('keyRespTestRelease.duration', keyRespTestRelease.duration)
        # Run 'End Routine' code from testSetupCode
        categoryMatch = sampleCategories[trials.thisN]   == testCategories[trials.thisN]  
        print('keyReleased',keyRespTestRelease.keys)
        if categoryMatch: 
            if keyRespTestRelease.keys == 'space': # release 
                correct = 'Correct'
            else: # no release
                correct = 'Incorrect'
        else: 
            if keyRespTestRelease.keys == 'space': # release 
                correct = 'Incorrect'
            else: # no release 
                correct = 'Correct'
        
        fixation = "Keep Fixation" if gazeShift > 2 else ""
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if testRoutine.maxDurationReached:
            routineTimer.addTime(-testRoutine.maxDuration)
        elif testRoutine.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "feedbackRoutine" ---
        # create an object to store info about Routine feedbackRoutine
        feedbackRoutine = data.Routine(
            name='feedbackRoutine',
            components=[feedbackText],
        )
        feedbackRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from feedbackCode
        
        feedbackText.setText(f"{correct} \n {fixation}")
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
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackText* updates
            
            # if feedbackText is starting this frame...
            if feedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackText.frameNStart = frameN  # exact frame index
                feedbackText.tStart = t  # local t and not account for scr refresh
                feedbackText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackText.started')
                # update status
                feedbackText.status = STARTED
                feedbackText.setAutoDraw(True)
            
            # if feedbackText is active this frame...
            if feedbackText.status == STARTED:
                # update params
                pass
            
            # if feedbackText is stopping this frame...
            if feedbackText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackText.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackText.tStop = t  # not accounting for scr refresh
                    feedbackText.tStopRefresh = tThisFlipGlobal  # on global time
                    feedbackText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbackText.stopped')
                    # update status
                    feedbackText.status = FINISHED
                    feedbackText.setAutoDraw(False)
            
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedbackRoutine.maxDurationReached:
            routineTimer.addTime(-feedbackRoutine.maxDuration)
        elif feedbackRoutine.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed nDirections*2*1 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "exitRoutine" ---
    # create an object to store info about Routine exitRoutine
    exitRoutine = data.Routine(
        name='exitRoutine',
        components=[exitText, exitResp],
    )
    exitRoutine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for exitResp
    exitResp.keys = []
    exitResp.rt = []
    _exitResp_allKeys = []
    # store start times for exitRoutine
    exitRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    exitRoutine.tStart = globalClock.getTime(format='float')
    exitRoutine.status = STARTED
    thisExp.addData('exitRoutine.started', exitRoutine.tStart)
    exitRoutine.maxDuration = None
    # keep track of which components have finished
    exitRoutineComponents = exitRoutine.components
    for thisComponent in exitRoutine.components:
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
    
    # --- Run Routine "exitRoutine" ---
    exitRoutine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *exitText* updates
        
        # if exitText is starting this frame...
        if exitText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitText.frameNStart = frameN  # exact frame index
            exitText.tStart = t  # local t and not account for scr refresh
            exitText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exitText.started')
            # update status
            exitText.status = STARTED
            exitText.setAutoDraw(True)
        
        # if exitText is active this frame...
        if exitText.status == STARTED:
            # update params
            pass
        
        # *exitResp* updates
        waitOnFlip = False
        
        # if exitResp is starting this frame...
        if exitResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitResp.frameNStart = frameN  # exact frame index
            exitResp.tStart = t  # local t and not account for scr refresh
            exitResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exitResp.started')
            # update status
            exitResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(exitResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(exitResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if exitResp.status == STARTED and not waitOnFlip:
            theseKeys = exitResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _exitResp_allKeys.extend(theseKeys)
            if len(_exitResp_allKeys):
                exitResp.keys = _exitResp_allKeys[-1].name  # just the last key pressed
                exitResp.rt = _exitResp_allKeys[-1].rt
                exitResp.duration = _exitResp_allKeys[-1].duration
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
            exitRoutine.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exitRoutine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exitRoutine" ---
    for thisComponent in exitRoutine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for exitRoutine
    exitRoutine.tStop = globalClock.getTime(format='float')
    exitRoutine.tStopRefresh = tThisFlipGlobal
    thisExp.addData('exitRoutine.stopped', exitRoutine.tStop)
    # check responses
    if exitResp.keys in ['', [], None]:  # No response was made
        exitResp.keys = None
    thisExp.addData('exitResp.keys',exitResp.keys)
    if exitResp.keys != None:  # we had a response
        thisExp.addData('exitResp.rt', exitResp.rt)
        thisExp.addData('exitResp.duration', exitResp.duration)
    thisExp.nextEntry()
    # the Routine "exitRoutine" was not non-slip safe, so reset the non-slip timer
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
