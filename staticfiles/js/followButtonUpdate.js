/**
 * Script to adjust follow button display to account for whether user is 
 * already following trip
 * - Check whether user is logged in
 * - If si, get username from page
 * - Get all follow buttons on the page
 * - Loop through follow buttons, accessing the paragraph containing 
 *   the followers of each trip.
 * - If the innerText of that paragraph contains the logged-in username,
 *   change the follow button text to 'Following'
 */
const loginStatus = document.getElementById("loginStatus")
const loginStatusString = loginStatus.innerText
if (loginStatusString.includes('logged in')){
    let uNameIndex = loginStatusString.indexOf('as') + 3
    const uName = loginStatusString.substring(uNameIndex)
    
    const followButtons = document.getElementsByClassName('btn-follow')
    for (let i=0; i<followButtons.length; i++) {
        let followP = document.getElementById(`followers_${i+1}`)
        let followText = followP.innerText
        console.log(followP.innerText)
        if (followText.includes(uName)){
            followButtons[i].innerText = "Following"
        }
    }
}