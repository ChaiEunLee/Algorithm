#include <stdio.h>
//int argc, char const* argv[]
int main(){
    double A,B;

    scanf("%lf %lf", &A, &B); //lf는 소수점 6자리까지 출력. 이걸 늘려줘야함

    printf("%.13lf", A/B);
    return 0;
}


