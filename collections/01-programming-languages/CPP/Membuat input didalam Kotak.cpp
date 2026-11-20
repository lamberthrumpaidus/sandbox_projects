#include <iostream>
#include <string>

using namespace std;

int main() {
    string inputText;

    cout << "Masukkan teks yang ingin dimasukkan: ";
    getline(cin, inputText);


    int maxWidth = inputText.length() + 4;
    int maxHeight = 3;

    // Karakter persegi panjang
    char topLeft = char(218);      // Sudut kiri atas
    char topRight = char(191);     // Sudut kanan atas
    char bottomLeft = char(192);   // Sudut kiri bawah
    char bottomRight = char(217);  // Sudut kanan bawah
    char horizontal = char(196);   // Garis horizontal
    char vertical = char(179);     // Garis vertikal

    cout << endl;

    for (int i = 0; i < maxHeight; i++) {
        for (int j = 0; j < maxWidth; j++) {
            if (i == 0 && j == 0) {
                cout << topLeft;
            }
            else if (i == 0 && j == maxWidth - 1) {
                cout << topRight;
            }
            else if (i == maxHeight - 1 && j == 0) {
                cout << bottomLeft;
            }
            else if (i == maxHeight - 1 && j == maxWidth - 1) {
                cout << bottomRight;
            }
            else if (i == 0 || i == maxHeight - 1) {
                cout << horizontal;
            }
            else if (j == 0 || j == maxWidth - 1) {
                cout << vertical;
            }
            else if (i == maxHeight / 2 && j == 2) {
                cout << inputText;
                j += inputText.length() - 1;
            }
            else {
                cout << ' ';
            }
        }
        cout << endl;
    }

    return 0;
}