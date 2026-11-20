using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassAndObject5826
{
    internal class Dosen
    {
        public string nik { get; set; }

        public string nama { get; set; }


        public void mengajar()
        {
            Console.WriteLine("{0} mengajar matematika diskret", nama);
        }

        public void menulis()
        {
            Console.WriteLine("{0} menulis riset NLP", nama);
        }
    }
}
