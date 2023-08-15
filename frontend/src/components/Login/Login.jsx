import axios from "axios"
import { useState } from "react"
import './styles.css'

function Login() {
    const [error, setError] = useState()
    const [loading, setLoading] = useState(false)
    const loginEndpoint = "http://192.168.1.100:8000/auth/token/"
    function handleSubmit(event, loginEndpoint) {
        event.preventDefault()
        const password = event.target.elements.password_field.value
        const username = event.target.elements.username_field.value
        
        if (username && password) {
            console.log(username, password);
            setLoading(true)
            setError("")
            axios.post(loginEndpoint, {
                "username": username,
                "password": password
            })
                .finally(()=>{
                    setLoading(false)
                })
                .then(response=>{
                const data = response.data
                localStorage.setItem("access_token", data.access)
                localStorage.setItem("refresh_token", data.refresh)
            })
                .catch(error=>{
                    if (error.response.status===401) {
                        setError('Incorrect login credentials')
                    }
                })
        } else {
            setError('Please, enter a password and an username')
        }
        // 
    }
    return (
        <div id="login_container">
            <h2>Login</h2>
            <form onSubmit={(e)=>handleSubmit(e, loginEndpoint)}>
                <label htmlFor="username_field">Username</label><br />
                <input id="username_field" type="text" /><br />
                <label htmlFor="password_field">Password</label> <br />
                <input id="password_field" type="password" /><br /><br />
                {loading ? <p id="login-loading">Loading...</p> : null}
                {error ? <p id="login-error">{error}</p> : null}
                <input type="submit" value={"Login"}/>
            </form>
        </div>
    )
}

export default Login