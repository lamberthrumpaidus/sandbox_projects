#include <iostream>
using namespace std;

int main() {
    float bil1, bil2, hasil;
    char operasi;

    cout << "Masukkan bilangan pertama: ";
    cin >> bil1;

    cout << "Masukkan bilangan kedua: ";
    cin >> bil2;

    cout << "Masukkan operator (+, -, *, /): ";
    cin >> operasi;

    switch (operasi) {
    case '+':
        hasil = bil1 + bil2;
        break;
    case '-':
        hasil = bil1 - bil2;
        break;
    case '*':
        hasil = bil1 * bil2;
        break;
    case '/':
        hasil = bil1 / bil2;
        break;
    default:
        cout << "Operator yang dimasukkan tidak valid.";
        return 0;
    }

    cout << "Hasil: " << bil1 << " " << operasi << " " << bil2 << " = " << hasil;
    return 0;
}