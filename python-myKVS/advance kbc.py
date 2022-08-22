 # -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:07:17 2021

@author: Home
"""
import random
print("-------------------------------------------------------------------------------")
print('|!!!!!!!*******$$$$$$$ WELCOME TO KBC $$$$$$$*******!!!!!!!                   |')
print("-------------------------------------------------------------------------------")
print("|######!!!!!{{{{THIS GAME IS DEVELOPED BY AMIT SIROHI}}}}!!!!!######          |")
print("-------------------------------------------------------------------------------")
print('|RULES of game are very simple:                                               |')
print('|1.Five questions will be displayed on your screen.                           |')
print('|2.You will get 10 points for each correct answer.                            |')
print('|3.Game will get over as soon as you input wrong answer.                      |')
print("-------------------------------------------------------------------------------")
print(" SO LETS BEGIN..........!")
#question bank
questions1=['MS-Word is an example of _____ a) An operating system; b) A processing device; c) Application software; d) An input device',
            'Which latitude passes through the middle of India? a)equator b)Arctic Circle c)Tropic of Cancer d)Tropic of Capricorn',
            'Hardest Part of the Human Body? a)femur b)backbone c)tooth enamel d)skull',
            'Which foreign country is closest to Andaman Islands? a)Sri Lanka b)Indonesia c)Myanmar d)Pakistan',
            'Which of the following is the National Aquatic animal of India? a)Salt water crocodile b)Sea Turtle c)Dolphin d)Dugong']
questions2=['Which Indian State have the longest coast line? a)Gujarat; b)Maharashtra; c)West bengal; d)Odisha ',
            '13-Chambered heart occurs in________ a)cockroach b)snail c)leech d)ant',
            'Revolver discovered by______ a) Colt b)Mercafter c)Bushwell d)Daimler',
            'India is not a member of______ a)G-8 b)G-20 c)SAARC d)U.N',
            'The country with longest coastline in the world is a)Canada b)Norway c)Russia d)japan']
questions3=['First Indian woman to win Man Booker Prize was________ a)Kiran Desai; b)V.S.Naipaul; c)Salman Rushdie; d) Arundhati Roy',
            'The dornier aircraft belongs to which category? a)Reconnaissance aircraft b)Surveillance aircraft c)Strategic Airlifter d)Light Utility aircraft',
            '‘Naseem-Al-Bahr’ is a bilateral naval exercise between India and which country? a)Indonesia b)Iran c)Saudi Arabia d)Oman',
            'JIMEX is a maritime exercise between which two nations? a)USA and UK b)India and Jamaica c)India and Russia d)India and Japan',
            'Golden Arrows, that was seen in news, is the squadron of which Armed Force of India? a)Indian Army b)Indian Navy c)Indian coast guard d)Indian Airforce']
questions4=['How many layers of skin does a human have? a)one; b)two; c)three; d)four',
            'The device used for measuring altitudes is? a)audiometer b)latitudemeter c)altimeter d)ammeter',
            'Indias first atomic reactor is______a)Zerlina b)Dhruva c)Apsara d)Kamini',
            'Satellite launching station is located at_____a)Solapur b)Salem c)Sriharikotta d)Warangal',
            'Rabindranath Tagore receive Nobel Prize in 1913 in the field of_______a)physics b)peace c)literature d)economy']
questions5=['Which country has "This is the root of all evil" written on its coins? a)Italy; b)Vatican City; c)Cuba; d)Russias1',
            'Which supersonic cruise missile with Indigenous Booster has been successfully flight tested? a)Nirbhay b)BrahMos c)Shaurya d)Viraat',
            'The Central Command of Army is located at a)Pune b)Lucknow c)Udhampur d)Mhow',
            'The first man-made satellite was launched by______a)USA b)USSR c)England d)China',
            'The Scottish bacteriologist who discovered penicillin was_____ a)Albert Einstein b)Alexander Fleming c)Archimeder d)Aryabhatta']
quest1=random.choice(questions1)
quest2=random.choice(questions2)
quest3=random.choice(questions3)
quest4=random.choice(questions4)
quest5=random.choice(questions5)
a,b,c,d="a","b","c","d"
print("-----------------------------------------------------------------------------------------------------")
print('Here is your 1st question-',random.choice(questions1))
first=input('Enter the correct option(a,b,c,d) here:')
print('')
score=0
count=0
while count<=4:
  count+=1
  if first==c:
    score=score+10
    print("WOW! Thats correct.You are very smart.10 points added")
    print('As you have ansered 1st question correctly. So the next question is-')
    print("-----------------------------------------------------------------------------------------------------")
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     | Total score:',score,'|')
    print("-----------------------------------------------------------------------------------------------------")
    while count<=4:
        count=count+1
    print('2.',random.choice(questions2))
    second=input('Enter the correct option(a,b,c,d) here:')
    if second==a:
        score=score+10
        print('WOW! Thats correct.You are very smart.10 points added')
        print("As you have ansered 2nd question correctly. So the next question is-")
        print("-----------------------------------------------------------------------------------------------------")
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   | Total score:',score,'|')
        print("-----------------------------------------------------------------------------------------------------")
        while count<=3:
            count=count+1
        print('3.',random.choice(questions3))
        third=input('Enter the correct option(a,b,c,d) here:')
        if third==d:
            score=score+10
            print('WOW! Thats correct.You are very smart.10 points added')
            print("As you have ansered 3rd question correctly. So the next question is-")
            print("-----------------------------------------------------------------------------------------------------")
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    | Total score:',score,'|')
            print("-----------------------------------------------------------------------------------------------------")
            while count<=2:
                count=count+1
            print('4.',random.choice(questions4))
            fourth=input('Enter the correct option(a,b,c,d) here:')
            if fourth==c:
                score=score+10
                print('WOW! Thats correct.You are very smart.10 points added')
                print("As you have ansered 4th question correctly you have reached the last question. So the last question is-")
                print("-----------------------------------------------------------------------------------------------------")
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    | Total score:',score,'|')
                print("-----------------------------------------------------------------------------------------------------")
                while count<=1:
                    count=count+1
                print('5.',random.choice(questions5))
                fifth=input('Enter the correct option(a,b,c,d) here:')
                if fifth==b:
                    print('WOW! Thats correct.You are very smart.10 points added. Your total is |50 points|')
                    print("-----------------------------------------------------------------------------------------------------")
                    print('Congratulations and Thank you for playing this game :)')
                    print("-----------------------------------------------------------------------------------------------------")
                    print("Press F5 to play again")
                    print("-----------------------------------------------------------------------------------------------------")
                else:
                    print("-----------------------------------------------------------------------------------------------------")
                    print('Bad luck :/, your answer is not correct. The correct answer was option b. Your total score is 40 points.Thank you for playing this game :)')
                    print("-----------------------------------------------------------------------------------------------------")
                    print("Press F5 to play again")
                    print("-----------------------------------------------------------------------------------------------------")
                    break
            else:
                print("-----------------------------------------------------------------------------------------------------")
                print('Bad luck :/, your answer is not correct. The correct answer was option c. Your total score is 30 points.Thank you for playing this game :)')
                print("-----------------------------------------------------------------------------------------------------")
                print("Press F5 to play again")
                print("-----------------------------------------------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------------------------------------------")
            print('Bad luck :/, your answer is not correct. The correct answer was option d. Your total score is 20 points.Thank you for playing this game :)')
            print("-----------------------------------------------------------------------------------------------------")
            print("Press F5 to play again")
            print("-----------------------------------------------------------------------------------------------------")
            break
                
    else:
        print("-----------------------------------------------------------------------------------------------------")
        print("Bad luck :/, your answer is not correct. The correct answer was option a. Your total score is 10 points.Thank you for playing this game :)")
        print("-----------------------------------------------------------------------------------------------------")
        print("Press F5 to play again")
        print("-----------------------------------------------------------------------------------------------------")
        break
  else:
   print("-----------------------------------------------------------------------------------------------------")
   print("Bad luck :/, your answer is not correct. The correct answer was option c.Your score is 0 points.Thank you for playing this game :)")
   print("-----------------------------------------------------------------------------------------------------")
   print("Press F5 to play again")
   print("-----------------------------------------------------------------------------------------------------")
  break
timepass=input("🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁")
