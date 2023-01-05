#include <iostream>
using namespace std;

int main(){
    bool hwlist[31]={false};
    int index;

    for(int i=0;i<28;i++){
        cin >> index;
        hwlist[index] = true;
    }

    for (int j=1; j<31; j++){
        if(hwlist[j]==0){
            cout << j << '\n';
        }
    }

}
