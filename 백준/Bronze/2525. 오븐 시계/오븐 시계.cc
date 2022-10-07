#include <iostream>

int main(){
    int A, B, C;
    std::cin >> A >> B;
    std::cin >> C;

    if (B+C < 60){
        B = B+C;
    }
    else if (A + ((B+C)/60) < 24){
        A = A + ((B+C)/60);
        B = (B+C)%60;
    }
    else if (A+(B+C)/60 >= 24){
        A = A + ((B+C)/60) -24;
        B = (B+C)%60;
    }
    std::cout << A << ' ' << B;
}

