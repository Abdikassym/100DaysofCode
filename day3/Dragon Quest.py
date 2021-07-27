print('''
                        /\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \_} '  {        /~\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                 -sjm
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
     ` ``

''')
print("Welcome to the Dragon Quest.")
print("Your mission is to find and kill a dragon.\n") 


# creatures HP
player = 5


# Start a game

step1 = input("You just have left you castle and heading to dragon mountain\nYour path divides by 3, which way will you choose? Right - Left - Center\n")
step1 = step1.lower()


if step1 == "right":
  print("\nYOU CAME TO A WRONG HOUSE, FOOL! (Game over)")

elif step1 == "center":
  print("\nYou met sirens, who charmed you. Now you are seeing dreams forever... (Game over)")

else:
  print("\nRight Choice! Now you see 2 treasures in front of you!\nThere is a sign, which says 'Choose wisely, it will affect your future...'")
  
  
  treasure = input("Which treasure will you choose? Blue one or Red one?\n")
  if treasure.lower() == 'red':
    print("\nThis treasure is an arrow trap! You did not manage to evade an arrow... (Game Over)")
  else:
    player += 1
  

    print("\nYou made you choice. Now you see a dragon's cave and you are heading towards it...")
    print("BOOOM!")
    print('''

                                            ,   ,
                                            $,  $,     ,
                                            "ss.$ss. .s'
                                    ,     .ss$$$$$$$$$$s,
                                    $. s$$$$$$$$$$$$$$`$$Ss
                                    "$$$$$$$$$$$$$$$$$$o$$$       ,
                                  s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s
                                  s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,
                                  s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"
                                s$$$$$$$$$$'         `"""ss"$"$s""
                                s$$$$$$$$$$,              `"""""$  .s$$s
                                s$$$$$$$$$$$$s,...               `s$$'  `
                            `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-
                              `""""$$$$$$$$$$$$$$$$$$$$#####$$$$$$"     $.$'
                                    "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|
                                      "$$$$$$$$$$$$$$$$$$$$$$$$##s    .$$" $
                                      $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `
                                      $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""'
                                ,   ,"     '  $$$$$$$$$$$$$$$$####s
                                $.          .s$$$$$$$$$$$$$$$$$####"
                    ,           "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"
                    $           .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"
                    Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""
                      "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"
              ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'
              $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,
              $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$
                "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$
                  $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.
      )          $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.
      ((          $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$
      ) \         $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
    (   )        $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$'
    )  ( (       $$"$$$$$$$$$$$#####.$$$$$###' -Tua Xiong     .###$$$$$$$$$$"
    (  )  )   _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$
    ) (  ( \.         "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"
    (   )$ )  )        ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"
    (   ($$  ( \     _sS"  `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,
    )  )$$$s ) )  .      .   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'  `$$
      (   $$$Ss/  .$,    .$,,s$$$$$$##S$$$$$$$$$$$$$$$$$$$$$$$$S""        '
        \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$        `$$.        `$$.
            `"S$$$$$$$$$$$$$$$$$#"      $          `$          `$
                `"""""""""""""'         '           '           '
                ''')
    print("OMG! THERE IS A HUGE DRAGON! BE CAREFUL!")
    print("\nIF YOU WANT TO LIVE, YOU MUST ANSWER MY QUESTIONS AND I WILL DECIDE IF YOU ARE WORTH TO LIVE!")
    
    
    # Fight the dragon
    
    question1 = int(input("TELL ME! WHAT IS 2 + 2 * 2, MORTAL?\n"))
    if question1 == 6:
      player += 1
    else:
      player -=1
    
    
    question2 = input("WELL, WELL... NOW TELL ME THE NAME OF A CAPITAL OF GREAT BRITAIN KINGDOM!\n")
    if question2.lower() == "london":
      player += 1
    else:
      player -=1


    question3 = input("THERE IS A MASTERPIECE CALLED MONA LISA, WHICH WAS MADE BY A HUMAN. WHAT WAS HIS NAME?\n")
    if question3.lower() == "leonardo da vinci":
      player += 1
    else:
      player -=1


    question4 = int(input("DO YOU EVEN KNOW HOW MANY WORLDS (Planets) ARE THERE IN OUR DIMENSION!?(Solar System, exclude Pluto)\n"))
    if question4 == 8:
      player += 1
    else:
      player -=1


    question5 = input("I SEE... NOW, WHAT IS THE NAME OF CREATOR OF THIS WORLD? THAT ALL I HAD TO ASK...\n")
    if question5.lower() == "abdikassym" or question5.lower() == "abdikasym":
      player += 1
    else:
      player -=1


    print("\nNow, Dragon decides if it is worth to leave you alive or not...")
    print("(Your score has been calculated since the start of you game).\n\nIf you manage to have more than 9 points, then you win!")

    print(f"\nYour current score is {player}!")
    if player >= 9:
      print("Well done! You have beaten a dragon!")
    else:
      print("You were not strong enough. Dragon has consumed you...\n___GAME___OVER___")















