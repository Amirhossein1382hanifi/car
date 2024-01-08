#include "carGame.hpp"
#include <iostream>
#include <fstream>

int main() {
    CarGame carGame;
    carGame.menu();
    // std::fstream myfile("score.dat", ios::out | ios::binary);
    // myfile.open();
    // myfile(reinterpret_cast<char *>(&carGame));

    return 0;
}

