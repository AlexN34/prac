
function palindrome(str) {
  // Good luck!
  str = str.replace(/[^A-Za-z0-9]/g, '');
  for (var i =0; i < str.length; i++) {
    if (i)
      if (str[i].toLowerCase() != str[str.length - i - 1].toLowerCase()) {
        return false;
      }
  }
  return true;
}



// palindrome("eye");
// palindrome("eye") should return a boolean.
//   palindrome("eye") should return true.
//   palindrome("_eye") should return true.
//   palindrome("race car") should return true.
//   palindrome("not a palindrome") should return false.
//   palindrome("A man, a plan, a canal. Panama") should return true.
//   palindrome("never odd or even") should return true.
//   palindrome("nope") should return false.
//   palindrome("almostomla") should return false.
//   palindrome("My age is 0, 0 si ega ym.") should return true.
