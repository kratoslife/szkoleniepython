from pathlib import Path

with open("E:\\Seriale\\pliczki\\wynik.txt", mode="w") as f2:

    sumacalkowita=0

    for p in Path('E:\\Seriale\\pliczki').iterdir():

        sum = 0

        with open(p) as f:

            for l in f.readlines():

                sum = sum + int(l)
                print("linie w pliku",l)

        sumacalkowita+=sum
        print("suma w pliku",sum,p,file=f2)

    print("suma calkowita",sumacalkowita,file=f2)