hipotenusa::Float -> Float -> Float
hipotenusa a b = sqrt((a^2) + (b^2))

main::IO()
main = do
    print(hipotenusa 3 4)