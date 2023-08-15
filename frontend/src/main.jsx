import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { RouterProvider, createBrowserRouter} from 'react-router-dom'
import Home from './components/Home/Home'
import Login from './components/Login/Login'
import Register from './components/Register/Register'
import Leaderboard from './components/Leaderboard/Leaderboard'
import ErrorPage from './components/ErrorPage/ErrorPage'
import NavBar from './components/NavBar/NavBar.jsx'
import Account from './components/Account/Account.jsx'
import Logout from './components/Logout/Logout.jsx'

const router = createBrowserRouter([
	{
		path: '/',
		element: <App />,
		errorElement: <ErrorPage />,
    children: [
      {
        path: '/',
        element: <Home />
      },
      {
        path: '/leaderboard',
        element: <Leaderboard />
      },
      {
        path: '/login',
        element: <Login />
      },
      {
        path: '/register',
        element: <Register />
      },
      {
        path: '/account',
        element: <Account />
      },
      {
        path: '/logout',
        element: <Logout />
      }
    ]
	},
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
