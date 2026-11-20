using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassAndObject5826
{
    internal class Mahasiswa
    {
      
            public string nik { get; set; }

            public string nama { get; set; }


            public void mengajar()
            {
                Console.WriteLine("{0} mengikutin kelas matematika diskret", nama);
            }

            public void menulis()
            {
                Console.WriteLine("{0} membaca riset NLP", nama);
            }
        
    }
}

