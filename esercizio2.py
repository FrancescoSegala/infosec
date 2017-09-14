import sys


def substitution(in_path, out_path,mapdiz, o_flag):
    encr=open(in_path,"r").read()
    decrypted=open(out_path,"w+")
    for letter in encr :
        if letter.isalpha() :
            resletter=mapdiz[letter]
            decrypted.write(resletter)
        elif o_flag:
            decrypted.write(letter)
        else :
            continue


def main():
    encrypted_txt="enc1.txt"
    plaintext="res.txt"
    in_path=plaintext
    out_path=encrypted_txt
    o_flag=False
    d_flag=False
    mapped_key="uoieazyxwvtsrqpnmlkjhgfdcb" #the default one
    origin_key="abcdefghijklmnopqrstuvwxyz"
    diz={}
    if len(sys.argv) == 3:
        mapped_key=sys.argv[2]
    elif len(sys.argv)== 4 :
        mapped_key=sys.argv[3]
    else:
         mapped_key=sys.argv[1]

    for arg in sys.argv :
        if arg == "-o":
            o_flag=True
            mapped_key_capital=mapped_key.upper()
            mapped_key=mapped_key+mapped_key_capital
            origin_key_capital=origin_key.upper()
            origin_key=origin_key+origin_key_capital
        if arg == "-d":
            d_flag=True
            in_path=encrypted_txt
            out_path=plaintext

    if d_flag:
        for index in range(0,len(mapped_key )):
            diz[mapped_key[index]] = origin_key[index]
    else :
        for index in range(0,len(mapped_key )):
            diz[origin_key[index]] = mapped_key[index]

    substitution(in_path,out_path,diz,o_flag)



if __name__ == "__main__":
    main()
