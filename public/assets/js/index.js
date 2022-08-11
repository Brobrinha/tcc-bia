const audioSpectrum = document.querySelectorAll('div');
const button = document.querySelector('button');

button.addEventListener('click', event => {

    event.preventDefault();
    
    audioSpectrum.forEach((element) => {

        if(element.classList.contains('child')) {
            element.classList.remove('child')
        } else {
            element.classList.add('child')
        }

    })
  
})