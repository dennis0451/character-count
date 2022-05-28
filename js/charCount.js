exports.charCount = function(string) {
    //sort array and return sorted array
    let charObj = {}
    for(let i = 0; i < string.length ; i++){
        if(charObj.hasOwnProperty(string[i])){
            charObj[string[i]] += 1
        }else{
            charObj[string[i]] = 1
        }
    }
    return Object.entries(charObj)
};
