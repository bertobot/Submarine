#include <Servo.h> 
#include <SPI.h>
#include <Ethernet.h>
//Pins for each motor
# define MOTOR1_PIN 10 //left motor
# define MOTOR2_PIN 11 // right motor
# define MOTOR3_PIN 12 // bottom

// create servo object to control a servo
Servo motor1; 
Servo motor2;
Servo motor3;
int vval = 93;    // vertical variable to read values from analog pin
int hval = 93;    // horizontal variable to read the value from the analog pin 
int speed = 1;  
String readString;  // string that will be parsed from client
//setup ethernet connection
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED }; //physical mac address
byte ip[] = { 192, 168, 1, 3 }; // ip in lan
byte gateway[] = { 10, 0, 0, 1 }; // internet access via router
byte subnet[] = { 255, 255, 255, 0 }; //subnet mask
EthernetServer server(80); //server port

//////////////////////

void setup(){
  //start Ethernet
Ethernet.begin(mac, ip, gateway, gateway, subnet);
server.begin(); // start webserver
Serial.begin(9600);
motor1.attach(MOTOR1_PIN); //attaches left motor to pin 10  
motor2.attach(MOTOR2_PIN); //attaches right motor to pin 11
motor3.attach(MOTOR3_PIN);  //attaches bottom motor to pin 12


  Serial.println("Submarine Online"); // so I can keep track of what is loaded
  Serial.println("Power Up check:");
  Serial.println("Left Motor Pin: ");
  Serial.print(MOTOR1_PIN);
  Serial.println("Right Motor Pin: ");
  Serial.print(MOTOR2_PIN);
  Serial.println("Bottom Motor Pin: ");
  Serial.print(MOTOR3_PIN);
  Serial.println("Host IP: ");
  int i;
  for (i = 0; i < 3; i = i + 1) {
  Serial.println(ip[i]);
  }
  Serial.println("Host Subnet: ");
  i=0;
  for (i = 0; i < 3; i = i + 1) {
  Serial.println(subnet[i]);
  }
  Serial.println("Host Gateway: ");
  i=0;
  for (i = 0; i < 3; i = i + 1) {
  Serial.println(gateway[i]);
  }
  Serial.println("All checks completed, read to go maggot?");  
}

void loop(){
  // Create a client connection
  EthernetClient client = server.available();
  if (client) {
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        //read char by char HTTP request
        if (readString.length() < 100) {
          //store characters to string 
          readString += c; 
          //Serial.print(c);
        } 
        //if HTTP request has ended
        if (c == '\n') {

         ///////////////
          Serial.println(readString); //print to serial monitor for debuging 

          client.println("HTTP/1.1 200 OK"); //send new page
          client.println("Content-Type: text/html");
          client.println();

          client.println("<HTML>");
          client.println("<HEAD>");
          client.println("<TITLE>Arduino GET test page</TITLE>");
          client.println("</HEAD>");
          client.println("<BODY>");

          client.println("<H1>Zoomkat's simple Arduino button</H1>");
          
          client.println("<a href=\"/?on\">ON</a>"); 
          client.println("<a href=\"/?off\">OFF</a>"); 

          client.println("</BODY>");
          client.println("</HTML>");
 
          delay(1);
          //stopping client
          client.stop();

          ///////////////////// control arduino pin
          if(readString.indexOf("up") >0)//moves submarine up
          {
             vval += 1 + speed;
             Serial.print("Increased Vertical Speed To: ");
             Serial.println(vval);
     
          }
          if(readString.indexOf("down") >0)//moves submarine down
          {
             vval -= 1 + speed;
             Serial.print("Decreased Vertical Speed To: ");
             Serial.println(vval);
     
          }
          if(readString.indexOf("forward") >0)//moves submarine forward
          {
             hval += 1 + speed;
             Serial.print("Increased Speed To: ");
             Serial.println(hval);
     
          }
          if(readString.indexOf("back") >0)//moves submarine backwards 
          {
             hval -= 1 + speed;
             Serial.print("Decreased Speed To: ");
             Serial.println(hval);
          }
          if(readString.indexOf("reverse") >0)//moves submarine reverse
          {
             Serial.print("Going in Reverse"); 
             for (int pos=hval; pos>=70; pos-=1)
              { motor1.write(pos);
                motor2.write(pos);
                Serial.print(pos);
                delay(100);
                hval=pos;
               }
               Serial.println("");
          }
          if(readString.indexOf("hstop") >0)//stops horizontal motors slowly 
          {
             Serial.println("Slowly Stopping Horizontal Motors");
             if (hval>=93 ) {
             for (int pos=hval; pos>=93; pos-=1)
              { motor1.write(pos);
                motor2.write(pos);
                delay(100);
                Serial.print(pos);
                hval=pos;
              }
              } else {
              for (int pos=hval; pos>=1; pos-=1)
              { motor1.write(pos);
                motor2.write(pos);
                delay(100);
                Serial.print(pos);
                hval=pos;
              }
             }    
          Serial.println("");
          }
          if(readString.indexOf("vstop") >0)//stops vertical motor slowly 
          {
             Serial.println("Slowly Stopping Vertical Motor");
             if (vval>=93 ) {
             for (int pos=vval; pos>=93; pos-=1)
              { motor1.write(pos);
                motor2.write(pos);
                delay(100);
                Serial.print(pos);
                vval=pos;
              }
              } else {
              for (int pos=vval; pos>=1; pos-=1)
              { motor1.write(pos);
                motor2.write(pos);
                delay(100);
                Serial.print(pos);
                vval=pos;
              }
             }    
          Serial.println("");
          }
          if(readString.indexOf("halt") >0)//halts abruptly the submarine in place
          {
          Serial.println("Halting motors");
          hval = 0 ;
          }
          if(readString.indexOf("speed0") >0)//sets motor speed to 0
          {
          speed = 0;
          Serial.print("Speed set to: ");
          Serial.print(speed);
          }
          if(readString.indexOf("speed1") >0)//sets motor speed to 10
          {
          speed = 19;
          Serial.print("Speed set to: ");
          Serial.print(speed);
          }
          if(readString.indexOf("speed2") >0)//sets motor speed to 20
          {
          speed = 20;
          Serial.print("Speed set to: ");
          Serial.print(speed);
          }
          if(readString.indexOf("speed3") >0)//sets motor speed to 30
          {
          speed = 30;
          Serial.print("Speed set to: ");
          Serial.print(speed);
          }
          if(readString.indexOf("speed4") >0)//sets motor speed to 40
          {
          speed = 40;
          Serial.print("Speed set to: ");
          Serial.print(speed);
          }
          if(readString.indexOf("speed5") >0)//sets motor speed to 50
          {
          speed = 50;
          Serial.print("Speed set to: ");
          Serial.print(speed);
          }
          
            
          motor1.write(hval);
          motor2.write(hval);
          motor3.write(vval);
          //clearing string for next read
          readString="";

        }
      }
    }
  }
} 
