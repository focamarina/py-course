myStr = 'hello world';

##############################################################

#View the methods of str
print(dir(myStr));

##############################################################

#Apply the str methods
print(myStr.upper());
print(myStr.title());
print(myStr.lower());
print(myStr.swapcase());
print(myStr.capitalize());
print(myStr.replace('hello','bye').upper());