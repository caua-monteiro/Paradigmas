areaCirculo:: Float -> Float
areaCirculo r = pi*r^2

diferencaCirculo:: Float -> Float -> Float
diferencaCirculo a b = (areaCirculo a) - (areaCirculo b)

main::IO()
main = do
    print(areaCirculo 10)
    print(diferencaCirculo 4 2)