#include <iostream>

int main(){
    int year;
    bool yearYN;
    std::cin >> year;

    if (year%400 == 0){
        yearYN = true;
    }
    else if (year%100 == 0){
        yearYN = false;
    }
    else if (year%4 == 0){
        yearYN = true;
    }
    else{
        yearYN = false;
    }
    std::cout << yearYN;
}
