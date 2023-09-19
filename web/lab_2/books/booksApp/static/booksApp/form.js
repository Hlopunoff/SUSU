document.addEventListener('DOMContentLoaded', () => {
    const submitBtn = document.querySelector('.form__submit');

    const getFormData = () => {
        const form = document.querySelector('.form');
        const formData = new FormData(form);
        console.log(formData.get('descr'));
    };

//    submitBtn.addEventListener('click', (e) => {
//        e.preventDefault();
//
//        getFormData();
//    });
});