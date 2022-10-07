#include <iostream>

int main(){
    int H, M;
    std::cin >> H >> M;

    if (M-45 >=0){
        M = M-45;
    }
    else if (H==0){
        H = 23;
        M = M-45+60;
    }
    else{
        H = H-1;
        M = M-45+60;
    }
    std::cout << H << ' ' << M;
}
