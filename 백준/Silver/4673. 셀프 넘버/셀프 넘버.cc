#include <iostream>

bool ifselfnum[20000]={false};

int selfnum(int n){
    int nsum=n;
    while(n != 0){ // 모든 자리수를 다 더할 때까지
        nsum += n%10; //일의 자리
        n = n/10;
    }
    return nsum;
}

int main(){
    int num;
    for (int i=1; i<10001; i++){ //
        num = i;
        while(num<10001){
            num = selfnum(num);
            if ((ifselfnum[num]==false)&&(num<10001)){
                ifselfnum[num]=true;
            }
        }
    }

    for (int j=1; j<10001; j++){
        if (ifselfnum[j]==false){
            std::cout << j << '\n';
        }
    }
}