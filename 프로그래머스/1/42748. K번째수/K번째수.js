function solution(array, commands) {
    var ans=[];
    
    for(let command of commands){
        var start = command[0];
        var end = command[1];
        var index = command[2];
        var newArr = array.slice(start-1, end);
        newArr.sort((a,b)=>{return a-b;});
        ans.push(newArr[index-1]);
    }
    
    return ans;
}