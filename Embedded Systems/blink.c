#include<reg51.h>

sbit led=P1^1; //^ for .
void delay();
	
void main()
{
	while(1)
	{	
		led=1;
		delay();
		led=0;
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