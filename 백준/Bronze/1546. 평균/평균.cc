#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    float score[N];
    int maxScore = 0;
    float totalScore = 0;
    for(int i=0;i<N;i++){
        cin >> score[i];
        if (score[i] > maxScore){
            maxScore = score[i];
        }
    }
    for (int i=0;i<N;i++){
        totalScore += score[i]/maxScore*100;
    }
    cout << totalScore/N;
}
