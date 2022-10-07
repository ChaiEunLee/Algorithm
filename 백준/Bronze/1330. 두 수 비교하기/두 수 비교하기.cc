#include <iostream>

int main(){
    int A,B;
    std::cin >> A >> B;
    
    if (A < B){ 
       std::cout << '<'; //한글자는 char도 가능
    }
    else if (A>B)
    {
        std::cout << ">"; //한글자는 string도 가능
    }
    else {
        std::cout << "=="; //string은 ""
    }
    return 0;
}
