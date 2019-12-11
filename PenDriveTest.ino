#include <AFMotor.h>

AF_Stepper motor(200, 1);
AF_Stepper motor2(200,2);
float dest;
float loc;
float dif;
float updown;
float stepnum;
float bpm;
float del;
float freq;
void setup() {
  loc = 9;
  bpm = 100;

  
  freq = bpm/120;
  del = (freq - 1.016)/(-.00121);
  
  dest = (del - 41.42)/4.718;
  
  dif = dest - loc;
  Serial.begin(9600);
  Serial.print(dest);
  Serial.print(del);


  if (dif > 0) {
   updown = FORWARD;
  }
  else {
   updown = BACKWARD;
  }
  motor.setSpeed(10);
  motor.release();
  delay(5000);

  dif = abs(dif);
  stepnum = dif*39;
  motor2.setSpeed(25);
  motor2.step(stepnum,updown,SINGLE);
  
  
}

void loop() {
  motor2.step(.2,BACKWARD,SINGLE);
  //motor.step(20,BACKWARD, SINGLE);
  delay(del);
  motor.step(15,FORWARD, DOUBLE);
  motor.release();
  delay(del);
  motor.step(15,BACKWARD, DOUBLE);
  motor.release();
  //delay(50);
  //motor.step(10,FORWARD, SINGLE);
  //delay(50);
} 
