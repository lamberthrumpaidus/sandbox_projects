#include<iostream>
#include<vector>
using namespace std;
//Credit by LamberthRumpaidus
struct Transaksi {
    string jenis;
    int nominal;
};

int main() {
    int pin = 23115826, pilihan, saldo = 1000000, nominal;
    vector<Transaksi> mutasi;
    cout << "Masukkan PIN: ";
    cin >> pin;
    if (pin == 1234) {
        do {
            cout << "1. Cek Saldo\n";
            cout << "2. Tarik Tunai\n";
            cout << "3. Transfer\n";
            cout << "4. Deposit\n";
            cout << "5. Cek Mutasit\n";
            cout << "6. Ganti PIN\n";
            cout << "7. Keluar\n";
            cout << "Pilih Menu: ";
            cin >> pilihan;
            switch (pilihan) {
            case 1:
                system("cls");
                cout << "Saldo Anda: Rp" << saldo << "\n";
                break;
            case 2:
                system("cls");
                cout << "Masukkan Nominal: ";
                cin >> nominal;
                if (nominal <= saldo) {
                    saldo -= nominal;
                    cout << "Penarikan Berhasil\n";
                    mutasi.push_back({ "Tarik Tunai", nominal });
                }
                else {
                    cout << "Saldo Tidak Cukup\n";
                }
                break;
            case 3:
                system("cls");
                cout << "Masukkan Nominal Transfer: ";
                cin >> nominal;
                if (nominal <= saldo) {
                    saldo -= nominal;
                    cout << "Transfer Berhasil\n";
                    mutasi.push_back({ "Transfer", nominal });
                }
                else {
                    cout << "Saldo Tidak Cukup\n";
                }
                break;
            case 4:
                system("cls");
                cout << "Masukkan Nominal Deposit: ";
                cin >> nominal;
                saldo += nominal;
                cout << "Deposit Berhasil\n";
                mutasi.push_back({ "Deposit", nominal });
                break;
            case 5:
                system("cls");
                for (int i = 0; i < mutasi.size(); i++) {
                    cout << mutasi[i].jenis << ": Rp" << mutasi[i].nominal << "\n";
                }
                break;
            case 6:
                system("cls");
                int pinBaru, konfirmasiPinBaru;
                cout << "Masukkan PIN Baru: ";
                cin >> pinBaru;
                cout << "Konfirmasi PIN Baru: ";
                cin >> konfirmasiPinBaru;
                if (pinBaru == konfirmasiPinBaru) {
                    pin = pinBaru;
                    cout << "PIN Berhasil Diganti\n";
                }
                else {
                    system("cls");
                    cout << "PIN Tidak Cocok\n";
                }
                break;
            case 7:
                system("cls");
                cout << "Terima Kasih\n";
                break;
            default:
                cout << "Pilihan Tidak Tersedia\n";
            }
        } while (pilihan != 7);
    }
    else {
        cout << "PIN Salah\n";
    }
    return 0;
}
