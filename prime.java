public class prime
 {
public static void main(String[] args) {
System.out.println("Prime numbers between 1 and 100 are:");
for (int i=2; i<= 100; i++) 
{
if( isPrime=(i))
{
system.out.print(i+" ");
}
}
} 
for (int i = 2; i <= Math.sqrt(number); i++) {
                if (number % i == 0) {
                    isPrime = false; // If divisible, it's not a prime number
                    break; // No need to check further, break the inner loop
                }
            }

            // If isPrime is still true, the number is prime
            if (isPrime) {
                System.out.print(number + " ");
            }
        }
    }
}
