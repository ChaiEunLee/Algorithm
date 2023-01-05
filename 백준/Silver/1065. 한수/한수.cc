#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;

    int totsum =0;
// 100 이하는 다 한수.
    if (N < 100){
        totsum = N;
    } else {
        for(int i=100; i<N+1; i++){
            int hunds, tens, units;
            hunds = i/100;
            tens = (i/10)%10;
            units = i%10;
            if((hunds-tens)==(tens-units)){
                totsum++;
            }
        }
        totsum += 99;
    }
    cout << totsum;
}