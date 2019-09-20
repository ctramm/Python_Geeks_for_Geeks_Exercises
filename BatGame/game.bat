@echo off
title 'Cameron's Game of Chance'
color 0A
if "%1" neq "" ( goto %1)
echo Welcome to My Game. Please enjoy yourself! :) 
pause

:Menu
cls
echo 1. Start
echo 2. Instructions
echo 3. Exit
set /p Menu_answer= Type the number of your option and press enter.
if %Menu_answer%==1 goto Start_1
if %Menu_answer%==2 goto Instructions
if %Menu_answer%==3 goto Exit

:Exit
cls
echo !~!~!~!~!~!~!~!~!~!~!
echo Thanks for playing!~!
echo !~!~!~!~!~!~!~!~!~!~!
pause
exit /b

:Instructions
cls
echo Please follow the onscreen instructions for each step of the game.
echo. 
pause
goto Menu

REM THE FOLLOWING CODE IS RELATED TO LEVEL 1 OF THE GAME.

:Start_1
cls
echo You have run into bad guys. Their forces are...
goto Troops_1

:Troops_1
set /a Troop1_num=%random%
if %Troop1_num% gtr 4 goto Troops_1
if %Troop1_num% lss 1 goto Troops_1
if %Troop1_num%==1 echo a horde of farmers
if %Troop1_num%==2 echo a few farmers
if %Troop1_num%==3 echo an entire village of farmers
if %Troop1_num%==4 echo a lot of farmers
echo.

echo You have a high chance of winning
echo.
set /p Troop1_answer= Would you like to fight or run?
if %Troop1_answer%==Fight goto Fight_1
if %Troop1_answer%==fight goto Fight_1
if %Troop1_answer%==F goto Fight_1
if %Troop1_answer%==f goto Fight_1
if %Troop1_answer%==Run goto Run_1
if %Troop1_answer%==run goto Run_1
if %Troop1_answer%==R goto Run_1
if %Troop1_answer%==r goto Run_1

:Run_1
cls
echo You ran away safely !
pause
goto Menu

:Fight_1
cls
echo You have chosen to fight.
echo The battle is waging...
echo.
goto Fight_1_Loop

:Fight_1_Loop
set /a Fight1_num=%random%
if %Fight1_num% gtr 4 goto Fight_1_Loop
if %Fight1_num% lss 1 goto Fight_1_Loop
if %Fight1_num%==1 goto Lose_Fight_1
if %Fight1_num%==2 goto win_Fight_1
if %Fight1_num%==3 goto win_Fight_1
if %Fight1_num%==4 goto win_Fight_1

