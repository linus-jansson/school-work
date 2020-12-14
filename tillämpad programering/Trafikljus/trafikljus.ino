// Functioner som slutar på respktive nummer under 
// är antingen huvudled eller korsande väg
// Huvudled: 0
// Korsande väg: 1

#define LED_GREEN0 5
#define LED_YELLOW0 6
#define LED_RED0 7

#define LED_GREEN1 8
#define LED_YELLOW1 9
#define LED_RED1 10

#define STATE_LED_RED 0
#define STATE_LED_YELLOW 1
#define STATE_LED_GREEN 2
#define STATE_LED_YELLOW2 3

#define SENSOR_PIN 2
#define DEBOUNCEDELAY 50

int lightstate0 = STATE_LED_GREEN;
int lightstate1 = STATE_LED_RED;

bool carSensed = false;
int numOfClicks;

// Used for the pause function
unsigned long previousMillis;

bool ready = true;

// Debouncing
int buttonState;             // the current reading from the input pin
int lastButtonState = LOW;   // the previous reading from the input pin
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled

void setup()
{

    pinMode(LED_RED0, OUTPUT);
    pinMode(LED_YELLOW0, OUTPUT);
    pinMode(LED_GREEN0, OUTPUT);

    pinMode(LED_RED1, OUTPUT);
    pinMode(LED_YELLOW1, OUTPUT);
    pinMode(LED_GREEN1, OUTPUT);

    pinMode(SENSOR_PIN, INPUT);

    Serial.begin(57000);

}

void readSensors()
{

    if (digitalRead(SENSOR_PIN) == HIGH)
        numOfClicks++;

    if (ready == true)
    {
        // read the state of the switch into a local variable:
        int isButtonReading = digitalRead(SENSOR_PIN);

        // If the switch changed, due to noise or pressing:
        if (isButtonReading != lastButtonState) {
            // reset the debouncing timer
            lastDebounceTime = millis();
        }
        
        if ((millis() - lastDebounceTime) > DEBOUNCEDELAY) {
            // whatever the reading is at, it's been there for longer than the debounce
            // delay, so take it as the actual current state:

            // if the button state has changed:
            if (isButtonReading != buttonState) {
                buttonState = isButtonReading;

                // Car is sensed if button is pressed
                if (buttonState == HIGH && lightstate0 == STATE_LED_GREEN) {
                    carSensed = true;
                }

            }
        }

        // save the reading. Next time through the loop, it'll be the lastButtonState:
        lastButtonState = isButtonReading;   
    }
    // om huvudleden är grön och den inte är ready
    else if (lightstate0 == STATE_LED_GREEN)
    {
        Serial.println("Button cooldown...");
        pause(2500);
        ready = true;
        Serial.println("Button cooldown done!");

    }
     
}



void pause(int PAUSETIME)
{
    // Serial.print("Waiting for: ");
    // Serial.println(PAUSETIME);

    while (true)
    {
        if ((millis() - previousMillis) >= PAUSETIME) 
        {
            previousMillis = millis();
            break;
        }
    }
    
}


void setLEDlight0(int lightstate)
{

    switch (lightstate)
    {

        case STATE_LED_GREEN:
            digitalWrite(LED_GREEN0, HIGH);
            digitalWrite(LED_YELLOW0, LOW);
            digitalWrite(LED_RED0, LOW);
            // Serial.println("0: Green on");
            break;

        case STATE_LED_YELLOW:
        case STATE_LED_YELLOW2:
            digitalWrite(LED_GREEN0, LOW);
            digitalWrite(LED_YELLOW0, HIGH);
            digitalWrite(LED_RED0, LOW);
            // Serial.println("0: Yellow on");
            break;

        case STATE_LED_RED:
            digitalWrite(LED_GREEN0, LOW);
            digitalWrite(LED_YELLOW0, LOW);
            digitalWrite(LED_RED0, HIGH);
            // Serial.println("0: Red on");
            break;

    }
}

void setLEDlight1(int lightstate)
{
    // tänder och släcker ledsen beroende på lightstate
    switch (lightstate)
    {

        case STATE_LED_GREEN:
            digitalWrite(LED_GREEN1, HIGH);
            digitalWrite(LED_YELLOW1, LOW);
            digitalWrite(LED_RED1, LOW);
            // Serial.println("1: Green on");
            break;

        case STATE_LED_YELLOW:
        case STATE_LED_YELLOW2:
            digitalWrite(LED_GREEN1, LOW);
            digitalWrite(LED_YELLOW1, HIGH);
            digitalWrite(LED_RED1, LOW);
            // Serial.println("1: Yellow on");
            break;

        case STATE_LED_RED:
            digitalWrite(LED_GREEN1, LOW);
            digitalWrite(LED_YELLOW1, LOW);
            digitalWrite(LED_RED1, HIGH);
            // Serial.println("1: Red on");
            break;

    }
}

void runStateMachine0()
{

    switch (lightstate0)
    {
        case STATE_LED_GREEN:
            // Om det kommer en bil så ska den byta till gult
            // och så ska den kolla ifall längden som den har varit grönt är större än en viss tid

            if (carSensed && ready && digitalRead(SENSOR_PIN) == LOW)
            {
                // Serial.print("Num of cars: ");
                // Serial.println(numOfClicks);
                Serial.println("cars waiting on crossing street");
                
                ready = false;

                pause(1000);
                // Serial.println("0: Green -> Yellow");
                lightstate0 = STATE_LED_YELLOW;

            }

            break;

        case STATE_LED_YELLOW:
            pause(1000);
            // Serial.println("0: Yellow -> Red");
            lightstate0 = STATE_LED_RED;
            
            break;
        
        case STATE_LED_RED:

            // Om det inte kommer en bil / längre och andra rödljuset är rött så ska den byta tillbaka till gult mot grönt
            if (carSensed == false && lightstate1 == STATE_LED_RED)
            {
                Serial.println("Going back to normal");
                pause(1500);
                // Serial.println("0: Red -> Yellow");
                numOfClicks = 0;
                lightstate0 = STATE_LED_YELLOW2;
            }

            break;

        case STATE_LED_YELLOW2:
            pause(1000);
            // Serial.println("0: Yellow -> Green");
            lightstate0 = STATE_LED_GREEN;
            
            break;
    }

    // Ändrar ljuset efter lightState
    setLEDlight0(lightstate0);
    
}

void runStateMachine1()
{   

    switch (lightstate1)
    {

        case STATE_LED_RED:

            // kommer det en bil och andra rödljuset är rött så kan den byta mot grönt
            if (lightstate0 == STATE_LED_RED && carSensed == true)
            {
                pause(500);
                // Serial.println("1: Red -> Yellow");
                lightstate1 = STATE_LED_YELLOW2;
            }
            break;

        case STATE_LED_YELLOW2:
            pause(1000);
            // Serial.println("1: Yellow -> Green");
            lightstate1 = STATE_LED_GREEN;
            break;

        case STATE_LED_GREEN:
            // Green LED is turned on longer when the button is pressed for a longer time
            Serial.println("letting cars through...");
            if (numOfClicks > 1000)
                pause(2000);
            else
                pause(500);     
            // Serial.println("1: Green -> Yellow");
            carSensed = false;
            lightstate1 = STATE_LED_YELLOW;
            break;

        case STATE_LED_YELLOW:
            pause(1000);
            // Serial.println("1: Yellow -> Red");
            lightstate1 = STATE_LED_RED;
            break;
    }  

    // Ändrar ljuset efter lightState
    setLEDlight1(lightstate1);

}


void loop()
{
    readSensors();
    runStateMachine0();
    runStateMachine1();

}