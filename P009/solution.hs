list = [(a,b,c) | a<-[1..997], b<-[a..998], c <- [1000 - a -b], a+b+c==1000, a*a+b*b==c*c]

ans (a,b,c) = a*b*c

answer = ans (head list)