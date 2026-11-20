using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassAndObjectMahasiswa
{
    internal class Program
    {
     
            static void Main(string[] args)
            {
                Mahasiswa saya = new Mahasiswa();
                Mahasiswa kamu = new Mahasiswa();

                saya.Nim = "5826";
                saya.Nama = "Lamberth";
                saya.Ipk = 3.95f;

                kamu.Nim = "1234";
                kamu.Nama = "Novi";
                kamu.Ipk = 3.70f;

                saya.Registrasi();
                saya.Isikrs();

                kamu.Registrasi();
                kamu.Isikrs();

                Console.ReadKey();
            }
        
    }
}
   
