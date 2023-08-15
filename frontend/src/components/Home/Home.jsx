import { useState, useEffect, useRef } from 'react'
import 'axios'
import axios from 'axios'
import './styles.css'

function PlusOne() {
	return (
		<div className="plusone">
			+1
		</div>
	)
}

function Home() {
	const [count, setCount] = useState(0)
	const ws = useRef(null)

	const countingApi = axios.create({
		baseURL: "http://192.168.1.100:8000/api/counting/"
	})

	function handleAdd() {
		ws.current.send(JSON.stringify({
			'type': 'add_count'
		}))
		ws.current.send(JSON.stringify({
			'type': 'update_count'
		}))


		//e.preventDefault()


	}

	/*useEffect(() => {
		
		countingApi.get('season/latest/')
		.then((data) => {
			//setCount(data.data.count)
			setCount(data.data.count)
		})
		.catch(error => {
			console.log(error);
		})
}, [countingApi])*/

	useEffect(() => {
		ws.current = new WebSocket('ws://192.168.1.100:8000/ws/test/')
		ws.current.onerror = error => {
			console.log(error);
		}
		ws.current.onopen = () => {
			console.log('WS Connected')
			// ws.send(JSON.stringify({
			// 	'type': 'update_count'
			// }))
		}

		ws.current.onmessage = event => {
			const data = JSON.parse(event.data)
			console.log(data.type);
			if (data.type == "update_count") {
				setCount(data.count)
				console.log(data);
			}
			if (data.type == "add_count") {
				setCount(data.count)
				console.log('xd');
			}
		}
		return () => ws.current.close()
	}, [])

	/*useEffect(()=>{
		const interval = setInterval(() => {
			countingApi.get('season/latest/')
				.then((data) => {
					//setCount(data.data.count)
					console.log(data.data.count);
					setCount(data.data.count)
				})
				.catch(error => {
					console.log(error);
				})
		}, 2000)
		return () => {
			clearInterval(interval)
		}
	}, [countingApi])*/

	return (
		<div id="main-section">
			<button onClick={() => handleAdd()} id="addClickButton">
				<p>
					{count}
				</p>

			</button>
		</div>
	)
}

export default Home
