using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassAndObject5826
{
    internal class mobil
    {
        public string merk { get; set; }

        public string  warna{ get; set; }


        public void nyalakanmesin()
        {
            Console.WriteLine("Mobil anda {0}", merk);
        }

        public void matikanmesin()
        {
            Console.WriteLine("Mobil anda {0}", warna);
        }
    }
}
