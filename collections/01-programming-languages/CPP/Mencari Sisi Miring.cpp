#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a, b, c;
    cout << "Masukkan panjang sisi tegak: ";
    cin >> a;
    cout << "Masukkan panjang sisi mendatar: ";
    cin >> b;
    c = sqrt(pow(a, 2) + pow(b, 2));
    cout << "Panjang sisi miring adalah: " << c << endl;
    return 0;
}
