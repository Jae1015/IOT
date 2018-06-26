#include<reg51.h> //include library to use registers defined in it
sbit RS=P2^6; 
sbit EN=P2^7;

char a[8]={ 'J','A','S','P','R','E','E','T' };

void cmd(unsigned char cmd);  //to send command
void lcdData(unsigned char cmd[]);  //to send data
void delay(); //to cause some delay

void main(){
	while(1){
		cmd(0x38);  delay();  //initialising LCD
		cmd(0x0E); delay();   //display ON, cursor ON
		cmd(0x01); delay();  //clear display screen
		cmd(0x80); delay();  //cursor on line 1 ,location1
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

void lcdData(unsigned char cmd[8]){	//to send data
	int i;
	for(i=0;i<8;i++){
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