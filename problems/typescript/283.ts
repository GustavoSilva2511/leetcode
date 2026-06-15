/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
    let left = 0;
    let right = 0;
    
    while(right < nums.length && left < nums.length) {
        if (nums[left] != 0) {
            left++;
        } else if (nums[right] == 0 || right < left) {
            right++;
        } else {
            nums.splice(left, 1, nums[right]);
            nums.splice(right, 1, 0);
            right++;
        }
    }
};

const s = [1, 0];
moveZeroes(s);
console.log(s)
