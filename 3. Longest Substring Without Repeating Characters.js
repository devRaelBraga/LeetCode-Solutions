/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let currentSubstring = ''
    let longestSubstring = ''

    for (let i = 0; i < s.length; i++) {
        if(!currentSubstring.includes(s[i])) {
            currentSubstring += s[i]
        }
        else {
            currentSubstring = currentSubstring.slice(currentSubstring.indexOf(s[i]) + 1) + s[i]
        }
        if(currentSubstring.length > longestSubstring.length) {
            longestSubstring = currentSubstring
        }
    }

    return(longestSubstring.length)
};
