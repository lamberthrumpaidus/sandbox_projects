#include <iostream>
using namespace std;

int main() {
    float input, output;
    int choice;

    cout << "Pilih satuan suhu yang ingin dikonversi: " << endl;
    cout << "1. Celsius" << endl;
    cout << "2. Fahrenheit" << endl;
    cout << "3. Kelvin" << endl;
    cout << "4. Reamur" << endl;
    cout << "Masukan input : ";
    cin >> choice;

    cout << "Masukkan suhu dalam satuan yang dipilih: ";
    cin >> input;

    switch (choice) {
    case 1:
        output = (input * 9.0 / 5.0) + 32;
        cout << input << " derajat Celsius sama dengan " << output << " derajat Fahrenheit." << endl;
        output = input + 273.15;
        cout << input << " derajat Celsius sama dengan " << output << " derajat Kelvin." << endl;
        output = input * 4.0 / 5.0;
        cout << input << " derajat Celsius sama dengan " << output << " derajat Reamur." << endl;
        break;
    case 2:
        output = (input - 32) * 5.0 / 9.0;
        cout << input << " derajat Fahrenheit sama dengan " << output << " derajat Celsius." << endl;
        output = (input - 32) * 5.0 / 9.0 + 273.15;
        cout << input << " derajat Fahrenheit sama dengan " << output << " derajat Kelvin." << endl;
        output = (input - 32) * 4.0 / 9.0;
        cout << input << " derajat Fahrenheit sama dengan " << output << " derajat Reamur." << endl;
        break;
    case 3:
        output = input - 273.15;
        cout << input << " derajat Kelvin sama dengan " << output << " derajat Celsius." << endl;
        output = (input - 273.15) * 9.0 / 5.0 + 32;
        cout << input << " derajat Kelvin sama dengan " << output << " derajat Fahrenheit." << endl;
        output = (input - 273.15) * 4.0 / 5.0;
        cout << input << " derajat Kelvin sama dengan " << output << " derajat Reamur." << endl;
        break;
    case 4:
        output = input * 5.0 / 4.0;
        cout << input << " derajat Reamur sama dengan " << output << " derajat Celsius." << endl;
        output = input * 9 / 4 + 32;
        cout << input << " derajat Reamur sama dengan " << output << " derajat Fahrenheit." << endl;
        output = input + 273 / 16 * 5;
        cout << input << " derajat Reamur sama dengan " << output << " derajat Kelvin." << endl;
        break;
    default:
        cout << "Pilihan tidak valid" << endl;
    }

    return 0;
}
