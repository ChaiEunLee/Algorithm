#include <iostream>
using namespace std;

int alpha[26], cnt = 0;
string input;

int main(){
    cin >> input;

    for (int i=0; i<input.length(); i++){
        if(input[i]<97) { //대문자면
            alpha[input[i] - 65]++; //65만 빼고
        } else {alpha[input[i] - 97]++;} //소문자면 97 다 빼기
    }
    int max=0, max_index=0;

    for (int j=0;j<26;j++){
        if(alpha[j] > max){
            max = alpha[j];
            max_index = j;
        }
    }

    for (int k=0;k<26;k++){
        if(alpha[k]==max){
            cnt++;
        }
    }
    if (cnt >=2){
        cout << "?";
    } else {cout << (char)(max_index+65);}
}

