let arr = [45,112,21,5,8,9,56,0,46];
arr.sort((a,b) => a-b);

console.log(`sorted Array:${arr}`);

let start = 0;
let mid = Math.floor(arr.length / 2)
let end = arr.length;

let search = 56;

while ( start < end) {
	if (arr[mid] > search) {
		let temp = end;
		end = mid;
		mid = Math.floor(temp / 2)
	} 

	if (arr[mid] < search) {
		start = mid;
		mid = Math.floor(end - start / 2);
	}

	if (arr[mid] === search) {
		console.log(arr);
		console.log(`${search} is present in the array at ${mid}`);
		return;
	}
}

