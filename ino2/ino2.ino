// slider_led - Arduino UNO
// LEDs PWM: D3, D5, D6, D9
// Botón físico: D2 a GND con INPUT_PULLUP
//
// Comandos por Serial (una línea):
//   LED1:0-255
//   LED2:0-255
//   LED3:0-255
//   LED4:0-255
//   ALL:0-255
//   STATE
//
// Respuestas:
//   OK:LEDn:val
//   OK:ALL:val
//   STATE:v1,v2,v3,v4
//   ERR:CMD

const byte NLEDS = 4;
const byte LED_PINS[NLEDS] = {3, 5, 6, 9}; // PWM
const byte BTN_PIN = 2;

int values[NLEDS] = {0, 0, 0, 0};
bool allOn = false;

// Debounce
int lastReading = HIGH;
int stableState = HIGH;
unsigned long lastChangeMs = 0;
const unsigned long debounceMs = 40;

char buf[48];

int clamp255(int v) {
  if (v < 0) return 0;
  if (v > 255) return 255;
  return v;
}

void applyLed(byte idx, int v) {
  v = clamp255(v);
  values[idx] = v;
  analogWrite(LED_PINS[idx], v);
}

void applyAll(int v) {
  v = clamp255(v);
  for (byte i = 0; i < NLEDS; i++) {
    applyLed(i, v);
  }
  allOn = (v > 0);
}

void publishState() {
  Serial.print("STATE:");
  Serial.print(values[0]); Serial.print(",");
  Serial.print(values[1]); Serial.print(",");
  Serial.print(values[2]); Serial.print(",");
  Serial.println(values[3]);
}

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(30);

  pinMode(BTN_PIN, INPUT_PULLUP);

  for (byte i = 0; i < NLEDS; i++) {
    pinMode(LED_PINS[i], OUTPUT);
    analogWrite(LED_PINS[i], 0);
  }

  Serial.println("OK:READY");
}

void loop() {
  // ---------- Botón físico: toggle ALL ----------
  int reading = digitalRead(BTN_PIN);

  if (reading != lastReading) {
    lastChangeMs = millis();
    lastReading = reading;
  }

  if ((millis() - lastChangeMs) > debounceMs) {
    if (stableState != reading) {
      stableState = reading;

      if (stableState == LOW) { // presionado
        allOn = !allOn;
        applyAll(allOn ? 255 : 0);
      }
    }
  }

  // ---------- Serial: comandos ----------
  if (!Serial.available()) return;

  int n = Serial.readBytesUntil('\n', buf, sizeof(buf) - 1);
  buf[n] = '\0';

  while (n > 0 && (buf[n-1] == '\r' || buf[n-1] == ' ' || buf[n-1] == '\t')) {
    buf[n-1] = '\0';
    n--;
  }

  // STATE
  if (strcmp(buf, "STATE") == 0) {
    publishState();
    return;
  }

  // ALL:val
  if (strncmp(buf, "ALL:", 4) == 0) {
    int v = clamp255(atoi(buf + 4));
    applyAll(v);
    Serial.print("OK:ALL:");
    Serial.println(v);
    return;
  }

  // LEDn:val
  if (strncmp(buf, "LED", 3) == 0) {
    int idx = buf[3] - '1'; // '1'..'4' => 0..3
    char* p = strchr(buf, ':');

    if (idx >= 0 && idx < (int)NLEDS && p) {
      int v = clamp255(atoi(p + 1));
      applyLed((byte)idx, v);

      bool anyOn = false;
      for (byte i = 0; i < NLEDS; i++) if (values[i] > 0) anyOn = true;
      allOn = anyOn;

      Serial.print("OK:LED");
      Serial.print(idx + 1);
      Serial.print(":");
      Serial.println(v);
      return;
    }
  }

  Serial.println("ERR:CMD");
}
