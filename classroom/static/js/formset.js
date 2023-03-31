document.addEventListener("DOMContentLoaded", () => {
    let addTopicButton = document.getElementById("addTopicButton");
    let formsetItems = document.querySelectorAll(".formset-item");
    let totalForms = document.getElementById("id_form-TOTAL_FORMS");
    let formsetContainer = document.querySelector(".formsets");
    let numForm = formsetItems.length - 1;


    function addTopic(event) {
        event.preventDefault();
        let newForm = formsetItems[0].cloneNode(true);

        let formRegex = RegExp(`form-(\\d)+-`,'g');

        numForm++;
        newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${numForm}-`);
        formsetContainer.insertBefore(newForm, addTopicButton);
        totalForms.setAttribute("value", `${numForm +1}`);
    }

    addTopicButton.addEventListener("click", addTopic);
})
