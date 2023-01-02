#include <iostream> 

int main(){
    int N;
    std::cin >> N;

    for(int i=1; i<N+1;i++){
        std::cout << std::string(N-i,' ') << std::string(i,'*') <<'\n';
    }
}