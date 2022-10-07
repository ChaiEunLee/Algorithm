#include <iostream>

int main(){
    int inputScore;
    char score;
    std::cin >> inputScore;

    if (inputScore >= 90){        score = 'A';    }
    else if (inputScore >= 80)    {        score = 'B';    }
    else if (inputScore >= 70)    {        score = 'C';    }
    else if (inputScore >= 60)    {        score = 'D';    }
    else {        score = 'F';    }
    
    std::cout << score;
}
