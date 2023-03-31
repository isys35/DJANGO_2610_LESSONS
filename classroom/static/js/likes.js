document.addEventListener("DOMContentLoaded", () => {
    let addLikeButtons = document.querySelectorAll(".add-like");

    function like(event) {
        event.preventDefault();
        let parent = event.target.closest(".like");
        let addLikeUrl = parent.getAttribute("data-like-url");
        let csrftoken = getCookie("csrftoken");

        axios({
            url: addLikeUrl,
            method: "post",
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                "X-CSRFToken": csrftoken
            },
        })
            .then((response) => {
                let countLikes = parent.querySelector(".count-likes")
                countLikes.innerHTML = response.data;
            });
    }

    addLikeButtons.forEach((btn) => {
        btn.addEventListener("click", like);
    })
})