/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
    let aux: string;
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        aux = s[left];
        s.splice(left, 1, s[right]);
        s.splice(right, 1, aux);

        left++;
        right--;
    }
};

const s = ["h","e","l","l","o"];
reverseString(s);
console.log(s);