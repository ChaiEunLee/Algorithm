#include <iostream>

int main(){
    int N;
    std::cin >> N;
    std::string number;
    std::cin >> number;

    int totsum=0;
    for (int i=0; i<number.size(); i++){
        totsum += (int)number[i] - 48;
    }

    std::cout << totsum;
}
