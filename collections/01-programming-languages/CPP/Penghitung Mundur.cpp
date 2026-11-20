#include <iostream>
#include <chrono>
#include <thread>


using namespace std;

int main() {

    int seconds;
    cout << "Masukkan jumlah detik: ";
    cin >> seconds;
    for (int i = seconds; i >= 0; i--) 
    {
        cout << "Sisa waktu: " << i << " detik" << endl;
        this_thread::sleep_for(chrono::seconds(1));
    }

    cout << "Waktu habis!" << endl;

    return 0;
}
