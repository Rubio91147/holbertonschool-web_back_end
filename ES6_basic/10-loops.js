export default function appendToEachArrayValue(array, appendString) {
  const newArray = array;
  for (const value of array) {
    const idx = newArray.indexOf(value);
    newArray[idx] = appendString + value;
  }

  return newArray;
}
