#include <iostream>
#include <cmath>

int main() {
    double base, exponent;
    std::cout << "Masukkan basis dan eksponen: ";
    std::cin >> base >> exponent;
    std::cout << base << " pangkat " << exponent << " adalah " << pow(base, exponent) << std::endl;
    return 0;
}
