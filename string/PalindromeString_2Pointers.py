s = input()
def Palindrome(s):
  l = 0
  r = len(s)-1
  while l<r:
      if( s[l].isalnum() and s[r].isalnum()):
          if(s[l].casefold() != s[r].casefold()):
              return "false"
              break
          l = l+1
          r = r-1
      elif(s[l].isalnum()):
          r = r-1
      else:
          l = l+1
  return "true"
result = Palindrome(s)
print(result)