:Lose_Fight_1
cls
echo Sorry, you have lost the battle :(
pause 
goto menu

:Win_Fight_1
cls
echo Congrats, you won the fight!
set /p Win1_answer= Would you like to save?
if %Win1_answer%==Yes goto Save_1
if %Win1_answer%==yes goto Save_1
if %Win1_answer%==Y goto Save_1
if %Win1_answer%==y goto Save_1
if %Win1_answer%==No goto Start_2
if %Win1_answer%==no goto Start_2
if %Win1_answer%==N goto Start_2
if %Win1_answer%==n goto Start_2

:Save_1
cls
echo Your game has been saved.
echo.
echo Do you wish to continue playing or quit?
set /p Save1_answer= Please type '1' and enter to continue or '2' and enter to quit.
if %Save1_answer%==1 goto Start_2
if %Save1_answer%==2 goto Menu

goto Menu

 REM The following code is related to level 2 of the game.

:Start_2
cls
echo Congratulations!~!~! You have reached level 2.
echo.
echo.
echo You have run into bad guys. Their forces are:
goto :Troops_2

:Troops_2
set /a Troop2num=%random%
if %Troop2num% gtr 4 goto Troops_2
if %Troop2num% lss 1 goto Troops_2
if %Troop2num%==1 echo a horde of guards
if %Troop2num%==2 echo a few guards
if %Troop2num%==3 echo an entire army of guards
if %Troop2num%==4 echo a lot of guards
echo.

echo You have a high chance of winning
echo.
set /p Troop2answer= Would you like to fight or run?
if %Troop2answer%==Fight goto Fight_2
if %Troop2answer%==fight goto Fight_2
if %Troop2answer%==F goto Fight_2
if %Troop2answer%==f goto Fight_2
if %Troop2answer%==Run goto Run_2
if %Troop2answer%==run goto Run_2
if %Troop2answer%==R goto Run_2
if %Troop2answer%==r goto Run_2

:Run_2
cls
echo You ran away safely!
pause
goto Menu

:Fight_2
cls
echo You have chosen to fight.
echo.
echo The battle is waging...
goto Fight_2_Loop

:Fight_2_Loop
set /a Fight2num=%random%
if %Fight2num% gtr 4 goto Fight_2_Loop
if %Fight2num% lss 1 goto Fight_2_Loop
if %Fight2num%==1 goto Lose_Fight_2
if %Fight2num%==2 goto win_Fight_2
if %Fight2num%==3 goto win_Fight_2
if %Fight2num%==4 goto win_Fight_2

:Lose_Fight_2
cls
echo Sorry, you have lost the battle :(
pause 
goto menu

:Win_Fight_2
cls
echo Congrats, you won the fight!
set /p Fight2answer= Would you like to save?
if %Fight2answer%==Yes goto Save_2
if %Fight2answer%==yes goto Save_2
if %Fight2answer%==Y goto Save_2
if %Fight2answer%==y goto Save_2
if %Fight2answer%==No goto Start_3
if %Fight2answer%==no goto Start_3
if %Fight2answer%==N goto Start_3
if %Fight2answer%==n goto Start_3

:Save_2
cls
echo Your game has been saved.
echo.
echo Do you wish to continue playing or quit?
set /p Save2answer= Please type '1' and enter to continue or '2' and enter to quit.
if %Save2answer%==1 goto Start_3
if %Save2answer%==2 goto Menu

goto Menu

REM The following code is related to level 3 of the game.

:Start_3
cls
echo Congratulations!~!~! You have reached level 3.
echo.
echo.
echo You have run into bad guys. Their forces are:
goto :Troops_3

:Troops_3
set /a Troop3num=%random%
if %Troop3num% gtr 4 goto Troops_3
if %Troop3num% lss 1 goto Troops_3
if %Troop3num%==1 echo a horde of dragons
if %Troop3num%==2 echo a few dragons
if %Troop3num%==3 echo an entire clan of dragons
if %Troop3num%==4 echo a lot of dragons
echo.

echo You have a high chance of winning
echo.
set /p Troop3answer= Would you like to fight or run?
if %Troop3answer%==Fight goto Fight_3
if %Troop3answer%==fight goto Fight_3
if %Troop3answer%==F goto Fight_3
if %Troop3answer%==f goto Fight_3
if %Troop3answer%==Run goto Run_3
if %Troop3answer%==run goto Run_3
if %Troop3answer%==R goto Run_3
if %Troop3answer%==r goto Run_3

:Run_3
cls
echo You ran away safely!
pause
goto Menu

:Fight_3
cls
echo You have chosen to fight.
echo.
echo The battle is waging...
goto Fight_3_Loop

:Fight_3_Loop
set /a Fight3num=%random%
if %Fight3num% gtr 4 goto Fight_3_Loop
if %Fight3num% lss 1 goto Fight_3_Loop
if %Fight3num%==1 goto Lose_Fight_3
if %Fight3num%==2 goto win_Fight_3
if %Fight3num%==3 goto win_Fight_3
if %Fight3num%==4 goto win_Fight_3

:Lose_Fight_3
cls
echo Sorry, you have lost the battle :(
pause 
goto menu

:Win_Fight_3
cls
echo Congrats, you won the fight!
set /p Win3answer= Would you like to save?
if %Win3answer%==Yes goto Save_3
if %Win3answer%==yes goto Save_3
if %Win3answer%==Y goto Save_3
if %Win3answer%==y goto Save_3
if %Win3answer%==No goto Start_4
if %Win3answer%==no goto Start_4
if %Win3answer%==N goto Start_4
if %Win3answer%==n goto Start_4

:Save_3
cls
echo Your game has been saved.
echo.
echo Do you wish to continue playing or quit?
set /p Save3answer= Please type '1' and enter to continue or '2' and enter to quit.
if %Save3answer%==1 goto Start_4
if %Save3answer%==2 goto Menu

REM THE FOLLOWING CODE IS RELATED TO LEVEL 4 OF THE GAME.

:Start_4
cls
echo Congratulations!~!~! You have reached level 4.
echo.
echo.
echo You have run into bad guys. Their forces are:
goto :Troops_4

:Troops_4
set /a Troop4num=%random%
if %Troop4num% gtr 4 goto Troops_4
if %Troop4num% lss 1 goto Troops_4
if %Troop4num%==1 echo an entire village of cyclops
if %Troop4num%==2 echo a couple of cyclops
if %Troop4num%==3 echo an entire clan of cyclops who are hungry
if %Troop4num%==4 echo a group of cyclops
echo.

echo You have a high chance of winning
echo.
set /p Troop4answer= Would you like to fight or run?
if %Troop4answer%==Fight goto Fight_4
if %Troop4answer%==fight goto Fight_4
if %Troop4answer%==F goto Fight_4
if %Troop4answer%==f goto Fight_4
if %Troop4answer%==Run goto Run_4
if %Troop4answer%==run goto Run_4
if %Troop4answer%==R goto Run_4
if %Troop4answer%==r goto Run_4

:Run_4
cls
echo You ran away safely!
pause
goto Menu

:Fight_4
cls
echo You have chosen to fight.
echo.
echo The battle is waging...
goto Fight_4_Loop

:Fight_4_Loop
set /a Fight4num=%random%
if %Fight4num% gtr 4 goto Fight_4_Loop
if %Fight4num% lss 1 goto Fight_4_Loop
if %Fight4num%==1 goto Lose_Fight_4
if %Fight4num%==2 goto win_Fight_4
if %Fight4num%==3 goto win_Fight_4
if %Fight4num%==4 goto win_Fight_4

:Lose_Fight_4
cls
echo Sorry, you have lost the battle :(
pause 
goto menu

:Win_Fight_4
cls
echo Congrats, you won the fight!
set /p Win4answer= Would you like to save?
if %Win4answer%==Yes goto Save_4
if %Win4answer%==yes goto Save_4
if %Win4answer%==Y goto Save_4
if %Win4answer%==y goto Save_4
if %Win4answer%==No goto Start_5
if %Win4answer%==no goto Start_5
if %Win4answer%==N goto Start_5
if %Win4answer%==n goto Start_5

:Save_4
cls
echo Your game has been saved.
echo.
echo Do you wish to continue playing or quit?
set /p Save4answer= Please type '1' and enter to continue or '2' and enter to quit.
if %Save4answer%==1 goto Start_5
if %Save4answer%==2 goto Menu

:Start_5
echo More content coming soon!...
pause
goto exit

