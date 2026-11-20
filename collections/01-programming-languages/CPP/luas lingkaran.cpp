#include <iostream>
#define PI 3.14159

int main() {
    float radius;
    std::cout << "Masukkan jari-jari lingkaran: ";
    std::cin >> radius;
    std::cout << "Luas lingkaran: " << PI * radius * radius << std::endl;
    return 0;
}
