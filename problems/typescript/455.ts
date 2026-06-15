function findContentChildren(g: number[], s: number[]): number {
	let gp = 0;
	let sp = 0;
	let childs = 0;

	g = g.sort((a, b) => b - a)
	s = s.sort((a, b) => b - a)

	while (gp < g.length) {
		
		if (g[gp] <= s[sp]) {
			childs++;
			gp++;
			s.splice(sp, 1);
			sp = 0;
		} else if (sp < s.length){
			sp++;
		} else {
			gp++;
			sp = 0;
		}
	}

	return childs;
};
const g = [1, 2 ,3]
const s = [1, 1]
console.log(findContentChildren(g, s))