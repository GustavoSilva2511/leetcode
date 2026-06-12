function strStr(haystack: string, needle: string): number {
    let p1: number = 0;
    let size: number = needle.length;

    if (haystack.length < 1) {
        return -1;
    }

    while (p1 + size <= haystack.length) {
        if (haystack.slice(p1, p1+size) == needle) {
            return p1;
        }
        p1++;
    };
    return -1;
};

const res = strStr("sadbutsad", "sad")
console.log(res)