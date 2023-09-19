document.addEventListener('DOMContentLoaded', () => {
    const submitBtn = document.querySelector('.form__submit');
    const mainForm = document.querySelector('.form');

    const sendData = async (direction) =>  {
        try {
            const formData = new FormData(mainForm);
            const res = await fetch('http://localhost:8000/auth/', {
                method: 'POST',
                body: JSON.stringify(formData),
                headers: {
                    direction,
                },
                mode: 'no-cors'
            });

            if (!res.ok) {
                throw new Error('Не получилось отправить данные:' + res.status)
            }

            const data = await res.json();
            console.log(data);
        } catch(e) {
            console.error(e.message);
        }
    }

    submitBtn.addEventListener('click', (e) => {
        e.preventDefault();
        const target = e.target;

        if (target.getAttribute('data-btn-type') === 'login') {
            sendData('login');
        } else {
            sendData('register')
        }
    })
});