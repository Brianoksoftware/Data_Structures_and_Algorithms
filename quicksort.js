//Quicksort algorithm recursive implementation
	function quicksort(arr){
		if(arr.length <= 1){
			return arr;
		}
		else{
			const pivot = arr[Math.floor(arr.length/2)];
			const lesser = [];
			const greater = [];

			for(let m = 0; m < arr.length; m++){
				if(arr[m] < pivot){
					lesser.push(arr[m]);
				}
				else if(arr[m] > pivot){
					greater.push(arr[m]);
				}
			}
			return quicksort(lesser).concat(pivot, quicksort(greater));
		}
	}
	console.log("Quicksort results: " + quicksort([3,4,1,7,0,2,5]));

	
	//Quicksort algorithm in ES6 recursively...using Arrow functions
	const quicksrrt = array => { 
		if(array.length <= 1){
			return array;
		}
		else{
			const pivot = array[Math.floor(array.length/2)];
			const left =[];
			const right =[];

			for(i=0; i<array.length; i++){
				if(array[i] < pivot){
					left.push(array[i]);
				}
				else if(array[i]>pivot){
					right.push(array[i]);
				}
			}
			return quicksrrt(left).concat(pivot, quicksrrt(right));
		}
	}
	console.log("result:" + quicksrrt([3,1,2,4,0]));



//quicksort algorithm in ES6 using recursion...mastery 1
arr = [4,3,2,1];

const quicksort = (arr) => {
    if(arr.length <= 1){
        return arr;
    }
    //choosing middle index
    const pivot =arr[Math.floor(arr.length/2)];
    const lesser = [];
    const greater = [];
    
    for(let x=0;x<arr.length;x++){
        if(arr[x] < pivot){
            lesser.push(arr[x]);
        }
        else if(arr[x] > pivot){
            greater.push(arr[x]);
        }
    }
    return quicksort(lesser).concat([pivot], quicksort(greater));
}

console.log("Quicksorted array:", quicksort(arr))

