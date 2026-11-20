#include <iostream>
using namespace std;

char board[3][3] = { {'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'} };
char currentPlayer = 'X';

void DrawBoard()
{
    cout << "-------------" << endl;
    for (int i = 0; i < 3; i++)
    {
        cout << "| ";
        for (int j = 0; j < 3; j++)
        {
            cout << board[i][j] << " | ";
        }
        cout << endl;
        cout << "-------------" << endl;
    }
}

void SwitchPlayer()
{
    if (currentPlayer == 'X')
    {
        currentPlayer = 'O';
    }
    else
    {
        currentPlayer = 'X';
    }
}

bool CheckWin()
{
    for (int i = 0; i < 3; i++)
    {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2])
        {
            return true;
        }
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i])
        {
            return true;
        }
    }
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2])
    {
        return true;
    }
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0])
    {
        return true;
    }
    return false;
}

bool CheckDraw()
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] != 'X' && board[i][j] != 'O')
            {
                return false;
            }
        }
    }
    return true;
}

void UpdateGame(int cell)
{
    int row = (cell - 1) / 3;
    int col = (cell - 1) % 3;
    if (board[row][col] != 'X' && board[row][col] != 'O')
    {
        board[row][col] = currentPlayer;
        if (CheckWin())
        {
            cout << "Player " << currentPlayer << " wins!" << endl;
            exit(0);
        }
        if (CheckDraw())
        {
            cout << "Draw!" << endl;
            exit(0);
        }
        SwitchPlayer();
    }
    else
    {
        cout << "Cell already occupied. Try again." << endl;
    }
}

int main()
{
    int cell;
    DrawBoard();
    while (true)
    {
        cout << "Player " << currentPlayer << ", enter a cell number: ";
        cin >> cell;
        UpdateGame(cell);
        DrawBoard();
    }
    return 0;
}