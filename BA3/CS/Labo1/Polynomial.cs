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