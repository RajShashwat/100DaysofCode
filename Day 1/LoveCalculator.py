print('''        hugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&
        &            hugs&kisses&hugs&kisses&hu         &hugs&kisses
        s&h        es&hugs&kisses&hugs&kiss                 gs&kisse
        es&h      sses&hugs&kisses&hugs&k                     s&kiss
        ses&      isses&hugs&kisses&hugs            &kiss      s&kis
        sses      kisses&hugs&kisses&hu           ugs&kiss      s&ki
        isse      &kisses&hugs&kisses&h          &hugs&kiss     gs&k
        kiss      s&kisses&hugs&kisses&         es&hugs&kis     ugs&
        &kis      gs&kisses&hugs&kisses        sses&hugs&k      hugs
        s&ki      ugs&kisses&hugs&kisse       kisses&hugs       &hug
        gs&k      hugs&kisses&hugs&kiss      s&kisses&hu        s&hu
        ugs&      &hugs&kisses&hugs&kis     ugs&kisses&         es&h
        hugs      s&hugs&kisses&hugs& i     hugs&kisse          ses&
        &hug      es&hugs&kisses&hug  k      hugs&kis           sses
        s&hu      ses&hugs&kisses&h   &       hugs&             isse
        es&h      sses&hugs&kisse     s&                       &kiss
        s                             gs&ki                 hugs&kis
        s                             ugs&kisse         sses&hugs&ki
        i             ses&h                                        k
        k             sses&                                        &
        &kis      gs&kisses&hug   isses&hugs      s&hugs&kisse     s
        s&kis      gs&kisses&h   &kisses&hug      es&hugs&kisses   g
        gs&ki      ugs&kisses&   s&kisses&hu      ses&hugs&kisses  u
        ugs&ki      ugs&kisse   ugs&kisses&h      sses&hugs&kisses h
        hugs&k      hugs&kiss   hugs&kisses&      isses&h gs&kisses&
        &hugs&k      hugs&ki   s&hugs&kisses      kisses  ugs&kisses
        s&hugs&      &hugs&k   es&hugs&kisse              hugs&kisse
        es&hugs&      &hugs   sses&hugs&kiss      s&kiss  &hugs&kiss
        ses&hugs      s&hug   isses&hugs&kis      gs&kiss s&hugs&kis
        sses&hugs      s&h   &kisses&hugs&ki      ugs&kisses&hugs& i
        isses&hug      es&   s&kisses&hugs&k      hugs&kisses&hug  k
        kisses&hug      e   ugs&kisses&hugs&      &hugs&kisses&h   &
        &kisses&hu          hugs&kisses&hugs      s&hugs&kisse     s
        s&kisses&hu        s&hugs&kisses                           g
        gs&kisses&h        es&hugs&kisse                           u
        ugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&hugs&kisses&h''')

print("Welcome to the Love Calculator")

name1 = input("Enter your name: \n")
name2 = input("Enter your partener's name: \n")

combined_name = name1 + name2

combined_name.lower()

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

true = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

love = l + o + v + e

message = f"Your Love Score is : {str(true) + str(love)}"

print(message)


