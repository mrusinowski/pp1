from QuadraticEquation import *

a,b,c = czytajWspolczynniki()
delta = obliczDelte(a,b,c)
x1,x2 = obliczPierwiastki(a,b,delta)
wyswietlPierwiastki(x1,x2)