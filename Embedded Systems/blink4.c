#include<reg51.h>

sbit led0=P1^0;
sbit led1=P1^1;
sbit led2=P1^2;
sbit led3=P1^3;
void delay();

void main()
{
	while(1)
	{	
		led0=0;
		led2=0;
		led1=1;
		led3=1;
		delay();
		
		led0=1;
		led2=1;
		led1=0;
		led3=0;
		delay();
	}
}	

void delay()
	{
		unsigned int i,j;
		for(i=0;i<1000;i++)
		{
			for(j=0;j<100;j++);
		}
	}