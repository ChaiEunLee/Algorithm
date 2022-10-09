#include <iostream>
using namespace std;

int main(){
    int A,B;
    A = 1;
    B = 1;
    while(1){
        cin >> A >> B;
        if(A==0 && B==0){
        break;
        }
        cout << A+B << '\n';
    }
}
