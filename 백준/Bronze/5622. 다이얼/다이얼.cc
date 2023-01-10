#include <iostream>
using namespace std;

string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int number[27];

int main(){
    string input;
    cin >> input;

    int dial=2; //2초에서 시작

    for (int i=1;i<=26;i++){
        if((i<19)&&((i-1)%3 == 0)){
            dial++;
        } else if ((i>19)&&((i%10)==0)){ //19번째(S)는 그대로
            dial++;
        } else if ((i>22)&&((i%10)==3)) {
            dial++;
        }
        number[i-1] = dial;
//        cout << number[i-1] << ' ';
//        cout << alphabet[i-1] << '\n';

    }

    int index, timesum=0;
    for(int j=0; j<input.size();j++){
        index = alphabet.find(input[j]);
        timesum += number[index];
    }
    cout << timesum;
}