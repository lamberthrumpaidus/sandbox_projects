#include <iostream>
#include <conio.h>
#include <windows.h>

using namespace std;

int main() {
    char Musik;

    while (true) {
        Musik = _getch();

        switch (Musik) {
        case '1':
            printf("Do\n");
            Beep(262, 500);
            break;
        case '2':
            printf("re\n");
            Beep(294, 500);
            break;
        case '3':
            printf("mi\n");
            Beep(330, 500);
            break;
        case '4':
            printf("fa\n");
            Beep(349, 500);
            break;
        case '5':
            printf("sol\n");
            Beep(392, 500);
            break;
        case '6':
            printf("la\n");
            Beep(440, 500);
            break;
        case '7':
            printf("si\n");
            Beep(494, 500);
            break;
        case '8': 
            return 0;
        default:
            cout << "Nada tidak valid." << endl;
            break;
        }
    }
}