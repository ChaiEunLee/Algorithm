#include <iostream>
using namespace std;

int main(){
    int num1, num2, hunds, tens, units, newnum1, newnum2;
    cin >> num1 >> num2;

    hunds = num1/100;
    tens = (num1/10)%10;
    units = num1%10;

    newnum1 = units*100 + tens*10 + hunds; 

    hunds = num2/100;
    tens = (num2/10)%10;
    units = num2%10;

    newnum2 = units*100 + tens*10 + hunds; 

    if(newnum1>newnum2){
        cout << newnum1;
    } else { cout << newnum2;}

}
