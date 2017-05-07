//assume lowest n is 0
function largestOfFour(arr) {
  var cur; var max = '\0'; var final = [];
  arr.forEach(function(sub){
    sub.forEach(function(num){
      if (max === '\0') {
        max = num;
      } else {
        if (max > num) {
          max = num;
        }
      }
    });
    final.push(max);
    max = '\0';

  });
}


largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
