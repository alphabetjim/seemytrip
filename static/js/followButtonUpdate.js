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
    console.log(uName)
    const followButtons = document.getElementsByClassName('link-follow')
    const followersParas = document.getElementsByClassName('followersP')
    for (para of followersParas){
        console.log(para.innerText)
    }
    let underscoreIndex = followersParas[0].id.indexOf('_')+1
    let i=0;
    let followButtonId=0;
    while (i<followersParas.length) {
        let id = followButtons[followButtonId].id
        console.log(id)
        
        let followText = followersParas[i].innerText
        let followersParasId = followersParas[i].id.substring(underscoreIndex)

        console.log(`${id} vs ${followersParasId}: ${id==followersParasId}`)
        console.log(followText)
        if(id == followersParasId){

            if (followText.includes(uName)){
                followButtons[followButtonId].innerText = "Following"
            }
            followButtonId++
        }
        i++
        
    }
}