#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    for(int j=0; j<N; j++){
        string inputstr;
        cin >> inputstr;
        int cumsum=0;
        int totsum=0;

        for (int i=0;i<inputstr.size();i++){
            if(inputstr[i]=='O'){
                cumsum ++;
                totsum += cumsum;
            } else {cumsum = 0;}
        }
    cout << totsum << '\n';
    }
}