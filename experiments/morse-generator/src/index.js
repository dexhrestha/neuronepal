// Third-party imports
import {
  Color,
  Mesh,
  MeshStandardMaterial,
  SphereGeometry,
  Vector2,
  Vector3,
} from 'three';

// Package imports
import {
  Experiment,
  Block,
  DisplayElement,
  Survey,
  InstructionsPanel,
  CSS2D,
} from 'ouvrai';
import { fileContents } from './fileContents.js';
import { rnorm, sampleDelay } from './utils.js'
/*
 * Main function contains all experiment logic. At a minimum you should:
 * 1. Create a `new Experiment({...config})`
 * 2. Initialize the state machine with `exp.state.init(states, changeFunc)`
 * 3. Create stimuli and add them with `exp.sceneManager.scene.add(...objects)`
 * 4. Create trial sequence with `exp.createTrialSequence([...blocks])`
 * 5. Start the main loop with `exp.start(calcFunc, stateFunc, displayFunc)`
 * 6. Design your experiment by editing `calcFunc`, `stateFunc`, and `displayFunc`
 */

async function main() {
  /*
   * The first step is always to create a new Experiment({...config}) with your configuration options.
   * Ouvrai configuration options are documented in the Experiment class.
   * You can also provide other experiment-level variables here as additional fields.
   * All values in the configuration object will be saved in your data.
   * You can add variables throughout the experiment using `exp.cfg.VARNAME = VALUE`.
   */
  
  const config = JSON.parse(import.meta.env.VITE_CONFIG);
  

  const exp = new Experiment({
    // Options to make development easier
    devOptions: {
      skipConsent: true,
      saveTrialList: false,
      allowExitFullscreen: false,
      allowExitPointerlock: false,
    },

    // Platform settings
    requireDesktop: true,
    requireChrome: false,

    // Three.js settings
    orthographic: true,
    cssScene: true,
    // demo: true,
    // Scene quantities
    // Assume meters and seconds for three.js, but note tween.js uses milliseconds
    cursorRadius: 0.02,
    cursorMinXYZ: new Vector3(-1, -1, -5),
    cursorMaxXYZ: new Vector3(1, 1, 5),
    targetRadius: 0.04,
    homeRadius: 0.05,
    score:0,

    // Procedure
    delayDuration: sampleDelay(0.5,1.5),
    
    
    //Morse
    sequence: '-C.G.C-G-C.CU', //tGGiGGmGGe -C.G.C-G-C.U
    // normal speed : 1x = 10 words per minute #29 units 3.48 s + delay(0.5,1.5)s
    // speed : [1,0.5,2],
    // totalDuration 
    speed:[1],
    dotDuration:  config.dotDuration,
    charDuration: config.dotDuration*3, //C
    gapDuration:  config.dotDuration, //G
    dashDuration: config.dotDuration*3,
    responseWaitTime:config.responseWaitTime,
    experimentSourceCode: fileContents,
    searchParams : new URLSearchParams(window.location.search),
  });

  /*
   * Initialize visual stimuli with three.js
   */

  
  const home = new Mesh(
    new SphereGeometry(exp.cfg.homeRadius),
    new MeshStandardMaterial() // we will set color in displayFunc()
  );
  const cursor = new Mesh(
    new SphereGeometry(exp.cfg.cursorRadius),
    new MeshStandardMaterial({ color: 'white' })
  );
  cursor.position.setZ(exp.cfg.homeRadius + exp.cfg.cursorRadius);
  const target = new Mesh(
    new SphereGeometry(exp.cfg.targetRadius),
    new MeshStandardMaterial({ color: 'orangered' })
  );
  target.visible = false;
  exp.sceneManager.scene.add(home, cursor, target);

  /*
   * You can display overlay text on the scene by adding CSS2D to cssScene
   */
  const overlayText = new CSS2D();
  overlayText.object.position.set(0, 0.67, 0);
  exp.sceneManager.cssScene.add(overlayText.object);

  const scoreText = new CSS2D();
  scoreText.object.position.set(0.7,0.5,0);
  exp.sceneManager.cssScene.add(scoreText.object);

  /*
   * Create trial sequence from array of block objects.
   */
  if (exp.cfg.searchParams.get("DAY")>=5){
    exp.createTrialSequence([
      new Block({
        variables: {
          // targetDirection: [-1, 1],
          // targetDistance: [0.2, 0.2],
          speed:[...Array.from({ length:config.numTrials}, (_, i) => 1)]
        },
        options: {
          name: `Day ${exp.cfg.searchParams.get("DAY")} Block 1 `,
          reps: config.numBlocksTest,
          shuffle: true,
        },
      }),
      new Block({
        variables: {
          speed:[...Array.from({ length:config.numTrials}, (_, i) => 1),...Array.from({ length:15}, (_, i) => 2),...Array.from({ length:15}, (_, i) => 0.5)]
        },
        options: {
          name: `Day ${exp.cfg.searchParams.get("DAY")} Block 2 `,
          reps: config.numBlocksTest,
          shuffle: true,
        },
      }),
    ]);
  }else{
    exp.createTrialSequence([
      new Block({
        variables: {
          speed:[...Array.from({ length:config.numTrials}, (_, i) => 1)]
        },
        options: {
          name: `Day ${exp.cfg.searchParams.get("DAY")} Block `,
          reps: config.numBlocksTrain,
          shuffle: true,
        },
      }),
    ]);
  }

  /*
   * You must initialize an empty object called trial
   */
  let trial = {};

  /**
   * An instructions panel overlaid in the top-right of the screen.
   * Keep these instructions short. Use CSS2D to overlay instructions on the scene.
   */
  exp.instructions = new InstructionsPanel({
    content: `Use the Right key to reproduce the morse code in ${trial.speed}x speed`,
  });

  /**
   * Ask questions at the end of the experiment with the Survey class.
   * You probably don't need to ask for funding agency required demographic information.
   * On Prolific, most participants have already provid  ed this information.
   * On Mechanical Turk, Ouvrai collects this information separately on the HIT posting.
   */
  exp.survey = new Survey();
  // exp.survey.addQuestion({
  //   type: 'list',
  //   name: 'device',
  //   message:
  //     'Did you use a mouse, trackpad, or something else for this experiment?',
  //   choices: ['Mouse', 'Tra ckpad', 'Other'],
  //   options: { required: true },
  // });
  exp.survey.addQuestion({
    type: 'list',
    name: 'hand',
    message: 'Which hand did you primarily use during the experiment?',
    choices: ['Right', 'Left'],
    options: { required: true },
  });

  /**
   * Initialize Finite State Machine (FSM) that manages the flow of your experiment.
   * You will define the behavior and transitions of the FSM below in stateFunc().
   */
  exp.state.init(
    [
      'CONSENT',
      'SIGNIN',
      'SETUP',
      'INSTRUCTION',
      'START',
      'DELAY',
      //GENERATE
      '.', // dot 
      '-', // dash
      'G', // gap
      'C', // inter character gap
      //REPRODUCE
      'DOWN',
      'U',// INSTRUCTION FOR REPRODUCE
      'RETURN',
      'FINISH',
      'ADVANCE',
      'SURVEY',
      'CODE',
      'FULLSCREEN',
      'POINTERLOCK',
      'DATABASE',
      'BLOCKED',
    ],
    handleStateChange
  );

  /*
   * Add a custom event handler that moves the cursor in response to mouse/trackpad inputs
   */
  document.body.addEventListener('mousemove', handleMouseMove);
  document.body.addEventListener('keydown', handleKeyDown);
  document.body.addEventListener('keyup',handleKeyUp);


  // Start the main loop! These three functions will take it from here.
  exp.start(calcFunc, stateFunc, displayFunc);

  /**
   * Use `calcFunc` for calculations used in _multiple states_
   */
  function calcFunc() {
    // Objects are in 3D space so we copy to Vector2 to ignore the depth dimension
    let cursPosXY = new Vector2().copy(cursor.position);
    let homePosXY = new Vector2().copy(home.position);
    let targPosXY = new Vector2().copy(target.position);
    

    cursor.atHome =
      cursPosXY.distanceTo(homePosXY) <
      exp.cfg.homeRadius - exp.cfg.cursorRadius;
    cursor.atTarget =
      cursPosXY.distanceTo(targPosXY) <
      exp.cfg.targetRadius - exp.cfg.cursorRadius;
  
    // Determine if fullscreen and pointerlock are required
    exp.fullscreen.required = exp.pointerlock.required =
      exp.state.between('SETUP', 'ADVANCE') ||
      exp.state.between('FULLSCREEN', 'POINTERLOCK');
  }

  /**
   * Define your procedure as a switch statement implementing a Finite State Machine.
   * Ensure that all states are listed in the array given to `exp.state.init()`
   * @method `exp.state.next(state)` Transitions to new state on next loop.
   * @method `exp.state.once(function)` Runs function one time on entering state.
   */
  function stateFunc() {
    /**
     * If one of these checks fails, divert into an interrupt state.
     * Interrupt states wait for the condition to be satisfied, then return to the previous state.
     * Interrupt states are included at the end of the stateFunc() switch statement.
     */
    if (exp.databaseInterrupt()) {
      exp.blocker.show('database');
      exp.state.push('DATABASE');
      return;
    } else if (exp.fullscreenInterrupt()) {
      exp.blocker.show('fullscreen');
      exp.state.push('FULLSCREEN');
      return;
    } else if (exp.pointerlockInterrupt()) {
      exp.blocker.show('pointerlock');
      exp.state.push('POINTERLOCK');
      return;
    }

    switch (exp.state.current) {
      // CONSENT state can be left alone
      case 'CONSENT':
        exp.state.once(function () {
          if (exp.checkDeviceCompatibility()) {
            exp.state.next('BLOCKED');
          } else {
            exp.consent.show();
          }
        });
        if (exp.waitForConsent()) {
          exp.state.next('SIGNIN');
        }
        break;
      case 'SIGNIN':
        if (exp.waitForAuthentication()) {
          exp.state.next('SETUP');
        }
        break;

      // The following states should be modified as needed for your experiment

      case 'SETUP':
        // Start with a deep copy of the initialized trial from exp.trials
        trial = structuredClone(exp.trials[exp.trialNumber]);
        trial.trialNumber = exp.trialNumber;
        trial.startTime = performance.now();
        // Reset data arrays
        trial.t = [];
        trial.state = [];
        trial.posn = [];
        trial.stateChange = [];
        trial.stateChangeTime = [];
        trial.currentToken = 0;
        // Initialize trial parameters
        trial.demoTrial = exp.trialNumber === 0;
        trial.isTrain = exp.cfg.searchParams.get("DAY")>4
        // target.position.setY(trial.targetDistance * trial.targetDirection);
        exp.state.next('INSTRUCTION');
        scoreText.element.innerText = `Score :  ${Math.round(exp.cfg.score)}% \n Trials Completed : ${exp.trialNumber}`

        break;
      
      
      case 'INSTRUCTION':
        exp.state.once(() => {
          overlayText.element.innerText = "MOVE CURSOR TO HOME and PRESS SPACE TO START";
        });
      break;

      case 'START':
        exp.state.once(() => {
          overlayText.element.innerText = 'Go to the home position.';          
        });

        if(trial.currentToken>0){
          exp.state.next('FINISH')
        }
        
        if (cursor.atHome) {
          overlayText.element.innerText = '';
          exp.state.next('DELAY');
        }
        break;

      case 'DELAY':
        
        if (!cursor.atHome) {
          exp.state.next('START');
        } 
        else if (exp.state.expired(exp.cfg.delayDuration)) {
          exp.state.next(exp.cfg.sequence[trial.currentToken])
        }
        break;
      
      case '.':
        if (!cursor.atHome){
          exp.state.next('START');
        }else if (exp.state.expired(exp.cfg.dotDuration)){
          exp.state.next(exp.cfg.sequence[++trial.currentToken])
        }
      break;

      case '-':
        if (!cursor.atHome){
          exp.state.next('START');
        }else if (exp.state.expired(exp.cfg.dashDuration)){
          exp.state.next(exp.cfg.sequence[++trial.currentToken])
        }
      break;
      
      case 'G':
        if (!cursor.atHome){
          exp.state.next('START');
        }
        else if (exp.state.expired(exp.cfg.gapDuration)){
          exp.state.next(exp.cfg.sequence[++trial.currentToken])
        }
      break;

      case 'C':
        if (!cursor.atHome){
          exp.state.next('START');
        }else if (exp.state.expired(exp.cfg.charDuration)){
          exp.state.next(exp.cfg.sequence[++trial.currentToken])
        }
      break;

      case 'RETURN':
        exp.state.once(() => {
          overlayText.element.innerText = 'Return home.';
          exp.cfg.score = correlationScore();
        });
        handleFrameData();
        if (cursor.atHome) {
          exp.state.next('FINISH');
        }
        break;

      case 'FINISH':
        exp.firebase.saveTrial(trial);
        exp.state.next('ADVANCE');
        break;

      case 'ADVANCE':
        if (!exp.firebase.saveSuccessful) {
          break; // wait until firebase save returns successful
        } else if (exp.firebase.saveFailed) {
          exp.blocker.fatal(exp.firebase.saveFailed);
          exp.state.push('BLOCKED');
        }
        exp.nextTrial();
        if (exp.trialNumber < exp.numTrials) {
          exp.state.next('SETUP');
        } else {
          exp.complete(); // !!! Critical !!! Must call at end of experiment !!!

          // Clean up
          DisplayElement.hide(exp.sceneManager.renderer.domElement);
          DisplayElement.hide(exp.sceneManager.cssRenderer.domElement);
          exp.fullscreen.exitFullscreen();
          exp.state.next('SURVEY');
        }
        break;

      case 'SURVEY':
        exp.state.once(() => exp.survey.show());
        if (exp.cfg.completed && exp.survey?.submitted) {
          exp.survey.hide();
          exp.firebase.saveTrial(exp.cfg);
          exp.state.next('CODE');
        }
        break;

      case 'CODE':
        if (!exp.firebase.saveSuccessful) {
          break;
        }
        exp.state.once(function () {
          exp.goodbye.show(); // show the goodbye screen w/ code & prolific link
        });
        break;

      // The remaining states are interrupt states and can be left alone
      case 'DOWN':
        if (!cursor.atHome) {
          exp.state.next('START');
        }
        //reset 
        exp.state.once(()=>console.log(performance.now()) )
      break;
 
      case 'U':
        exp.state.once(()=>{
          overlayText.element.innerText = `Reproduce the morse code using Right Key `+ (trial.isTrain?` at ${trial.speed}x speed`:'')
          exp.state.once(()=>console.log(performance.now()))
        })
        if (!cursor.atHome) {
          exp.state.next('START');
        }
        if(exp.state.expired(exp.cfg.delayDuration+exp.cfg.responseWaitTime)) {
          exp.state.next('FINISH')
        }
      break;


      case 'FULLSCREEN':
        if (!exp.fullscreenInterrupt()) {
          exp.blocker.hide();
          exp.state.pop();
        }
        break;

      case 'POINTERLOCK':
        if (!exp.pointerlockInterrupt()) {
          exp.blocker.hide();
          exp.state.pop();
        }
        break;

      case 'DATABASE':
        if (!exp.databaseInterrupt()) {
          exp.blocker.hide();
          exp.state.pop();
        }
        break;
    }
  }

  /**
   * Compute and update stimulus and UI presentation.
   */
  function displayFunc() {
    // Set the color of the home position material
    home.material.color = new Color(
      ['.','DOWN','-'].includes(exp.state.current) ? 'hsl(0, 100%, 50%)' : 'hsl(210, 50%, 35%)'
    );

    
    
    // Show or hide the cursor
    cursor.visible = exp.state.between('SETUP', 'ADVANCE');
    // Render
    exp.sceneManager.render();
  }

  /**
   * Event handlers
   */

  // Update the cursor position
  function handleMouseMove(e) {
    if (!cursor.visible) return;
    cursor.position.x += (e.movementX * 2) / window.innerHeight;
    cursor.position.y -= (e.movementY * 2) / window.innerHeight;
    cursor.position.clamp(exp.cfg.cursorMinXYZ, exp.cfg.cursorMaxXYZ);
  }

  function handleKeyDown(e){
    if (exp.state.current=='INSTRUCTION' && e.key==' '){
      exp.state.next('START')
    }

    if (exp.state.current==='U' && e.key=='ArrowRight'){
      exp.state.next('DOWN')
    }
    
  }

  function handleKeyUp(e){
    if (exp.state.current==='DOWN' && e.key=='ArrowRight'){
      exp.state.next('U')
    }

    
  }

  // Record frame data
  function handleFrameData() {
    trial.t.push(performance.now());
    trial.state.push(exp.state.current);
    trial.posn.push(cursor.position.clone()); // clone!
  }

  // Record state transition data
  function handleStateChange() {
    trial?.stateChange?.push(exp.state.current);
    trial?.stateChangeTime?.push(performance.now());
  }

  function getRandomItem(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}
}

window.addEventListener('DOMContentLoaded', main);
