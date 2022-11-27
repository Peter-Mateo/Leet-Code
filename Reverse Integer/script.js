var reverse = function(x) {
    if(x == 0){
        return 0;
    }
    let str = x.toString();
    let len = str.length;
    let last = "";
    if(str.includes("-")){
        last += "-"
        str.replace(str[0], '');
    };
    for (let i = len - 1; i >= 0; i--) {
        if(str[i] == "-"){
            continue;
        }
        last += str[i];
    };
    if (last > 2147483647 || last < - 2147483647){
        console.log("0")
        return 0;
    }
    return last;
};
reverse(-1534236469);