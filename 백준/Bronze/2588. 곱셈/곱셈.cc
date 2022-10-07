#include <iostream>

int main(){
    int A,B;
    std::cin >> A;
    std::cin >> B;
    std::cout << ((B%10) * A) << '\n' <<  ((B%100)/10) * A << '\n' << (B/100) * A << '\n' << A*B;
}
