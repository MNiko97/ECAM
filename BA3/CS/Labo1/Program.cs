using System;

namespace Labo1
{
    class Program
    {
        static void Main(string[] args)
        {
            /*double a = Input("a");
            double b = Input("b");
            double c = Input("c");
            TrinomialRoot(a, b, c);*/

            double[] a = { 1, 0, -2 };
            int degree = a.Length - 1;
            int i = 0;
            double res = 0;
            while (i < a.Length)
            {
                Console.WriteLine(a[i]);
                res += a[i]*Math.Pow(2, degree);
                i++;
            }
        }
        private static double Input(string value)
        {
            while (true)
            {
                try
                {   
                    Console.Write("Enter real number : ");
                    string input = Console.ReadLine();
                    double output = Convert.ToDouble(input);
                    return output;
                }
                catch (System.FormatException)
                {
                    Console.WriteLine("Not a number");
                    continue;
                }
            }
        }
    }
}
