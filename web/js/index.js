document.body.onload = () => {

    let txt1 = document.querySelector('#txt1');
    let div1 = document.querySelector('#div1');
    let loading = document.querySelector('.loading');
    txt1.onkeydown = (e) => {
        if (e.keyCode == 13) {
            let prompt = txt1.value.trim();
            txt1.value = '';
            if (prompt) {

                txt1.disabled = true;
                div1.innerHTML += '<p class="title_you"> You&nbsp;&nbsp;' + new Date().toLocaleTimeString() + '</p>';
                div1.innerHTML += '<p class="message"> ' + prompt + '</p><br>';
                div1.scrollTop = div1.scrollHeight;

                loading.style.display = 'block';
                var formdata = new FormData();
                formdata.append('prompt', prompt);
                fetch('http://localhost:8000/chat', {
                    'method': "POST",
                    body: formdata
                }).then(res => res.json()).then((res) => {
                    loading.style.display = 'none';
                    div1.innerHTML += '<p class="title_ai"> AI&nbsp;&nbsp;' + new Date().toLocaleTimeString() + '</p>';
                    div1.innerHTML += '<p class="message"> ' + res.replace(/\n/g, "<br>") + '</p><br>';
                    div1.scrollTop = div1.scrollHeight;
                    txt1.disabled = false;
                })
            }
        }
    }
}