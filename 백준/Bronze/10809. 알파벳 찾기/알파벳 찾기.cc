#include <iostream>
using namespace std;

int main(){
    string input, alphabet;
    cin >> input;
    alphabet = "abcdefghijklmnopqrstuvwxyz";
    int index;

    for (int i=0; i<alphabet.size();i++){    
        index = input.find(alphabet[i]);
        cout << index << ' ';
    }
}
