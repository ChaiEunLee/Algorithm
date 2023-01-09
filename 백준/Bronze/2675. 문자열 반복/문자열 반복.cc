#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    for (int j=0; j<N; j++){
        int num;
        cin >> num;
        string input;
        cin >> input;

        for(int i=0; i<input.size(); i++){
            cout << string(num, input[i]);
        }
        cout << '\n';
    }
}
