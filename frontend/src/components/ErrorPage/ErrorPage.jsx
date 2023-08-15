import { DO_NOT_USE_OR_YOU_WILL_BE_FIRED_EXPERIMENTAL_REACT_NODES } from "react"
import { useRouteError } from 'react-router-dom'
import NavBar from '../NavBar/NavBar'


function ErrorPage() {
    const error = useRouteError()
    console.log(error)

    return (
        <div id="errorPage">
            <NavBar />
            <h1>Oops!</h1>
            <p>An unexpected error has ocurred</p>
            <p>{error.status} {error.statusText || error.message}</p>
            
        </div>
    )
}

export default ErrorPage