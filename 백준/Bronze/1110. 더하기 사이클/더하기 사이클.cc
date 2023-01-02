#include <iostream>

int main(){
    int N, units, tens, newU, newT,newN=-1,cycle=0;
    std::cin >> N;
    units = N%10;
    tens = N/10;

    while (newN != N){
        cycle += 1;
        newT = units;
        newU = (tens+units)%10;
        newN = newT*10 + newU;

        tens = newT;
        units = newU;
    }
    std::cout << cycle;

}