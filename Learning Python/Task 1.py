def word_distribution(text_string):
    ketqua={}    
    y=text_string.split(" ")
    for index in range(0,len(y)):
        z=0
        y[index]=y[index].lower()
        if str.isalpha(y[index][-1])==False:
            y[index]=y[index][0:-1]
        for index2 in range(0,len(y)):
            y[index2]=y[index2].lower()
            if str.isalpha(y[index2][-1])==False:
                y[index2]=y[index2][0:-1]
            if y[index2]==y[index]:
                z=z+1
                ketqua[y[index2]]=z    
    return (ketqua)