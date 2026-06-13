function isHappy(n: number): boolean {
    let currNumber: string = n.toString();
    const ocurrences: string[] = [];

    while (currNumber != "1") {
        if (ocurrences.includes(currNumber)) {
            return false;
        }
        ocurrences.push(currNumber);

        const newNumberList = currNumber.split("").map(char => Math.pow(parseInt(char), 2));

        currNumber = newNumberList.reduce((acumulator, currentValue) => {
            return acumulator + currentValue;
        }, 0).toString();
    }

    return true;
};

console.log(isHappy(2));