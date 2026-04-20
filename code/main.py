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
