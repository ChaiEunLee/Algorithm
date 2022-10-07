#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false); //이걸 쓰면 속도는 올라가지만 다른 입출력 못 씀.

    int T, A, B;
    cin >> T;
    for (int i=0;i<T;i++){
        cin >> A >> B;          
        cout << A+B << '\n';
    }
    
}