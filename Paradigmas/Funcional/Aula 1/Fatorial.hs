fatorial:: Int -> Int
fatorial n 
    | n == 1 = 1
    | otherwise = n * fatorial (n-1)
    
main:: IO ()
main = do
    print(fatorial 6)
