import time
class interface :

    def play_again(self) :
        ob.space()
        print("*************************************************************************************************************************")
        print("                                                                                                       WANNA PLAY AGAIN ??                                                ")
        print("*************************************************************************************************************************")
        for i in range(3) :
            print()
        s=input("YES/NO >>> ").upper()
        if s[0]=="Y" :
            time.sleep(4)
            ob.core()
        elif s[0]=="N" :
                    ob.space()
                    print()
                    time.sleep(2)
                    print("                                                                                      <<<<",end=' ')
                    time.sleep(1)
                    print(" GAME",end=' ')
                    time.sleep(1)
                    print(" END ",end=' ')
                    time.sleep(1)
                    print(">>>>")
                    time.sleep(1)
                    for i in range(11) :
                        print(" ")
        else :
            print("Invalid Input !! Try Again !!")
            time.sleep(1)
            ob.play_again()
        
    def  corrector(self,s) :
        ''' ideal input is "A1" character followed by number ,
             however again there are CRAZY MANIACs who will do the opposite so :) '''
        if s[-1] not in "123" :
             return (s[::-1]).upper()
        else :
            return s.upper()

    def user_info(self) : # To Input Custom Details From The User. 
        ob.space()
        print("*************************************************************************************************************************")
        print("                                                                                                        TIC TAC TOE                                                   ")
        print("*************************************************************************************************************************")
        for i in range(3) :
            print()
        print("                                                                                             << CUSTOM USER INFO >>")
        print("                                 (NOTE :  Avoid using long names and symbols, incase of long symbols first character will be taken.)")
        for i in range(3) :
            print()
        pa=input("PLAYER-1's  NAME      >>>  ")
        ca=input("PLAYER-1's   SYMBOL >>>  ")[0]
        time.sleep(1)
        for _ in range(3) :
            print()
        pb=input("PLAYER-2's  NAME      >>>  ")
        cb=input("PLAYER-2's  SYMBOL  >>>  ")[0]
        if cb==ca or pa==pb :
                time.sleep(1)
                print("Same Symbol Or Name . Try Again !!!")
                ob.user_info()
        for _ in range(3) :
            print()
        print("GAME BEGINS IN 3.",end=' ')
        time.sleep(1)
        print('2.',end=' ')
        time.sleep(1)
        print('1.',end=' ')
        time.sleep(1)
        print('0',end=' ')
        time.sleep(1)
        return [pa,pb,ca,cb]
        
            
    def WinTester(self,pa) : # Tests For All The Winning Combinations In The Player String.
        win_patterns = ['A1-A2-A3','B1-B2-B3','C1-C2-C3','A1-B1-C1','A2-B2-C2','A3-B3-C3','A1-B2-C3','A3-B2-C1']
        for i in win_patterns :
            k=i.split('-')
            if ((k[0] in pa) and (k[1] in pa) and (k[-1] in pa)) :
                    return True
        return False


        
    def modifier(self,sa,sb,syma,symb) : # Modifies The Pattern As Per The User Inputs
                lm=[['','',''],['','',''],['','','']]
                d={'A':0,'B':1,'C':2}
                for i in sa[0:-1] :
                       k=ob.corrector(i)
                       lm[d[k[0]]][int(k[-1])-1]=syma
                for i in sb[0:-1] :
                       k=ob.corrector(i)
                       lm[d[k[0]]][int(k[-1])-1]=symb
                return lm
                      
    def tic_handler(self,pa,pb,syma,symb) : # Lengthy And Complex Function That Takes Inputs From The Users And Does Various Operations On it.
                #pa,pb='A','B'
                #syma,symb='O','X'
                pata,patb='',''
                count=0
                s1="                                                                                                _______1__________2_________3____"
                s2="                                                                                                A |     {}     |       {}      |    {}     |"
                s3="                                                                                                B |     {}     |       {}      |    {}     |"
                s4="                                                                                                C |     {}     |       {}      |    {}     |"
                s5="                                                                                                ----------------------------------"
                l=[[],[]]
                lm=[['','',''],['','',''],['','','']]
                flag=True
                k=0
                while k!=9 :
                          count+=1
                          if count%2==0 and flag==True :
                               sp=pb
                          elif count%2!=0 and flag==True :
                              sp=pa
                          print("*************************************************************************************************************************")
                          print("                                                                                                        TIC TAC TOE                                                   ")
                          print("*************************************************************************************************************************")
                          for i in range(6) :
                                      if i==1 :
                                          print("______________________________________________________________________________________________________________________________________________________")
                                          print("              {0}'s  PATTERN :  {1}                                                                                         {2}'s PATTERN : {3} ".format(pa,pata[0:-1],pb,patb[0:-1]))
                                          print("______________________________________________________________________________________________________________________________________________________")
                                      if i==3 :
                                          print("                                                                                               <<< {}'s TURN >>>".format(sp))
                                      print()
                          print(s1+'\n'+s2.format(lm[0][0],lm[0][1],lm[0][2])+'\n'+s3.format(lm[1][0],lm[1][1],lm[1][2])+'\n'+s4.format(lm[2][0],lm[2][1],lm[2][2])+'\n'+s5+'\n')
                          s=input(" Player {}'s Turn     >>>> ".format(sp))
                          sc="a1a2a3b1b2b3c1c2c31a2a3a1b2b3b1c2c3c"
                          if s.lower()=='x' :
                              print("                                                                                                         <<<  GAME ENDED >>>")
                              break
                          if (count%2==0) and (len(s)==2) and (s.upper() not in pata+patb) and (s.lower() in sc) and s :
                               patb+=ob.corrector(s)+'-'
                               l[1]=patb.split('-')
                               k+=1
                               flag=True
                               if ob.WinTester(patb) :
                                   for _ in range(2) :print(" ")
                                   print("                                                                                                               {} WON !!!!".format(pb))
                                   time.sleep(5)
                                   ob.play_again()
                                   break
                          elif (count%2!=0) and (len(s)==2) and (s.upper() not in pata+patb) and (s.lower() in sc) and s  :
                               pata+=ob.corrector(s)+'-'
                               l[0]=pata.split('-') 
                               k+=1
                               flag=True
                               if ob.WinTester(pata) :
                                   for _ in range(2) :print(" ")
                                   print("                                                                                                               {} WON !!!!".format(pa))
                                   time.sleep(5)
                                   ob.play_again()
                                   break
                          else :
                              count-=1
                              flag=False
                          time.sleep(1)
                          lm=ob.modifier(l[0],l[1],syma,symb)
                          for i in range(3) : print()
                          
    def space(self) :    #Prints blank lines 32 times so as to provide interactive interface.
        for i in range(32) :
                            print()

    def drama1(self) : #Displays A Simple Animation Before DEV Message 
        ob.space()
        print('                                                                                                    DEVELOPERS OF CODRAW                                    ')
        print('                                                                                                                  PRESENT                                           ')
        for i in range(10) :
            print()
        time.sleep(5)
        print("                                                                                      <<<< TIC",end=' ')
        time.sleep(1)
        print(" TAC",end=' ')
        time.sleep(1)
        print(" TOE >>>>")
        for i in range(11) :
            print()
        time.sleep(4)
            
    def first_page(self) : #Provides with a heading titled TIC TAC TOE
        ob.space()
        print("*************************************************************************************************************************")
        print("                                                                                                        TIC TAC TOE                                                   ")
        print("*************************************************************************************************************************")
        for i in range(3) :
            print()

    def dev_mess(self) : #Displays The Developers Message
       print("                                                                                          << WORD FROM THE DEV >>> ")
       print()
       print("The following program is developed by a group of  developers from CODRAW with a primary aim to replicate TIC-TAC-TOE")
       print("game using python programming language. The program is coded to provide best user-experience in Python IDLE and may")
       print("or may not provide the same in other available IDE/IDLEs .  ")
       print("   ")
       print("The users are encouraged to play the game for fun as well as update/modify the codes as per their interests. ")
       print("Incase of any query or issue with the program make sure to email the same to us at : codraw.official@gmail.com")
       print()
       print("                                                                                              ---Have A  Nice Game --- ")
       print("______________________________________________________________________________________________________________________________________________________")
       print()
       print()
       time.sleep(2)

    def core(self) : # Main Function That Handles And Controls The Flow Of Program
       ob.drama1()
       n=input("      Press Any Key To Continue ---->   ")
       if n : # If User Enters Anything From The Keyboard.
              ob.first_page()
              ob.dev_mess()
              time.sleep(5)
       else : # Incase User Is A Crazy Maniac And Doesn't Input Suitable Input :)
           while True :
                  ob.drama1()
                  n=input("      Press Any Key To Continue ---->   ")
                  if n :
                          break
                  else :
                          continue
           ob.first_page()
           ob.dev_mess()
           time.sleep(5)
       l=ob.user_info()
       ob.space()
       ob.tic_handler(l[0],l[1],l[2],l[-1])

ob=interface()
ob.core()


