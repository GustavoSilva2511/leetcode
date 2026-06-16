function flipAndInvertImage(image: number[][]): number[][] {
    let left = 0;
    let right = 0;
    let aux;
    const reversed = [1, 0]

    image.forEach((row) => {
        left = 0;
        right = row.length - 1;

        while (left <= right) {
            aux = row[right];
            row.splice(right, 1, reversed[row[left]]);
            row.splice(left, 1, reversed[aux]);
            left++;
            right--;
        }
    })
    return image
}

const image = [[1, 1, 0], [0, 0, 1]];
console.log(flipAndInvertImage(image))