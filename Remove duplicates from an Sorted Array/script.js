var removeDuplicates = function(nums) {
    for (let a = 0; a < nums.length; a++) {
        k = 0;
        if (a == 0){
            continue;
        }
        for(b = 0; b < nums.length; b++) {
            if (nums[a] == nums[b]){k++};
        }
    }
    return k;
};

nums = [1,1,2];
expectedNums = [1,2];

k = removeDuplicates(nums);

/*
console.log(nums)

console.log(k.length + " " + expectedNums.length)

console.log(k == expectedNums.length)

for(let i = 0; i < k; i++) {

    console.log(nums[i] == expectedNums[i]);

} */