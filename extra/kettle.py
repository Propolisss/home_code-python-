n = int(input()) #количество бутылок, которые друзья взяли с собой.
a = int(input()) #количество литров воды, которые вмещает одна бутылка.
x = int(input()) #количество литров воды, которое необходимо, чтобы промыть чайник.
m = int(input()) #количество людей, которые пойдут на пикник.
l = ((n * a) - x) // m

print(l)