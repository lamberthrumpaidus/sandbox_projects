#include <wiringPi.h>

int main() {
    wiringPiSetup();  // Inisialisasi library wiringPi
    pinMode(0, OUTPUT);  // Set pin 0 sebagai output

    while(1) {
        digitalWrite(0, HIGH);  // Nyalakan LED
        delay(1000);  // Tunggu 1 detik
        digitalWrite(0, LOW);  // Matikan LED
        delay(1000);  // Tunggu 1 detik
    }

    return 0;
}
