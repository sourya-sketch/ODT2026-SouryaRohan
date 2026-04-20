# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`Music Minds`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Sourya Sankar Banerjee` | `[Electronics / Mechanics]` | `[App]` | `[Ideation, Spatial strength]` |
| `Rohanpreet Singh` | `[Coding / Fabrication]` | `[App]` | `[Execution, Coding experience]` |

## 1.3 Project Title
`[Music-Whackamole]`

## 1.4 One-Line Pitch
`[Musical lights direct your moves]`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
This project is a rhythm-based interactive game inspired by reflex machines and music rhythm games. It consists of six physical pads arranged spatially, each embedded with limit switches to detect hits. A central NeoPixel lighting system visually guides the player by sending light pulses toward a specific pad in sync with a beat.
The player must hit the correct pad at the right moment, following the light cues. If the player misses the beat, the system pauses, reinforcing timing accuracy. The experience is designed to be fast, reactive, and physically engaging, combining elements of rhythm games, sports reflex training, and arcade-style play.
The project supports both single-player and two-player modes. In single-player mode, the player tries to survive as long as possible while maintaining rhythm. In two-player mode, players compete against each other to survive. 

Technologies involved include an ESP32 microcontroller, NeoPixel LED strips for dynamic lighting feedback, and limit switches for physical interaction detection. The system is programmed using MicroPython.
---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
The experience is a fast-paced rhythm reaction game where players must respond quickly to visual cues. The player feels urgency, focus, and excitement as they try to match the beat and hit the correct pad. The system creates tension by giving limited time to react and rewards accuracy with continuous gameplay. Missing a beat interrupts the flow, making the player want to try again and improve. Players would want to retry because of the challenge, increasing speed, and the satisfaction of correctly timing hits in sync with the lights.

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
We are designing this project as if we are a small creative studio making a game for classmates and exhibition visitors.

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| Boxing Punching Machine | https://www.amazon.in/Lufjika-Machine-Bluetooth-Traineing-Equipment/dp/B0GCJWLZJZ?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=A3JOXW2N90ZGX9&th=1 | Spatial distribution of pads, light feature |
| Whack-a-mole | https://www.youtube.com/watch?v=VoP1E9J4jpg | Game dynamics |

## 3.2 Original Twist
What makes your project original?

**Response:**  
Unlike traditional rhythm games that use screens, this project creates a fully physical interaction using punching pads and spatial lighting. The combination of directional light travel and physical impact makes the experience more immersive and bodily engaging.
Software wise we have also introduced 2-player games and more experiences integrating music to make it stand out.

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
light travels → player reacts → hits pad → system checks timing → continues or stops

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | Students and exhibition visitors |
| Age range | 15–25 |
| Solo or multiplayer | Solo |
| Expected duration of one round |30 seconds – 3 minutes|
| What should the player feel? | Excited, focused, competitive |
| Is explanation required before use? | Minimal (intuitive interaction) |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** Player sees illuminated pads and central light source
2. **Start:** Game begins automatically or via input
3. **First Action:** Light travels to a pad
4. **Main Interaction:** Player punches the correct pad on beat
5. **System Response:** Lights confirm hit or stop on miss
6. **Win / Lose / End Condition:** Game ends on missed beat
7. **Reset:** System returns to idle state and restarts

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- Player must hit the pad indicated by the light
- Player must hit within the given time window
- Missing a beat ends the game
- In two-player mode, players alternate turns

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] All 6 pads detect input reliably
- [ ] LED strip correctly indicates target pad
- [ ] Game loop runs continuously without crashing
- [ ] Miss detection works correctly

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
A basic version with 2–3 pads, working LED indication, and hit/miss detection without advanced animations or multiplayer.

## 5.3 Stretch Features
What features are nice to have but not essential?

