#include <iostream>

int main(){
    int H, M, time, newM, newH;
    std::cin >> H >> M;
    std::cin >> time;
    
    newM = (M+time)%60;
    newH = H + (M+time)/60; //int라서 이렇게만해도 될듯.

    if (newH >= 24){
        newH = newH - 24;
    }

    std::cout << newH << ' ' << newM;
}
