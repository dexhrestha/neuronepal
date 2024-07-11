// Third-party imports
import {
  AlwaysStencilFunc,
  Color,
  Mesh,
  MeshBasicMaterial,
  MeshStandardMaterial,
  PlaneGeometry,
  ReplaceStencilOp,
  SphereGeometry,
  TextureLoader,
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
import { sampleDelay } from './utils.js';
import { step } from 'three/examples/jsm/nodes/Nodes.js';

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

    experimentSourceCode: fileContents,
    searchParams : new URLSearchParams(window.location.search),

  });

  /*
   * Initialize visual stimuli with three.js
   */

  const config = JSON.parse(import.meta.env.VITE_CONFIG);
  console.log(config)

  let score = 0;
  let moveLeft =false;
  let moveRight = false;
  const landmarkHeight = config.landmarkHeight;
  const landmarkWidth = config.landmarkWidth;
  const interlmdistance = config.interLandmarkDistance;
  const landmarks = [];
  const textureLoader = new TextureLoader();
  const imageset = config.imageset;
  const numLandmarks = config.numLandmarks;
  const images = [...Array(numLandmarks).keys()].map(num => `landmarks/images/imageset${imageset}/${num}.jpg`)
  
  const geometry = new PlaneGeometry(landmarkWidth, landmarkHeight);


  images.forEach((image, index) => {
    const texture = textureLoader.load(image); // Replace with the path to your image
    const material = new MeshBasicMaterial({ map:texture });
    const landmark = new Mesh(geometry, material);
    landmark.position.x = index * (landmarkWidth + interlmdistance)
    landmark.position.setY(0.2);
    landmarks.push(landmark);
});

const maskGeometry = new PlaneGeometry(landmarkWidth*5,landmarkHeight);
const maskMaterial = new MeshBasicMaterial({ color: 0x242424, depthWrite: false, stencilWrite: true, stencilFunc: AlwaysStencilFunc, stencilRef: 1, stencilMask: 0xff, stencilFail: ReplaceStencilOp, stencilZFail: ReplaceStencilOp, stencilZPass: ReplaceStencilOp });
const mask = new Mesh(maskGeometry, maskMaterial);
mask.position.setY(0.2);
mask.position.setX(-1.5);
mask.position.z = 0.1;


// exp.sceneManager.camera.z = 10;
const maskGeometry2 = new PlaneGeometry(landmarkWidth*5,landmarkHeight);
const maskMaterial2 = new MeshBasicMaterial({ color:  0x242424, depthWrite: false, stencilWrite: true, stencilFunc: AlwaysStencilFunc, stencilRef: 1, stencilMask: 0xff, stencilFail: ReplaceStencilOp, stencilZFail: ReplaceStencilOp, stencilZPass: ReplaceStencilOp });
const mask2 = new Mesh(maskGeometry2 , maskMaterial2);
mask2.position.setX(1.5);
mask2.position.setY(0.2);
mask2.position.z = 0.1;

