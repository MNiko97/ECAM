using System;

namespace Labo1
{
    class Polynomial
    {
        private double[] polynome;
        public Polynomial(double [] polynome)
        {
            this.polynome = polynome;
        }
        public int Degree
        {
            get
            {
                return 0;
            }
        }
        public double Evaluate(double x)
        {
            return 0;
        }
        public override string ToString()
        {
            return base.ToString();
        } 
        public static void TrinomialRoot(double a, double b, double c)
        {
            double delta = Math.Pow(b, 2) - 4 * a * c;
            if (delta < 0)
            {
                Console.WriteLine("No real root");
            }
            else if (delta == 0)
            {
                double res = -b / 2 * a;
                Console.WriteLine("One root found : ", +res);
            }
            else
            {
                double res1 = (-b + Math.Sqrt(delta)) / 2 * a;
                double res2 = (-b - Math.Sqrt(delta)) / 2 * a;
                Console.WriteLine("Two root found : " + res1 + " ; " + res2);
            }
        }
    }
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
