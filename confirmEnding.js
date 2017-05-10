
function confirmEnding(str, target) {
  // "Never give up and good luck will find you."
  // -- Falcor
  var indexOffset = target.length * -1;
  return Boolean(str.substr(indexOffset) === target);
}


confirmEnding("Bastian", "n");
