#include <Servo.h>

// Define the pins for the two ultrasonic sensors
const int trigPin1 = 2;
const int echoPin1 = 3;
const int trigPin2 = 4;
const int echoPin2 = 5;

// Define the pins for the servo
const int servoPin = 6;

// Create a servo object
Servo myservo;

void setup() {
  // Initialize the serial communication
  Serial.begin(9600);

  // Set the trigger and echo pins for the ultrasonic sensors
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

  // Attach the servo to the pin
  myservo.attach(servoPin);
}

void loop() {
  // Rotate the servo from 0 to 180 degrees
  for (int angle = 0; angle <= 180; angle++) {
    myservo.write(angle);

    // Wait for the servo to move
    delay(15);

    // Get the distance from the first ultrasonic sensor
    long duration1, distance1;
    digitalWrite(trigPin1, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin1, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin1, LOW);
    duration1 = pulseIn(echoPin1, HIGH);
    distance1 = duration1 * 0.034 / 2;

    // Get the distance from the second ultrasonic sensor
    long duration2, distance2;
    digitalWrite(trigPin2, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin2, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin2, LOW);
    duration2 = pulseIn(echoPin2, HIGH);
    distance2 = duration2 * 0.034 / 2;

    // Print the distances to the serial monitor
    Serial.print("Angle: ");
    Serial.print(angle);
    Serial.print(", Distance1: ");
    Serial.print(distance1);
    Serial.print(", Distance2: ");
    Serial.println(distance2);
  }
}
