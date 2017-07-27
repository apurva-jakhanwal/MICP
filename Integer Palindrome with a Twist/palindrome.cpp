#include <iostream>
using namespace std;

int reverseNum(int number){
  int reverse = 0;
  int rem = 0;
  while(number != 0){
      rem = number % 10;
      reverse = (reverse*10) + rem;
      number = number/10;
  }
  return reverse;
}

bool palindrome(int number){
  int reverse = reverseNum(number);
  if(reverse == number)
      return true;
  else
      return false;
}


bool palindromeProcess(int number){
  while (number < 1000000){
      if(palindrome(number))
          return true;
      int reverse = reverseNum(number);
      int sum = number + reverse;
      number = sum;
  }
  return false;
}

bool testing(){
  if(palindromeProcess(3) and palindromeProcess(444) and palindromeProcess(21) and palindromeProcess(1234) and !palindromeProcess(999998))
    return true;
  return false;
}

int main(){
    if(testing())
      cout << "All tests passed" << endl;
    else
      cout << "All tests did not pass" << endl;

    /*string choice="Y";
    while(choice=="Y"){
          cout << "Enter Number : " << endl;
          int num = 0;
          cin >> num;
          if(num > 1000000){
            cout << "Out of Bounds" << endl;
            exit(0);
          }
          if(palindromeProcess(num))
              cout << "Palindrome" << endl;
          else
              cout << "Not a palindrome" << endl;
          cout << "Do you wish to continue checking for other numbers?(Y/N)" << endl;
          cin >> choice;
          if(choice=="N") exit(0);
     }*/
}
