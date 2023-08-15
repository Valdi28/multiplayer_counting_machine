import { useNavigate } from "react-router-dom"

function Logout() {
    const navigate = useNavigate()
    function handleConfirmation(confirmed) {
        if (confirmed) {
            localStorage.removeItem("access_token")
            localStorage.removeItem("refresh_token")
        } else {
            navigate('/')
        }
    }
    return (
        <>
            <h1>Logout</h1>
            <p>Are you sure you want to log out?</p>
            <button onClick={() => handleConfirmation(true)}>Yes</button>
            <button onClick={() => handleConfirmation(false)}>No</button>
        </>
    )
}

export default Logout