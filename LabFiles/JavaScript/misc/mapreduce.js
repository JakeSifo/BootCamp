/*
 * An educational MapReduce framework implemented in Javascript
 * https://code.google.com/p/mapreduce-js/
 * 
 */
let mapreduce = function (data, map, reduce) {
	let mapResult = [], reduceResult = [];
	let mapIx, reduceKey;
	
	let mapEmit = function(key, value) {
		if(!mapResult[key]) {
			mapResult[key] = [];
		}
		mapResult[key].push(value);
		console.log("Map phase:: Occurrences of key [" + key + "] : " + mapResult[key]);
	};
	
	let reduceEmit = function(obj) {
		reduceResult.push(obj);
		console.debug("Reduce phase:: " + JSON.stringify(reduceResult));
	};
	
	for(mapIx = 0; mapIx < data.length; mapIx++) {
		map(data[mapIx], mapEmit);
	}
	
	for(reduceKey in mapResult) {
		reduce(reduceKey, mapResult[reduceKey], reduceEmit);
	}
	
	return reduceResult;
};