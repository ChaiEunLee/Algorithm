#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    int number = N; //alias가 아니겠찌? 얕은 copy?
    int count = 0;

    while(true){
    int one = N/10;
    int two = N%10;
    int three = one+two;

    N = (two*10)+(three%10);
    count ++;
    if (number==N){break;}
    }
    cout << count << endl;
}