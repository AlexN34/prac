
function titleCase(str) {
  var words = str.split(" ");
  var final = [];
  words.forEach(function(word) {
    final.push(word[0].toUpperCase() + word.substr(1, word.length - 1).toLowerCase());
  });
  str = final.join(" ");
  return str;
}

titleCase("I'm a little tea pot");
