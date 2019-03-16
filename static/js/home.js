var offset = 25;

function stripPx(pxValue) {
	var pixels = pxValue.match(/[0-9]*/);
	return parseInt(pixels[0], 10);
}

function appendPx(numValue) {
	return numValue + "px";
}

function enlarge(image) {
	var computedStyles = window.getComputedStyle(image);

	var height = stripPx(computedStyles.height);
	height += (offset * 2);
	image.style.height = appendPx(height);

	var width = stripPx(computedStyles.width);
	width += (offset * 2);
	image.style.width = appendPx(width);
	
	var topOffset = stripPx(computedStyles.top);
	topOffset -= offset;
	image.style.top = appendPx(topOffset);

	var left = stripPx(computedStyles.left);
	var right = stripPx(computedStyles.right);
	
	if (left < right) {
		var leftOffsetValue = left - offset;
		image.style.left = appendPx(leftOffsetValue);
	} else {
		var rightOffsetValue = right - offset;
		image.style.right = appendPx(rightOffsetValue);
	}
}

function resize(image) {
	var computedStyles = window.getComputedStyle(image);

	var height = stripPx(computedStyles.height);
	height -= (offset * 2);
	image.style.height = appendPx(height);

	var width = stripPx(computedStyles.width);
	width -= (offset * 2);
	image.style.width = appendPx(width);
	
	var topOffset = stripPx(computedStyles.top);
	topOffset += offset;
	image.style.top = appendPx(topOffset);
	
	var left = stripPx(computedStyles.left);
	var right = stripPx(computedStyles.right);
	
	if (left < right) {
		var leftOffsetValue = left + offset;
		image.style.left = appendPx(leftOffsetValue);
	} else {
		var rightOffsetValue = right + offset;
		image.style.right = appendPx(rightOffsetValue);
	}
}
