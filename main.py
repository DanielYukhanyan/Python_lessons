from random import randint
import random
import time
r=0
print("Hello i'm schoolGPT i can help you with any problem at school")
print("""Okey,we have code about tests to exercise your brain for that press 1
We have code about login for that press 2
We have code about year mark for that press 3
We have code about hard exam for that press 4
We have code about brain games for that press 5
We have Chatbot for that press 6
We have calculator code for that press 7
We have library code for that press 8
We have Motivation code for that press 9
if you want to leave press 10""")
rights=0
falses=0
library=["To Kill a Mockingbird", "Perfume: The Story of a Murderer", "Harry Potter", "The Lord of the Rings", "A Moveable Feast", "The Little Prince", "Stream of Consciousness", "The Alchemist", "The Master and Margarita", "1984"]
library_rating=[184,123,297,300,58,91,47,108,135,206]
year=["January", "February", "March", "April", "May", "Jun", "July", "August", "September", "October", "November", "December"]
grade_1a=["What is the letter Ա called in the Armenian alphabet?", "How is the word կին pronounced?", "How is the word աղ pronounced?", " What is the letter Բ called in the Armenian alphabet?"]
grade_1m=["2+3=?", "6-4=?", "How many fingers on two hands?", "How many fingers on one hand?"]
grade_2m=["2*5+6=?", "10*10+30=?", "30/6*5=?", "56/7=?", "60/2-15=?", "40/40+5=?", "45/5=?", "30*1-12=?", "20*100=?"]
grade_2a=["Who is the creator of Armenia?", "How many people live in Armenia?", "Who is the creator of Armenian letters?"]
grade_3m=["How much is 7 multiplied by 8?", "If you had 15 apples and you ate 6, how many apples do you have left?", "Anna has 3 boxes of candies. There are 10 candies in each box. How many candies ", "What is the result of 24 divided by 4?"]
grade_3a=["How do you translate the word գիշեր into English?", "What is the letter Ե called in the Armenian alphabet?", "How do you translate the word շաբաթ into English?", "How do you translate the word կենդանի into English?"]
grade_4m=["3*3*3*3=?", "(908-8)/300=?", "159-23=?", "500-346=?", "47*7=?", "133/19=?", "20+57=?", "140/70=?", "280/40=?", "5*120=?"]
grade_4a=["What does Մաշկ mean in Armenian?", "How do you translate the word ձուկ into Russian?", "What does the word արմատ mean in Russian?", "How is the word տեսակ translated into English?"]
grade_5a=["3/5+1/5?", " Solve the equation: 2x+5=15.", "Find the perimeter of a rectangle with sides of 8 cm and 12 cm.", "If a year has 365 days, how many days are in 6 years?"]
grade_5m=[" How is the word հոգեբանություն translated into Russian?", "Translate the phrase մեր աշխարհը գեղեցկությունն է into English.", " What does the word համբուրություն mean?", "How is the word մանրամասնություն translated into English?"]
grade_6m=["2/3+4/3=?", "50/17+10/17=?", "4/2*2/4=?", "67/10+40/10=?", "51/68+10/34=?", "24/18-7/6=?", "341/10-241/10=?", "45/20*20/45=?"]
grade_6a=["What does the word մշակել mean?", "How is the word կապիկ translated into English?", "How is the phrase երկիրը շրջապատում է translated into English?", "How is the word վագրի translated into English?"]
grade_7m=["Solve the equation:3x+7=22.", "Find the area of a triangle with sides of 6 cm, 8 cm, and 10 cm.", " How many centimeters are in 2 meters?", "Express 40% as a decimal fraction."]
grade_7a=["How is the word զորացնել translated into English?", "How is the phrase ուղիղ ճանապարհ translated into English?", "What does the word մեկարեւ mean?", " How is the word ոսկե translated into English?"]
grade_8m=["%^162=?", "%^64=?", "%^196=?", "%^25=?", "%^81=?"]
grade_8a=["What does the word գրեթե mean?", "How is the phrase սահմանափակել կամայականները translated into English?", "What does the word կաթ mean?", "How is the word գեղեցկություն translated into English?"]
pgrade_1a=["A(a)", "Kin", "Ax", "B"]
pgrade_1m=["5", "2", "10", "5"]
pgrade_2m=["16", "130", "25", "8", "15", "6", "9", "18", "2000"]
pgrade_2a=["Tigran the Great", "Approximately 3 million", "Mesrop Mashtots"]
pgrade_3m=["56", "9", "30", "6"]
pgrade_3a=["night", "Ye", "Saturday", "animal"]
pgrade_4m=["81", "3", "136", "154", "329", "7", "77", "2", "7", "600"]
pgrade_4a=["head", "hand", "apple", "type"]
pgrade_5a=["4/5", "x=5", "40", "2190"]
pgrade_5m=["Psychology", "Our world is beauty", "Union", "Detail"]
pgrade_6m=["2/1", "60/17", "1/1", "107/10", "71,68", "1/6", "292/5", "1/1"]
pgrade_6a=["to create", "flower", "Sunrise", "vineyard"]
pgrade_7m=["5", "24", "200", "0.4"]
pgrade_7a=["Strengthen", "Straight road", "Lightning", "Beauty"]
pgrade_8m=["12", "8", "14", "5", "9"]
pgrade_8a=["Play", "Limit rights", "Lightning", "Beauty"]
exam_questions=["1.What is the sum of 3/5 and 1/4?", "2.What is the term for a word that indicates a pronoun pointing to the second person?", "3.Who was the first president of the United States?", "4.What is the largest lake in the world by area?", "5.What happens to water at a temperature of 100 degrees Celsius?", "6.What is the name of the book that describes the adventure of a little boy who enters a magical land through a mirror?", "7.Who painted the Mona Lisa?", "8.What sport is considered the most popular in the world?", "9.What type of government does Russia have?"]
exam_answers=["17/20", "Second-person pronoun", "George Washington", "The Caspian Sea", "It boils", "Alice's Adventures in Wonderland", "Leonardo da Vinci", "Soccer (football)", "Federal"]
enter=int(input("""1.Progress at school
2.Want to log in
3.input marks to know your year mark
4.pass exam
5.brain games 
6.Chatbot
7.calculator
8.go to library
9.Motivation code
10.Exit"""))
loop=True
while enter!=10:
  if enter==1:
    grade=int(input("Enter what grade do you study at"))
    if grade==1:
        rights=0
        falses=0
        login=input("Please enter your name")
        print("Hello "+login+" .Let's find out your mark i can help you only with math and Armenian in your grade (1-8)")
        math_or_Arm=input("enter math or Arm have bad marks or don't have bad marks")
        if math_or_Arm=="math":
          math_mark=int(input("Enter your math mark"))
          if math_mark<=8:
            print("Oh,LET's LEARN!!!!!")
            for i in range(len(grade_1a)):
              print(grade_1m[i])
              z=input("enter answer")
              if z==pgrade_1m[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_1m[i])
            if rights>=falses:
              math_mark=math_mark+2
              print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
            else:
              print("Sorry,but i can't fix your mark")
          elif math_or_Arm=="Arm":
            Arm_mark=int(input("Enter your Arm mark"))
            if Arm_mark<=8:
              print("Oh,LET's LEARN!!!!!")
              for i in range(len(grade_1a)):
                print(grade_1a[i])
                z=input("enter answer")
              if z==pgrade_1a[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_1a[i])
              if rights>=falses:
                Arm_mark=Arm_mark+2
                print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
              else:
                print("Sorry,but i can't fix your mark")
            else:
              print("Sorry but why you come here(just kidding) I'm kidding.Ok Good luck")
        else:
          print("Ok you don't have bad marks good luck")
    elif grade==2:
        rights=0
        falses=0
        login=input("Please enter your name")
        print("Hello "+login+" .Let's find out your mark i can help you only with math and Armenian in your grade (1-8)")
        math_or_Arm=input("enter math or Arm have bad marks or don't have bad marks")
        if math_or_Arm=="math":
          math_mark=int(input("Enter your math mark"))
          if math_mark<=8:
            print("Oh,LET's LEARN!!!!!")
            for i in range(len(grade_2a)):
              print(grade_2m[i])
              z=input("enter answer")
              if z==pgrade_2m[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_2m[i])
            if rights>=falses:
              math_mark=math_mark+2
              print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
            else:
              print("Sorry,but i can't fix your mark")
        elif math_or_Arm=="Arm":
            Arm_mark=int(input("Enter your Arm mark"))
            if Arm_mark<=8:
              print("Oh,LET's LEARN!!!!!")
              for i in range(len(grade_2a)):
                print(grade_2a[i])
                z=input("enter answer")
              if z==pgrade_2a[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_2a[i])
              if rights>=falses:
                Arm_mark=Arm_mark+2
                print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
              else:
                print("Sorry,but i can't fix your mark")
            else:
              print("Sorry but why you come here(just kidding) I'm kidding.Ok Good luck")
        else:
          print("Ok you don't have bad marks good luck")
    elif grade==3:
        rights=0
        falses=0
        login=input("Please enter your name")
        print("Hello "+login+" .Let's find out your mark i can help you only with math and Armenian in your grade (1-8)")
        math_or_Arm=input("enter math or Arm have bad marks or don't have bad marks")
        if math_or_Arm=="math":
          math_mark=int(input("Enter your math mark"))
          if math_mark<=8:
            print("Oh,LET's LEARN!!!!!")
            for i in range(len(grade_3a)):
              print(grade_3m[i])
              z=input("enter answer")
              if z==pgrade_3m[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_3m[i])
            if rights>=falses:
              math_mark=math_mark+2
              print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
            else:
              print("Sorry,but i can't fix your mark")
        elif math_or_Arm=="Arm":
            Arm_mark=int(input("Enter your Arm mark"))
            if Arm_mark<=8:
              print("Oh,LET's LEARN!!!!!")
              for i in range(len(grade_3a)):
                print(grade_3a[i])
                z=input("enter answer")
              if z==pgrade_1a[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_1a[i])
              if rights>=falses:
                Arm_mark=Arm_mark+2
                print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
              else:
                print("Sorry,but i can't fix your mark")
            else:
              print("Sorry but why you come here(just kidding) I'm kidding.Ok Good luck")
        else:
          print("Ok you don't have bad marks good luck")
    elif grade==4:
        rights=0
        falses=0
        login=input("Please enter your name")
        print("Hello "+login+" .Let's find out your mark i can help you only with math and Armenian in your grade (1-8)")
        math_or_Arm=input("enter math or Arm have bad marks or don't have bad marks")
        if math_or_Arm=="math":
          math_mark=int(input("Enter your math mark"))
          if math_mark<=8:
            print("Oh,LET's LEARN!!!!!")
            for i in range(len(grade_4a)):
              print(grade_4m[i])
              z=input("enter answer")
              if z==pgrade_4m[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_4m[i])
            if rights>=falses:
              math_mark=math_mark+2
              print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
            else:
              print("Sorry,but i can't fix your mark")
        elif math_or_Arm=="Arm":
            Arm_mark=int(input("Enter your Arm mark"))
            if Arm_mark<=8:
              print("Oh,LET's LEARN!!!!!")
              for i in range(len(grade_4a)):
                print(grade_4a[i])
                z=input("enter answer")
              if z==pgrade_4a[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_4a[i])
              if rights>=falses:
                Arm_mark=Arm_mark+2
                print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
              else:
                print("Sorry,but i can't fix your mark")
            else:
              print("Sorry but why you come here(just kidding) I'm kidding.Ok Good luck")
        else:
          print("Ok you don't have bad marks good luck")
    elif grade==5:
        rights=0
        falses=0
        login=input("Please enter your name")
        print("Hello "+login+" .Let's find out your mark i can help you only with math and Armenian in your grade (1-8)")
        math_or_Arm=input("enter math or Arm have bad marks or don't have bad marks")
        if math_or_Arm=="math":
          math_mark=int(input("Enter your math mark"))
          if math_mark<=8:
            print("Oh,LET's LEARN!!!!!")
            for i in range(len(grade_5a)):
              print(grade_5m[i])
              z=input("enter answer")
              if z==pgrade_5m[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_5m[i])
            if rights>=falses:
              math_mark=math_mark+2
              print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
            else:
              print("Sorry,but i can't fix your mark")
        elif math_or_Arm=="Arm":
            Arm_mark=int(input("Enter your Arm mark"))
            if Arm_mark<=8:
              print("Oh,LET's LEARN!!!!!")
              for i in range(len(grade_5a)):
                print(grade_5a[i])
                z=input("enter answer")
              if z==pgrade_5a[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_5a[i])
              if rights>=falses:
                Arm_mark=Arm_mark+2
                print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
              else:
                print("Sorry,but i can't fix your mark")
            else:
              print("Sorry but why you come here(just kidding) I'm kidding.Ok Good luck")
        else:
          print("Ok you don't have bad marks good luck")
    elif grade==6:
        rights=0
        falses=0
        login=input("Please enter your name")
        print("Hello "+login+" .Let's find out your mark i can help you only with math and Armenian in your grade (1-8)")
        math_or_Arm=input("enter math or Arm have bad marks or don't have bad marks")
        if math_or_Arm=="math":
          math_mark=int(input("Enter your math mark"))
          if math_mark<=8:
            print("Oh,LET's LEARN!!!!!")
            for i in range(len(grade_6a)):
              print(grade_6m[i])
              z=input("enter answer")
              if z==pgrade_6m[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_6m[i])
            if rights>=falses:
              math_mark=math_mark+2
              print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
            else:
              print("Sorry,but i can't fix your mark")
        elif math_or_Arm=="Arm":
            Arm_mark=int(input("Enter your Arm mark"))
            if Arm_mark<=8:
              print("Oh,LET's LEARN!!!!!")
              for i in range(len(grade_6a)):
                print(grade_6a[i])
                z=input("enter answer")
              if z==pgrade_6a[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_6a[i])
              if rights>=falses:
                Arm_mark=Arm_mark+2
                print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
              else:
                print("Sorry,but i can't fix your mark")
            else:
              print("Sorry but why you come here(just kidding) I'm kidding.Ok Good luck")
        else:
          print("Ok you don't have bad marks good luck")
    elif grade==7:
        rights=0
        falses=0
        login=input("Please enter your name")
        print("Hello "+login+" .Let's find out your mark i can help you only with math and Armenian in your grade (1-8)")
        math_or_Arm=input("enter math or Arm have bad marks or don't have bad marks")
        if math_or_Arm=="math":
          math_mark=int(input("Enter your math mark"))
          if math_mark<=8:
            print("Oh,LET's LEARN!!!!!")
            for i in range(len(grade_7a)):
              print(grade_7m[i])
              z=input("enter answer")
              if z==pgrade_7m[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_7m[i])
            if rights>=falses:
              math_mark=math_mark+2
              print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
            else:
              print("Sorry,but i can't fix your mark")
        elif math_or_Arm=="Arm":
            Arm_mark=int(input("Enter your Arm mark"))
            if Arm_mark<=8:
              print("Oh,LET's LEARN!!!!!")
              for i in range(len(grade_7a)):
                print(grade_7a[i])
                z=input("enter answer")
              if z==pgrade_7a[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_7a[i])
              if rights>=falses:
                Arm_mark=Arm_mark+2
                print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
              else:
                print("Sorry,but i can't fix your mark")
            else:
              print("Sorry but why you come here(just kidding) I'm kidding.Ok Good luck")
        else:
          print("Ok you don't have bad marks good luck")
    elif grade==8:
        rights=0
        falses=0
        login=input("Please enter your name")
        print("Hello "+login+" .Let's find out your mark i can help you only with math and Armenian in your grade (1-8)")
        math_or_Arm=input("enter math or Arm have bad marks or don't have bad marks")
        if math_or_Arm=="math":
          math_mark=int(input("Enter your math mark"))
          if math_mark<=8:
            print("Oh,LET's LEARN!!!!!")
          for i in range(len(grade_8a)):
            print(grade_8m[i])
            z=input("enter answer")
            if z==pgrade_8m[i]:
              print("right answer")
              rights=rights+1
            else:
              falses=falses+1
              print("wrong answer :right answer is "+pgrade_8m[i])
          if rights>=falses:
            math_mark=math_mark+2
            print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
          else:
              print("Sorry,but i can't fix your mark")
        elif math_or_Arm=="Arm":
            Arm_mark=int(input("Enter your Arm mark"))
            if Arm_mark<=8:
              print("Oh,LET's LEARN!!!!!")
              for i in range(len(grade_8a)):
                print(grade_8a[i])
                z=input("enter answer")
              if z==pgrade_8a[i]:
                print("right answer")
                rights=rights+1
              else:
                falses=falses+1
                print("wrong answer :right answer is "+pgrade_8a[i])
              if rights>=falses:
                Arm_mark=Arm_mark+2
                print("not bad your math mark is good .you earned two extra points `"+str(math_mark))
              else:
                print("Sorry,but i can't fix your mark")
            else:
              print("Sorry but why you come here(just kidding) I'm kidding.Ok Good luck")
        else:
          print("Ok you don't have bad marks good luck")
  elif enter=="2":
    name_log=input("please enter your name")
    age=int(input("please enter your age "))
    print("Hello "+name_log+"you're "+str(age)+" have good and productiv day in school")
  elif enter==3:
    year_name=input("please enter name of lesson")
    for i in range(len(year)):
      year_count=int(input("please enter how much marks you earned in "+year[i]))
      year_sum=int(input("enter sum of marks in "+year[i]))
      summ=summ+year_sum
    total_count=summ/year_count
    print("your year mark is "+str(total_count))
  elif enter==4:
    rights_exam=0
    falses_exam=0
    for i in range(len(exam_questions)):
      print(exam_questions[i])
      j=input("enter answer")
      if j==exam_questions[i]:
        print("right answer")
        rights_exam=rights_exam+1
      else:
        falses_exam=falses_exam+1
        print("wrong answer :right answer is "+exam_answers[i])
    print("your exam mark is "+str(rights_exam))
  elif enter==5:
    games_enter=int(input("""please enter what game do you want to play
    1.Hangman
    2.rock paper sciccors
    3.number guessing"""))
    if games_enter==1:
      name=input("what is your name")
      print("hello "+name+" time to play hangman game")
      time.sleep(1)
      print("start guessing")
      time.sleep(0.5)
      print("good luck")
      print("you will guess capital cities")
      word_list=["Yerevan","Tehran","Brazilia","Moscow","Berlin"]
      secret=random.choice(word_list)
      guesses="auieoyAUEOIY"
      turns=5
      while turns>0:
        missed=0
        for letter in secret:
          if letter in guesses:
            print(letter)
          else:
            print("-")
            missed=missed+1
        print("")
        if missed==0:
          print("\nyou win")
          break
        guess=input("\nguess a letter")
        guesses=guesses+guess
        if guess not in secret:
          turns=turns-1
          print("you have \n"+str(turns)+" turns")
          if turns<5:print ("""\n  |    """)
          if turns<4: print ("""  O """)
          if turns<3:print (""" /|\ """)
          if turns<2:print ("""  |  """)
          if turns<1:print("""  / \  """)
          if turns==0:print("\nyou not guessed.the answer is "+str(secret))
    elif games_enter==2:
      man=0
      computer=0
      ch=["rock","paper","scissors"]
      print("""rock-->scissors
paper-->rock
scissors-->paper""")
      player=input("do you want to be rock,paper,scissors or exit")
      while player!="exit":
        player=player.lower()
        comp=random.choice(ch)
        print("you choice "+player+" and computer choice "+comp)
        if player==comp:
          print("draw")
        elif player=="rock":
          if comp=="scissors":
            print("!YOU WIN!")
            man=man+1
          else:
            print("computer win")
            computer=computer+1
        elif player=="paper":
          if comp=="rock":
            print("!YOU WIN!")
            man=man+1
          else:
            print("computer win")
            computer=computer+1
        elif player=="scissors":
          if comp=="paper":
            print("!YOU WIN!")
            man=man+1
          else:
            print("computer win")
            computer=computer+1
        else:
          print("bad input")
        print("")
        player=input("do you want to be rock,paper,scissors or exit")
      print("computer wins are "+str(computer))
      print("man wins are "+str(man))
    elif games_enter==3:
      ran=randint(1,100)
      n=int(input("enter num i can say what is that number"))
      pop=10
      while pop!=0:
        if n==ran:
          break
        else:
          if n<ran:
            pop=pop-1
            print("your num is smaller.you have "+str(pop)+" chanses")
          else:
            pop=pop-1
            print("your num is bigger.you have "+str(pop)+" chanses")
        n=int(input("enter num i can say what is that number"))
      print("YOU WIN!!!! the num is "+str(ran))
  elif enter==6:
    print("Hello I'm Chatbot")
    names_=input("Hello what is your name?")
    print("Thats a beautifull name "+names_+" and my name is chatbi")
    ages_=input("how old are you?")
    print("so you are "+ages_+ " years old and I dont have an age,because I am an AI:)")
    locations_=input("Where do you live?")
    print("Wow you live in a place of wonders,so be happy")
    Movies_=input("And what is your most favorite Movie?")
    print("For me "+Movies_+" is a fantastic Movie")
    Hobbys_=input("What are your hobbies?")
    print("I love "+Hobbys_+" also,and i like "+Hobbys_)
  elif enter==7:
    print("Hello I'm calculateGPT i can help you with any problems only in math")
    calc=input("please enter what do you want to do (+,-,*,/)")
    if calc=="+":
      num=int(input("please enter first num"))
      num2=int(input("please enter second num"))
      f=num+num2
      print("the count is "+str(f))
    elif calc=="-":
      num=int(input("please enter first num"))
      num2=int(input("please enter second num"))
      f=num-num2
      print("the count is "+str(f))
    elif calc=="*":
      num=int(input("please enter first num"))
      num2=int(input("please enter second num"))
      f=num*num2
      print("the count is "+str(f))
    else:
      num=int(input("please enter first num"))
      num2=int(input("please enter second num"))
      f=num/num2
      print("the count is "+str(f))
  elif enter==8:
    print("Hello this is library you can read books here")
    for i in range(len(library)):
      r=r+1
      print("this is books "+str(r)+"."+str(library[i]))
      print("this is rating "+str(r)+"."+str(library_rating[i])+" people")
    print("this is rating of all popular books in your school")
    library_enter=int(input("please enter what book do you want to read (1-10)"))
    if library_enter==1:
      print("there is link to book ")
    elif library_enter==2:
      print("there is link to book ")
    elif library_enter==3:
      print("there is link to book ")
    elif library_enter==4:
      print("there is link to book ")
    elif library_enter==5:
      print("there is link to book ")
    elif library_enter==6:
      print("there is link to book ")
    elif library_enter==7:
      print("there is link to book ")
    elif library_enter==8:
      print("there is link to book ")
    elif library_enter==9:
      print("there is link to book ")
    elif library_enter==10:
      print("there is link to book ")
    else:
      print("we don't have enough books")
  elif enter==9:
    print(".•♫•♬• 🅼🅴🅸🅻🅸 •♬•♫•.")
    choices=["Keep it simple","TIP:If you like taking breaks you should use the pomodoro technique","Without a doubt you are creative","Love yourself","you are doing great","yes,you are wonderfull","Most likely to be happy","If you study you will get smarter"]
    question=input("P1 ex done-")
    while question!=exit:
      print(random.choice(choices))
      print("____________________")
      question=input("P1 ex done-")
  elif enter==10:
    loop==False
  enter=int(input("""1.Progress at school
2.Want to log in
3.input marks to know your year mark
4.pass exam
5.brain games 
6.Chatbot
7.calculator
8.go to library
9.Motivation code
10.Exit"""))
      
      
      