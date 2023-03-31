document.addEventListener("DOMContentLoaded", () => {
    let addCommentButton = document.getElementById("addComment");
    let commentInput = document.getElementById("commentInput");
    let listComments = document.getElementById("listComments");
    let addCommentUrl = getPyData("add_comment_url");
    let csrftoken = getCookie("csrftoken");

    function addComment(event) {
        event.preventDefault();
        axios({
            url: addCommentUrl,
            method: "post",
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                "X-CSRFToken": csrftoken
            },
            data: {
                "comment": commentInput.value,
            },
        })
            .then((response) => {
                let template = document.createElement("template");
                template.innerHTML = response.data;
                listComments.appendChild(template.content.firstChild);
                commentInput.value = "";
            })
    }

    addCommentButton.addEventListener("click", addComment)

})