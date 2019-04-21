module P004.Solution where
import Data.List
list :: (Num a, Ord a, Enum a) => [a]
list = reverse $ sort [x*y | x <- [999,998..100], y<-[999,998..100], x >= y]

palindrome ::(Show a) => a -> Bool
palindrome x = s == reverse s
     where s = show x

ans :: [a] -> (a -> Bool) -> a
ans (x:xs) f = if f x then x else ans xs f

answer ::(Num a, Ord a, Enum a, Show a) => a
answer = ans list palindrome

-- More elegant and faster solution, from the fact that abccba = 11(9091a + 910b + 100c)
answer2 = head [m | a <- [9], b <- [0..9], c<-[0..9], m <- [100001*a + 10010*b + 1100*c], [x|x<-[100..999], m `mod` x ==0 && m `div` x < 1000] /= []]