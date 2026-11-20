#include <iostream>
#include <cstdlib>  // Untuk rand() dan srand()
#include <ctime>    // Untuk time()

int main() {
    // Inisialisasi random seed
    srand(static_cast<unsigned int>(time(0)));
    
    // Komputer memilih angka acak antara 1 dan 100
    int angkaRahasia = rand() % 100 + 1;
    int tebakan;
    int jumlahTebakan = 0;

    std::cout << "Selamat datang di permainan tebak angka!" << std::endl;
    std::cout << "Saya telah memilih sebuah angka antara 1 dan 100." << std::endl;
    std::cout << "Coba tebak angka tersebut: ";

    do {
        std::cin >> tebakan;
        jumlahTebakan++;

        if (tebakan > angkaRahasia) {
            std::cout << "Tebakan Anda terlalu tinggi. Coba lagi: ";
        } else if (tebakan < angkaRahasia) {
            std::cout << "Tebakan Anda terlalu rendah. Coba lagi: ";
        } else {
            std::cout << "Selamat! Anda telah menebak angka yang benar: " << angkaRahasia << std::endl;
            std::cout << "Jumlah tebakan Anda: " << jumlahTebakan << std::endl;
        }
    } while (tebakan != angkaRahasia);

    return 0;
}
#include <iostream>
#include <cstdlib>  // Untuk rand() dan srand()
#include <ctime>    // Untuk time()

int main() {
    // Inisialisasi random seed
    srand(static_cast<unsigned int>(time(0)));
    
    // Komputer memilih angka acak antara 1 dan 100
    int angkaRahasia = rand() % 100 + 1;
    int tebakan;
    int jumlahTebakan = 0;

    std::cout << "Selamat datang di permainan tebak angka!" << std::endl;
    std::cout << "Saya telah memilih sebuah angka antara 1 dan 100." << std::endl;
    std::cout << "Coba tebak angka tersebut: ";

    do {
        std::cin >> tebakan;
        jumlahTebakan++;

        if (tebakan > angkaRahasia) {
            std::cout << "Tebakan Anda terlalu tinggi. Coba lagi: ";
        } else if (tebakan < angkaRahasia) {
            std::cout << "Tebakan Anda terlalu rendah. Coba lagi: ";
        } else {
            std::cout << "Selamat! Anda telah menebak angka yang benar: " << angkaRahasia << std::endl;
            std::cout << "Jumlah tebakan Anda: " << jumlahTebakan << std::endl;
        }
    } while (tebakan != angkaRahasia);

    return 0;
}
