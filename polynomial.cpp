#include<stdio.h>
#include<stdlib.h>
struct node{
	int data;
	char alp;
	struct node* next;
};

	struct node* first;
	struct node* last;
	struct node* nn;


void insert()
{
//	struct node* nn;
	nn=(struct node*)malloc(sizeof(struct node));
	
	int a,b;
	
	printf(" enter the coiffecient and exponent");
	scanf("%d %d",&a,&b);
	
	nn->data=a;
	nn->alp=b;
	nn->next=NULL;
	
	if(first==NULL)
	{
		first=nn;
		last=nn;
	}
	else
	{
		last->next=nn;
		last=nn;
	}
}

void sort()
{
	struct node* max=first;
	struct node* p=first;

    int temp,tempa;
	
	while(max->next!=NULL)
	{
		while(p != NULL)
		{
			if(max->alp < p->alp)
			{
				temp=max->data;
				tempa=max->alp;
				max->data=p->data;
				max->alp=p->alp;
				p->data=temp;
				p->alp=tempa;
				temp=tempa=0;
			}
			p=p->next;
		}
		max=max->next;
		p=max->next;
	}
}

void display()
{
	struct node* p=first;
	while(p !=NULL)
	{
		printf("%dx%d + ",p->data,p->alp);
		p=p->next;
	}
//		printf("%dx%d",p->data,p->alp);
//		p=p->next;
	
}

void compute()
{
	int a,i=0,r=1,m=1,res=0;
	struct node* p=first;

	printf("enter the value of x");
	scanf("%d",&a);
	
	while(p != NULL)
	{
		for(i=0;i<p->alp;i++)
		{
			r=r*a;
		}
		m=p->data*r;
		res=res + m;
		p=p->next;
	}
	
	printf(" result = %d",res);
}

int main()
{
	int y=1,k;
	
	while(y)
	{
		printf(" press 1 for insert \n");
		printf(" press 2 for display \n");
		printf(" press 3 for sorting  \n");
		printf(" press 4 for exit \n");
		printf(" press 5 for compute value \n");

		
		scanf("%d",&k);
		switch(k)
		{
			case 1:
				insert();
				break;
			
			case 2:
				display();
				break;
            
            case 3:
				sort();
				break;

            case 4:
            	y=0; 
				break;
				
			case 5:
           	compute(); 
			break;
            
            default:
            	break;
            	
		}
	}
	return 0;
}
