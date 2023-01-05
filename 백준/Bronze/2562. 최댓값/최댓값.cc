#include <iostream>
using namespace std;

int main(){
    int input;
    int intmax=0;
    int intmaxid;

    for (int i=0; i < 9; i++){
        cin >> input;
        if (intmax < input){
            intmax = input;
            intmaxid = i+1;
        }
    }
    cout << intmax << '\n' << intmaxid;
}
