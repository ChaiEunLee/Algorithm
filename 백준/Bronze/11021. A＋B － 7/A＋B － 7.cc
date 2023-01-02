#include <iostream>

int main(){
    int T, A, B;
    std::cin >> T;

    for(int i=1; i<T+1; i++){
        std::cin >> A >> B;
        std::cout << "Case #" << i << ": " << A+B << '\n';
    }

}