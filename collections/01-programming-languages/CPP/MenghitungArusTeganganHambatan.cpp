#include <iostream>
#include <string>

using namespace std;

int main() {
    int pilihan;
    char pilih;
    double V, I, R;

    atas:
    atas2:
    system("cls");
    cout << "===================================================================================================" << endl;
    cout << "Program Menghitung Tegangan (V), Arus (I), dan Hambatan (R) (Hukum Ohm) by LamberhPaulinusRumpaidus" << endl;
    cout << "===================================================================================================" << endl;
    cout << "Pilih yang ingin dihitung:" << endl;
    cout << "1. Tegangan (V)" << endl;
    cout << "2. Arus (I)" << endl;
    cout << "3. Hambatan (R)" << endl;
    cout << "Silakan masukkan pilihan (1/2/3): ";
    cin >> pilihan;

    if (pilihan == 1) {
        cout << "Masukkan Nilai Arus (I) dalam Ampere (A): ";
        cin >> I;
        cout << "Masukkan Nilai Hambatan (R) dalam Ohm (Ω): ";
        cin >> R;
        V = I * R;
        cout << "Tegangan (V) = " << V << " Volt (V)" << endl;
    }
    else if (pilihan == 2) {
        cout << "Masukkan Nilai Tegangan (V) dalam Volt (V): ";
        cin >> V;
        cout << "Masukkan Nilai Hambatan (R) dalam Ohm (Ω): ";
        cin >> R;
        I = V / R;
        cout << "Arus (I) = " << I << " Ampere (A)" << endl;
    }
    else if (pilihan == 3) {
        cout << "Masukkan Nilai Tegangan (V) dalam Volt (V): ";
        cin >> V;
        cout << "Masukkan Nilai Arus (I) dalam Ampere (A): ";
        cin >> I;
        R = V / I;
        cout << "Hambatan (R) = " << R << " Ohm (Ω)" << endl;
    }
    else {
        cout << "Pilihan tidak valid." << endl;
        goto atas;
    }
    pilih:
    cout << "======================================================" << endl;
    cout << "Apakah Anda masih ingin menggunakan program? (Y/N): ";
    cin >> pilih;
    if (pilih == 'Y' || pilih == 'y') 
    {
        system("cls");
        goto atas;
    }
    else if (pilih == 'N' || pilih == 'n') 
    {
        cout << "Terima Kasih Telah Menggunakan Program" << endl;
        return 0;
    }
    else
    {
        system("cls");
        cout << "Silakan Input yang benar" << endl;
        goto pilih;
    }
}
