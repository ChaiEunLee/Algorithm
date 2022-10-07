#include <iostream>

int main(){
    double A,B;
    std::cin >> A >> B;

    std::cout.precision(12); //출력할 실수 전체 자리수를 n자리로 고정.(소수점 위, 아래 전체)
    std::cout << std::fixed; //precision으로 넘겨준 값만큼 소수점 아래로 지정.
// std::cout.unset(ios::fixed) //참고) 고정 소수점 표기 해제
    if (A>0 and B<10){
    std::cout << A/B;
    }
}