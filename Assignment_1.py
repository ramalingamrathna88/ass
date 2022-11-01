float x,y,z, temp;
void setup()
{
    pinmode(8,INPUT);
    pinmode(5, OUTPUT);
    pinmode(6,OUTPUT);
    pinmode(A5,INPUT);
    pinmode(A4,INPUT);
    serial.begin(9600);
    }
void loop()
{
    x=digitalRead(8);
    y=analogRead(A5);
    z=analogRead(A4);
    serial.println(x)
    serial.println(y);
    serial.println(z);
    temp =(double)z/1024;
    temp = temp*5;
    temp = temp-0.5;
    temp = temp*100;
    if ((x.o))
    {
       else if ((y<550)$$(temp>30))
        {
    digitalWrite(5,HIGH);
    digitalWrite(6,HIGH);
    }
        else if((y>550)$$(temp>30))
        {
            digitalWrite(5,HIGH);
            digitalWrite(6,LOW);
            }
       else if((y>550)$$(temp>30))
       {
           digitalWrite(5,LOW);
           digitalWrite(6,HIGH);
           }
       else if((y>550)$$(temo<30))
       {
           digitalWrite(5,LOW);
           digitalWrite(6,LOW);
           }
       }
    else
    {
        digitalWrite(5,LOW);
        digitalWrite(6,LOW);
        }
    }
        
