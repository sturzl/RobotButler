const int LED_PIN = 13;
int coefficient = 7;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if(Serial.available()){
    coefficient = Serial.read() - '0';
    Serial.println("Received: " + coefficient);
  }
  digitalWrite(LED_PIN, HIGH);
  delay(coefficient*100);
  digitalWrite(LED_PIN, LOW);
  delay(coefficient*100);
}