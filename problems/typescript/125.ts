function isPalindrome(s: string): boolean {
    let start = 0;
    let last = s.length - 1;

    const regex = /[a-z0-9]/i

    while (start <= last) {
        let currFirst = s[start];
        let currLast = s[last];

        if(!regex.exec(currFirst)) {
            start++;
        } else if (!regex.exec(currLast)) {
            last--;
        } else {
            if (currFirst.toLocaleLowerCase() != currLast.toLocaleLowerCase()) {
                return false;
            }
            start++;
            last--;
        }
    }
    return true;
};

console.log(isPalindrome("A man, a plan, a canal: Panama"))
