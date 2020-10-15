using System;
using System.Collections.Generic;
namespace EvalManager
{
    class Person{
        public String Firstname;
        public String Lastname;
        public Person(String Firstname, String Lastname){
            this.Firstname = Firstname;
            this.Lastname = Lastname;
        }
        public void DisplayName(){
            Console.WriteLine(Firstname + " " + Lastname);
        }
    }
    class Teacher : Person{
        public int Salary;
        public Teacher(String Firstname, String Lastname, int Salary) : base(Firstname, Lastname)
        {
            this.Salary = Salary;
        }

    }
    class Student : Person{
        private List<Evaluation> Cours;
        public Student(String Firstname, String Lastname) : base(Firstname, Lastname)
        {
            this.Cours = new List<Evaluation>();
        }
        public void Add(Evaluation Evaluation){
            Cours.Add(Evaluation);
        }
        public double Average(){
            int totalMarks = 0;
            int totalCourses = Cours.Count;
            Cours.ForEach(mark => totalMarks += mark.Note());
            double averageResult = totalMarks/totalCourses;
            Console.WriteLine("Total Marks : " + totalMarks);
            Console.WriteLine("Total Courses : " + totalCourses);
            Console.WriteLine(averageResult);
            return averageResult;
        }
        public void Bulletin(){ //normalement String dans l'énoncé
            /*Cours.ForEach(mark => Console.WriteLine("[{0}] {1} ({2} {3}, {4}ECTS): {5}", mark.Activity.Code, mark.Activity.Name, 
            mark.Activity.Teacher.Firstname, mark.Activity.Teacher.Lastname, mark.Activity.ECTS, mark.Note())); 
            Console.WriteLine("");
            Console.WriteLine("Average: ", Average());*/
        }
    }
    class Activity{
        public int ECTS;
        public String Name;
        public String Code;
        public Teacher Teacher;
        public Activity(int ECTS, String Name, String Code, Teacher Teacher){
            this.ECTS = ECTS;
            this.Name = Name;
            this.Code = Code;
            this.Teacher = Teacher;
        }
    }
    class Evaluation{
        public Activity Activity;
        public Evaluation(Activity Activity){
            this.Activity = this.Activity;
        }
        public virtual int Note(){
            return 0;
        }
    }
    class Cote : Evaluation{
        private int note;
        public Cote(Activity Activity, int note) : base(Activity)
        {
            this.note = note;
        }
        public override int Note(){
            return note;
        }
        public void setNote(int newNote){
            note = newNote;
        }
    }
    class Appreciation : Evaluation{
        private String appreciation;
        public Appreciation(Activity Activity, String appreciation) : base(Activity)
        {
            this.appreciation = appreciation;
        }
        public override int Note(){
            int result;
            switch(appreciation){
                case "X":
                    result = 20;
                    break;
                case "TB":
                    result = 16;
                    break;
                case "B":
                    result = 12;
                    break;
                case "C":
                    result = 8;
                    break;
                case "N":
                    result = 4;
                    break;
                default:
                    result=-1;
                    break;
            }
            return result;
        }
        public void setAppreciation(String newAppreciation){
            appreciation = newAppreciation;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Teacher programmingTeacher = new Teacher("Quentin", "Lurkin", 10000);
            Teacher dataBaseTeacher = new Teacher("André", "Lorge", 8000);

            Activity programming = new Activity(5, "Programming", "PO3L", programmingTeacher);
            Activity dataBase = new Activity(4, "Data Base", "DB3L", dataBaseTeacher);

            Student student18365 = new Student("Nikola", "Mitrovic");
            student18365.DisplayName();
            student18365.Add(new Cote(programming, 14));
            student18365.Add(new Cote(dataBase, 18));
            student18365.Add(new Appreciation(programming, "TB"));
            student18365.Average();
            //student18365.Bulletin();
        }
    }
}
