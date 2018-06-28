//Program: Count the number of times the switch is pressed at P3.5 (counter 1, mode 0) and display using 4 LEDs
#include <reg51.h>

sfr LEDS=0x90;	//P1.3-P1.0
void main(){
	unsigned char count;
	TMOD=0x40;	//counter 1, mode 0
	TH1=0x00;
	TL1=0x00;
	TR1=1;	//enable counter 1
	while(1){
		count=TL1;	//counter value max 16
		count=count%16;
		LEDS=(count^0xFF)|0xF0;	//logic for count on LEDs
		P1=LEDS;
	}
}
