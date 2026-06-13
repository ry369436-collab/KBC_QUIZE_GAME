print("Hello Dear!!")
print("Welcome to KBC!!\n")
print("RULES:")
print("There are 5 MCQs questions with four options.")
print("Each Qs have one coreect answer,")
print("Choose correct one and move ahead.\n")

dict={
    "Qs1":"What does the continue statement do in a loop?",
    "answer1":["A:Skips the current iteration and continues with the next",
        "B:Stops the loop","C:Restarts the loop","D:None of the above"],
    "Qs2":"Which data structure is primarily used when implementing a Breadth-First Search (BFS) algorithm?",
    "answer2":["A:Stack","B:Queue","C:Tree","D:Graph"],
    "Qs3":"What is the time complexity of binary search?",
    "answer3":["A:O(n)","B:O(n^2)","C:O(log(n))","D:O(nlog(n))"],
    "Qs4":"What does SQL stand for?",
    "answer4":["A:Structured Query Language","B:Simple Query Language",
                    "C:Standard Query Language","D:None of the above"],
    "Qs5":"who is the Director of KNIT sultanpur?",
    "answer5":["A:Raju","B:R.K. Upadhyay","C:Bitti","D:Chitti"]
}
print(dict["Qs1"])
for x in dict["answer1"]:
    print(x)
answer=input("Enter correct option(A,B,C,D):")  
if(answer=="A"):
    print("Correct answer\n")
    print(dict["Qs2"])
    for x in dict["answer2"]:
        print(x)
    answer=input("Enter correct option(A,B,C,D):")
    if(answer=="B"):
        print("correct answer")
        print(dict["Qs3"])
        for x in dict["answer3"]:
            print(x)
        answer=input("Enter correct option(A,B,C,D):")
        if(answer=="C"):
            print("correct answer")
            print(dict["Qs4"])
            for x in dict["answer4"]:
                print(x)
            answer=input("Enter correct option(A,B,C,D):")
            if(answer=="A"):
                print("correct answer")
                print(dict["Qs5"])
                for x in dict["answer5"]:
                    print(x)
                answer=input("Enter correct option(A,B,C,D):")
                if(answer=="B"):
                    print("🎉You are a Crorepati")

                else:
                    print("❌ Wrong answer. You won ₹4000")



            else:
                 print("❌ Wrong answer. You won ₹3000")


        else:
            print("❌ Wrong answer. You won ₹2000")
            

    else:
         print("❌ Wrong answer. You won ₹1000")    

else:
     print("❌ Wrong answer. You won ₹00")    

