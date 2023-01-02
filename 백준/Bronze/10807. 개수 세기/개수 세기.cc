#include <iostream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;

int main(){
    int N;
    cin >> N;
    cin.ignore();//cin에서 \n을 남겨두고있다가 getline에서 처리해버리면서 종료돼서 ignore() 추가
    int inputList[N];
    
    string str;
    getline(cin,str); 

    stringstream ss(str);
    string stringBuffer;
    int i=0;
    while(getline(ss, stringBuffer,' ')){
        inputList[i] = stoi(stringBuffer);
        i++;
    }

    int v;
    cin >> v;

    int count=0;
    for(int i=0; i<N; i++){
        if (inputList[i]==v){
            count ++;
        }
    }
    cout << count;
}