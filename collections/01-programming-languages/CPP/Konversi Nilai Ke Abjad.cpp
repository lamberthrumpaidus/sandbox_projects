#include <iostream>
using namespace  std;

int main()
{
	int nilai;
	cout << "Silahkan Input Nilai :  ";
	cin >> nilai;

	if (nilai <= 70) 
	{
		cout << "Nilai anda E" << endl;
	}
	else if (nilai > 70 && nilai < 80) {
		cout << "Nilai anda C, Bagus Mi" << endl;
	}
	else if (nilai > 80 && nilai < 90) {
		cout << "Nilai anda B" << endl;
	}
	else if (nilai >= 90 && nilai <= 100) {
		cout << "Nilai anda A" << endl;
	}
	else {
		cout << "NILAI TIDAK VALID" << endl;
	}

}