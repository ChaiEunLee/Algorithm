#include <iostream>
using namespace std;

int hansoo(int n){
    int hunds, tens, units;
    if (n<100){
        return 1;
    } else {
        hunds = n/100;
        tens = (n/10)%10;
        units = n%10;
        if((hunds-tens)==(tens-units)){
            return 1;
        } else { return 0; }
    }
}

int main(){
    int N;
    cin >> N;
    int totsum = 0;

    for (int i=1; i<=N; i++){
        totsum += hansoo(i);
    }
    cout << totsum;
}