collatz x = collatzUtil x 1

collatzUtil x n
   | x == 1 = n
   | mod x 2 == 1 = collatzUtil (3*x+1) (n+1)
   | otherwise = collatzUtil (div x 2) (n+1)

answer = (maximum . map (\x -> (collatz x, x)) ) [1..999999]

-- Takes 150 seconds. lol.