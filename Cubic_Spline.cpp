#include <iostream>
#include <math.h>

using namespace std;
//solve for n-2 dervatives
//function to solve the trigonal matrix by thomas algorithm
//a-->first column
//b-->second column
//c-->third column
//d-->right hand side of the matrix
//n-->number of elements
void solve(double* a, double* b, double* c, double* d, int n) {
n--; // since we start from x0 (not x1)
    c[0] /= b[0];
    d[0] /= b[0];

    for (int i = 1; i < n; i++) {
        c[i] /= b[i] - a[i]*c[i-1];
        d[i] = (d[i] - a[i]*d[i-1]) / (b[i] - a[i]*c[i-1]);
    }

    d[n] = (d[n] - a[n]*d[n-1]) / (b[n] - a[n]*c[n-1]);

    for (int i = n; i-- > 0;) {
        d[i] -= c[i]*d[i+1];
    }
}
int main(){
    int n=11;
    double a[11];
    double b[11];
    double c[11];
    double x[11]={250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750};
    double y[11]={1.003, 1.005, 1.008 ,1.013,1.020, 1.029, 1.040 ,1.051 ,1.063 ,1.075, 1.087};
    // double x[16]={0.002,0.33,1.7,3.8,5.5,7,8.9,10.4,12,14.6,16,18.4,20,21.2,21.6,22};
    // double y[16]={998.64,928.96,859.58,802.83,767.52,739.72,706.85,681.77,655.18,610.18,584.99,534.13,490.19,443.83,418.75,369.77};
    double d[11];
    double z[11];
    double xx;
    //cout<<"Enter the value of x where you want to calculate:"<<endl;
    // cin>>xx;
    xx=273;// value of xx at which we want to find y
    //generate coefficients for trigonal matrix
     for(int i=1;i<n-1;i++){
        if(i==1){
            a[i-1]=0;
        }
        else{
            a[i-1]=x[i]-x[i-1];
        }
    }
    for(int i=1;i<n-1;i++){
         b[i-1]=2*(x[i+1]-x[i-1]);
    }
    for(int i=1;i<n-1;i++){
        if(i==n-2){
            c[i-1]=0;
        }
        else{
            c[i-1]=x[i+1]-x[i];
        }
    }
    for(int i=1;i<n-1;i++){
        d[i-1]=6*(((y[i+1]-y[i])/(x[i+1]-x[i]))+((y[i-1]-y[i])/(x[i]-x[i-1])));
    }
    solve(a,b,c,d,n-2);//calling the function to solve the matrix
    for (int i = 1; i < n-1; i++) {
		z[i]=d[i-1];
        z[0]=0;
        z[n-1]=0;
	}
    int ii=0;
    int f=0;
    //to find the interval where xx is lying
    for(int i=0;i<n;i++){
        if(xx<=x[i]){
            ii=i;
            f=1;
        }
        if(f==1){
            break;
        }
    }
    //generating the terms to calculate the value of y
    double term11=z[ii-1]*pow((x[ii]-xx),3);
    double term12=6*(x[ii]-x[ii-1]);
    double term1= term11/term12;

    double term21= z[ii]*pow((xx-x[ii-1]),3);
    double term22= 6*(x[ii]-x[ii-1]);
    double term2= term21/term22;

    double term31= y[ii-1]/(x[ii]-x[ii-1]);
    double term32= z[ii-1]*((x[ii]-x[ii-1])/6);
    double term3= (term31-term32)*(x[ii]-xx);

    double term41= y[ii]/(x[ii]-x[ii-1]);
    double term42= z[ii]*((x[ii]-x[ii-1])/6);
    double term4=(term41-term42)*(xx-x[ii-1]);

    double result = term1+term2+term3+term4;
    cout<<"The corresponding value of y is: "<<result<<endl;
    return 0;
}