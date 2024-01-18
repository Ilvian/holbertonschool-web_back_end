export default function appendToEachArrayValue(array, appendString) {
    const myValue = [];
    for (const idx of array) {
        myValue.push(appendString + idx);
    }
    return myValue;
};