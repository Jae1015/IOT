//Exercise2: Send your name from your smart phone to 8051 board via Bluetooth and display it on the LCD.
#include <reg51.h>

sbit RS=P2^6; 
sbit EN=P2^7;
sbit LED=P1^0;


char a[32];

void cmd(unsigned char cmd);  //to send command
void lcdData(unsigned char cmd[]);  //to send data
void delay(); //to cause some delay

void main(){
	int i=0;
	unsigned int chr;
	TMOD=0x20;	//timer 1 mode 2
	TH1=0xFD;	//9600 baud
	SCON=0x50;	//enable UART
	TR1=1;	//enable timer 1
	while(1){
	
		cmd(0x38);  delay();  //initialising LCD
		cmd(0x0E); delay();   //display ON, cursor ON
		cmd(0x01); delay();  //clear display screen
		cmd(0x80); delay();  //cursor on line 1 ,location1

		while(RI==0);	//wait for reception
		RI=0;
		chr=SBUF;	//received character
		while(chr)	//if charcter='y'
		{
			if(i<32)
			{
				a[i]=chr;
				chr=SBUF;
				i++;
			}
		}
		lcdData(a);  delay(); 
	}
}


void cmd(unsigned char cmd){	//to send command
	P0=cmd;
	RS=0;  //for command
	//RW=0;  //for write
	EN=1; //to enable
	delay();
	EN=0;  //disable
}

void lcdData(unsigned char cmd[32]){	//to send data
	int i;
	for(i=0;i<32;i++){
		P0=cmd[i];
		RS=1;  //send data
		//RW=0; //write
		EN=1;
		delay();
		EN=0;
	}
}

void delay(){
	int i,j;
	for(i=0;i<1000;i++)
	for(j=0;j<10;j++);
}

