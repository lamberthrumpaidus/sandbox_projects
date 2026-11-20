#include <iostream>

int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int num;
    std::cout << "Masukkan angka: ";
    std::cin >> num;
    std::cout << "Fibonacci ke-" << num << " adalah " << fibonacci(num) << std::endl;
    return 0;
}
