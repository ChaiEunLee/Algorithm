#include <iostream>
#include <math.h> //round
using namespace std;

int main(){
    int C;
    cin >> C;

    for (int c=0;c<C;c++){
        int N;
        cin >> N;
        int scorelist[N];
        int score;
        float totscore=0;
        for (int i=0; i<N;i++){
            cin >> score;
            scorelist[i] = score;
            totscore += score;
        }
        float scoreavg = totscore/N;

        float above=0;
        for (int j=0; j<N; j++){
            if(scorelist[j] > scoreavg){
                above++;
            }
        }

        cout << fixed; // 소수점 
        cout.precision(3); //3자리 까지
        cout << round(above*100000/N)/1000 << '%' << '\n';

//        printf("%.3f", round(above*100000/N)/1000);
    }

}