- Increasing speed over time
- Sound feedback (buzzer/music sync)
- Score display system
---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [ ] Mechanical
- [x] Sensor-based
- [ ] App-connected
- [ ] Motorized
- [ ] Sound-based
- [x] Light-based
- [ ] Screen/UI-based
- [ ] Fabricated structure
- [x] Game logic based
- [x] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  

The system takes input from limit switches placed under each pad. These inputs are processed by the ESP32 microcontroller, which determines whether the correct pad was hit within the time window.
Based on the game logic, the ESP32 sends output signals to a NeoPixel LED strip, which visually indicates the target pad through traveling light animations.
The physical structure consists of six pads arranged spatially, allowing the player to interact through punching. The system operates as a closed loop of input (hit detection), processing (timing logic), and output (LED feedback).

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `Limit Switch(x6)` | Input | `Detects press from user inside the tapping pad and sends a signal to the controller` |
| `ESP32 / Controller` | Processing | `Receives input signals, processes game logic (timing, scoring), and sends output signals` |
| `LED Strip / RGB LEDs(x90)` | Output | ` Provides visual feedback (beat indicators, hit/miss signals)` |
| `Tapping Surface / Pad` | Physical Action | `Interface where user interacts, transfers force to sensors` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `45 cm` |
| Width | `45 cm` |
| Height | `8 cm` |
| Estimated weight | `1-2 kg` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [x] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
The system consists of six tapping pads, each integrated with a limit switch positioned beneath the surface. When the user taps a pad, the top surface compresses slightly and actuates the limit switch, converting the mechanical force into a digital input signal.

Each pad is designed to ensure consistent force transfer while protecting the internal components. The structure includes a rigid base, a slightly flexible top layer, and internal spacing to allow controlled movement without damaging the switch.

Surrounding each pad is a cluster of 15 NeoPixel LEDs (5 at the center leading up to it and 10 forming an outer ring), embedded within the structure. They are all soldered together. These LEDs provide immediate visual feedback corresponding to user interaction. The LEDs and the button will sync according to the beats.

The overall mechanism is designed to be durable, responsive, and repeatable, enabling fast tapping interactions required for a rhythm-based gameplay system.

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
- What moves:
The top surface of each tapping pad moves vertically by a small amount when pressed.

- What causes the movement:
User-applied force (finger tap) causes the pad surface to compress and activate the limit switch.

- How far it moves:
The displacement is minimal, typically around 1–3 mm, just enough to trigger the switch reliably.

- How fast it moves:
Movement is instantaneous and directly dependent on user tapping speed, supporting rapid repeated inputs.

- What could go wrong:
Potential issues include switch wear over time, inconsistent triggering due to uneven force distribution, structural loosening, or reduced responsiveness if the pad material degrades.

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[Write here]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `ESP32` | `1` | `Main controller to process inputs and control LEDs` |
| `Limit Switch` | `6` | `Detects user taps from each pad` |
| `NeoPixel LEDs` | `90` | `Provides visual feedback for each pad` |
| `Resistor (330Ω)` | `1` | `Protects LED data line from voltage spikes` |
| `Power Supply (5V)` | `1` | `owers the LED strip and system` |
| `Jumper Wires` | `Multiple` | `Electrical connections between components` |
| `Breadboard / PCB ` | `1` | `Mounting and organizing circuit connections` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
The ESP32 acts as the central controller. Each of the six limit switches is connected to a separate GPIO pin configured as digital input, with a common ground connection.

The NeoPixel LEDs are connected in a chained configuration. A single data pin from the ESP32 is connected to the input of the first LED, and the signal propagates through all 90 LEDs.

A resistor (330Ω) is placed between the ESP32 data pin and the first NeoPixel to protect the data line. A capacitor (1000µF) is connected across the power supply terminals to stabilize voltage and prevent fluctuations.

