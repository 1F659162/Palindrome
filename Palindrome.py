# 6206021620159
# Kaittrakul Jaroenpong IT 1RA
# Python Chapter 5 Example 3

print(">> Program Palindrome Number <<")
number = input("Enter integer number : ")
count = -1
for i in range(len(number)//2):
    if number[i] == number[count] :
        print(f"Digit {number[i]} equal to Digit {number[count]}")
        Palin = "is Palindrome Number."
    else :
        print(f"Digit {number[i]} not equal to Digit {number[count]}")
        Palin = "isn't Palindrome Number."
        break
    count -= 1
if len(number)%2 == 1 and i == len(number)//2:
    print(f"Digit {number[len(number)//2]} equal to Digit {number[len(number)//2]}")
print(f"Your enter number : {number} {Palin}")
print(f"Exit Program")
