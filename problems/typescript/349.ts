function intersection(nums1: number[], nums2: number[]): number[] {
    const response: number[] = [];
    const minor = nums1 < nums2 ? nums1 : nums2;
    const bigger = nums1 > nums2 ? nums1 : nums2;

    let left = 0;
    let right = minor.length - 1;

    while (left <= right) {
        
        if (bigger.includes(minor[left]) && !response.includes(minor[left])) {
            response.push(minor[left]);
        }

        if (bigger.includes(minor[right]) && !response.includes(minor[right])) {
            response.push(minor[right]);
        }

        left++;
        right--;
    }
    return response;
};

console.log(intersection([1, 2, 2, 1], [2, 2]))