The LEDs are powered using a 5V external power supply, while the ESP32 shares a common ground with the LED circuit to ensure proper signal reference.

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `5V DC External Power Adapter` |
| Voltage required | `5V DC` |
| Current concerns | `90 NeoPixels at max brightness (white) draw ~5.4A. Ensure the PSU is rated for at least 6A–10A, or use software to limit max brightness to prevent current overload.` |
| Safety concerns | `Avoid powering LEDs directly through the ESP32 (use direct power injection). Ensure correct polarity (common ground), use a fuse for the main power line, and ensure adequate wire gauge to prevent heating.` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `MicroPython` | `Firmware development and logic implementation for the ESP32 controller.` |
| `HTML` | `Designing the frontend interface and structure for the user dashboard.` |
| `Java` | `Implementing backend processing and application-level logic.` |
| `Thonny IDE` | `The primary development environment for writing and uploading MicroPython code to the ESP32.` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
Startup Behavior
The ESP32 initializes all hardware components, including the 90-LED NeoPixel strip and the 6 GPIO pins configured as digital inputs with pull-up resistors. The system creates a Wi-Fi access point and launches a web server at http://192.168.4.1, serving the HTML interface. Simultaneously, the PC-side Python script initializes pygame for audio and establishes serial communication with the ESP32, placing the system in a "ready" state waiting for commands.

Input Handling
Input is captured from three sources:

Physical: The 6 limit switches detect hits (triggered by a LOW signal).

Web Interface: The user can interact with the dashboard to set the BPM, or press the "Start" or "Stop" buttons, which trigger the appropriate API endpoints.

Keyboard (PC): The Python script listens for keyboard interrupts: P to pause/resume the current audio track and Q to quit the program.

Sensor Reading
In every execution loop, the ESP32 reads the state of the 6 limit switches using Pin.value(). To prevent false triggers, a debounce algorithm—consisting of a ~20 ms delay—is applied. During an active beat, the system polls these inputs to determine if the correct pad is pressed within a valid 200 ms timing window.

Decision Logic
The system logic is governed by the selected BPM, which dictates the beat_interval using the formula 60 / BPM. At each interval, the system activates a target pad. The logic compares the user's physical input against the active target:

Hit: Score increases.

Miss: Miss count increments.
If the miss_count reaches 3, the game automatically stops. On the PC side, the logic triggers the corresponding MP3 file playback and stops audio when a "Game Over" or "Stop" signal is received.

Output Behavior
Visual and audio feedback are synchronized for the user experience:

LEDs: The first 5 LEDs serve as a blue "arm" animation. The next 10 LEDs act as target pads; they turn green to indicate a target, flash white on a hit, and turn red on a miss.

Web Interface: The dashboard displays the real-time score, updated every 500 ms.

Audio: pygame plays the selected song, with status signals (e.g., AUDIO_STARTED, AUDIO_ENDED) transmitted to the ESP32 to maintain sync.

Communication Logic
The system uses a dual-communication architecture:

ESP32 ↔️ Web Browser: Communicates via HTTP requests (/start, /stop, /score) to handle user interface interactions.

ESP32 ↔️ PC (Python): Uses serial communication (USB) to exchange game status updates (song selection, game over) and audio control signals. This ensures the hardware-side gameplay remains perfectly aligned with the PC-side audio playback.

Reset Behavior
Upon pressing "Stop" or triggering a "Game Over" event, the game loop halts immediately. The LEDs are cleared, and audio playback stops. When restarting the game, the system resets all global variables—score and miss counts are set to 0, and the game state is reinitialized to ensure a fresh session.

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`Images are in image folder`

## 10.4 Pseudocode

