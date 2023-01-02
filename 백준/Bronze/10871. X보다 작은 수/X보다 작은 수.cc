#include <iostream>
#include <sstream> //stringstream
using namespace std;

int main(){
    int N,X;
    cin >> N >> X;
    cin.ignore();
    int intList[N]; //array 생성
    
    string str;
    getline(cin, str);
    stringstream ss(str);

    string stringBuffer;
    while(getline(ss, stringBuffer,' ')){
        if (X > stoi(stringBuffer)){
            cout<<stringBuffer<<' ';
        }
    }
}