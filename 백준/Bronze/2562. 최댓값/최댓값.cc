#include <iostream>
using namespace std;

int main(){
    int newNum;
    int maxVal = 0;
    int order = 0;
    int myArray[9];

    for(int i=0;i<9;i++){
        cin >> newNum;
        myArray[i] = newNum;
        if (newNum > maxVal){
            maxVal = newNum;
        }
   }
   for(int i=0;i<9;i++){
    if(myArray[i]==maxVal){
        cout << maxVal << '\n' << i+1;
    }
   }
}
