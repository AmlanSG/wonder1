import string


def main():
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        punc = string.punctuation
        p1 = list (punc)
        print (p1)
        print (type(p1))
        sentence = input('Type what you would like translated into pig-latin and press ENTER: ')
        sentence = sentence.split()
        print("After Split:",sentence)
        st =[]
        for k in range(len(sentence)):
                i = list (sentence[k])
                x = len(i)
                print(i[0])
                if i[0] in vowels:

                        i.append("way")
                        var = "".join(i)
                        st.append(var)

                elif  i[0]  in p1:
                        st.append(i[0])
                else:
                        for j in range(1,x-1):
                                if i[j] in vowels:
                                        var1 =i[j:]+i[:j]+list('ay')
                                        word = "".join(var1)
                                        st.append(word)
                                        print (st)
                        #return
        print (st)
        return ' '.join(st)

if __name__ == "__main__":
        x = main()
        print(x)