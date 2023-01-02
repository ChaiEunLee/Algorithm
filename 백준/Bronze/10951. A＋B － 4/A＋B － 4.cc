#include <iostream>

int main(){
    int A, B;

    while(!(std::cin>>A>>B).eof()){
        std::cout << A+B << '\n';
    }
    
}