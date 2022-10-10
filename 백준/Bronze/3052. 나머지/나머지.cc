#include <iostream>
using namespace std;
#include <set>

int main(){
    set<int> s;
    int newNum;

    for (int i=0;i<10;i++){
        cin >> newNum;
        s.insert(newNum%42);
    }
    cout << s.size();
}

