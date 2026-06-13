function reverseVowels(s: string): string {
    const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    let splited = s.split("");

    let left = 0;
    let right = s.length - 1;
    let aux: string;

    while (left < right) {
        if (!vowels.includes(s[left])) {
            left++;
        } else if (!vowels.includes(s[right])) {
            right--;
        } else {
            aux = s[left];
            splited.splice(left, 1, s[right]);
            splited.splice(right, 1, aux);

            left++;
            right--;
        }  
    }

    return splited.join("");
};

console.log(reverseVowels("IceCreAm"));