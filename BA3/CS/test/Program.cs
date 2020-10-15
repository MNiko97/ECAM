using System;

namespace test
{
    class Person {
        public override string ToString() {
        return "je suis une personne";
        }
    }

    class Employee : Person {
        public override string ToString() {
            return "je suis un employé";
        }
    }

    class Program {
        public static void Main(string [] args) {
            Person e = new Employee();
            Console.WriteLine(e);
        }
    }
}
