function solution(N, stages) {
    var answer = [];
    
    for(var i=1;i<=N;i++){
        var n = stages.length;
        stages = stages.filter((s) => s !== i);
        answer.push([i, (n-stages.length)/n]);
    }
    
    answer.sort((a,b) => { return b[1] - a[1];});
    return answer.map((a) => a[0]);
}