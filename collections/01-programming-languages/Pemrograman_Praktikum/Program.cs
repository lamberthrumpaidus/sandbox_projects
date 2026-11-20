using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassAndObject5826
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Dosen dosen1 = new Dosen();
            dosen1.nik = "1234";
            dosen1.nama = "novi";
            dosen1.mengajar();
            dosen1.menulis();

            Mahasiswa mahasiswa1 = new Mahasiswa();
            mahasiswa1.nik = "5826";
            mahasiswa1.nama = "lamberth";
            mahasiswa1.mengajar();
            mahasiswa1.menulis();

            mobil mobil1 = new mobil();
            mobil1.merk = "Ferari";
            mobil1.warna = "merah Putih";
            mobil1.nyalakanmesin();
            mobil1.matikanmesin();

            mobil mobil2 = new mobil();
            mobil2.merk = "Bugati";
            mobil2.warna = "Hytam";
            mobil1.nyalakanmesin();
            mobil2.matikanmesin();

            mobil mobil3 = new mobil();
            mobil3.merk = "Avanza";
            mobil3.warna = "Putih";
            mobil3.nyalakanmesin();
            mobil3.matikanmesin();

        }
    }
}
