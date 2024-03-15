/***
 * Script to implement edit/delete functinality for TripComment model
 *  - Use event listeners to edit/delete buttons for all TripComments
 *  - Edit: 
 *      - Populate new tripcomment form with body of comment to edit
 *      - Change submit button to update with action targeting edit view
 *  - Delete:
 *      - Get ID of comment that user wishes to delete
 *      - Change target of delete button to reflect this
 *      - Display delete modal
 */
const editButtons = document.getElementsByClassName('btn-edit');
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById('commentForm');
const submitButton = document.getElementById('submitButton');

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Edit event listeners

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let tripcommentId = e.target.getAttribute("comment_id");
        let tripcommentContent = document.getElementById(`comment${tripcommentId}`).innerText;
        commentText.value = tripcommentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_tripcomment/${tripcommentId}`);
    });
}

// Delete event listeners
console.log(window.location.pathname)
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let tripcommentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `delete_tripcomment/${tripcommentId}`;
      deleteModal.show();
    });
  }