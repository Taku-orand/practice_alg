# void call(int n){
#   int i = 1;
#  CHECK_NUM:
#   int x = i;
#   if ( x % 3 == 0 ){
#     cout << " " << i;
#     goto END_CHECK_NUM;
#   }
#  INCLUDE3:
#   if ( x % 10 == 3 ){
#     cout << " " << i;
#     goto END_CHECK_NUM;
#   }
#   x /= 10;
#   if ( x ) goto INCLUDE3;
#  END_CHECK_NUM:
#   if ( ++i <= n ) goto CHECK_NUM;

#   cout << endl;
# }
n = int(input())
x = 0

for i in range(1,n+1):
    if i%3 == 0:
            print(" %d"%i,end = "");
    else:
        x = i
        while (x):
            if x%10 == 3:
                print(" %d"%i,end = "")
                break
            x //= 10
print()