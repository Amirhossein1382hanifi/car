#ifndef CARGAME_HPP
#define CARGAME_HPP

#include <iostream>
#include <windows.h>

#define SCREEN_WIDTH 90
#define SCREEN_HEIGHT 26
#define WIN_WIDTH 70
class CarGame {
private:
    HANDLE console;
    COORD CursorPosition;

    int enemyY[3];
    int enemyX[3];
    int enemyFlag[3];
    char car[4][4] = { ' ','*','*',' ',
                      '*','*','*','*',
                      ' ','*','*',' ',
                      '*','*','*','*' };

    int carPos;
    int score;

public:
    CarGame();

    void gotoxy(int x, int y);

    void setcursor(bool visible, DWORD size);

    void drawBorder();

    void genEnemy(int ind);

    void drawEnemy(int ind);

    void eraseEnemy(int ind);

    void resetEnemy(int ind);

    void drawCar();

    void eraseCar();

    int collision();

    void gameover();

    void updateScore();

    void instructions();

    void play();

    void menu();
};


#endif // CARGAME_HPP