const maskGeometry3 = new PlaneGeometry(landmarkWidth*3,landmarkHeight);
const maskMaterial3 = new MeshBasicMaterial({ color: 0x242424, depthWrite: false, stencilWrite: true, stencilFunc: AlwaysStencilFunc, stencilRef: 1, stencilMask: 0xff, stencilFail: ReplaceStencilOp, stencilZFail: ReplaceStencilOp, stencilZPass: ReplaceStencilOp });
const mask3 = new Mesh(maskGeometry3 , maskMaterial3);
mask3.position.setX(0);
mask3.position.setY(0.2);
mask3.position.z = 0.1;
exp.sceneManager.scene.add(mask,mask2,mask3)


  const target  = new Mesh(
    geometry,
    new MeshStandardMaterial() // we will set color in displayFunc()
  );

  const cursor = new Mesh(
    new SphereGeometry(exp.cfg.cursorRadius),
    new MeshStandardMaterial({ color: 'red' })
  );
  cursor.position.setZ(exp.cfg.homeRadius + exp.cfg.cursorRadius);

  const home = new Mesh(
    new SphereGeometry(exp.cfg.cursorRadius*2),
    new MeshStandardMaterial({ color: 'white' })

  )
  home.position.setY(-0.1);
  cursor.position.setY(-0.1);

  exp.sceneManager.scene.add(home,cursor)

  /*
   * You can display overlay text on the scene by adding CSS2D to cssScene
   */
  const overlayText = new CSS2D();
  overlayText.object.position.set(0, 0.67, 0);
  exp.sceneManager.cssScene.add(overlayText.object);

  // Display a score
  const scoreText = new CSS2D();
  scoreText.object.position.set(0.7,0.5,0);
  scoreText.element.innerText = ' Score: ';  
  /*
   * Create trial sequence from array of block objects.
   */
  const stepSizes = config.stepSizes;
    console.log(stepSizes[0])

  exp.createTrialSequence([
    new Block({
      variables: {
        startId : Array.from({ length: numLandmarks*(numLandmarks-1) * 3 }, (_, i) => Math.floor(i / (numLandmarks-1))%numLandmarks),
        // startId : Array.from({ length:  5 }, (_, i) => 0),
        targetId :  Array.from({ length: numLandmarks*3  }, (_, i) => [...Array(numLandmarks).keys()].filter(num => num !== i % numLandmarks)).flat(),
        // targetId :  Array.from({ length:5}, (_, i) => 8),
        stepSize :[
          ...Array(numLandmarks*(numLandmarks-1)).fill(stepSizes[0]),
          ...Array(numLandmarks*(numLandmarks-1)).fill(stepSizes[1]),
          ...Array(numLandmarks*(numLandmarks-1)).fill(stepSizes[2])
        ]
        // stepSize : Array.from({ length:5}, (_, i) => stepSize),
      },
      options: {
        name: exp.cfg.searchParams.get('DAY'),
        reps: 1,
        shuffle: true,
      },
    }),
  ]);

  /*
   * You must initialize an empty object called trial
   */
  let trial = {};

  /**
   * An instructions panel overlaid in the top-right of the screen.
   * Keep these instructions short. Use CSS2D to overlay instructions on the scene.
   */
  exp.instructions = new InstructionsPanel({
    content: `Use the mouse/trackpad to hit the targets.\nTry to hit as many targets as possible!`,
  });

  /**
   * Ask questions at the end of the experiment with the Survey class.
   * You probably don't need to ask for funding agency required demographic information.
   * On Prolific, most participants have already provided this information.
   * On Mechanical Turk, Ouvrai collects this information separately on the HIT posting.
   */
  exp.survey = new Survey();
  exp.survey.addQuestion({
    type: 'list',
    name: 'device',
    message:
      'Did you use a keyboard or something else for this experiment?',
    choices: ['Keyboard', 'Other'],
    options: { required: true },
  });
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
      'START',
      'DELAY',
      'INITIAL',
      'GO',
      'MOVING',
      'STOP',
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
    let targPosXY = new Vector2().copy(trial.targetId===undefined?cursor.position:landmarks[trial.targetId].position);

    if (exp.state.current == 'STOP'){ 
      target.distance = Math.abs(targPosXY.x - homePosXY.x); 
    target.reached =  target.distance <= config.tolerance * landmarkWidth;
  }

    cursor.atHome =
      cursPosXY.distanceTo(homePosXY) <
      exp.cfg.homeRadius - exp.cfg.cursorRadius;

    if (!cursor.atHome){
      overlayText.element.innerText = 'Go to the home position.';
      exp.state.next('SETUP')
    }

    
    // cursor.atTarget =
    //   cursPosXY.distanceTo(targPosXY) <
    //   exp.cfg.targetRadius - exp.cfg.cursorRadius;

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

      // SIGNIN state can be left alone
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
        trial.attempt = 1;
        // Initialize trial parameters
        trial.demoTrial = exp.trialNumber === 0;
        // target.position.setY(trial.targetDistance * trial.targetDirection);
        trial.isTrain = exp.cfg.searchParams.get('DAY')<5;

        landmarks.forEach((landmark,index)=>{
          landmark.position.x = (index-trial.startId) * (landmarkWidth + interlmdistance)
          console.log(landmark.position.x,trial.startId)
          exp.sceneManager.scene.add(landmark)
        });
        
        console.log("StartID",trial.startId)
        target.material.map = textureLoader.load(images[trial.targetId]);
        target.position.setY(-landmarkHeight);
        exp.sceneManager.scene.add(target)
        target.visible = false;
        mask3.visible = true;
        if (cursor.atHome) {
          exp.state.next('START');
        }
        break;

      case 'START':
        exp.state.once(() => {
          overlayText.element.innerText = 'Go to the home position.';
        });
        if (cursor.atHome) {
          overlayText.element.innerText = '';
          exp.state.next('INITIAL');
        }
        break;
      
        case 'INITIAL':
          exp.state.once(()=>{
            target.visible = false;
            mask3.visible = false;
            mask2.position.setX(-1.3);
            mask.position.setX(1.3);
          })
          if (!cursor.atHome) {
            exp.state.next('START');
          } else if (exp.state.expired(sampleDelay(0.5,1.5))) {
              exp.state.next('DELAY');
          }
          break;

      case 'DELAY':
        if (!cursor.atHome) {
          exp.state.next('START');
        } else if (exp.state.expired(sampleDelay(0.5,1.5))) {
          if (mask3.visible){
            exp.state.next('INITIAL');
          }else{
            exp.state.next('GO');
          }
        }
        break;

      case 'GO':
        exp.state.once(() => {
          overlayText.element.innerText = `Move left or right to match the target below using left or right key.`;
          // overlayText.element.innerText = `SESSION TYPE: ${exp.cfg.searchParams.get('DAY')} `
          target.visible = true;
          
        });

        handleFrameData();
        if (cursor.atHome) {
          if (moveLeft||moveRight) {
            exp.state.next('MOVING');
          }
        }
        break;

      case 'MOVING':
        exp.state.once(()=>{
          mask2.position.setX(-1.5);
          mask.position.setX(1.5);
          // console.log("moving",landmarks[trial.startId].position.x)
          if (!trial.isTrain){
            landmarks.filter((landmark)=>(landmark.position.x>0.7)||(landmark.position.x<-0.7)).forEach((landmark)=>{landmark.visible=false})
          }
        })
        handleFrameData();

        
        if (cursor.atHome) {
          // target.visible = false;
          if (!(moveLeft||moveRight)) {
            // target.visible = false;
            exp.state.next('STOP');
          }
          if (!trial.isTrain){
            if(((landmarks[trial.startId].position.x>0.7)||((landmarks[trial.startId].position.x<-0.7)))){
              landmarks[trial.startId].visible=false;
            }
          }
        }
        break;

      case 'STOP':
        exp.state.once(() => {
          // overlayText.element.innerText = 'Stopped checking target ';
          if (!trial.isTrain){
            landmarks.filter(l=>(l.position.x>-0.7)||(l.position.x<0.7)).forEach(l=>{l.visible=true})
          }
          // console.log(landmarks[trial.targetId].position.x)
        });
        handleFrameData();
        if (cursor.atHome) {
          if (moveLeft||moveRight) {
            trial.attempt +=1;
            console.log("Attempt no:",trial.attempt);
            exp.state.next('MOVING');
          }
        }
        if (target.reached) {
          if (trial.attempt === 1){
            exp.cfg.score +=1;
          }
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
        // Change the code to caluclate score and display
        // Wrtie score calculating algorithm
        console.log("SCORE",Math.round(exp.cfg.score/(exp.trialNumber+1)*100,2))
        scoreText.element.innerText = `Score :  ${Math.round(exp.cfg.score/(exp.trialNumber+1)*100,2)}% \n Trials Completed : ${exp.trialNumber+1}`
        exp.sceneManager.cssScene.add(scoreText.object)
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
      cursor.atHome ? 'hsl(210, 100%, 60%)' : 'hsl(210, 50%, 35%)'
    );

    cursor.material.color = new Color(
      exp.state.between('GO','ADVANCE') ? 'hsl(0, 0%, 100%)' : 'hsl(0, 100%, 50%)'
    )
    
    // Show or hide the cursor
    cursor.visible = exp.state.between('SETUP', 'ADVANCE');
    // Render
    exp.sceneManager.render();
        if (landmarks[0].position.x > parseFloat(landmarkWidth*1.3).toFixed(2)){
      moveRight = false;
    }
    if (landmarks[landmarks.length-1].position.x < parseFloat(-landmarkWidth*1.3).toFixed(2)){
      moveLeft = false;
    }

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

  function handleKeyUp(e){
    if (e.key=='ArrowRight'){moveRight = false;}
    if (e.key=='ArrowLeft'){moveLeft = false;}
  }

  function handleKeyDown(e){
    if (exp.state.between("GO","FINISH")){
      if (e.key=='ArrowRight'){moveRight = true;}
      if (e.key=='ArrowLeft'){moveLeft = true;}
    }
  }
  
  function animate(){
    requestAnimationFrame(animate);
    landmarks.forEach(landmark => {
      if (cursor.atHome){
      if (moveLeft) {
        landmark.position.x -= trial.stepSize;
      }
      if (moveRight) {
        landmark.position.x += trial.stepSize;
      }}
  });
}

  animate();
  
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
}

window.addEventListener('DOMContentLoaded', main);
