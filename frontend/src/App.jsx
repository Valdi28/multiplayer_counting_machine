import { useState, useEffect } from 'react'
import './App.css'
import 'axios'
import axios from 'axios'
import NavBar from './components/NavBar/NavBar'
import { Outlet } from 'react-router-dom'
import Home from './components/Home/Home'
import Login from './components/Login/Login'
import Register from './components/Register/Register'
import Leaderboard from './components/Leaderboard/Leaderboard'
import ErrorPage from './components/ErrorPage/ErrorPage'



function App() {

	return (
		<>
			<NavBar />
			<div id='detail'>
				<Outlet />
			</div>
		</>
	)
}

export default App
