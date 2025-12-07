document.addEventListener('DOMContentLoaded', ()=>{
const loginForm = document.getElementById('loginForm')
const registerForm = document.getElementById('registerForm')


if(loginForm){
loginForm.addEventListener('submit', async (e)=>{
e.preventDefault();
const form = new FormData(loginForm)
const body = Object.fromEntries(form.entries())
const res = await fetch('/api/login', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)})
if(res.ok) window.location.href = '/profile'
else alert('Login failed')
})
}


if(registerForm){
registerForm.addEventListener('submit', async (e)=>{
e.preventDefault();
const form = new FormData(registerForm)
const body = Object.fromEntries(form.entries())
const res = await fetch('/api/register', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)})
if(res.ok) window.location.href = '/profile'
else alert('Register failed')
})
}
})