```text
from machine import Pin
import neopixel
import time
import socket

# -------------------------
# CONFIG
# -------------------------
NUM_LEDS = 90
LED_PIN = 4
SWITCH_PINS = [13, 12, 14, 25, 26, 27]

np = neopixel.NeoPixel(Pin(LED_PIN), NUM_LEDS)
switches = [Pin(p, Pin.IN, Pin.PULL_UP) for p in SWITCH_PINS]

bpm = 120
beat_interval = 60 / bpm

score = 0
miss_count = 0
current_pad = 0
game_running = False

last_beat = time.ticks_ms()

# -------------------------
# LED FUNCTIONS
# -------------------------
def clear_leds():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

def animate_pad(pad):
    start = pad * 15

    # arm (5 LEDs)
    for i in range(5):
        np[start + i] = (0, 0, 255)

    # pad (10 LEDs)
    for i in range(5, 15):
        np[start + i] = (0, 255, 0)

    np.write()

# -------------------------
# INPUT
# -------------------------
def check_hit(pad):
    if switches[pad].value() == 0:
        time.sleep_ms(20)
        return True
    return False

# -------------------------
# HTML PAGE
# -------------------------
html = """<!DOCTYPE html>
<html>
<head>
<title>Boxing Target</title>
<style>
body { font-family: Arial; text-align: center; }
button { padding: 10px; margin: 10px; font-size: 18px; }
</style>
</head>
<body>

<h1>🥊 Boxing Target</h1>

<label>BPM:</label>
<input type="number" id="bpm" value="120"><br>

<button onclick="start()">Start Workout</button>
<button onclick="stop()">Stop</button>

<h2>Score: <span id="score">0</span></h2>

<audio id="player" controls>
  <source src="song.mp3" type="audio/mpeg">
</audio>

<script>
function start() {
    let bpm = document.getElementById("bpm").value;
    fetch("/start?bpm=" + bpm);
    document.getElementById("player").play();
}

function stop() {
    fetch("/stop");
    document.getElementById("player").pause();
}

function updateScore() {
    fetch("/score")
    .then(res => res.text())
    .then(data => {
        document.getElementById("score").innerText = data;
    });
}

setInterval(updateScore, 500);
</script>

</body>
</html>
"""

# -------------------------
# WEB SERVER SETUP
# -------------------------
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Server running at http://192.168.4.1")

# -------------------------
# MAIN LOOP
# -------------------------
while True:

    # --- Handle Web Requests (non-blocking) ---
    try:
        s.settimeout(0.01)
        conn, addr = s.accept()
        request = conn.recv(1024).decode()

        if "/start" in request:
            try:
                bpm_val = int(request.split("bpm=")[1].split(" ")[0])
                bpm = bpm_val
                beat_interval = 60 / bpm
            except:
                pass

            score = 0
            miss_count = 0
            game_running = True

        elif "/stop" in request:
            game_running = False
            clear_leds()

        elif "/score" in request:
            conn.send("HTTP/1.1 200 OK\nContent-Type: text/plain\n\n")
            conn.send(str(score))
            conn.close()
            continue

        conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n")
        conn.send(html)
        conn.close()

    except:
        pass

    # --- GAME LOOP ---
    if game_running:
        now = time.ticks_ms()

        if time.ticks_diff(now, last_beat) >= beat_interval * 1000:
            last_beat = now

            clear_leds()
            animate_pad(current_pad)

            hit = False
            start = time.ticks_ms()

            while time.ticks_diff(time.ticks_ms(), start) < 200:
                if check_hit(current_pad):
                    score += 1
                    hit = True
                    break

            if not hit:
                miss_count += 1

            if miss_count >= 3:
                game_running = False
                clear_leds()

            current_pad = (current_pad + 1) % 6
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [ ] No
- [x] Third party interface used

If yes, complete this section.

## 11.2 Why is the app needed?


Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
Remote Control & Ease of Access: By hosting the interface on the ESP32 via Wi-Fi, the user can manage the system directly from a smartphone. This eliminates the need to physically interact with the laptop during gameplay, allowing for a more immersive training experience.

Mode & Difficulty Selection: The interface allows for dynamic selection of songs and difficulty levels (BPM), enabling users to customize the challenge in real-time without pausing or restarting the connection to the PC.

Centralized Game Management: It provides a user-friendly dashboard for starting and stopping the game, ensuring that the control layer is physically separated from the audio-processing layer (the PC).

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `Song Selector` | `Enables selection of the specific audio track to be played during the game.` |
| `Start/Stop Buttons` | `Provides tactile control to trigger the game start sequence or halt execution safely.` |
| `Difficulty Selector` | `Allows the user to select song and see the bpm(beats per minute) to match the game intensity to their skill level.` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`Image uploaded in images folder`

## 11.5 App Screen Flow

1. `The user connects to the ESP32 Wi-Fi network and accesses the local web URL (192.168.4.1) via their smartphone browser. The main screen loads, displaying the "RHYTHMPAD" header and the scrollable list of available tracks categorized by difficulty (Easy vs. Hard).`
2. `The user browses the library and taps on a specific track card out of the 3 available ones (e.g., "Sunflower"). This action triggers a focus event, highlighting the selected song for review.`
3. `A modal pop-up appears, providing a clear summary of the song title, artist, BPM, and difficulty level. The user reviews these details and either taps "Start Game" to initialize the session or "Cancel" to return to the track list.`
4. `Once "Start Game" is pressed, the web interface sends the configuration command to the ESP32. The hardware initializes the light sequences, and the system sends a trigger to the PC to begin synchronized audio playback.`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `ESP32-WROOM-32` | `Chosen for its built-in Wi-Fi, allowing the hosting of the web server for remote control.` |
| `Limit switch` | `6` | `Yes` | `No` | `0` | `Limit switch` | `For spring-like mechanism` |
| `RGB LED Strips` | `2` | `No` | `Yes` | `980` | `NeoPixel` | `Addressable LEDs allow for individual control of each pixel, perfect for dynamic game feedback.` |
| `Jumper Cables` | `50` | `Yes` | `Yes` | `100` | `M-F/M-M` | `Used for modular connections between the ESP32, sensors, and power rails.` |
| `Sponges` | `6` | `No` | `Yes` | `sourced for free` | `High-density foam` | `Sourced for free as a cost-effective, impact-absorbing material for the pressure pads.` |
| `Power Supply` | `1` | `Yes` | `Yes` | `0` | `5V Power supply` | `Required to power 90 LEDs at full brightness; 10A prevents power sag during intense visuals.` |
| `Acrylic` | `12` | `No` | `Yes` | `0` | `High quality acrylic sheet` | `Required to dissipate the RGB light in a hazy effect.` |
| `Wood` | `45x45cm` | `No` | `Yes` | `0` | `High quality thick Plywood sheet` | `Required to build the base of the game.` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
Acrylic (Housing/Surface): We selected acrylic for the main structure because of its high durability and rigidity, which is essential for sustaining repeated impact during gameplay. Furthermore, We sanded it so its translucent properties allow us to diffuse the NeoPixel LED lighting effectively, creating a clean and hazy, professional "glow" effect when a pad is hit, which would not be possible with opaque materials like MDF or cardboard.

Sponges (Impact Absorption): Sponges were sourced as a zero-cost, high-density cushioning solution. They provide necessary shock absorption for the limit switches, preventing mechanical damage from repeated impacts while being lightweight and easy to replace.

ESP32 (Microcontroller): Chosen for its integrated Wi-Fi capabilities, which are central to our project's goal of enabling remote control via a smartphone without needing a dedicated app, effectively turning the device into a standalone web-hosted peripheral.

RGB NeoPixel strip (Visual Feedback): These addressable LEDs were chosen for their individual controllability, allowing us to implement complex animation states (idle, target, hit, miss) that would be impossible with standard analog LEDs.

Plywood (Rigid base): Required to build the base of the game for tapping the foam buttons.
We didn't use MDF as it would break easily.


## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `RGB LED strips` | `Visual feedback` | `https://robu.in/product/1m-ws2812b-5v-addressable-rgb-non-waterproof-led-strip-light-60leds-m` | `12-04-26` | `Received` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `980` |
| Mechanical parts | `100` |
| Fabrication materials | `0` |
| Purchased extras | `200` |
| Contingency | `200` |
| **Total** | `1480` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
The total project cost of approximately 1,500 INR was well within our allocated budget and represents excellent value for the functionality achieved. By sourcing structural materials like sponges locally and wood from the lab, we kept fabrication costs to near zero, allowing us to prioritize our budget on high-quality electronics (LED strips) that are critical to the system's performance and visual feedback. This investment was highly worthwhile, as it resulted in a durable, responsive, and fully interactive game prototype that meets all our design requirements.

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
Task Division: We operate on a collaborative model. Both team members contribute to both hardware assembly and software development. We assign a "lead" to specific tasks to ensure accountability, but the other member provides active support, pair-programming, and troubleshooting assistance.

