#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    float scoresum =0;
    int scoreMax = 0;
    float scoreList[N];

    for (int i=0; i<N; i++){
        cin >> scoreList[i];
        if (scoreMax < scoreList[i]){
            scoreMax = scoreList[i];
        }
        scoresum += scoreList[i];
    }
    cout << scoresum*100/(N*scoreMax);
}