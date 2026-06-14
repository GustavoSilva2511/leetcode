function isSubsequence(s: string, t: string): boolean {
    let ps = 0;
    let pt = 0;

    if (s.length == 0) {
        return true
    }
    


    while (pt < t.length) {
        if(s[ps] == t[pt]) {
            ps++;
        }

        if (ps == s.length) {
            return true;
        }

        pt++;
    }

    return false;
};

const s = "abc";
const t = "ahbgdc";

console.log(isSubsequence(s, t));