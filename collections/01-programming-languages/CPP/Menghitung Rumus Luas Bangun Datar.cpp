#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
    int pilihan;
    double Luas;
    string Pilih;

    atas:
    atas2:
    system("cls");
    cout << "====================================================================" << endl;
    cout << "  Program Menghitung Luas Bangun Datar by LamberthPaulinusRumpaidus" << endl;
    cout << "====================================================================" << endl;
    cout << "Pilih bangun datar yang ingin dihitung luasnya:" << endl;
    cout << "1. Persegi" << endl;
    cout << "2. Persegi Panjang" << endl;
    cout << "3. Segitiga" << endl;
    cout << "4. Trapesium" << endl;
    cout << "5. Jajar Genjang" << endl;
    cout << "6. Belah Ketupat" << endl;
    cout << "7. Layang Layang" << endl;
    cout << "8. Lingkaran" << endl;
    cout << "Silakan masukkan pilihan (1-8): ";
    cin >> pilihan;

    if (pilihan == 1) {
        double Sisi;
        cout << "Masukkan Panjang Sisi: ";
        cin >> Sisi;
        Luas = Sisi * Sisi;
    }
    else if (pilihan == 2) {
        double Panjang, Lebar;
        cout << "Masukkan Panjang: ";
        cin >> Panjang;
        cout << "Masukkan Lebar: ";
        cin >> Lebar;
        Luas = Panjang * Lebar;
    }
    else if (pilihan == 3) {
        double Alas, Tinggi;
        cout << "Masukkan Alas: ";
        cin >> Alas;
        cout << "Masukkan Tinggi: ";
        cin >> Tinggi;
        Luas = 0.5 * Alas * Tinggi;
    }
    else if (pilihan == 4) {
        double SisiAtas, SisiBawah, Tinggi;
        cout << "Masukkan Panjang Sisi Atas: ";
        cin >> SisiAtas;
        cout << "Masukkan Panjang Sisi Bawah: ";
        cin >> SisiBawah;
        cout << "Masukkan Tinggi: ";
        cin >> Tinggi;
        Luas = 0.5 * (SisiAtas + SisiBawah) * Tinggi;
    }
    else if (pilihan == 5) {
        double Alas, Tinggi;
        cout << "Masukkan Alas: ";
        cin >> Alas;
        cout << "Masukkan Tinggi: ";
        cin >> Tinggi;
        Luas = Alas * Tinggi;
    }
    else if (pilihan == 6) {
        double Diagonal1, Diagonal2;
        cout << "Masukkan Panjang Diagonal 1: ";
        cin >> Diagonal1;
        cout << "Masukkan Panjang Diagonal 2: ";
        cin >> Diagonal2;
        Luas = 0.5 * Diagonal1 * Diagonal2;
    }
    else if (pilihan == 7) {
        double Diagonal1, Diagonal2;
        cout << "Masukkan Panjang Diagonal 1: ";
        cin >> Diagonal1;
        cout << "Masukkan Panjang Diagonal 2: ";
        cin >> Diagonal2;
        Luas = 0.5 * Diagonal1 * Diagonal2;
    }
    else if (pilihan == 8) {
        double JariJari;
        cout << "Masukkan Jari-Jari Lingkaran: ";
        cin >> JariJari;
        Luas = 3.14159265359 * pow(JariJari, 2);
    }
    else {
        cout << "Pilihan tidak valid." << endl;
        goto atas2;
    }

    cout << "Luas adalah: " << Luas << endl;

    pilih:
    cout << "Apakah Anda masih ingin menggunakan program? (Y/N): ";
    cin >> Pilih;
    if (Pilih == "Y" || Pilih == "y") {
        goto atas;
    }
    else if (Pilih == "N" || Pilih == "n") {
        cout << "Terima Kasih Telah Menggunakan Program" << endl;
        return 0;
    }
    else {
        system("cls");
        cout << "Silakan Input yang benar" << endl;
        goto pilih;
    }
}
