exports.charCount = function(string) {
    //turning string into object of occurences
    let charObj = {}
    for(let i = 0; i < string.length ; i++){
        if(string[i] != " "){
            charObj.hasOwnProperty(string[i])? charObj[string[i]]++ : charObj[string[i]] = 1
        }
    }
    //turn object into an array
    let charArray = Object.entries(charObj)
    //sort array and return sorted array
    let result = charArray.sort(function (a,b){
        if (a[1] === b[1] ){
            if (a < b){return -1}
        }
         if (a[1] < b[1] ) {return 1}
         if (a[1] > b[1] ) {return -1}
    }
    )
return result    
};
