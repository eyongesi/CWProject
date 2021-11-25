print("Please answer Yes or No")
age = input("Are you a cigarette addict older than 75 years old? ").title().strip()
chronic = input("Do you have a severe chronic disease? ").title().strip()
immune = input("Is your immune system too weak? ").title().strip()
print("Based on the information provided",
      "\n Age > 79:", age, "\n Chronic disease:", chronic, "\n Immune system too weak:",immune)


if age  == "Yes" or chronic == "Yes" or immune == "Yes":
    Covid19_Risk = True
    print("You are in risky group")
elif age  == "No" or chronic == "No" or immune == "No":
    Covid19_Risk = False
    print("You are not in risky group")
else:
    print("Please Anser Yes or No")
    
