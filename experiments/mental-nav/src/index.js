// Third-party imports
import {
  AlwaysStencilFunc,
  CircleGeometry,
  Clock,
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
import { sampleDelay,randomUniform } from './utils.js';
import { degToRad, radToDeg } from 'three/src/math/MathUtils.js';
/*
 * Main function contains all experiment logic. At a minimum you should:
 * 1. Create a `new Experiment({...config})`
 * 2. Initialize the state machine with `exp.state.init(states, changeFunc)`
 * 3. Create stimuli and add them with `exp.sceneManager.scene.add(...objects)`
 * 4. Create trial sequence with `exp.createTrialSequence([...blocks])`
 * 5. Start the main loop with `exp.start(calcFunc, stateFunc, displayFunc)`
 * 6. Design your experiment by editing `calcFunc`, `stateFunc`, and `displayFunc`
 */


function worldToPixel(worldPosition, camera, screenWidth, screenHeight) {
  // Convert world position to NDC
  const ndc = worldToNDC(worldPosition, camera);
  
  // Convert NDC to screen coordinates
  return ndcToScreen(ndc, screenWidth, screenHeight);
}

function worldToNDC(worldPosition, camera) {
  const vector = new Vector3();
  vector.copy(worldPosition).project(camera);
  return vector;
}

function pixelToNDCSize(pixelSize) {
  // Convert pixelX to NDC x
  return (pixelSize / window.innerHeight) * 2;
  
}

function ndcToScreen(ndc, screenWidth, screenHeight) {

  const x = (ndc.x + 1) / 2 * screenWidth;
  const y = (-ndc.y + 1) / 2 * screenHeight; // Y is inverted
  return { x, y };
}

function vaToPixels(angleDegrees, distance, screenHeightcm) {
  // Convert angle from degrees to radians
  
  const dpp =  radToDeg(Math.atan2(0.5 * screenHeightcm, distance)) / (0.5 * window.innerHeight); //degree per pixel
  const pixelSize = angleDegrees / dpp;

  return pixelSize;
}

function vaToNdC(angleDegrees,distance,screenHeightcm){
  // const dpp =  radToDeg(Math.atan2(0.5 * screenHeightcm, distance)) / (0.5 * screenSize); //degree per pixel
  const pixelSize = vaToPixels(angleDegrees,distance,screenHeightcm);
  // console.log("pxel size",pixelSize);
  const ndc = pixelToNDCSize(pixelSize);
  // console.log("ndc",ndc);
  return ndc;
}

function ndcToVA(ndc,distance,screenHeightcm){
  const dpp =  radToDeg(Math.atan2(0.5 * screenHeightcm, distance)) / (0.5 * window.innerHeight); //degree per pixel
  
  const pixels = ((ndc+1)/2)* window.innerHeight;
  
  const va = pixels * dpp;
  
  return pixels;
}

async function main() {
  /*
   * The first step is always to create a new Experiment({...config}) with your configuration options.
   * Ouvrai configuration options are documented in the Experiment class.
   * You can also provide other experiment-level variables here as additional fields.
   * All values in the configuration object will be saved in your data.
   * You can add variables throughout the experiment using `exp.cfg.VARNAME = VALUE`.

*/

// Example usage
  
  const exp = new Experiment({
    // Options to make development easier
    devOptions: {
      skipConsent: true,
      saveTrialList: false,
      allowExitFullscreen: false, // set to flase
      allowExitPointerlock: false, //set to false
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
    acc:0,

    // Procedure
    delayDuration: sampleDelay(0.5,1.5),

    experimentSourceCode: fileContents,
    searchParams : new URLSearchParams(window.location.search),

  });

  const screenWidth = window.innerWidth;
  const screenHeight = window.innerHeight;    
  /*
   * Initialize visual stimuli with three.js
   */
  const config = JSON.parse(import.meta.env.VITE_CONFIG);
  //Display a cricle with random dots

  const segments = 64; // more segments = more smooth


  const patchgeometry = new CircleGeometry(config.patchRadius, segments);
  const patchmaterial = new MeshBasicMaterial({color:0x000000});

  const patch = new Mesh(patchgeometry,patchmaterial)
  patch.position.setX(0,0,0);
  exp.sceneManager.scene.add(patch)

  const dots = [];

for (let i = 0; i < config.ndots; i++) {
  // Generate a random radius between config.dotRadius / 2 and config.dotRadius
  const randomRadius = (Math.random() * (config.dotRadius / 2)) + (config.dotRadius / 2);

  // Create the geometry with the random radius
  const dotGeometry = new CircleGeometry(randomRadius, segments);
  const dotMaterial = new MeshBasicMaterial({ color: 0xc0c0c0 });

  // Create the dot mesh
  const dot = new Mesh(dotGeometry, dotMaterial);
  
  // Set a random position for the dot
  setRandomPosition(dot);

  // Assign a random life value to the dot
  dot.life = Math.random() * config.dotLife; // in distance

  // Add the dot to the scene and store it in the dots array
  exp.sceneManager.scene.add(dot);
  dots.push(dot);
}

  const objectDistance = config.objectDistance; //cm
  const screenHeightcm = config.screenHeightcm; //screenHeightcm

  let moveLeft = {lm:false,dot:false};

  let moveRight = {lm:false,dot:false};
  let isKeyDown = false;

  const landmarkHeight = Math.abs(vaToNdC(config.landmarkHeight,objectDistance,screenHeightcm));
  const landmarkWidth = Math.abs(vaToNdC(config.landmarkWidth,objectDistance,screenHeightcm));

  console.log("NDC H,w",landmarkHeight,landmarkWidth)

  const interlmdistance = Math.abs(vaToNdC(config.interLandmarkDistance,objectDistance,screenHeightcm));
  const landmarks = [];
  const textureLoader = new TextureLoader();
  const imageset = config.imageset;
  const numLandmarks = config.numLandmarks;
  const images = [...Array(numLandmarks).keys()].map(num => `landmarks/images/imageset${imageset}/${num}.jpg`)
  
  const geometry = new PlaneGeometry(landmarkWidth, landmarkHeight);

  let clock = new Clock();

  images.forEach((image, index) => {
    const texture = textureLoader.load(image); // Replace with the path to your image
    const material = new MeshBasicMaterial({ map:texture });
    const lm = new Mesh(geometry, material);
    lm.position.setX(parseInt(index * (landmarkWidth + interlmdistance)));
    lm.position.setY(config.landmarkY);

    // Create a central fixation dot
    const dotGeometry = new SphereGeometry(0.01, 32, 32); // Adjust the radius as needed
    const dotMaterial = new MeshBasicMaterial({ color: 0xff0000 }); // Red dot
    const fixationDot = new Mesh(dotGeometry, dotMaterial);

    // Position the fixation dot at the center of the landmark
    fixationDot.position.set(0, 0, 0); // Assuming the landmark's center is (0, 0, 0)

    // Add the fixation dot to the landmark
    lm.add(fixationDot);

    landmarks.push(lm);
});

const maskGeometry = new PlaneGeometry(landmarkWidth*5,landmarkHeight);
const maskMaterial = new MeshBasicMaterial({ color: 0x242424, depthWrite: false, stencilWrite: true, stencilFunc: AlwaysStencilFunc, stencilRef: 1, stencilMask: 0xff, stencilFail: ReplaceStencilOp, stencilZFail: ReplaceStencilOp, stencilZPass: ReplaceStencilOp });
const mask = new Mesh(maskGeometry, maskMaterial);


const maskGeometry2 = new PlaneGeometry(landmarkWidth*5,landmarkHeight);
const maskMaterial2 = new MeshBasicMaterial({ color:  0x242424, depthWrite: false, stencilWrite: true, stencilFunc: AlwaysStencilFunc, stencilRef: 1, stencilMask: 0xff, stencilFail: ReplaceStencilOp, stencilZFail: ReplaceStencilOp, stencilZPass: ReplaceStencilOp });
const mask2 = new Mesh(maskGeometry2 , maskMaterial2);


const maskGeometry3 = new PlaneGeometry(landmarkWidth*3,landmarkHeight);
const maskMaterial3 = new MeshBasicMaterial({ color: 0x242424, depthWrite: false, stencilWrite: true, stencilFunc: AlwaysStencilFunc, stencilRef: 1, stencilMask: 0xff, stencilFail: ReplaceStencilOp, stencilZFail: ReplaceStencilOp, stencilZPass: ReplaceStencilOp });
const mask3 = new Mesh(maskGeometry3 , maskMaterial3);
// exp.sceneManager.scene.add(mask,mask2,mask3)

landmarks.forEach((landmark)=>{
  landmark.visible = false;
  exp.sceneManager.scene.add(landmark);
});

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

  home.position.set(0,0,0);
  cursor.position.setY(0,0,0);

  exp.sceneManager.scene.add(home,cursor)

  /*
   * You can display overlay text on the scene by adding CSS2D to cssScene
   */
  const overlayText = new CSS2D({color:0xffffff});
  overlayText.object.position.set(0, 0.7);
  overlayText.element.innerText = '';
  overlayText.element.style.color = 'white';

  exp.sceneManager.cssScene.add(overlayText.object);

function setRandomPosition(dot){
  const angle = Math.random() * 2 * Math.PI;
  const r = config.patchRadius * Math.sqrt(Math.random());  // Uniform distribution within the circle
  const x = r * Math.cos(angle);
  const y = r * Math.sin(angle);
  dot.position.set(x,y,0)
}

  // Display a score
  const scoreText = new CSS2D();
  scoreText.object.position.set(0.9,0.7,0.01);
  scoreText.element.innerText = ' Score: ';  
  scoreText.element.style.color = 'white';

  /*
   * Create trial sequence from array of block objects.
   */
  const frameRate = 60;
  const initStep = (config.interLandmarkDistance/0.5)/frameRate;
  const stepSizes = config.stepSizes;
  if (exp.cfg.searchParams.get("COHORT")==1){ // use single speed for training(initialTrials) and multiple for testing
    
    exp.createTrialSequence([
      new Block({
        variables: {
          startId : Array.from({ length: numLandmarks*(numLandmarks-1) * stepSizes.length }, (_, i) => Math.floor(i / (numLandmarks-1))%numLandmarks),
          // startId : Array.from({ length:  5 }, (_, i) => 0),
          targetId :  Array.from({ length: numLandmarks*  stepSizes.length }, (_, i) => [...Array(numLandmarks).keys()].filter(num => num !== i % numLandmarks)).flat(),
          // targetId :  Array.from({ length:5}, (_, i) => 8),

        },
        options: {
          name: `COHORT : ${exp.cfg.searchParams.get('COHORT')}, DAY: ${exp.cfg.searchParams.get('DAY')}, SPEEDS: 3`,
          reps: 1,
          shuffle: true,
        },
      }),
      new Block({
        variables: {
          startId : Array.from({ length: numLandmarks*(numLandmarks-1) * stepSizes.length }, (_, i) => Math.floor(i / (numLandmarks-1))%numLandmarks),
          // startId : Array.from({ length:  5 }, (_, i) => 0),
          targetId :  Array.from({ length: numLandmarks*  stepSizes.length }, (_, i) => [...Array(numLandmarks).keys()].filter(num => num !== i % numLandmarks)).flat(),
          // targetId :  Array.from({ length:5}, (_, i) => 8),

        },
        options: {
          name: `COHORT : ${exp.cfg.searchParams.get('COHORT')}, DAY: ${exp.cfg.searchParams.get('DAY')}, SPEEDS: 3`,
          reps: 1,
          shuffle: true,
        },
      }),
      new Block({
        variables: {
          startId : Array.from({ length: numLandmarks*(numLandmarks-1) * stepSizes.length }, (_, i) => Math.floor(i / (numLandmarks-1))%numLandmarks),
          // startId : Array.from({ length:  5 }, (_, i) => 0),
          targetId :  Array.from({ length: numLandmarks*  stepSizes.length }, (_, i) => [...Array(numLandmarks).keys()].filter(num => num !== i % numLandmarks)).flat(),
          // targetId :  Array.from({ length:5}, (_, i) => 8),

        },
        options: {
          name: `COHORT : ${exp.cfg.searchParams.get('COHORT')}, DAY: ${exp.cfg.searchParams.get('DAY')}, SPEEDS: 3`,
          reps: 1,
          shuffle: true,
        },
      }),
      new Block({
        variables: {
          startId : Array.from({ length: numLandmarks*(numLandmarks-1) * stepSizes.length }, (_, i) => Math.floor(i / (numLandmarks-1))%numLandmarks),
          // startId : Array.from({ length:  5 }, (_, i) => 0),
          targetId :  Array.from({ length: numLandmarks*  stepSizes.length }, (_, i) => [...Array(numLandmarks).keys()].filter(num => num !== i % numLandmarks)).flat(),
          // targetId :  Array.from({ length:5}, (_, i) => 8),

        },
        options: {
          name: `COHORT : ${exp.cfg.searchParams.get('COHORT')}, DAY: ${exp.cfg.searchParams.get('DAY')}, SPEEDS: 3`,
          reps: 1,
          shuffle: true,
        },
      }),
    ]);
  }else{ // use multiple speed for both training(initialtrials) and testing
  exp.createTrialSequence([ //training block with 1x and 0.5 x speed 
    new Block({
      variables: {
        startId : Array.from({ length: numLandmarks*(numLandmarks-1) * 1 }, (_, i) => Math.floor(i / (numLandmarks-1))%numLandmarks),
        // startId : Array.from({ length:  5 }, (_, i) => 0),
        targetId :  Array.from({ length: numLandmarks * 1  }, (_, i) => [...Array(numLandmarks).keys()].filter(num => num !== i % numLandmarks)).flat(),
        // targetId :  Array.from({ length:5}, (_, i) => 8),
        train : true,
        // stepSize : Array.from({ length:5}, (_, i) => stepSize),
      },
      options: {
        name: `COHORT : ${exp.cfg.searchParams.get('COHORT')}, DAY: ${exp.cfg.searchParams.get('DAY')}, SPEEDS: 1`,
        reps: 1,
        shuffle: true,
      },
    }),
    new Block({ //testing block with 1x and 0.5 x speed 
      variables: {
        startId : Array.from({ length: numLandmarks*(numLandmarks-1) *  (stepSizes.length -1) }, (_, i) => Math.floor(i / (numLandmarks-1))%numLandmarks),
        // startId : Array.from({ length:  5 }, (_, i) => 0),
        targetId :  Array.from({ length: numLandmarks* (stepSizes.length -1)  }, (_, i) => [...Array(numLandmarks).keys()].filter(num => num !== i % numLandmarks)).flat(),
        // targetId :  Array.from({ length:5}, (_, i) => 8),
        train:false,
        // stepSize : Array.from({ length:5}, (_, i) => stepSize),
      },
      options: {
        name: `COHORT : ${exp.cfg.searchParams.get('COHORT')}, DAY: ${exp.cfg.searchParams.get('DAY')} , SPEEDS: 2`,
        reps: 1,
        shuffle: true,
      },
    }),
    new Block({ //testing block with 1x and 0.5 x speed 
      variables: {
        startId : Array.from({ length: numLandmarks*(numLandmarks-1) *  (stepSizes.length -1) }, (_, i) => Math.floor(i / (numLandmarks-1))%numLandmarks),
        // startId : Array.from({ length:  5 }, (_, i) => 0),
        targetId :  Array.from({ length: numLandmarks* (stepSizes.length -1)  }, (_, i) => [...Array(numLandmarks).keys()].filter(num => num !== i % numLandmarks)).flat(),
        // targetId :  Array.from({ length:5}, (_, i) => 8),
        train:false,
        // stepSize : Array.from({ length:5}, (_, i) => stepSize),
      },
      options: {
        name: `COHORT : ${exp.cfg.searchParams.get('COHORT')}, DAY: ${exp.cfg.searchParams.get('DAY')} , SPEEDS: 2`,
        reps: 1,
        shuffle: true,
      },
    }),
    new Block({ //testing block with 1x and 0.5 x speed 
      variables: {
        startId : Array.from({ length: numLandmarks*(numLandmarks-1) *  (stepSizes.length -1) }, (_, i) => Math.floor(i / (numLandmarks-1))%numLandmarks),
        // startId : Array.from({ length:  5 }, (_, i) => 0),
        targetId :  Array.from({ length: numLandmarks* (stepSizes.length -1)  }, (_, i) => [...Array(numLandmarks).keys()].filter(num => num !== i % numLandmarks)).flat(),
        // targetId :  Array.from({ length:5}, (_, i) => 8),
        train:false,
        // stepSize : Array.from({ length:5}, (_, i) => stepSize),
      },
      options: {
        name: `COHORT : ${exp.cfg.searchParams.get('COHORT')}, DAY: ${exp.cfg.searchParams.get('DAY')} , SPEEDS: 2`,
        reps: 1,
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
      'TARGET',
      'GO',
      'VISUAL',
      'MENTAL',
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
    // Objects are in 3D space so we copy to Vector2 to ignore the depth dimensionh
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
        if (exp.cfg.searchParams.get("DAY")<3 & exp.cfg.searchParams.get("COHORT") == 1) {
        // Handle Cohort 2 logic here
          if (exp.trialNumber < config.initialTrials) {
              // Initial trials: use the same speed for all intial visual trials
              exp.trials[exp.trialNumber].speed = 0; // Assuming the speed for initial trials is 1, adjust as needed
          } else {
              if (exp.trialNumber % config.blockSpeed === 0) {
                let previousSpeed = exp.trials[trial.trialNumber - 1]?exp.trials[exp.trialNumber - 1].speed:Math.random() * 3;
                let availableSpeeds = [0, 1].filter(speed => speed !== previousSpeed);
                exp.trials[exp.trialNumber].speed = availableSpeeds[Math.floor(Math.random() * availableSpeeds.length)];
            }else{
              exp.trials[exp.trialNumber].speed = exp.trials[exp.trialNumber-1].speed
            }
        }
      } else{
          if (exp.cfg.searchParams.get("DAY")<5){
          if (exp.trialNumber % config.blockSpeed === 0) {
            let previousSpeed = exp.trials[trial.trialNumber - 1]?exp.trials[exp.trialNumber - 1].speed:Math.random() * 3;
            let availableSpeeds = [0, 1].filter(speed => speed !== previousSpeed);
            exp.trials[exp.trialNumber].speed = availableSpeeds[Math.floor(Math.random() * availableSpeeds.length)];
        }else{
          exp.trials[exp.trialNumber].speed = exp.trials[exp.trialNumber-1].speed
        }
      }
      }
        
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
        trial.stepSize = config.stepSizes[trial.speed]
        // target.position.setY(trial.targetDistance * trial.targetDirection);
        // trial.startId = 5;
        // trial.targetId = 3;
        trial.isTrain = true;
        exp.cfg.acc = exp.cfg.score/(exp.trialNumber+1)
        if(exp.cfg.searchParams.get('DAY')<= config.accThresholds.length){ // for training days indicated  by number of thresholds
          if (exp.trialNumber < config.initialTrials)
            {
              trial.isTrain = true;
             }
          else{
            trial.isTrain = false;
          }
          // else{
          //   if(exp.cfg.acc >= config.accThresholds[exp.cfg.searchParams.get('DAY')-1]){
          //     trial.isTrain = false;
          //   }else{
          //     trial.isTrain = true;
          //   }
          // }
        }
        else{
          trial.isTrain = false; // for other days use mental nav
        }

        target.material.map = textureLoader.load(images[trial.targetId]);
        target.position.setY(config.targetY);
        exp.sceneManager.scene.add(target)
        target.visible = false;
        mask3.visible = true;
        if (cursor.atHome) {
          exp.state.next('START');
        }
// Set the speed for the trial (it will be the same for the next 15 trials)

        break;

      case 'START':
        exp.state.once(() => {

          if(exp.cfg.searchParams.get('DAY')>=5){
            // trial.stepSize = 0.05// draw from cont dist ();
            if (exp.trialNumber % config.blockSpeed === 0) {
              trial.stepSize =  randomUniform(10,40);
              exp.trials[exp.trialNumber].stepSize = trial.stepSize;
              }else{
                exp.trials[exp.trialNumber].stepSize = exp.trials[exp.trialNumber-1].stepSize;
                trial.stepSize =  exp.trials[exp.trialNumber-1].stepSize;
              }
  
          }
          console.log("Speed:",trial.stepSize);
          
  
          trial.trueTime = Math.abs(landmarks[trial.targetId].position.x-landmarks[trial.startId].position.x)/vaToNdC(trial.stepSize,objectDistance,screenHeightcm)*1000;
          overlayText.element.innerText = 'Go to the home position. \n Press s Key to End the experiment';
          
        landmarks.forEach((lm,index)=>{
          lm.position.setX((index - trial.startId) * (landmarkWidth + interlmdistance));
          if(trial.isTrain){
            lm.visible = trial.isTrain;
          }else{
            lm.visible = lm.position.x == 0;
          }
        })

          mask3.visible = true;

        });
        if (!cursor.atHome) {
          overlayText.element.innerText = 'Go to the home position. \n Press s Key to End the experiment';
          exp.state.next('SETUP')
        }
        else{
          overlayText.element.innerText = '';
          exp.state.next('INITIAL');
        }
        break;
      
        case 'INITIAL':
          exp.state.once(()=>{
            target.visible = false;
            mask3.visible = true;
            mask2.position.setX(-1.3);
            mask.position.setX(1.3);
          })

          if (!cursor.atHome) {
            overlayText.element.innerText = 'Go to the home position. \n Press s Key to End the experiment';
            exp.state.next('START')
          } else if (exp.state.expired(sampleDelay(0.5,1.5))) {
              exp.state.next('DELAY');
          }
          break;

      case 'DELAY': // BLANK WHEN DELAY 0.5x 0.75x 1x
        if (!cursor.atHome) {
          overlayText.element.innerText = 'Go to the home position. \n Press s Key to End the experiment';
          exp.state.next('START');
        } else if (exp.state.expired(sampleDelay(0.5,1.5))) {
            if (mask3.visible){
              exp.state.next('TARGET');  
            }else{
              exp.state.next('GO');
            }
        }
        break;

      case 'TARGET':
        exp.state.once(()=>{
          mask3.visible = false;
        })
        exp.state.next('DELAY')
      break;

      case 'GO':
        exp.state.once(() => {
          overlayText.element.innerText = `Move left or right to match the target below using left or right key. \n Press s Key to End the experiment. `;
          //  \n STEP: ${trial.stepSize} TN: ${trial.trialNumber} Attempt:${trial.attempt}`;
          // overlayText.element.innerText = `SESSION TYPE: ${exp.cfg.searchParams.get('DAY')} `
          target.visible = true;
          console.log(trial.isTrain);
        });

        mask.visible = false;
        mask2.visible = false;
        
        handleFrameData();
        if (!cursor.atHome) {
          overlayText.element.innerText = 'Go to the home position. \n Press s Key to End the experiment';
          exp.state.next('START')}
        else {
          if (moveLeft.lm||moveRight.lm) {
            exp.state.next('MOVING');
          }
        }
        break;

      case 'MOVING':
        exp.state.once(()=>{
          trial.keyDown = performance.now();
          mask2.position.setX(-1.5);
          mask.position.setX(1.5);
          overlayText.element.innerText = '';
          if (!trial.isTrain){
            // landmarks.filter((landmark)=>(landmark.position.x>0.7)||(landmark.position.x<-0.7)).forEach((landmark)=>{landmark.visible=false})
            landmarks.forEach(lm=>lm.visible=false)
          }
        })
        handleFrameData();

        target.visible= trial.isTrain;
        if (!cursor.atHome) {
          overlayText.element.innerText = 'Go to the home position.';
          exp.state.next('START')}
        else {
          // target.visible = false;
          if (!(moveLeft.lm||moveRight.lm)  && !isKeyDown) {
            // target.visible = false;
            exp.state.next('STOP');
          }

        landmarks.forEach(lm=>lm.visible=trial.isTrain)
        }
        break;

      case 'STOP':
        exp.state.once(() => {              
          trial.producedTime = performance.now() - trial.keyDown;
          console.log('produced Time',trial.producedTime);
          console.log('true Time',trial.trueTime);
          
          if (!trial.isTrain){
            landmarks.filter(l=>(l.position.x>-0.7)||(l.position.x<0.7)).forEach(l=>{l.visible=true})
          }
        target.visible= true;
        if (target.reached) {
          if (trial.attempt === 1){
            exp.cfg.score += 1;
          }
          if (exp.state.expired(sampleDelay(0.5,1.5))){
            exp.state.next('FINISH')
          } 
        }
        if (trial.isTrain){
          landmarks.forEach(l=>{l.visible=true})}
        else{
          landmarks.filter(l=>(l.position.x>=-2)&(l.position.x<=2)).forEach(l=>{l.visible=true})
        }
        overlayText.element.innerText = `Move left or right to match the target below using left or right key. \n Press s Key to End the experiment.`;
        // \n STEP: ${trial.stepSize} TN: ${trial.trialNumber} Attempt:${trial.attempt}`; 
        trial.currentTargetPos = landmarks[trial.targetId].position.x;
        
        

        });

        handleFrameData();
        if (!cursor.atHome) {
            overlayText.element.innerText = 'Go to the home position.';
            exp.state.next('START')}
          else  {
            if (target.reached) {
              if (trial.attempt == 1){
                exp.state.once(() => exp.cfg.score += 1);
              }
              
              if (exp.state.expired(sampleDelay(0.5,1.5))){
                exp.state.next('FINISH')
              } 
            }
            else{
              // if (exp.cfg.searchParams.get('DAY')<3){ // for trainingg days
                if (trial.attempt>1){  // show the  target and current  positiion
                  target.visible = true;
                  if(exp.state.expired(sampleDelay(0.5,1.5))){                  
                    cursor.material.color = new Color( 'hsl(0, 100%, 50%)')// change color to red and restart 
                    exp.state.next('FINISH')
                  }
                }
              // }else{
                // if (exp.state.expired(sampleDelay(0.5,1.5))){ //other days  go to finish
                //     exp.state.next('FINISH')
                //   }
              // }
            }
          if (moveLeft.lm||moveRight.lm) {
            trial.attempt +=1;
            exp.state.next('MOVING');
          }
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
        scoreText.element.innerText = `Score :  ${Math.round((exp.cfg.score/(exp.trialNumber+1))*100,2)}% \n Trials Completed : ${exp.trialNumber+1}`
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
      cursor.atHome ? 'hsl(116, 0%, 50%)' : 'hsl(0, 0%, 100%)'
    );

    cursor.material.color = new Color(
      exp.state.between('GO','ADVANCE') ? 'hsl(116, 100%, 50%)' : 'hsl(0, 100%, 50%)'
    )
    
    // Show or hide the cursor
    cursor.visible = exp.state.between('SETUP', 'ADVANCE');
    // Render
    exp.sceneManager.render();
    if (landmarks[0].position.x > parseFloat(landmarkWidth*1.3).toFixed(2)){
      moveRight.lm = false;
      moveRight.dot=trial.train?false:moveRight.dot;
    }
    if (landmarks[landmarks.length-1].position.x < parseFloat(-landmarkWidth*1.3).toFixed(2)){
      
      moveLeft.lm = false;
      moveLeft.dot=trial.isTrain?false:moveLeft.dot;
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

  function handleKeyUp(e) {
    isKeyDown = false;
    const keyActions = {
      'ArrowRight': () => { moveRight = { lm: false, dot: false }; },
      'ArrowLeft': () => { moveLeft = { lm: false, dot: false }; }
    };
    
    if (keyActions[e.key]) {
      keyActions[e.key]();
    }
  }

function handleKeyDown(e) {
  isKeyDown = true;
  
  const keyActions = {
    'ArrowRight': () => { moveRight = { lm: true, dot: true }; },
    'ArrowLeft': () => { moveLeft = { lm: true, dot: true }; },
    [config.stopKey]: () => {
      exp.trialNumber = exp.numTrials;
      exp.state.next('ADVANCE');
    }
  };

  if (exp.state.between("GO", "FINISH") && (e.key === 'ArrowRight' || e.key === 'ArrowLeft')) {
    keyActions[e.key]();
  }

  if (e.key === config.stopKey) {
    keyActions[config.stopKey]();
  }
}

  function animate(){
    requestAnimationFrame(animate);
  // Get the time difference between frames
  let deltaTime = clock.getDelta();  // Time elapsed since last frame in seconds  
  // Define the step size that should occur over 1 second
  const stepPerSecond = Math.abs(vaToNdC(trial.stepSize, objectDistance, config.screenHeightcm));
  
  // Adjust the step for the current frame based on deltaTime
  const step = stepPerSecond * deltaTime ; // Movement per frame
  
    landmarks.forEach(landmark => {
      if (cursor.atHome){
      if (moveLeft.lm) {
        landmark.position.x -= step;
        
      }
      if (moveRight.lm) {
        landmark.position.x += step;
      }}
  });

  dots.forEach(dot=>{
    if (cursor.atHome){
      
      if (dot.life<0){
            setRandomPosition(dot);
            dot.life = Math.random() * config.dotLife;
      }
  
    if (moveLeft.dot) {
      dot.life -= step;
      dot.position.x -= step;
    }
    if (moveRight.dot) {
      dot.life -= step;
      dot.position.x += step;
    }}
})
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
