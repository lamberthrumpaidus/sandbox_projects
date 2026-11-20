#include <iostream>
using namespace std;

int main() {
    int n, i;
    unsigned long long faktorial = 1;

    cout << "Masukkan bilangan bulat positif: ";
    cin >> n;

    for (i = 1; i <= n; ++i) {
        faktorial *= i;
    }

    cout << "Faktorial dari " << n << " = " << faktorial;
    return 0;
}