#include<reg51.h>

void delay();

void main()
{
	while(1)
	{	
		P1=0x0A; //port is already defined in the header file^ Therefoe no need to declared
		delay();
		P1=0x05;
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