Decision Making: All major design, coding, or structural changes are decided through mutual discussion. We prioritize ideas that are most efficient and easiest to maintain.

Progress Checks: We verify that hardware changes match the software code before finalizing any merge and also kept checking the wiring in between working many times to confirm the working of the game.

Handling Delays: Since we share responsibility, if one of us faces a hurdle, we immediately shift focus to help resolve the blocker together, ensuring the project stays on track.

Documentation: We maintain documentation as a team. We documented in a lot of videos. Before ending any session, we review the README.md together to ensure it reflects our combined progress accurately as well as the hardware parts of it including the wiring and the breadboard.

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `Hardware Setup (Pads & LEDs)` | `Rohan` | `10` | `-` | `16-04-26` | `20-04-26` | `Completed` |
| T2 | `Firmware and control logic` | `Sourya` | `8` | `17-04-26` | `T1` | `Completed` |
| T3 | `Web Dashboard & Integration` | `Rohan` | `7` | `18-04-26` | `T2` | `Completed` |
| T4 | `System Sync (Serial/API)` | `Sourya` | `6` | `18-04-26` | `T3` | `Completed` |
| T5 | `Playtesting & Calibration` | `Rohan` | `5` | `19-04-26` | `T4` | `Completed` |
| T6 | `Final touches/ code tweaks & Game experience design` | `Sourya` | `6` | `19-04-26` | `T5` | `Completed` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `Sourya` | `Rohan` |
| Electronics | `Rohan` | `Sourya` |
| Coding | `Sourya` | `Rohan` |
| App | `Rohan` | `Sourya` |
| Mechanical build | `Rohan` | `Sourya` |
| Testing | `Sourya` | `Rohan` |
| Documentation | `Sourya` | `Rohan` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [ ] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [x] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [x] Electronics tests completed
- [ ] CAD / structure planning completed
- [x] App UI started if needed
- [x] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [x] Physical body built
- [x] Electronics integrated
- [ ] Code connected to hardware
- [x] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | Idea, Sketches | Finalized rhythm game concept and sourced materials. | Shifted from Bluetooth to Wi-Fi hosting for better accessibility. | Begin electronics testing. |
| Week 2 | Build Subsystems | Tested NeoPixel/ESP32 logic; sourced free sponges. | Optimized LED logic for better sync, settled on acrylic for durability. | Integrate hardware into frame. |
| Week 3 | Integration | Assembled the physical pad structure and wired components. | Adjusted switch debounce timing for higher responsiveness. | Finalize Serial and API sync. |
| Week 4 | Refine and Finish | Completed software logic and polished Web UI. | Added multi-song selection via the web dashboard. | Final documentation & testing. |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `Serial communication latency` | `Technical` | `Medium` | `High` | `[Implement a robust handshake protocol; keep serial buffer clear.` | `Sourya` |
| `LED flicker / Power sag` | `Technical` | `High` | `Medium` | `Use a dedicated 5V 10A power supply; add large capacitors.` | `Rohan` |
| `Mechanical switch wear` | `Mechanical` | `[Medium]` | `[High]` | `[Ensure sponge padding is sufficient; use durable microswitches.]` | `[Rohan]` |
| `[Wi-Fi connectivity drops]` | `[Technical]` | `[Low]` | `[High]` | `[Ensure ESP32 is close to the router/device; include error handling.]` | `[Sourya]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
The single biggest uncertainty is the total latency of the end-to-end feedback loop. We are currently ensuring that the delay between the user physically hitting a pad (detected by the ESP32) and the corresponding audio/visual response on the PC is imperceptible. Minimizing this "input-to-feedback" lag to ensure a seamless, professional rhythm game feel—without sync drift during high-BPM gameplay—remains our primary technical challenge.

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `Wi-Fi Connectivity` | `Monitor serial output for IP assignment on startup.` | `Consistent connection to local network without drops.` |
| `Mechanical Pad Response` | `Press pads repeatedly at varying speeds.` | `Switches trigger consistently with no mechanical "stuck" states.` |
| `Sensor/LED Sync` | `Trigger sensor and observe LED feedback.` | `Instant (imperceptible) lighting change upon physical press.` |
| `Web Dashboard App` | `Send commands from phone to ESP32.` | `Dashboard updates state instantly, ESP32 executes commands.` |
| `End-to-End Latency` | `Compare physical hit time vs. audio/visual trigger.` | `Delay is under 50ms, feels "real-time" to the player.` |


## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `Observe new users without instructions, see if they naturally know to hit the pads when the lights flash.` |
| Is the interaction satisfying? | `Ask testers to rate the "tactile feel" (responsiveness) of the pads.` |
| Do players want another turn? | `Monitor if players voluntarily restart the game or ask to play a different song after their first run.` |
| Is the challenge balanced? | `Check if players can hit at least 70% of notes on "Easy" mode vs. failing quickly on "Hard" mode.` |
| Is the response clear and immediate? | `Use a "lag test": check if the delay between physical impact and LED/audio feedback feels "instant" to the player.` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `18-04-26` | `LEDs not working in a series` | `Mechanical` | `Redid the soldering` | `Worked` | `Testing LEDs` |
| `19-04-26` | `ad unresponsive intermittently` | `Mechanical` | `Adjusted the wiring inside the sponges` | `Worked` | `Testing switches` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `Classmate` | `Played on 'Easy'` | `The initial calibration screen` | `The light-up feedback when hitting pads` | `Add clearer visual cue on light strips` |
| `Friend` | `[Played on 'Hard'` | `Speed of the track selection` | `The tactile "clicky" feel of the pads` | `Tweak sensitivity on the switches` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
Base Preparation: We utilized a plywood board as the primary structural base. After measuring the layout, we drilled precise holes to accommodate the control buttons and provide mounts for the LED array.

Structural Assembly: We installed four wooden feet to the base to provide stability and ensure the device remains stationary during high-intensity gameplay.

Electronics Integration: We soldered 12 addressable LEDs into a custom radial configuration. This layout features 6 of the 5-LED clusters at the center, extending outward to an outer ring of 6 10-LED strip which is all connected in a series.

Final Assembly: Each button was aligned with the corresponding LED light path to ensure that visual feedback is synchronized with physical inputs. The wiring was routed through the base to keep the surface clean and prevent accidental disconnections during use.

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

```Images in folder 
```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| ` v0.1 ` | ` 10-Apr-2026 ` | Initial Concept | Established project requirements and budget. |
| ` v0.5 ` | ` 17-Apr-2026 ` | Electronics Prototype | Validated ESP32 firmware and LED radial configuration. |
| ` v1.0 ` | ` 20-Apr-2026 ` | System Integration | Integrated hardware with Web dashboard and finalized docs. |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
