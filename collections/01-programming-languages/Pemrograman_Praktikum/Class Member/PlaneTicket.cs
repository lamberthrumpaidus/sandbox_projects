using System;

public class PlaneTicket
{
    private string _origin = "";
    private string _destination = "";
    private double _cost;
    private string _currency = "";
    
    public string Origin
    {
        get { return _origin; }
        set { _origin = value; }
    }

    public string Destination
    {
        get { return _destination; }
        set { _destination = value; }
    }

    public double Cost
    {
        get { return _cost; }
        set { _cost = value; }
    }

    public string Currency
    {
        get { return _currency; }
        set { _currency = value; }
    }

    public void CetakTiket()
    {
        Console.WriteLine("=== RINGKASAN TIKET ===");
        Console.WriteLine("Origin: {0}", Origin);
        Console.WriteLine("Destination: {0}", Destination);
        Console.WriteLine("Cost: {0} ({1})", Cost, Currency);

        if (Currency == "USD")
        {
            double hasilRupiah = Cost * 15000;
            Console.WriteLine("Convert to Rupiah: {0}", hasilRupiah);
        }
        else if (Currency == "IDR")
        {
            double hasilDolar = Cost / 15000;
            Console.WriteLine("Convert to Dolar: {0}", hasilDolar);
        }
    }
}