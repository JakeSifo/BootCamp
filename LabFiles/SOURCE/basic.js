var arr = [1,2,3,4,5,6]
function sumit(a){
    var sum = 0;
    for (var i= 0; i < a.length; i++) {
        sum += a[i];
    }
    console.log('The sum of a is ' + sum);
}

function f1(a, f){
    f(a);
}