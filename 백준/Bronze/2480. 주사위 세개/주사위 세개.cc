#include <iostream>

int main(){
    int A,B,C;
    std::cin >> A >> B >> C;
    int money;
    if (A==B && B==C){
        money = 10000 + A*1000;
    }
    else if (A==B || B==C){
        money = 1000 + B*100;
    }
    else if (A==C){
        money = 1000 + A*100;
    }
    else{
        money = 100 * std::max(std::max(A,B),C);
        }
    std::cout << money;
}