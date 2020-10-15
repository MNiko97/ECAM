using System;


namespace CountDown
{
    class Program
    {
        static void Main(string[] args)
        {
            CountDown countDown = new CountDown(10);
            countDown.Start();
        }
    }

    class CountDown
    {
        private int count;
        
        public CountDown(int count){
            this.count = count;
        }
        public void Start(){
            Console.WriteLine(count);
            count--;
            if (count == 0){
                Stop();
            }
        }

        public void Stop(){

        }

        public int RemainingTime{
            get{
                return count;
            }
        }
    }
}
