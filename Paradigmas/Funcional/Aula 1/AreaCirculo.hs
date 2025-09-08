areaCirculo:: Float -> Float
areaCirculo r = pi*r^2


main::IO()
main = do
    print(areaCirculo 10)