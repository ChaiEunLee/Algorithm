#include <iostream>

int main(){
    int x,y,quadrant;
    std::cin >> x;
    std::cin >> y;

    if (x>0 && y>0){
        quadrant = 1;
    }
    else if(x>0 && y<0){
        quadrant = 4;
    }
    else if(x<0 && y>0){
        quadrant = 2;
    }
    else if(x<0 && y<0){
        quadrant = 3;
    }
    std::cout << quadrant;
}