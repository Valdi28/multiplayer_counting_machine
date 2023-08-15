import { useEffect, useState } from 'react'
import './index.css'
import { NavLink } from 'react-router-dom'

function NavBar() {
    const [isAuth, setAuth] = useState(false)

    useEffect(() => {
        function handleState() {
            if (localStorage.getItem('access_token') !== null) {
                setAuth(true)
            }
        }
        addEventListener("storage", handleState())
        return () => removeEventListener("storage")
    }, [])

    return (
        <div id='navBar'>
            <h1 id='navBarTitle'>Click It</h1>
            <nav id='navBarNav'>
                <ul>
                    <li>
                        <NavLink to={'/'}>Home</NavLink>
                    </li>
                    <li>
                        <NavLink to={'leaderboard'}>Leaderboard</NavLink>
                    </li>
                    {isAuth ?
                        <>
                            <li>
                                <NavLink to={'account'}>Account</NavLink>
                            </li>
                            <li>
                                <NavLink to={'logout'}>Logout</NavLink>
                            </li>

                        </>
                        :
                        <>
                            <li>
                                <NavLink to={'register'}>Register</NavLink>
                            </li>
                            <li>
                                <NavLink to={'login'}>Login</NavLink>
                            </li>
                        </>
                    }
                </ul>
            </nav>
        </div>
    )
}

export default NavBar