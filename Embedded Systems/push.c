#include<reg51.h>

sbit led=P1^1; 
sbit push=P3^5;
void main()
{
	while(1)
	{	
		if(push==0)
			led=0;
		else
			led=1;
	}
}